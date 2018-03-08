import requests
from bs4 import BeautifulSoup

url = 'http://www.itest.info/courses' #定义被抓取页面的url
# 获取被抓取页面的html代码，并使用html.parser来实例化BeautifulSoup，属于固定套路
soup = BeautifulSoup(requests.get(url).text,'html.parser')
# 遍历页面上所有的h4
for course in soup.find_all('h4'):
    print(course.text) #打印出h4的text属性