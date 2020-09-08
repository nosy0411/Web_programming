"""
다음 코드는 네이버의 메인 페이지를 캡쳐해서
"NaverTitle.png" 라는 이름으로 저장합니다.
프로그램은 크롬 헤드리스 드라이버를 추출한 다음 드라이버가 URL의 웹 페이지를 읽어 들이고, 
그리고 화면을 캡처해서 파일로 저장합니다. close() 메서드로 크롬 브라우저를 종료합니다.
"""
from selenium import webdriver
import os

# 크롬 드라이버가 있는 파일 경로를 설정한다.
path = os.getcwd()

# working directory를 변경
os.chdir(path)

# 셀레니움 웹드라이브가 웹페이지를 따로 열지 않고도 데이터를 가져올 수 있게 해주는 장치이다.
# 만약 없으면 코드 실행 중 페이지가 자동으로 열린다.
options = webdriver.ChromeOptions()
options.add_argument('headless')  # headless: 크롤링 할때 브라우저가 안뜨도록 설정

# 설치한 크롬드라이브의 위치를 webdriver에게 알려줘야 한다. chromedriver.exe가 있는 경로를 설정해준다.
driver = webdriver.Chrome('chromedriver.exe', options=options)

url = "http://www.naver.com"

# URL 읽어들이기
driver.get(url)

# 화면 캡쳐하기
driver.save_screenshot("NaverTitle.png")

# 브라우저 종료하기
driver.close()

"""
기본적으로 알아두면 좋은 Selenium의 메서드는 다음과 같습니다.

URL에 접근
get(url)

페이지의 단일 element에 접근
find_element_by_name(‘HTML_name’)
find_element_by_id(‘HTML_id’)
find_element_by_xpath(‘/html/body/some/xpath’)

페이지의 여러 elements에 접근
find_element_by_css_selector(‘#css > div.selector’)
find_element_by_class_name(‘some_class_name’)
find_element_by_tag_name(‘h1’)

굉장히 다양한 메서드가 있는데 기초적인 것은 여기까지 알아보겠습니다.
더 다양한 메서드를 알고 싶다면http://selenium-python.readthedocs.io/index.html에서 찾아보시기 바랍니다.
"""
