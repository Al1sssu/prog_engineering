import folium
from geopy.distance import geodesic

# Задаем последовательность точек
points = [(48.858093, 2.294694), (48.860321, 2.297066), (48.862549, 2.299438), (48.864777, 2.301810)]

# Вычисляем длину пути
total_distance = 0
for i in range(len(points) - 1):
    total_distance += geodesic(points[i], points[i+1]).km

print(f"Длина пути: {total_distance:.2f} км")

# Создаем карту, центрированную на средней точке пути
center_lat = sum(point[0] for point in points) / len(points)
center_lon = sum(point[1] for point in points) / len(points)
map_center = (center_lat, center_lon)
map_zoom = 14
map = folium.Map(location=map_center, zoom_start=map_zoom)

# Добавляем маршрут на карту
folium.PolyLine(locations=points, color="red", weight=3, opacity=0.5).add_to(map)

# Добавляем метку в средней точке пути
folium.Marker(location=map_center, icon=folium.Icon(color="blue", icon="info-sign")).add_to(map)

# Сохраняем карту в HTML-файл
map.save("map2.html")
