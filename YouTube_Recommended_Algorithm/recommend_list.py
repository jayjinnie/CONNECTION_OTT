# 유튜브 추천 영상 제목, 채널 추출
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import pandas as pd

# 셀레니움 열기
browser = webdriver.Chrome()
browser.maximize_window()
browser.delete_all_cookies()

# 유튜브 홈 화면 접근
url = "https://youtube.com"
browser.get(url)

# 로그인
time.sleep(3)
browser.find_element_by_xpath('//*[@id="buttons"]/ytd-button-renderer/a').click()

## 이메일 입력
time.sleep(2)
email = browser.find_element_by_css_selector('input[type=email]')
email.send_keys('kim???.ott@gmail.com')
print("이메일 입력 완료")

browser.find_element_by_id("identifierNext").click()
time.sleep(2)

## 비밀번호 입력
password = browser.find_element_by_css_selector('input[type=password]')
password.send_keys('hyerica1243')
print("비밀번호 입력 완료")

browser.find_element_by_id("passwordNext").click()
print("로그인 성공")


# 스크롤 내리기
time.sleep(3)
endk = 5
while endk:
    browser.find_element_by_tag_name('body').send_keys(Keys.END)
    time.sleep(1)
    endk -= 1

# 뷰티풀숲  파싱
## 데이터 프레임 생성
page = browser.page_source
soup = BeautifulSoup(page, 'html.parser')

title = soup.select('a#video-title-link')
channel = soup.select('a#avatar-link')

title_list = []
channel_list = []

for i in range(len(title)):
    title_list.append(title[i].text.strip())

for i in range(len(channel)):
    channel_list.append(channel[i].get('title'))
    
youtubeDic = {
    '추천 영상 제목': title_list,
    '채널명': channel_list
}

# csv 파일 저장
youtubeDf = pd.DataFrame(youtubeDic)
print(youtubeDf.head())
youtubeDf.to_csv('???_추천영상리스트_?일차.csv', encoding='utf-8-sig', index=False)