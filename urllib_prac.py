from urllib.request import urlopen
from urllib.error import HTTPError
from bs4 import BeautifulSoup

"""
urllib은 표준 파이썬 라이브러리입니다.
request 라는 라이브러리는 설치가 필요하지만 urllib는 뭔가 추가로 설치할 필요가 없습니다. request는 다음에 다룹니다.
urllib는 웹을 통해 데이터를 요청하는 함수, 쿠키를 처리하는 함수, 심지어 헤더나 유저 에이전트 같은 메타데이터를 바꾸는 함수도 포함하는 통합 패키지 입니다.
urllib 패키지에서 포함한 함수인 urlopen은 네트워크를 통해 원격 객체를 읽습니다. urlopen은 HTML파일이나 이미지 파일, 기타 파일 스트림을 쉽게 열 수 있는 매우 범용적인 라이브러리입니다. 여기서는 우선 urlopen으로 HTML 파일 소스코드를 읽어왔습니다. 이 읽어온 HTML 파일은 BeautifulSoup 이라는 패키지에서 처리하여 데이터화 시킵니다.

BeautifulSoup 객체에 들어 있는 태그에 접근할 때마다 그 태그가 실제 존재하는지 체크하는 편이 좋습니다. 가능한 에러를 모두 체크하고 처리하는 게 처음에는 지겨워 보일 수 있지만, 코드르 조금만 수정하면 좀 더 쉽게 읽을 수 있게 만들 수 있습니다.
이 예제에서는 페이지 타이틀을 반환하거나, 어떤 문제가 있으면 None 객체를 반환하는 getTitle 함수를 만듭니다.

"""


def getTitle(url):
    try:
        html = urlopen(url)
    except HTTPError as e:
        return None
    try:
        bsObj = BeautifulSoup(html.read(), "html.parser")
        title = bsObj.body.h1
    except AttributeError as e:
        return None
    return title


title = getTitle("http://www.pythonscraping.com/pages/page1.html")
if title == None:
    print("Title could not be found")
else:
    print(title)
