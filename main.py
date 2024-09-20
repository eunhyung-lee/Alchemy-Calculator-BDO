import requests
from bs4 import BeautifulSoup

# from bs4 import BeautifulSoup

Garmoth_BDO = "https://garmoth.com/market/item/715001/0"
BDOlytics_BDO = "https://bdolytics.com/ko/KR/market/central-market/mainhand/longsword"
Naver = "https://naver.com"
Exchange_BDO = "https://trade.kr.playblackdesert.com/Home/list/hot"
VELIA_INN = "https://veliainn.com/market-queue"


session = requests.Session()
# User-Agent 헤더를 브라우저처럼 설정
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}


# # requests를 사용해 페이지 요청
response = requests.get(VELIA_INN, headers=headers)  # , headers=headers)
print(response.status_code)  # 응답 상태 코드 출력
print(response.text)
