from django.shortcuts import render
from bs4 import BeautifulSoup
import requests

def main(request):
    info_url = 'http://www.kma.go.kr/wid/queryDFSRSS.jsp?zone=2723064500'
    res = requests.get(info_url)
    soup = BeautifulSoup(res.content, 'lxml') # pip install lxml 다운받아야 함
    
    location = soup.find('category').text # 위치 정보 갖고 오기 
    data_all = soup.find_all('data') # 모든 날씨 데이터 갖고 오기
    
    today = data_all[0] # 최신 날씨 데이터 갖고 오기
    now= today.find('temp').text # 기온 정보 갖고 오기
    sky = today. find('wfkor').text # 날씨 정보 갖고 오기

    for w in data_all:
        if w.find('day').text == '1' and w.find('hour').text == today.find('hour').text:
            tomorrow = w
            break
    to_temp = tomorrow.find('temp').text
    to_sky = tomorrow.find('wfkor').text

    return render(request, 'home.html', {'location': location, 'now':now, 'sky':sky, 'to_temp':to_temp, 'to_sky':to_sky})

def parse(request):
    url = request.POST['parse_url']
    res = requests.get('https://www.kmdb.or.kr/db/kor/detail/movie/K/15021'+ url) #해당 url로 GET 요청을 함
    

    parsed_page = BeautifulSoup(res.content, 'html.parser')
    
    title = parsed_page.find('dd').text #title 태그 찾아서 텍스트만 추출하기
    body = parsed_page.find(attrs = {'type2'} )
    contents = body.find('a').text # 첫 번째 p 태그의 텍스트 가져 오기 text 빼먹어서 안 됐었음
    return render(request, 'parsing.html', {'title': title, 'contents': contents})

# Create your views here.
