import requests
import json

request_url = 'https://petfriends1.herokuapp.com/api/key'
get_email_pass_header = {'email': 'artemgrebnev@gmail.com',
                         'password': 'Sobaka123'}


def get_API_key(url, header):
    r = requests.get(url, headers=header)
    print(f' Status-Code: {r.status_code}')
    print(f' Status: {r.status_code == requests.codes.ok}')
    templates = r.text
    dict_key = json.loads(templates)
    key = dict_key['key']
    print(f' Earned key: {key}')
    return key


get_key = get_API_key(request_url, get_email_pass_header)

