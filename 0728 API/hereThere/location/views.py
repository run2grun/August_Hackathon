from django.shortcuts import render
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Create your views here.
def location(request):
    return render(request,'location.html')

def home(request):
    return render(request, 'home.html')

def parse(request):
    title = request.GET['parse_url']
    
    options = webdriver.ChromeOptions()
    options.add_argument('headless')
    
    driver = webdriver.Chrome("C:\\Users\\user\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")
    #,chrome_options=options
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

    return render(request,'parse.html',{'title':title,'contents':split_contents})