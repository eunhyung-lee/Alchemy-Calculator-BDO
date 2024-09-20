from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

# ChromeOptions 객체 생성
chrome_options = Options()
chrome_options.add_argument("--headless")  # 브라우저를 보이지 않게 실행
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument("--disable-dev-shm-usage")

# 사용자 에이전트 설정
chrome_options.add_argument(
    "user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
)

# ChromeDriver 설정
service = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=service, options=chrome_options)

try:
    # 웹 페이지 열기
    driver.get("https://bdolytics.com/ko/KR/market/central-market/mainhand/longsword")

    # 페이지가 완전히 로드될 때까지 대기
    time.sleep(10)  # 페이지 로딩을 충분히 기다리기 위해 대기 (필요에 따라 조정)

    # # 전체 HTML 가져오기
    # page_source = driver.page_source

    # # HTML 출력
    # print(page_source)

    # 요소가 나타날 때까지 대기
    elements = driver.find_elements(
        By.CSS_SELECTOR, "div.vue3-easy-data-table__main.hoverable"
    )

    # 데이터 추출
    for element in elements:
        print(element.text)  # 텍스트 출력


finally:
    # 브라우저 닫기
    driver.quit()
