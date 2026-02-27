# 반응형 디자인 가이드라인

## 📱 반응형 디자인 원칙

이 프로젝트의 모든 코드는 반응형으로 제작되어야 합니다. 다양한 화면 크기에서 최적의 사용자 경험을 제공하기 위한 가이드라인입니다.

## 🎯 기본 원칙

### 1. 모바일 퍼스트 (Mobile First)
- 작은 화면부터 시작하여 큰 화면으로 확장
- 기본 스타일은 모바일용으로 작성
- 미디어 쿼리로 데스크톱 스타일 추가

### 2. 유연한 단위 사용
- 고정 픽셀(`px`) 대신 상대 단위 사용
- `rem`, `em`, `%`, `vw`, `vh`, `clamp()` 활용

### 3. 유연한 레이아웃
- Flexbox와 Grid 사용
- 고정 너비 대신 `max-width`, `min-width` 활용

## 📐 브레이크포인트

```css
/* 모바일 (기본) */
/* 0px ~ 575px */

/* 태블릿 (작은 화면) */
@media screen and (min-width: 576px) { }

/* 태블릿 (중간 화면) */
@media screen and (min-width: 768px) { }

/* 데스크톱 (작은 화면) */
@media screen and (min-width: 992px) { }

/* 데스크톱 (중간 화면) */
@media screen and (min-width: 1200px) { }

/* 데스크톱 (큰 화면) */
@media screen and (min-width: 1400px) { }
```

## 🛠️ 필수 반응형 기법

### 1. clamp() 함수 사용
```css
/* 폰트 크기 */
font-size: clamp(14px, 2vw, 18px);

/* 패딩 */
padding: clamp(10px, 2vw, 20px);

/* 마진 */
margin: clamp(15px, 3vw, 30px);

/* 너비 */
width: clamp(200px, 50vw, 400px);
```

### 2. 유연한 그리드 레이아웃
```css
/* 자동 조정 그리드 */
display: grid;
grid-template-columns: repeat(auto-fit, minmax(250px, 1fr));
gap: clamp(10px, 2vw, 20px);

/* 반응형 컬럼 */
@media screen and (max-width: 991px) {
    grid-template-columns: repeat(2, 1fr);
}

@media screen and (max-width: 767px) {
    grid-template-columns: 1fr;
}
```

### 3. Flexbox 반응형
```css
.container {
    display: flex;
    flex-wrap: wrap;
    gap: clamp(15px, 3vw, 30px);
}

.item {
    flex: 1 1 300px; /* 최소 300px, 가능한 만큼 확장 */
    min-width: 0; /* 오버플로우 방지 */
}

@media screen and (max-width: 767px) {
    .item {
        flex: 1 1 100%;
    }
}
```

### 4. 이미지 반응형
```css
img {
    max-width: 100%;
    height: auto;
    display: block;
}

/* 반응형 이미지 컨테이너 */
.image-container {
    width: 100%;
    aspect-ratio: 16 / 9;
    overflow: hidden;
}

.image-container img {
    width: 100%;
    height: 100%;
    object-fit: cover;
}
```

### 5. 텍스트 반응형
```css
/* 제목 */
h1 {
    font-size: clamp(24px, 4vw, 36px);
    line-height: 1.2;
}

h2 {
    font-size: clamp(20px, 3vw, 28px);
    line-height: 1.3;
}

h3 {
    font-size: clamp(18px, 2.5vw, 24px);
    line-height: 1.4;
}

/* 본문 */
p {
    font-size: clamp(14px, 1.8vw, 16px);
    line-height: 1.6;
}
```

### 6. 버튼 반응형
```css
.button {
    padding: clamp(10px, 1.5vw, 15px) clamp(20px, 3vw, 30px);
    font-size: clamp(14px, 1.8vw, 16px);
    border-radius: clamp(6px, 1vw, 8px);
    min-width: clamp(100px, 20vw, 150px);
}
```

### 7. 테이블 반응형
```css
.table-container {
    overflow-x: auto;
    -webkit-overflow-scrolling: touch;
}

table {
    width: 100%;
    min-width: 600px; /* 최소 너비 보장 */
}

th, td {
    padding: clamp(8px, 1.5vw, 15px);
    font-size: clamp(12px, 1.6vw, 16px);
}

@media screen and (max-width: 767px) {
    table {
        font-size: 12px;
    }
    
    th, td {
        padding: 8px 4px;
    }
}
```

### 8. 폼 요소 반응형
```css
input, textarea, select {
    width: 100%;
    padding: clamp(10px, 1.5vw, 15px);
    font-size: clamp(14px, 1.8vw, 16px);
    border-radius: clamp(6px, 1vw, 8px);
}

.form-group {
    margin-bottom: clamp(15px, 2.5vw, 25px);
}
```

## 📱 모바일 최적화

### 1. 터치 친화적
```css
/* 최소 터치 영역 44x44px */
button, a, input[type="button"] {
    min-height: 44px;
    min-width: 44px;
}

/* 터치 스크롤 */
.scrollable {
    -webkit-overflow-scrolling: touch;
    overflow-y: auto;
}
```

### 2. 뷰포트 메타 태그
```html
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
```

### 3. 모바일 네비게이션
```css
/* 햄버거 메뉴 */
.mobile-menu-toggle {
    display: none;
}

@media screen and (max-width: 991px) {
    .mobile-menu-toggle {
        display: block;
    }
    
    .desktop-menu {
        display: none;
    }
}
```

