from django.shortcuts import render
from bs4 import BeautifulSoup
import urllib.request
import urllib.parse

def main(request):
    return render(request, 'home.html')

def parse(request):
    # url = request.POST.get('parse_url','')
    # res = requests.get('https://www.kmdb.or.kr/db/kor/detail/movie/K/15021'+ url) #해당 url로 GET 요청을 함

    web_url = 'https://www.kmdb.or.kr/db/kor/detail/movie/K/15021'
    with urllib.request.urlopen(web_url) as response:
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
    # res = requests.get('https://www.kmdb.or.kr/db/kor/detail/movie/K/15021') #해당 url로 GET 요청을 함
    # parsed_page = BeautifulSoup(res.content, 'html.parser')
    
    title = soup.find('div', class_='na1').text #title 태그 찾아서 텍스트만 추출하기
    contents = soup.find('dd', class_='type2').text #.text 뒤에 더하면 에러난다 
    # 반복문으로 출력하는 방법????
    
    # body = soup.find(attrs = {'class': 'txtblue'} )
    # contents = body.find('a').text # 첫 번째 p 태그의 텍스트 가져 오기 text 빼먹어서 안 됐었음
    # return render(request, 'parse.html', {'title': title, 'contents': contents})
    return render(request, 'parse.html', {'title': title, 'contents':contents})