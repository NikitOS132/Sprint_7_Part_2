import allure
import requests
from data import Url, MetroStationList

class TestCreationOrder:

    @allure.title('Successful order creation with all color variations. Handle:/api/v1/orders')
    def test_create_order_with_different_colors(self, create_order):
        order_data = create_order
        order_status = requests.post(url= f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data)
        print(order_status.url)
        print(order_status.status_code)
        print(order_status.json())
        print(order_status.content)