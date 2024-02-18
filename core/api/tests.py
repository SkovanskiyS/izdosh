from django.test import TestCase

# Create your tests here.
import requests

url = 'http://172.24.200.54:8000/api/v1/image_process/'
json_data = {'data':'Hello World'}
res = requests.post(url=url, json=json_data)
print(res.status_code)
print(res)

