import allure
import requests
from data import Url, Flags

class TestOrdersList:

    @allure.title('Test get order list. Handle:/api/v1/orders')
    def test_successful_get_order_list(self):
        response_status = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}')
        assert response_status.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response_status.json()

    @allure.title('Test get order list with certain metro. Handle:/api/v1/orders')
    def test_successful_get_order_list_with_certain_metro(self, create_order_metro_1, create_order_metro_2):
        nearestStation = {'1': create_order_metro_1[0], '2': create_order_metro_2[0]}
        response_status = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}', params=nearestStation)
        assert response_status.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response_status.json()