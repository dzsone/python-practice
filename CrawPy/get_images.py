import requests
from bs4 import BeautifulSoup

headers = {'user-agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_1) AppleWebKit/537.66 (KHTML, like Gecko) Chrome/57.0.2987.133 Safari/537.36)'}

def download_file(url):
    print('Download %s' %url)
    local_filename = url.split('/')[-1]
    r = requests.get(url,stream = True,headers = headers)
    with open(local_filename,'wb') as f :
        for chunk in r.iter_content(chunk_size=1024):
            if chunk :
                f.write(chunk)
                f.flush()
    return local_filename

url = 'http://jandan.net/drawings'
soup = BeautifulSoup(requests.get(url,headers=headers).text,'html.parser')

def valid_img(src):
    return src.endswith('jpg') and 'img.jandan.net' in src

for img in soup.find_all('img',src = valid_img):
    src = img['src']
    if not src.starswith('http'):
        src = 'http:' + src
    download_file(src)