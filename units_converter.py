print('Конвертация единиц измерения температуры из метрической в неметрическую')

temperature = int(input(' 1. Цельсий -> Фаренгейт\n 2. Цельсий -> Кельвин\n'))
if temperature == 1:
  temperature_celsius = float(input('Введите значение температуры по Цельсию:\n'))
  print(temperature_celsius, 'градусов по Цельсию =', round((((9/5) * temperature_celsius +32)), 2),'градусов по Фаренгейту')
elif temperature == 2:
  temperature_сelsius = float(input('Введите значение температуры по Цельсию:\n'))
  print(temperature_сelsius, 'градусов по Цельсию =', round((temperature_сelsius + 273.15), 2),'градусов по Кельвину')