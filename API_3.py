import requests
import io
from PIL import Image
from staticmap import StaticMap, CircleMarker

def get_satellite_image(latitude, longitude, zoom=15, size=(640, 640)):


    # Создаем статическую карту
    m = StaticMap(size[0], size[1], url_template='https://tile.openstreetmap.org/{z}/{x}/{y}.png')

    # Добавляем маркер на карту
    marker = CircleMarker((longitude, latitude), '#FF0000', 10)
    m.add_marker(marker)

    # Получаем изображение карты
    image = m.render(zoom=zoom)

    # Сохраняем изображение в файл
    image.save('map3.png')

# Пример использования
latitude = 48.858093
longitude = 2.294694

get_satellite_image(latitude, longitude)

print(f"Спутниковый снимок сохранен в файл map3.png")