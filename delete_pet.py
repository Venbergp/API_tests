import get_api_key
import get_list_of_pets
import requests


key = (get_api_key.get_key)
dct = get_list_of_pets.get_list

for i in range(len(dct[0])):
    if dct[0][i]['name'] == 'Boltik':
        pet_id = dct[0][i]['id']

delete_header_path = {"auth_key": key, "pet_id": pet_id}
request_url = "https://petfriends1.herokuapp.com/api/pets/" + pet_id


def delete(url, param, header):
    r = requests.delete(url, params=param, headers=header)
    if r.status_code == requests.codes.ok:
        print(f'\n Status-Code: {r.status_code}')
        print(f' Status: {r.status_code == requests.codes.ok}')
        print(' Питомец был удален')
    else:
        print(" PostError")


delete_pet = delete(request_url, delete_header_path, delete_header_path)
