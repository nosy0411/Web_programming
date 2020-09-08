from selenium import webdriver

url1 = 'http://www.icampus.ac.kr/front/main/MainAction.do?method=list'
# url2 = 'https://admin.skku.edu/co/COCOUsrLoginAction.do'
# url3 = 'http://www.icampus.ac.kr/front/mypage/CourseAction.do?method=list'
# url4 = 'http://www.icampus.ac.kr/front/login/loginAction.do?method=checkLoginAuth'
# url5 = 'http://www.icampus.ac.kr/front/poll/PollAction.do?method=list'

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
# options.add_argument("disable-gpu")
# 혹은 options.add_argument("--disable-gpu")

driver = webdriver.Chrome('/home/inhosecond/chromedriver', chrome_options=options)

driver.implicitly_wait(1)
driver.get(url1)
driver.find_element_by_name('uid').send_keys('')
driver.find_element_by_name('pwd').send_keys('')
driver.find_element_by_xpath('//a[@href="javascript:onLogin();"]').click()
driver.find_element_by_xpath('//img[@src="/images/front/ko/mbann01.gif"]').click()
driver.get_screenshot_as_file('icampus_main_headless.png')
print(driver.find_element_by_tag_name("tbody").text)

# wrap에 scontent에 form1으로 들어가서 con에 contents 찾고 board_view(tbody),board_view_con(tbody)뒤지면
# 제목, 글쓴이, 올린날짜 알 수 있음. 이건 공지의 경우인데 웬만해서는 마찬가지로 tbody찾으면 다 있음. (강의목록은 tbl_list)
# 첨부파일은... 개인정보도 있으니까 안쓰는게 좋을듯. 과제점수, 시험점수도 마찬가지.
# 과제는 과제명, 제출기간, 상태, 제출일자, 제출여부 나타내면 될듯
# Q&A는 tbl_list외에 paging도 있따... 생각해보자...
# driver.implicitly_wait(1)
# 자료실1(교수, 학생), 자료실2(교수 only), bdotDiv=02, bdotDiv=01 차이
# driver.get(url3)
# driver.get_screenshot_as_file('icampus_course_headless.png')

driver.quit()