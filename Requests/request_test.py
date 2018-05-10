'''
import requests

url = 'https://www.v2ex.com/api/nodes/show.json'

querystring = {'name':'python'}

headers = {
    'cache-control':'no-cache',
    'postman-token': "a596dcc5-ab8b-8456-79c7-94a6ac11378e"
}

response = requests.request("GET",url,headers=headers,params=querystring)
print(response.text)
'''
'''
import requests
import unittest

class V2exAPITestCase(unittest.TestCase):
    def test_node_api(self):
        url = "https://www.v2ex.com/api/nodes/show.json"
        querystring = {'name':'python'}
        response = requests.request("GET",url,params=querystring).json()
        self.assertEqual(response['name'],'python')
        self.assertEqual(response['id'],90)


if __name__ == '__main__':
    unittest.main()
'''
'''
import requests

r = requests.get('http://github.com',timeout=0.001)
print(r.text)
'''
'''
import requests

r = requests.get('https://api.github.com/events')
print(r.status_code)
print(r.text)
'''
'''
import requests

r = requests.post('http://httpbin.org/post',data={'key':'value'})
print(r.status_code)
print(r.text)
'''