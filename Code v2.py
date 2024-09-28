import svgwrite
import subprocess

# Задаем длину гильзы в мм
barrel_mm = 125
cover_to_cover_mm = barrel_mm + 94  # длина поршня, внутренностей гильзы + ширина крышек 39 + 55 = 94
pc_mm = cover_to_cover_mm + 48  # 48 - длина штока

# Задаем размеры для изображений
rod_width = 1609
rod_height = 2585
front_cover_width = 2039
front_cover_height = 2585
back_cover_width = 2588
back_cover_height = 2585
barrel_height = 2585
barrel_length = (barrel_mm * 27.7787) - 27.7787  # Перевод мм в пиксели
front_view_width = 1383  # Условный размер для вида спереди
front_view_height = 2585  # Совпадает с высотой других элементов

# Масштабирование
scale_factor = 0.2

# Рассчитываем общие размеры холста с учетом нового изображения (вид спереди) и масштаба
canvas_width = (rod_width + front_cover_width + barrel_length + back_cover_width + front_view_width + 100) * scale_factor  # +100 - отступ между back_cover и видом спереди
canvas_height = max(rod_height, front_cover_height, barrel_height, back_cover_height, front_view_height) * scale_factor

# Инициализация нового чертежа с профилем 'full'
dwg = svgwrite.Drawing('pc.svg', size=(canvas_width, canvas_height), profile='full')

# Координаты для вставки изображений
rod_x = 0
rod_y = 0

front_cover_x = rod_width * scale_factor
front_cover_y = rod_y

barrel_x = (rod_width + front_cover_width) * scale_factor
barrel_y = rod_y

back_cover_x = (rod_width + front_cover_width + barrel_length) * scale_factor
back_cover_y = rod_y

# Добавляем отступ для вида спереди
front_view_offset = 100  # Отступ, который можно изменить по вашему желанию

# Координаты для вида спереди на ПЦ
front_view_x = (rod_width + front_cover_width + barrel_length + back_cover_width + front_view_offset) * scale_factor
front_view_y = rod_y

# Добавление изображений
dwg.add(dwg.image('rod.svg', insert=(rod_x, rod_y), size=(rod_width * scale_factor, rod_height * scale_factor)))
dwg.add(dwg.image('front_cover.svg', insert=(front_cover_x, front_cover_y), size=(front_cover_width * scale_factor, front_cover_height * scale_factor)))
dwg.add(dwg.image('barrel.svg', insert=(barrel_x, barrel_y), size=(barrel_length * scale_factor, barrel_height * scale_factor), preserveAspectRatio="none"))
dwg.add(dwg.image('back_cover.svg', insert=(back_cover_x, back_cover_y), size=(back_cover_width * scale_factor, back_cover_height * scale_factor)))

# Добавление вида спереди на ПЦ
dwg.add(dwg.image('front_view.svg', insert=(front_view_x, front_view_y), size=(front_view_width * scale_factor, front_view_height * scale_factor)))

# Позиция текста: среднее значение между передней крышкой, гильзой и задней крышкой + смещение на длину штока
text_x = (2000 + (rod_width + 443) + rod_width + front_cover_width + barrel_length + 831) / 2 * scale_factor  # 2000 - поправка на смещение
text_y = 2253 * scale_factor

# Позиция текста для ПЦ: среднее значение между передней крышкой, гильзой и задней крышкой + смещение на длину штока
text_xpc = ((2000 + 728 + rod_width + front_cover_width + barrel_length + 831) / 2) * scale_factor
text_ypc = 2417 * scale_factor

# Размер шрифта
font_size = 123 * scale_factor

# Вычисление ширины текста (приблизительно)
text_length = font_size * len(str(int(barrel_mm))) * 0.5  # Приблизительная ширина текста
text_x -= text_length / 2  # Смещение на половину ширины текста

# Добавление текста с указанием длины гильзы
dwg.add(dwg.text(
    f"{int(cover_to_cover_mm)}",
    insert=(text_x, text_y),
    font_size=font_size,
    font_family="GOST Type A",  # Оставляем шрифт
    fill="black",
    transform="skewX(-25)"  # Имитируем курсив через наклон
))

dwg.add(dwg.text(
    f"{int(pc_mm)}",
    insert=(text_xpc, text_ypc),
    font_size=font_size,
    font_family="GOST Type A",  # Оставляем шрифт
    fill="black",
    transform="skewX(-25)"  # Имитируем курсив через наклон
))

# Добавление линий и точек
line_y_position = rod_y + rod_height * scale_factor + 20  # Позиция по Y для линии и точек

# Определяем количество линий и расстояние между ними
num_lines = 3  # Количество линий
line_length = 300 * scale_factor  # Длина линий
spacing = 60 * scale_factor  # Расстояние между линиями

for i in range(num_lines):
    # Позиция по Y для текущей линии
    current_line_y = line_y_position + i * spacing
    
    # Добавляем линию
    dwg.add(dwg.line(start=(0, current_line_y), end=(line_length, current_line_y), stroke='black', stroke_width=2))
    
    # Добавляем точки под линиями
    for j in range(5):  # Количество точек
        point_x = j * (line_length / 4)  # Расчет позиции по X для точек
        dwg.add(dwg.circle(center=(point_x, current_line_y + 5), r=5, fill='black'))  # Отодвигаем точки немного вниз

# Сохранение SVG файла
dwg.save()

# Преобразование SVG в PDF через Inkscape
subprocess.run([r'D:\Programs\Inkscape\bin\inkscape.exe', 'pc.svg', '--export-filename=pc.pdf'])
