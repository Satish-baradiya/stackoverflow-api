import requests
import json

response = requests.get('https://api.stackexchange.com/2.3/questions?order=desc&sort=activity&site=stackoverflow')
check = ['python','Python','flask','Flask','django','Django']
for data in response.json()['items']:
    for checked in check:
        if data['answer_count'] == 0 and checked in data['title']:
            print(data['title'])
            print(data['link'])
