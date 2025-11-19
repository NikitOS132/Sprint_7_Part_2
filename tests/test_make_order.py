import allure
import pytest
import requests
from data import Url, Flags, DataForOrder

class TestCreationOrder:

    @allure.title('Successful order creation with all color variations. Handle:/api/v1/orders')
    def test_create_order_with_different_colors(self, order_data_with_color):
        order_status = requests.post(url=f'{Url.MAIN_URL}{Url.CREATE_ORDER}', json=order_data_with_color)
        assert order_status.status_code == 201 and Flags.SUCCESSFUL_ORDER_CREATION in order_status.json()