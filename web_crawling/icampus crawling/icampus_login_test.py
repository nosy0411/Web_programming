# parser.py
import requests

# 로그인할 유저정보를 넣어주자 (모두 문자열)
LOGIN_INFO = {
    'uid': '',
    'pwd': ''
}

# Session 생성, with 구문 안에서 유지
with requests.Session() as s:
    # HTTP POST request: 로그인을 위해 POST url와 함께 전송될 data를 넣어주자.
    login_req = s.post('https://www.clien.net/service/login', data=LOGIN_INFO)
    # 어떤 결과가 나올까요?
    print(login_req.status_code)
