from selenium import webdriver

url = 'https://www.zhihu.com/explore'
d = webdriver.Chrome()
d.get(url)

daily_div = d.find_element_by_css_selector('div[data-type="daily"]')

for link in daily_div.find_elements_by_css_selector('.question_link'):
    print(link.text)

d.quit()