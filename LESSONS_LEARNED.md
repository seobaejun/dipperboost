# 반복 실수 방지 교훈

## 핵심 교훈: position sticky가 작동하지 않을 때

### 원인
`body { overflow-x: hidden }` 또는 `body { overflow: hidden }` 이 설정되어 있으면
`position: sticky`가 **완전히 무력화**된다.

### 해결책
```css
html {
    overflow-x: hidden; /* overflow를 html로 이동 */
}
body {
    overflow-x: visible !important;
    overflow-y: visible !important;
}
```

### 체크리스트: sticky가 안 될 때 가장 먼저 확인할 것
1. **외부 CSS 파일(style.css)에서 `overflow` 설정 확인** ← 가장 먼저!
2. 부모 요소 중 `overflow: hidden/auto/scroll` 있는지 확인
3. `position: sticky` + `top` 값 설정 여부 확인
4. flex 컨테이너라면 `align-items: flex-start` 설정 여부 확인

---

## 레이아웃 구조 원칙

### 왼쪽 박스 + 오른쪽 메인 콘텐츠 구조
```html
<!-- page-wrapper: flex 컨테이너 -->
<div class="page-wrapper" style="display:flex; align-items:flex-start;">

    <!-- 왼쪽 작은 박스 (sticky) -->
    <aside class="left-sidebar" style="width:280px; position:sticky; top:100px; align-self:flex-start;">
        ...박스 내용...
    </aside>

    <!-- 오른쪽 메인 콘텐츠 (넓게) -->
    <main class="main-content" style="flex:1; min-width:0;">
        ...메인 내용...
    </main>

</div>
```

### 절대 하지 말 것
- `<aside>`를 왼쪽 전체 영역으로 만들기 (박스가 아닌 사이드바가 됨)
- HTML 구조를 바꾸기 전에 CSS 원인 분석 먼저 할 것
- `body`에 `overflow: hidden` 두면 sticky 절대 안 됨

---

## 문제 해결 순서 (앞으로 반드시 지킬 것)

1. **외부 CSS 파일 먼저 확인** (`grep overflow style.css`)
2. 원인 파악 후 최소한의 수정
3. HTML 구조는 건드리지 말고 CSS만 수정
4. 사용자 요청을 정확히 이해한 후 수정 시작
