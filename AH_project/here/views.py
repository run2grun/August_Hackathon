from django.shortcuts import render,redirect,get_object_or_404
from django.template.defaultfilters import linebreaksbr
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from .models import Text,Movie
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

    driver = webdriver.Chrome("C:\\Users\\Keunyung\\Documents\\GitHub\\August_Hackathon\\AH_project\\here\\chromedriver_win32\\chromedriver.exe")

    #,chrome_options=options -> 창안보이게 하기
    #혜진 경로 C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe
    #근영 경로 C:\\Users\\Keunyung\\Documents\\GitHub\\August_Hackathon\\chromedriver_win32\\chromedriver.exe
    print('크롤링 시작')
    driver.get('https://www.kmdb.or.kr/main')
    driver.find_element_by_name('mainSearchText').send_keys(title+Keys.ENTER)
    searchs = driver.find_elements_by_class_name('ftc-blue')
    cnt=0
    for search in searchs:
        print(search.text)
        if cnt==1:
            print("click")
            search.click()
            break
    
    return render(request,'parsing.html',{'title':title,'contents':split_contents,'t':t})



def parse(request):
    t=Text.objects
    m=Movie.objects
    title = request.GET['parse_url']
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    
    driver = webdriver.Chrome("C:\\Users\\Keunyung\\Documents\\GitHub\\August_Hackathon\\AH_project\\here\\chromedriver_win32\\chromedriver.exe")
    # ,chrome_options=options -> 창안보이게 하기
    # 혜진 경로 C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe
    print('크롤링 시작')
    driver.get('https://www.kmdb.or.kr/main')
    driver.find_element_by_name('mainSearchText').send_keys(title+Keys.ENTER)
    searchs = driver.find_elements_by_class_name('ftc-blue')
    # for search in searchs:
    #     print(search.text)
    #     if search.text==title:
    #         search.click()
    #         break
    cnt=0
    for search in searchs:
        print(search.text)
        if cnt==1:
            print("click")
            search.click()
            break
        cnt=cnt+1

    for movie in m.all() :
        if movie.title == title:
            content=movie.text
            split_contents = content.split(',')
            check=1
            break

    if check == 0:
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        driver = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe")
        # ,chrome_options=options -> 창안보이게 하기
        # 혜진 경로 C:\\Users\\user\\Downloads\\chromedriver_win32\\chromedriver.exe
        print('크롤링 시작')
        driver.get('https://www.kmdb.or.kr/main')
        driver.find_element_by_name('mainSearchText').send_keys(title+Keys.ENTER)
        searchs = driver.find_elements_by_class_name('ftc-blue')
        cnt=0
        for search in searchs:
            print(search.text)
            if cnt==1:
                print("click")
                search.click()
                break
            cnt=cnt+1

        a=''
        contents=driver.find_elements_by_class_name('gab1')
        for content in contents:
            a+=content.text
            print(content.text)

        print(a)

        split_contents = a.split(',')

        M=Movie()
        M.title=title
        M.text=a
        M.save()

    return render(request,'parsing.html',{'title':title,'contents':split_contents,'t':t})
