"""
http://finviz.com/quote.ashx?t=NVDA 는 미국주식 NVIDIA에 대한 데이터 테이블이 있습니다.
이 테이블은 HTML코드로 정렬되어 있는데 CSV 파일로 만들 전에 이것들을 제거 해야 합니다.
BeautifulSoup와 getText() 함수를 써서 짧은 코드로 그 일을 할 수 있습니다.
"""
import csv
import requests
from bs4 import BeautifulSoup as bs

# csv로 파일 쓰기
csvFile = open("nvda_fundamental.csv", "wt")
writer = csv.writer(csvFile)

ticker = "NVDA".lower()
url = f'http://finviz.com/quote.ashx?t={ticker}'

req = requests.get(url, headers=headers)
html = req.text

# html을 기본 파서로 사용하지만, lxml 파서가 더 빨리 작동하므로 lxml을 사용한다.
soup = bs(html, 'lxml')

names = soup.findAll(class_='snapshot-td2-cp')
datas = soup.findAll(class_='snapshot-td2')

try:
    for i in range(len(names)):
        name = names[i].getText()
        data = datas[i].getText()
        writer.writerow(("NVDA", name, data))
finally:
    csvFile.close()


"""
함수로 구현
"""


def getFinancialRatioUS(symbol, item):
    try:
        symbol = symbol.lower()
        url = f'http://finviz.com/quote.ashx?t={symbol}'

        req = requests.get(url, headers=headers)
        html = req.text
        soup = bs(html, 'lxml')
        pb = soup.find(text=item)
        pb_ = pb.find_next(class_='snapshot-td2').text
        return pb_
    except Exception as e:
        print(e)


# NVDA psr 파싱
psr = getFinancialRatioUS("NVDA", "P/S")
print(psr)
