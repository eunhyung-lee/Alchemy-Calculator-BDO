from playwright.sync_api import sync_playwright

# Playwright 실행
with sync_playwright() as p:
    # 브라우저 실행 (headless 모드)
    browser = p.chromium.launch(headless=True)

    # 사용자 에이전트 설정
    context = browser.new_context(
        user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
    )

    # 새 페이지 열기
    page = context.new_page()

    # 웹 페이지 열기
    page.goto("https://bdolytics.com/ko/KR/market/central-market/mainhand/longsword")

    # 페이지가 완전히 로드될 때까지 대기
    page.wait_for_timeout(8000)  # 10초 대기 (필요에 따라 조정)

    # 전체 HTML 가져오기
    # full_html = page.content()
    # print(full_html)  # 전체 HTML 출력

    # 요소 선택 및 데이터 추출 (CSS 선택자 사용)
    elements = page.query_selector_all("div.vue3-easy-data-table__main.hoverable")

    # 추출한 요소 출력
    for element in elements:
        print(element.inner_text())  # 텍스트 출력

    # 브라우저 닫기
    browser.close()
