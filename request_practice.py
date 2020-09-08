import requests

# HTTP GET Request
url = 'http://pythonscraping.com/pages/files/form.html'

# 해당 url으로 request.get 를 이용하여 GET 요청을 보낸다.
req = requests.get(url)
print(req)
print('req was printed')
print('\n')

# HTML 소스 가져오기
html = req.text
print(html)
print('html was printed')
print('\n')

# HTTP Header 가져오기
header = req.headers
print(header)
print('header was printed')
print('\n')

print(type(header))
print('\n')

# HTTP Status 가져오기 (200: 정상적으로 get 요청이 되었음)
status = req.status_code
print(status)
print('\n')

# HTTP가 정상적으로 되었는지 (True/False)
is_ok = req.ok
print(is_ok)
print('\n')
