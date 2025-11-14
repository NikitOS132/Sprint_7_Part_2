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

@pytest.fixture
def create_order():
    firstName = generators.first_name_generator()
    lastName = generators.last_name_generator()
    address = "Buzheninova 9"
    metroStation = "2"
    phone = generators.phone_generator()
    rent_time = 2
    delivery_date = "2024-10-15"
    comment = generators.comment_generator()
    create_order_body = {'firstName': firstName, 'lastName': lastName, 'address': address, 'metroStation': metroStation, 'phone': phone, 'rent_time': rent_time, 'delivery_date': delivery_date, 'comment': comment}
    ready_order = requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=create_order_body)
    yield [create_order_body]
    requests.put(f'{Url.MAIN_URL}{Url.ORDER_CANCEL}{ready_order.json()["track"]}')