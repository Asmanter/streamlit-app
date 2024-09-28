import svgwrite
import subprocess

# Задайте размеры для изображений
rod_width = 1609  # Ширина изображения штока
rod_height = 2585  # Высота изображения штока
front_cover_width = 2039  # Ширина изображения передней крышки
front_cover_height = 2585  # Высота изображения передней крышки
back_cover_width = 2588  # Ширина изображения задней крышки
back_cover_height = 2585  # Высота изображения задней крышки
barrel_height = 2585  # Высота изображения гильзы (совпадает с высотой штока и крышки)
barrel_length = (186 * 27.7787) - 27.7787   # Задаем длину гильзы (можно изменять)

# Масштабирование
scale_factor = 0.2  # Скалируем итоговое изображение на 20%

# Рассчитываем общие размеры холста с учетом масштаба
canvas_width = (rod_width + front_cover_width + barrel_length + back_cover_width) * scale_factor
canvas_height = max(rod_height, front_cover_height, barrel_height, back_cover_height) * scale_factor

# Инициализация нового чертежа с нужным размером
dwg = svgwrite.Drawing('pc.svg', size=(canvas_width, canvas_height), profile='tiny')

# Координаты для вставки изображений (с масштабированием)
rod_x = 0
rod_y = 0

front_cover_x = rod_width * scale_factor  # Крышка будет следовать за штоком
front_cover_y = rod_y  # Совпадение по Y

barrel_x = (rod_width + front_cover_width) * scale_factor  # Гильза будет следовать за передней крышкой
barrel_y = rod_y  # Совпадение по Y

back_cover_x = (rod_width + front_cover_width + barrel_length) * scale_factor  # Задняя крышка будет справа от гильзы
back_cover_y = rod_y  # Совпадение по Y

# Добавление изображения штока с масштабированием
dwg.add(dwg.image('rod.svg', insert=(rod_x, rod_y), size=(rod_width * scale_factor, rod_height * scale_factor)))

# Добавление изображения передней крышки с масштабированием
dwg.add(dwg.image('front_cover.svg', insert=(front_cover_x, front_cover_y), size=(front_cover_width * scale_factor, front_cover_height * scale_factor)))

# Добавление изображения гильзы с масштабированием по X
dwg.add(dwg.image('barrel.svg', insert=(barrel_x, barrel_y), size=(barrel_length * scale_factor, barrel_height * scale_factor), preserveAspectRatio="none"))

# Добавление изображения задней крышки с масштабированием
dwg.add(dwg.image('back_cover.svg', insert=(back_cover_x, back_cover_y), size=(back_cover_width * scale_factor, back_cover_height * scale_factor)))

# Сохранение чертежа в формате SVG
dwg.save()

# Преобразование SVG в PDF с использованием Inkscape через командную строку
import subprocess

subprocess.run([r'D:\Programs\Inkscape\bin\inkscape.exe', 'pc.svg', '--export-filename=pc.pdf'])