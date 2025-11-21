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
        order_data = [create_order_metro_1, create_order_metro_2]
        params={"nearestStation": '["1", "2"]'}
        response_status = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}', params=params)
        stations = [s["number"] for s in response_status.json()["availableStations"]]
        assert "1" in stations
        assert "2" in stations
        assert "3" not in stations
        
    @allure.title('Test get empty order. Handle:/api/v1/orders')
    def test_get_empty_order_list(self):
        params={"nearestStation": '["!"]'}
        response_status = requests.get(f'{Url.MAIN_URL}{Url.GET_ORDER_LIST}', params=params)
        assert response_status.status_code == 200 and Flags.SUCCESSFUL_GET_ORDER_LIST in response_status.json()