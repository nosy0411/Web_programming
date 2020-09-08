"""
자바 스크립트 실행해 보기
Selenium이 굉장히 다양한 기능을 제공하긴 하지만 원하는 기능이 없을 수도 있습니다. 
이럴때는 직접 자바스크립트 코드를 실행하는 방법이 있습니다. execute_script() 메서드를 사용하면 됩니다.
이 기능들이 익숙해 지면 다양하고 복잡한 사이트에서도 데이터를 긁어 올 수 있게 되며
기본적으로 웹 스크래핑이 막혀 있는 사이트도 긁어 올수 있습니다.
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

dirver.get("https://google.com")

# 자바스크립트 실행하기
r = driver.execute_script("return 100+50")
print(r)
