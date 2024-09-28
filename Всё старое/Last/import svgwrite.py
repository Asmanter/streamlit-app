import svgwrite
import cairosvg

# Задайте размеры для изображений
rod_width = 3465  # Ширина изображения штока
rod_height = 5907  # Высота изображения штока
front_cover_width = 2967  # Ширина изображения передней крышки
front_cover_height = 5907  # Высота изображения передней крышки
rear_cover_width = 5836  # Ширина изображения задней крышки
rear_cover_height = 5907  # Высота изображения задней крышки
barrel_height = 5907  # Высота изображения гильзы (совпадает с высотой штока и крышки)
barrel_length = 100 * 30  # Задаем длину гильзы (можно изменять)

# Масштабирование
scale_factor = 0.01  # Скалируем итоговое изображение на 10%

# Рассчитываем общие размеры холста с учетом масштаба
canvas_width = (rod_width + front_cover_width + barrel_length + rear_cover_width) * scale_factor
canvas_height = max(rod_height, front_cover_height, barrel_height, rear_cover_height) * scale_factor

# Инициализация нового чертежа с нужным размером
dwg = svgwrite.Drawing('pnevmocilinder.svg', size=(canvas_width, canvas_height), profile='tiny')

# Координаты для вставки изображений (с масштабированием)
rod_x = 0
rod_y = 0

front_cover_x = rod_width * scale_factor  # Крышка будет следовать за штоком
front_cover_y = rod_y  # Совпадение по Y

barrel_x = (rod_width + front_cover_width) * scale_factor  # Гильза будет следовать за передней крышкой
barrel_y = rod_y  # Совпадение по Y

rear_cover_x = (rod_width + front_cover_width + barrel_length) * scale_factor  # Задняя крышка будет справа от гильзы
rear_cover_y = rod_y  # Совпадение по Y

# Добавление изображения штока с масштабированием
dwg.add(dwg.image('rod.svg', insert=(rod_x, rod_y), size=(rod_width * scale_factor, rod_height * scale_factor)))

# Добавление изображения передней крышки с масштабированием
dwg.add(dwg.image('front_cover.svg', insert=(front_cover_x, front_cover_y), size=(front_cover_width * scale_factor, front_cover_height * scale_factor)))

# Добавление изображения гильзы с масштабированием по X
dwg.add(dwg.image('barrel.svg', insert=(barrel_x, barrel_y), size=(barrel_length * scale_factor, barrel_height * scale_factor), preserveAspectRatio="none"))

# Добавление изображения задней крышки с масштабированием
dwg.add(dwg.image('rear_cover.svg', insert=(rear_cover_x, rear_cover_y), size=(rear_cover_width * scale_factor, rear_cover_height * scale_factor)))

# Сохранение чертежа в формате SVG
dwg.save()

# Преобразование SVG в PDF с использованием CairoSVG с тем же масштабом
cairosvg.svg2pdf(url="pnevmocilinder.svg", write_to="pnevmocilinder.pdf", output_width=canvas_width, output_height=canvas_height)
