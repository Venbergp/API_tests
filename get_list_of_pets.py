import get_api_key
import requests
import json

key = (get_api_key.get_key)
get_header_query = {"auth_key ": key, "filter": "my_pets"}
request_url = "https://petfriends1.herokuapp.com/api/pets?filter=my_pets"


def get_list_of_pets(url, header):
    r = requests.get(url, headers=header)
    print(f'\n Status-Code: {r.status_code}')
    print(f' Status: {r.status_code == requests.codes.ok}')
    templates = r.text
    dict_id = json.loads(templates)
    d = list(dict_id.values())
    print(f' ID и имя всех питомцев:')
    for i in range(len(d[0])):
        print({d[0][i]['name']}, {d[0][i]['id']})

    return d


get_list = get_list_of_pets(request_url, get_header_query)