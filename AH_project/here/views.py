from django.shortcuts import render,redirect
from django.template.defaultfilters import linebreaksbr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import Text
from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def home(request):
    return render(request, 'home.html')

def location(request):
    return render(request, 'location.html')


def delete(request, name):
    t = Text.objects.get(id=name)
    t.delete()
    return redirect('/')

def text(request,title):
    text=Text()
    u=request.user
    text.title=title
    text.name=u.username
    text.text=request.GET['text1']
    text.save()

    t=Text.objects
    options = webdriver.ChromeOptions()
    options.add_argument('headless')

    driver = webdriver.Chrome("C:\\Users\\Keunyung\\Documents\\GitHub\\August_Hackathon\\chromedriver_win32\\chromedriver.exe")

    #,chrome_options=options -> 창안보이게 하기
    #혜진 경로 C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe
    print('크롤링 시작')
    driver.get('https://www.kmdb.or.kr/main')
    driver.find_element_by_name('mainSearchText').send_keys(title+Keys.ENTER)
    searchs = driver.find_elements_by_class_name('ftc-blue')
    for search in searchs:
        print(search.text)
        if search.text==title:
            search.click()
            break
    a=''
    contents=driver.find_elements_by_class_name('gab1')
    print(contents)
    for content in contents:
        a+=content.text
        print(content.text)

    print(a)
    #newstr = contents.replace("\n", "")

    
    split_contents = a.split(',')
    return render(request,'parsing.html',{'title':title,'contents':split_contents,'t':t})



def parse(request):
    t=Text.objects
    title = request.GET['parse_url']
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    
    driver = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe")
    # ,chrome_options=options -> 창안보이게 하기
    # 혜진 경로 C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe
    print('크롤링 시작')
    driver.get('https://www.kmdb.or.kr/main')
    driver.find_element_by_name('mainSearchText').send_keys(title+Keys.ENTER)
    searchs = driver.find_elements_by_class_name('ftc-blue')
    for search in searchs:
        print(search.text)
        if search.text==title:
            search.click()
            break
    a=''
    contents=driver.find_elements_by_class_name('gab1')
    print(contents)
    for content in contents:
        a+=content.text
        print(content.text)

    print(a)

    split_contents = a.split(',')
    return render(request,'parsing.html',{'title':title,'contents':split_contents,'t':t})
