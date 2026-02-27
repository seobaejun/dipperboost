from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=True)
    page = browser.new_page(viewport={"width": 1400, "height": 900})
    page.goto("http://localhost:8000", wait_until="networkidle", timeout=15000)
    page.wait_for_timeout(3000)
    
    # Before scroll
    page.screenshot(path="debug_v2_before.png", full_page=False)
    
    before = page.evaluate('''() => {
        const el = document.querySelector('aside.left-sidebar');
        const rect = el.getBoundingClientRect();
        const cs = window.getComputedStyle(el);
        return { top: rect.top, position: cs.position, marginTop: cs.marginTop };
    }''')
    print(f"BEFORE: {before}")
    
    # Scroll 800px
    for i in range(16):
        page.evaluate('window.scrollBy(0, 50)')
        page.wait_for_timeout(80)
    page.wait_for_timeout(500)
    
    page.screenshot(path="debug_v2_after800.png", full_page=False)
    
    after = page.evaluate('''() => {
        const el = document.querySelector('aside.left-sidebar');
        const rect = el.getBoundingClientRect();
        const cs = window.getComputedStyle(el);
        return { top: rect.top, position: cs.position };
    }''')
    print(f"AFTER 800px: {after}")
    print(f"TOP DIFF: {after['top'] - before['top']}px")
    
    # Check cache headers
    response = page.goto("http://localhost:8000", wait_until="networkidle")
    headers = response.headers
    print(f"\nCache-Control: {headers.get('cache-control', 'NOT SET')}")
    print(f"Pragma: {headers.get('pragma', 'NOT SET')}")
    
    browser.close()
