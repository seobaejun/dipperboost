from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1400, "height": 900})
    page.goto("http://localhost:8000", wait_until="networkidle", timeout=15000)
    page.wait_for_timeout(3000)
    
    # 현재 상태 확인
    info = page.evaluate('''() => {
        const sidebar = document.querySelector('aside.left-sidebar');
        const wrapper = sidebar.parentElement;
        const pw = wrapper.parentElement;
        const scs = window.getComputedStyle(sidebar);
        const wcs = window.getComputedStyle(wrapper);
        const pwcs = window.getComputedStyle(pw);
        return {
            sidebar_position: scs.position,
            sidebar_top_css: scs.top,
            wrapper_display: wcs.display,
            wrapper_height: Math.round(wrapper.getBoundingClientRect().height),
            pw_display: pwcs.display,
            pw_grid_template: pwcs.gridTemplateColumns,
            pw_height: Math.round(pw.getBoundingClientRect().height),
        };
    }''')
    print("현재 상태:")
    for k, v in info.items():
        print(f"  {k}: {v}")
    
    # JS로 직접 sticky 강제 적용 후 테스트
    page.evaluate('''() => {
        const sidebar = document.querySelector('aside.left-sidebar');
        sidebar.style.position = 'sticky';
        sidebar.style.top = '100px';
        sidebar.style.maxHeight = 'calc(100vh - 120px)';
        sidebar.style.overflowY = 'auto';
        console.log('sidebar style applied:', sidebar.style.cssText);
    }''')
    
    page.evaluate('window.scrollTo(0, 1200)')
    page.wait_for_timeout(500)
    
    test = page.evaluate('''() => {
        const el = document.querySelector('aside.left-sidebar');
        const rect = el.getBoundingClientRect();
        const cs = window.getComputedStyle(el);
        return { computed_position: cs.position, rect_top: Math.round(rect.top), inline_style: el.style.cssText };
    }''')
    print(f"\nJS 강제 적용 후: {test}")
    
    if test['rect_top'] >= 90 and test['rect_top'] <= 120:
        print("=> sticky 작동!")
    else:
        print(f"=> 여전히 안됨. 다른 원인 존재")
        
        # 모든 적용된 CSS 규칙 확인
        rules = page.evaluate('''() => {
            const el = document.querySelector('aside.left-sidebar');
            const matched = [];
            for (const sheet of document.styleSheets) {
                try {
                    for (const rule of sheet.cssRules) {
                        if (rule.selectorText && el.matches(rule.selectorText)) {
                            matched.push({
                                selector: rule.selectorText,
                                position: rule.style.position || '',
                                top: rule.style.top || '',
                                source: sheet.href ? sheet.href.split('/').pop() : 'inline'
                            });
                        }
                    }
                } catch(e) {}
            }
            return matched;
        }''')
        print("\n적용된 CSS 규칙:")
        for r in rules:
            if r['position'] or r['top']:
                print(f"  [{r['source']}] {r['selector']} => position:{r['position']} top:{r['top']}")
    
    page.screenshot(path="sticky_js_test.png")
    browser.close()
