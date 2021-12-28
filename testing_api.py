import pytest
import requests
import get_api_key
import get_list_of_pets
import create_pet
import add_information_about_new_pet
import add_photo
import delete_pet
import put_new_information


@pytest.fixture()
def get_api_key_fixture():
    get_api_key
    return True


def test_get_api_key(get_api_key_fixture):
    assert get_api_key_fixture == 1, "GetKey Error"


@pytest.fixture()
def get_list_fixture():
    get_list_of_pets
    return True


def test_get_list(get_list_fixture):
    assert get_list_fixture == 1, "GetList Error"


@pytest.fixture()
def post_simple_pet_fixture():
    create_pet
    return True


def test_post_simple_pet(post_simple_pet_fixture):
    assert post_simple_pet_fixture == 1, "PostSimplePet Error"


@pytest.fixture()
def post_add_info_fixture():
    add_information_about_new_pet
    return True


def test_post_add_info(post_add_info_fixture):
    assert post_add_info_fixture == 1, "PostAddInfo Error"


@pytest.fixture()
def post_set_photo_fixture():
    add_photo
    return True


def test_post_set_photo(post_set_photo_fixture):
    assert post_set_photo_fixture == 1, "SetPhoto Error"


@pytest.fixture()
def delete_pet_fixture():
    delete_pet
    return True


def test_delete_pet(delete_pet_fixture):
    assert delete_pet_fixture == 1, "DeletePet Error"


@pytest.fixture()
def put_pet_new_info_fixture():
    put_new_information
    return True


def test_put_new_pet(put_pet_new_info_fixture):
    assert put_pet_new_info_fixture == 1, "PutNewInfo Error"



