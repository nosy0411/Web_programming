# parser.py
import requests
import time

# 로그인할 유저정보를 넣어주자 (모두 문자열)
LOGIN_INFO = {
    'retPage': 'http://www.icampus.ac.kr/front/login/loginAction.do?method=checkLoginAuth',
    'method': 'loginHide',
    'D1': '',
    'D3': '',
    'roundkey': '',
    'language': 'ko',
    'loginId': '',
    'userPasswd': '',
    'type': '',
    'reqType': '',
}

LOGIN_INFO2 = {
    'retPage': 'http://www.icampus.ac.kr/front/login/loginAction.do?method=checkLoginAuth',
    'roundkey': '',
    'D1': '',
    'D3': 'SEED',
    'type': 'Y',
    'BIZ': '',
    'SKEY': '',
}
url1 = 'http://www.icampus.ac.kr/front/main/MainAction.do?method=list'
url2 = 'https://admin.skku.edu/co/COCOUsrLoginAction.do'
url3 = 'http://www.icampus.ac.kr/front/mypage/CourseAction.do?method=list'
url4 = 'http://www.icampus.ac.kr/front/login/loginAction.do?method=checkLoginAuth'
url5 = 'http://www.icampus.ac.kr/front/poll/PollAction.do?method=list'

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login = s.post(url4, data=LOGIN_INFO2, verify=False, allow_redirects=False)
    # 어떤 결과가 나올까요?
    login.raise_for_status()
    html1 = login.text
    header1 = login.headers
    print(header1)
    status1 = login.status_code
    print(status1)
    print(login.cookies.get_dict())
    redirected_url = header1['Location']
    print(redirected_url)

    time.sleep(3)
    print(login.cookies.get_dict())
    req = s.get(redirected_url)
    print(req.text)
