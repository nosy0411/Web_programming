# 파싱에 필요한 module 가져오기
from urllib.request import urlopen, Request
from urllib.parse import quote
from bs4 import BeautifulSoup as bs
import webbrowser
import re

# 데이터 받을 저장공간
page = 1
model_list = []
release_list = []
inch_list = []
price_list = []
resolution_list = []
os_list = []

list_all = [model_list, release_list, inch_list, price_list, os_list]

encoding_model_list = []
url_list = []

# 파싱
while True:
    string1 = 'https://review.cetizen.com/review.php?q=phone&just_one=&just_one_name=&just_one_pcat=&m%5B1%5D=1&m%5B2%5D=2&m%5B12%5D=12&cat%5B0%5D=3&keyword_p=&p_data=3&p_split=&recnum=50&p=' + str(
        page)
    url = string1
    req = Request(url)
    html = urlopen(req).read()
    soup = bs(html, 'html.parser', from_encoding='euc-kr')
    list_of_model = soup.find_all('span', {'class': ' p16 clr100 b ln18'})
    list_of_release = soup.find_all('div', {'style': 'float:left;'})
    list_of_addi = soup.find_all('li', {'style': "float:left;padding:3px;"})
    list_of_price = soup.find_all('span', {'class': 'p12'})

    if list_of_model == []:
        break

    list_of_inch = []
    list_of_resol = []
    list_of_os = []
    price_check = []


    # 항목별로 리스트 만들기
    for i in range(0, len(list_of_addi), 11):
        list_of_os.append(list_of_addi[i])
    for i in range(1, len(list_of_addi), 11):
        list_of_inch.append(list_of_addi[i])
    for i in range(2, len(list_of_addi), 11):
        list_of_resol.append(list_of_addi[i])
    for i in range(len(list_of_price)):
        price = re.findall(r'<span class="p12">(.+?)</span>', str(list_of_price[i]))
        price = str(price).replace('\\xa0', '')
        
        if price.find('출고가') == -1:
            continue
        price_check.append(price[10:-3])

    # 데이터를
    for j in range(len(list_of_release)):
        # re.findall : list를 반환
        model = re.findall(r'<span class=" p16 clr100 b ln18">(.+?)</span>', str(list_of_model[j]))
        model = str(model).replace('\\xa0', '')
        release = re.findall(r'<div style="float:left;">(.+?)</div>', str(list_of_release[j]))
        release = str(release).replace('\\xa0', '')
        inch = re.findall(r'<li style="float:left;padding:3px;"><img alt="(.+?)"', str(list_of_inch[j]))
        inch = str(inch)
        reso = re.findall(r'<li style="float:left;padding:3px;"><img alt="(.+?)"', str(list_of_resol[j]))
        reso = str(reso)
        ossystem = re.findall(r'<li style="float:left;padding:3px;"><img alt="(.+?)"', str(list_of_os[j]))
        ossystem = str(ossystem)

        # 필요하지 않는 데이터 거르기
        if release[4:-2] == '미출시' or int(release[4:8]) < 2017:
            continue
        else:
            release_list.append(release[4:-2])
            model_list.append(model[2:-2])
            inch_list.append(inch[2:-2])
            price_list.append(price_check[j])
            resolution_list.append(reso[8:-2])
            os_list.append(ossystem[2:-2])

    page += 1


# 운영체제 명칭 지정
for i in range(len(os_list)):
    if os_list[i] == '운영체제 : [5]':
        os_list[i] = 'ios'
    elif os_list[i] == '운영체제 : [2]':
        os_list[i] = '안드로이드'

# 모델별로 리스트로 묶음
data2 = [[model_list[i], os_list[i], price_list[i], inch_list[i], resolution_list[i], release_list[i]] for i in
         range(len(model_list))]

# 필요하지 않은 데이터 제거
data3 = []
for i in range(0, len(data2)):
    if "폴더" not in data2[i][0] and data2[i][1] != "해당없음" and data2[i][2] != "미정":
        data3.append(data2[i])

# 데이터의 자료형 변경
for i in range(len(data3)):
    data3[i][2] = int(data3[i][2].replace(',', ''))
    data3[i][3] = float(data3[i][3].replace(' 인치', ''))


