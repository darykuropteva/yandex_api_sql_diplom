# Дарья Куроптева, 39-я когорта — Финальный проект. Инженер по тестированию плюс

import configuration
import requests 
import data 

# POST-запрос на создание нового заказа и получение номера трека

def post_new_order_and_get_track(body):
    response = requests.post(
        configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
        json=body,
    )
    return response.json().get("track")

# GET-запрос для получения данных о заказе по номеру трека

def get_order_by_track(track):
    params = {"t": track}
    response = requests.get(
        configuration.URL_SERVICE + configuration.ORDER_TRACK_PATH,
        params=params
    )
    return response
