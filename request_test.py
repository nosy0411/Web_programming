## parser.py
import requests

## HTTP GET Request
url = 'http://pythonscraping.com/pages/files/form.html'

header = {'Accept-Language' : 'ko-KR'}

req = requests.get(url)
print(req)
## HTML 소스 가져오기
html = req.text
print(html)
## HTTP Header 가져오기
header = req.headers
print(header)
print(type(header))
## HTTP Status 가져오기 (200: 정상)
status = req.status_code
print(status)
## HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok
print(is_ok)



# final resp = await dio.get<List<dynamic>>( 'https://vod2.icampus.ac.kr/testservice.svc/GetHaksa_login', queryParameters: {'userid': uid, 'password': password}, options: Options( responseType: ResponseType.json, ), );