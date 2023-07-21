# Нагорный Антон, 6-я когорта — Финальный проект. Инженер по тестированию плюс
import requests

base_url = "https://c1b68e12-8fb1-43fe-ba1b-8d96ef9542f9.serverhub.praktikum-services.ru/api/v1"

def test_create_and_get_order():
    # Создать заказ
    create_order_payload = {
        "firstName": "Naruto",
        "lastName": "Uchiha",
        "address": "Konoha, 142 apt.",
        "metroStation": "4",
        "phone": "+7 800 355 35 35",
        "rentTime": 5,
        "deliveryDate": "2020-06-06",
        "comment": "Saske, come back to Konoha",
        "color": ["BLACK"]
    }

    response = requests.post(f"{base_url}/orders", json=create_order_payload)
    assert response.status_code == 201, "Failed to create order"

    # Номер трека заказа
    order_track = response.json().get("track")

    # Заказ по треку заказа
    get_order_payload = {
        "t": order_track
    }

    response = requests.get(f"{base_url}/orders/track", params=get_order_payload)
    assert response.status_code == 200, "Failed to get order by track"

    print("Тест успешно выполнен. Заказ создан и данные получены по треку заказа.")

if __name__ == "__main__":
    test_create_and_get_order()