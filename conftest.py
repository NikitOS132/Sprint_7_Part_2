import pytest
import requests
import generators
from data import Url

@pytest.fixture
def create_courier():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier_body)
    login_courier = requests.post(url= f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body)
    yield [create_courier_body, login_courier_body, login, password]
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()["id"]}')

@pytest.fixture
def generate_courier_data():
    login = generators.login_generator()
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'password': password, 'first_name': name}
    login_courier_body = {'login': login, 'password': password}
    yield [create_courier_body, login_courier_body]
    login_courier = requests.post(url= f'{Url.MAIN_URL}{Url.COURIER_LOGIN}', json=login_courier_body)
    requests.delete(f'{Url.MAIN_URL}{Url.COURIER_DELETE}{login_courier.json()["id"]}')

@pytest.fixture
def create_courier_no_login():
    password = generators.password_generator()
    name = generators.name_generator()
    create_courier_body = {'password': password, 'first_name': name}
    requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier_body)
    yield [create_courier_body]

@pytest.fixture
def create_courier_no_password():
    login = generators.login_generator()
    name = generators.name_generator()
    create_courier_body = {'login': login, 'first_name': name}
    requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_COURIER}', json=create_courier_body)
    yield [create_courier_body]

@pytest.fixture(params=[["BLACK"], ["GREY"], ["BLACK", "GREY"], []])
def order_data_with_color(request):
    firstName = generators.first_name_generator()
    lastName = generators.last_name_generator()
    address = "Buzheninova 9"
    metroStation = generators.metro_generator()
    phone = generators.phone_generator()
    rent_time = 2
    delivery_date = "2024-10-15"
    color = request.param
    comment = generators.comment_generator()
    
    create_order_body = {
        'firstName': firstName, 
        'lastName': lastName, 
        'address': address, 
        'metroStation': metroStation, 
        'phone': phone, 
        'rent_time': rent_time, 
        'delivery_date': delivery_date, 
        'color': color, 
        'comment': comment
    }
    ready_order = requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=create_order_body)
    yield create_order_body
    requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{ready_order.json()["track"]}')

@pytest.fixture
def create_order_metro_1():
    from data import DataForOrder
    order_data = DataForOrder.user_data.copy()
    order_data['metroStation'] = 1
    order = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
    track = order.json()['track']
    yield track
    requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{track}')

@pytest.fixture
def create_order_metro_2():
    from data import DataForOrder
    order_data = DataForOrder.user_data.copy()
    order_data['metroStation'] = 2
    order = requests.post(f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
    track = order.json()['track']
    yield track
    requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{track}')