# 1차 필터링함수 - 입력한 운영체제로
def sys_func(os):
    os_filter = []
    if os == 'all':
        os_filter = data3
    else:
        for i in range(len(data3)):
            if data3[i][1] == os:
                os_filter.append(data3[i])
    os_filter.sort(key=lambda x: list(x)[2])
    os_filter.sort(key=lambda x: list(x)[1])
    return os_filter


# 2차 필터링함수 - 입력한 출고가 범위로
def price_func(min_pr, max_pr, y):
    price_filter = []
    if min_pr == -1 and max_pr == -1:
        price_filter = y
    else:
        for i in range(len(y)):
            if y[i][2] >= min_pr and y[i][2] <= max_pr:
                price_filter.append(y[i])
    return price_filter


# 3차 필터링함수 - 입력한 화면크기 범위로
def inch_func(min_inch, max_inch, y):
    inch_filter = []
    if min_inch == -1 and max_inch == -1:
        inch_filter = y
    else:
        for i in range(len(y)):
            if y[i][3] >= min_inch and y[i][3] <= max_inch:
                inch_filter.append(y[i])
    return inch_filter


# 4차 필터링함수 - 입력한 화질

def resol_func(resol, y):
    resolution = []
    if resol == 'all':
        resolution = y
    else:
        if resol == 'C':
            for i in range(len(y)):
                if int(y[i][4][:4]) < 1000:
                    resolution.append(y[i])
        if resol == 'B':
            for i in range(len(y)):
                if int(y[i][4][:4]) > 1000 and int(y[i][4][:4]) < 1300:
                    resolution.append(y[i])
        if resol == 'A':
            for i in range(len(y)):
                if int(y[i][4][:4]) > 1300:
                    resolution.append(y[i])
    return resolution


# OUT
def recomma(price):
    price = str(price)
    if len(price) <= 6:
        price = price[:-3] + ',' + price[-3:]
    else:
        price = price[:-6] + ',' + price[-6:-3] + ',' + price[-3:]
    return price


def num_of_hanguel(name):
    a = 0
    for i in name:
        if ord(i) > 122:
            a += 1
    return a


def item():
    print('모델명'.ljust(13), '운영체제'.ljust(6), '출고가'.center(7), '화면크기'.center(6), '화질'.center(11), '출시일'.center(4))


def result(one):
    print(one[0].ljust(16 - num_of_hanguel(one[0])), one[1].ljust(10 - num_of_hanguel(one[1])),
          recomma(one[2]).rjust(10), str(one[3]).center(10), one[4].center(13), one[5].rjust(7))


# 사용자에게 입력값 받아 결과 도출

os = input("원하는 운영체제를 입력하세요(ios or 안드로이드): ")
item()
for i in sys_func(os):
    result(i)

min_pr, max_pr = input("원하는 최저출고가와 최고출고가를 입력하세요(최저출고가, 최고출고가): ").split(",")
min_pr = int(min_pr)
max_pr = int(max_pr)
item()
for i in price_func(min_pr, max_pr, sys_func(os)):
    result(i)

min_inch, max_inch = input("원하는 디스플레이의 크기 범위를 입력하세요(min, max): ").split(",")
min_inch = float(min_inch)
max_inch = float(max_inch)
item()
for i in inch_func(min_inch, max_inch, price_func(min_pr, max_pr, sys_func(os))):
    result(i)

resol = input("원하는 화질의 등급을 선택해주세요(A(1440P*) or B(1080P*) or C(720P*)): ")
item()

for i in resol_func(resol, inch_func(min_inch, max_inch, price_func(min_pr, max_pr, sys_func(os)))):
    result(i)

#최종 필터린 된 결과값을 이용해서 웹페이지 열기
final=resol_func(resol, inch_func(min_inch, max_inch, price_func(min_pr, max_pr, sys_func(os))))

#가격 낮은 순서 4개 모델 저장.
for i in range(len(final)):
    encoding_model_list.append(quote(final[i][0]))

    if i == 3:
        break

#4개 모델명과 가격 필터값으로 네이버 쇼핑 웹페이지 열기
chrome_path = "C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s"

for i in range(len(encoding_model_list)):
    url_list.append('https://search.shopping.naver.com/search/all.nhn?origQuery=' + str(
        encoding_model_list[i]) + '&pagingIndex=1&pagingSize=40&viewType=list&sort=rel&minPrice=' + str(
        min_pr) + '&maxPrice=' + str(max_pr) + '&frm=NVSHPRC&query=' + str(encoding_model_list[i]))
    webbrowser.get(chrome_path).open(url_list[i])
