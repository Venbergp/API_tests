# API_tests
Работа с Api

# Задания

Зарегистрироваться: https://petfriends1.herokuapp.com
Ознакомиться с документацией API: https://petfriends1.herokuapp.com/apidocs/#/
Написать приложение содержащие функции работы с API:
        реализовать методы:
        GET, 
        POST, 
        PUT, 
        DELETE
Написать тесты для функций работы с API
             Тесты должны содержать позитивные и негативные сценарии
             Необходимо сделать параметризацию
             Необходимо использовать фикстуры 
Запустить  тесты и сделать скриншот
Создаем файл README.md, с описанием приложения
Загружаем файлы на Github

# Код

Первое, что нам нужно - это получить клучь для работы с API

Сначала мы вводим ссылку на нужный API и Регистрационные данные

<img width="473" alt="image" src="https://user-images.githubusercontent.com/90000544/147555563-3c508bb2-98bf-4f9b-87c0-d3e93f45081b.png">

Затем мы запрашиваем ключ

<img width="476" alt="image" src="https://user-images.githubusercontent.com/90000544/147555764-0a0c5b66-4162-4d51-a9ed-5c01c1220e89.png">

Получаенный ключ поможет нам работать с другими API

Во время работы с API мы будем использовать несколько видов запросов 
POST - если нужно что-то отправить
GET - если нужно что-то забрать
DELETE - удалить из базы данных
PUT - добавить в базу данных

Рассмотрим взаимодействие с API каждого типа

Тип GET используется при получении списка животных

<img width="473" alt="image" src="https://user-images.githubusercontent.com/90000544/147556112-29b8a414-0c69-4a70-8a9c-5ddb82d5963b.png">

Тип POST используется при добавлении информации к животному

<img width="935" alt="image" src="https://user-images.githubusercontent.com/90000544/147556261-330fb41e-22bd-4a1b-ba4b-f11b8a969680.png">

После применения на сайте появляется наше животное, правда пока без фотки 

<img width="282" alt="image" src="https://user-images.githubusercontent.com/90000544/147556361-c67a646a-c53f-42ca-b9ad-5fbb61f269b7.png">


Теперь нужно добавить ему фотку

Используем для этого также API с методом POST

Парсим всех животных, находим id нашего и меняем ему фоточку

<img width="924" alt="image" src="https://user-images.githubusercontent.com/90000544/147556851-f408295c-0c16-4f44-8b16-7bd616de75f2.png">

Теперь посмотрим, как использовать метод DELETE

Сначала мы парсим всех животных и находим нужное, затем удаляем по id

<img width="527" alt="image" src="https://user-images.githubusercontent.com/90000544/147557385-e0ae1b99-7b39-4e2a-a9d8-cfa1a403f5a7.png">

Метод PUT мы используем, когда нужно загрузить новую информацию в питомца, мы его так же находим по id и загружаем что нам нужно в. 
Сначала мы парсим всех животных и находим нужное, затем удаляем по idбазу данных

<img width="936" alt="image" src="https://user-images.githubusercontent.com/90000544/147557556-220a76f3-9f39-4403-9d0e-cc3d73acc4c2.png">


Теперь проведем тесты наших программ
Будем использовать pytest

Делаем все, как в первой лабораторной работе, получаем:

<img width="656" alt="image" src="https://user-images.githubusercontent.com/90000544/147558030-57dbd6cf-243d-49de-9c29-1e5bafa6723d.png">

Все тесты пройдены, все хорошо работает, покрытие 100%
