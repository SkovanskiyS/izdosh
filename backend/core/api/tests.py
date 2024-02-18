from django.test import TestCase

# Create your tests here.
# import requests
#
# url = 'http://172.24.200.54:8000/api/v1/image_process/'
# json_data = {'data':'Hello World'}
# res = requests.post(url=url, json=json_data)
# print(res.status_code)
# print(res)
#


import requests
import json

url = "https://mohir.ai/api/v1/tts"
api_key = "d63a8f3f-8cd4-478c-a6c5-33c76a13676b:f076d6fe-cda5-4232-8c6d-8dea1de6025d"
webhook_url = "https://hooks.zapier.com/hooks/catch/17974498/3ehvuok/"

headers = {
    'Authorization': f'{api_key}',
    'Content-Type': 'application/json',
}

data = {
    "text": "Salom dunyo",
    "model": "dilfuza",
    "mood": "happy",
    "blocking": False,
    "webhook_notification_url": webhook_url,
}

response = requests.post(url, headers=headers, data=json.dumps(data))
print(response.text)



