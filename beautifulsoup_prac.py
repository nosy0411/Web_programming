from urllib.request import urlopen
from bs4 import BeautifulSoup
html1 = urlopen("http://www.pythonscraping.com/pages/warandpeace.html")
bsObj1 = BeautifulSoup(html1, "html.parser")
html2 = urlopen("http://www.pythonscraping.com/pages/page3.html")
bsObj2 = BeautifulSoup(html2,"html.parser")

"""
find() 와 findAll()
find()와 findAll()은 BeautifulSoup에서 가장 자주 쓰는 함수입니다. 이 함수를 쓰면 HTML 페이지에서 원하는 태그를 다양한 속성에 따라 쉽게 필터링할 수 있습니다.

두 함수는 거의 비슷합니다.

함수의 정의
findAll(tag, attributes, recursive, text, limit, keyword)
find(tag, attributes, recursive, text, keyword)

tag 와 attrutubes가 가장 중요합니다.

tag 매개변수는 태그 이름인 문자열을 넘기거나, 태그 이름으로 이루어진 파이썬 리스트를 넘길 수도 있습니다. attritubes 매개변수는 속성으로 이루어진 파이썬 딕셔너리를 받고, 그 중 하나에 일치하는 태그를 찾습니다. 헷갈리시죠? 예를 들어 다음 함수는 HTML 문서에서 녹색과 빨간색 span 태그를 모두 반환 합니다.
findAll("span",{"class":{"green","red"}")

recursive 매개변수는 불리언입니다. 문서에서 얼마나 깊이 찾아 들어가고 싶은지를 지정합니다. 왠만하면 그대로 두는 것이 좋습니다.
text 매개변수는 태그의 속성이 아니라 텍스트 콘텐츠에 일치하는 걸 찾습니다.
limit 매개변수는 페이지의 항목 처음 몇 개에만 관심 있을 때 사용합니다. find는 findAll을 호출하면서 limit을 1로 지정한 것과 같습니다.

keyword 매개변수는 특정 속성이 포함된 태그를 선택할 때 사용합니다.
 *keyword 매개변수는 사실 tag, attritutes의 조합으로도 표현 가능합니다. 다만 간결한 표현이 가능하다는 점이 다릅니다.

"""

nameList = bsObj1.findAll("span",{"class":"green"})
for name in nameList:
    print(name.get_text())
print('------------------------------------------')

"""children And descendants(자식과 자손)

BeautifulSoup 라이브러리는 자식과 자손을 구별합니다. 자식은 항상 부모보다 한 태그 아래에 있고, 자손은 조상보다 몇 단계든 아래에 있을 수 있습니다. 예를들어 앞에서 tr 캐그는 table 태그의 자식이며 tr과 th, td, img, span은 모두 table 태그의 자손입니다.
일반적으로 BeautifulSoup 함수는 항상 현재 선택된 태그의 자손을 다룹니다.
bsObj.div.findAll("img")는 문서의 첫 번째 div 태그를 찾고, 그 div 태그의 자손인 모든 img 태그의 목록을 가져옵니다. 자식만 찾을 때는 .children을 사용합니다.
이 코드는 giftList 테이블에 들어 있는 제품 행 목록을 출력합니다. 
"""

for child in bsObj2.find("table",{"id":"giftList"}).children:
    print(child)
print('------------------------------------------')

"""
형제 다루기

BeaufifulSoup의 next_siblings() 함수는 테이블에서 데이터를 쉽게 수집할 수 있으며, 특히 테이블에 타이틀 행이 있을 때 유용합니다.
타이틀 행을 선택하고 next_sibling을 호출했으므로, 타이틀 행 자체를 제외한 모든 테이블 행을 선택하게 됩니다. next_siblings를 보완하는 previous_siblings 함수도 있습니다.
"""

for sibling in bsObj2.find("table",{"id":"giftList"}).tr.next_siblings:
    print(sibling)
print('------------------------------------------')

"""
부모다루기

가끔 자식이나 형제가 아니라 부모를 찾아야 할 때도 있습니다.  가끔 .parent 와 parents가 필요할 때가 있다는 말입니다.
이 코드는 ../img/gifts/img1.jpg 이미지가 나타내는 객체의 가격을 출력합니다.
"""

print(bsObj2.find("img",{"src":"../img/gifts/img1.jpg"}).parent.previous_sibling.get_text())










