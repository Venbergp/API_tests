import get_api_key
import get_list_of_pets
import requests

key = (get_api_key.get_key)
dct = get_list_of_pets.get_list

for i in range(len(dct[0])):
    if dct[0][i]['name'] == 'Boltik':
        pet_id = dct[0][i]['id']

put_header_path_formData = {"auth_key": key, "pet_id": pet_id, "name": "Boltik", "animal_type": "Pitbull", "age": "1"}
request_url = "https://petfriends1.herokuapp.com/api/pets/" + pet_id


def rename(url, param, header):
    r = requests.put(url, params=param, headers=header)
    if r.status_code == requests.codes.ok:
        print(f'\n Status-Code: {r.status_code}')
        print(f' Status: {r.status_code == requests.codes.ok}')
        print(' Питомец был переименован')
    else:
        print(" PostError")


put_new_info = rename(request_url, put_header_path_formData, put_header_path_formData)
