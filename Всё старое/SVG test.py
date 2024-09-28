import svgwrite
from IPython.display import SVG, display

# Путь к файлам SVG частей пневмоцилиндра
front_cover_path = 'front_cover.svg'
rear_cover_path = 'rear_cover.svg'
barrel_path = 'barrel.svg'
rod_path = 'rod.svg'

# Функция для объединения частей в один SVG
def create_pneumatic_cylinder(output_file, barrel_length=100):
    # Создаем новый SVG файл
    dwg = svgwrite.Drawing(output_file, profile='tiny')

    # Добавляем заднюю крышку
    rear_cover = dwg.image(href=rear_cover_path, insert=(0, 50))
    dwg.add(rear_cover)

    # Добавляем гильзу
    barrel = dwg.image(href=barrel_path, insert=(50, 50))
    dwg.add(barrel)
    
    # Вычисляем смещение для передней крышки
    front_cover_x = barrel_length + 50  # Длина гильзы плюс смещение

    # Добавляем переднюю крышку
    front_cover = dwg.image(href=front_cover_path, insert=(front_cover_x, 50))
    dwg.add(front_cover)

    # Добавляем шток
    rod = dwg.image(href=rod_path, insert=(front_cover_x + 30, 50))  # Смещение штока
    dwg.add(rod)

    # Сохраняем итоговый SVG файл
    dwg.save()

    print(f"SVG файл пневмоцилиндра создан: {output_file}")

# Пример использования
create_pneumatic_cylinder('pneumatic_cylinder.svg', barrel_length=200)

# Отображение SVG файла
display(SVG('pneumatic_cylinder.svg'))