## 🎨 반응형 컴포넌트 패턴

### 1. 카드 그리드
```css
.card-grid {
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: clamp(20px, 3vw, 30px);
    padding: clamp(20px, 4vw, 40px);
}

@media screen and (max-width: 767px) {
    .card-grid {
        grid-template-columns: 1fr;
        gap: 20px;
        padding: 20px;
    }
}
```

### 2. 히어로 섹션
```css
.hero-section {
    padding: clamp(40px, 10vw, 100px) clamp(20px, 5vw, 60px);
    min-height: clamp(300px, 50vh, 600px);
}

.hero-title {
    font-size: clamp(28px, 5vw, 48px);
    margin-bottom: clamp(20px, 3vw, 30px);
}
```

### 3. 네비게이션 바
```css
.navbar {
    padding: clamp(10px, 2vw, 20px) clamp(15px, 3vw, 40px);
    height: clamp(60px, 10vw, 80px);
}

.navbar-logo {
    max-height: clamp(40px, 7vw, 60px);
    height: auto;
}
```

## ⚠️ 주의사항

### 1. 절대 피해야 할 것
- ❌ 고정 픽셀 값만 사용 (`width: 300px`)
- ❌ `!important` 남용
- ❌ 미디어 쿼리 없이 고정 레이아웃
- ❌ 작은 화면에서 가로 스크롤 발생

### 2. 권장 사항
- ✅ `clamp()` 함수 적극 활용
- ✅ 상대 단위(`rem`, `em`, `%`, `vw`, `vh`) 사용
- ✅ Flexbox와 Grid 활용
- ✅ 모든 컴포넌트에 모바일 스타일 포함
- ✅ 터치 친화적 인터페이스 설계

## 📝 코드 작성 체크리스트

새로운 컴포넌트를 작성할 때 다음을 확인하세요:

- [ ] `clamp()` 함수로 폰트 크기 설정
- [ ] `clamp()` 함수로 패딩/마진 설정
- [ ] 모바일(767px 이하) 스타일 포함
- [ ] 태블릿(768px ~ 991px) 스타일 포함
- [ ] 데스크톱(992px 이상) 스타일 포함
- [ ] 이미지가 `max-width: 100%` 적용
- [ ] 버튼 최소 크기 44x44px
- [ ] 가로 스크롤이 발생하지 않음
- [ ] 터치 친화적 인터페이스
- [ ] 모든 텍스트가 읽기 가능한 크기

## 🔍 테스트 방법

1. **브라우저 개발자 도구**
   - 다양한 디바이스 크기로 테스트
   - 모바일, 태블릿, 데스크톱 확인

2. **실제 디바이스 테스트**
   - 실제 스마트폰에서 확인
   - 다양한 브라우저에서 테스트

3. **반응형 확인 사항**
   - 모든 콘텐츠가 화면에 맞게 조정되는가?
   - 텍스트가 읽기 쉬운가?
   - 버튼이 클릭하기 쉬운가?
   - 가로 스크롤이 없는가?

## 📚 참고 예시

### 완전한 반응형 컴포넌트 예시

```css
/* 반응형 카드 컴포넌트 */
.responsive-card {
    /* 기본 (모바일) */
    padding: clamp(15px, 3vw, 30px);
    margin-bottom: clamp(15px, 3vw, 30px);
    border-radius: clamp(8px, 1.5vw, 12px);
    box-shadow: 0 2px clamp(8px, 1.5vw, 12px) rgba(0, 0, 0, 0.1);
}

.responsive-card-title {
    font-size: clamp(18px, 3vw, 24px);
    font-weight: 700;
    margin-bottom: clamp(10px, 2vw, 20px);
}

.responsive-card-text {
    font-size: clamp(14px, 1.8vw, 16px);
    line-height: 1.6;
    margin-bottom: clamp(15px, 2.5vw, 25px);
}

.responsive-card-button {
    padding: clamp(10px, 1.5vw, 15px) clamp(20px, 3vw, 30px);
    font-size: clamp(14px, 1.8vw, 16px);
    border-radius: clamp(6px, 1vw, 8px);
    min-height: 44px;
}

/* 태블릿 */
@media screen and (min-width: 768px) {
    .responsive-card {
        display: grid;
        grid-template-columns: repeat(2, 1fr);
        gap: clamp(20px, 3vw, 30px);
    }
}

/* 데스크톱 */
@media screen and (min-width: 992px) {
    .responsive-card {
        grid-template-columns: repeat(3, 1fr);
    }
}
```

## 🎯 핵심 요약

1. **항상 `clamp()` 사용**: 폰트, 패딩, 마진, 너비 등
2. **모바일 퍼스트**: 작은 화면부터 시작
3. **유연한 레이아웃**: Flexbox와 Grid 활용
4. **상대 단위**: `px` 대신 `rem`, `em`, `%`, `vw`, `vh`
5. **미디어 쿼리**: 모든 주요 브레이크포인트에서 테스트
6. **터치 친화적**: 최소 44x44px 터치 영역
7. **가로 스크롤 방지**: `max-width: 100%` 사용

---

**이 가이드라인을 항상 참고하여 모든 코드를 반응형으로 작성하세요!**

