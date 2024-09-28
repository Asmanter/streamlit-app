import tkinter as tk
from PIL import Image, ImageDraw, ImageFont

# Функция для создания чертежа
def create_drawing():
    try:
        # Получаем введенные значения
        barrel_length = int(entry_barrel.get())
        rod_length = int(entry_rod.get())
        
        # Открываем исходные изображения деталей
        front_cover = Image.open('front_cover.png').convert('RGBA')
        rear_cover = Image.open('rear_cover.png').convert('RGBA')
        barrel = Image.open('barrel.png').convert('RGBA')
        rod = Image.open('rod.png').convert('RGBA')
        
        # Изменяем размер гильзы по горизонтали на основе введенной длины
        barrel = barrel.resize((round(barrel_length * 8.3), barrel.height))  # 8.3 - коэффициент пересчёта
        
        # Создаем новое изображение для финального результата
        result_width = rod.width + front_cover.width + barrel.width + rear_cover.width
        result_height = max(front_cover.height, barrel.height, rear_cover.height, rod.height)
        result = Image.new('RGBA', (result_width, result_height), (255, 255, 255, 0))
        
        # Вставляем элементы на изображение
        result.paste(rod, (0, (result_height - rod.height) // 2), rod)
        result.paste(front_cover, (rod.width, (result_height - front_cover.height) // 2), front_cover)
        result.paste(barrel, (rod.width + front_cover.width, (result_height - barrel.height) // 2), barrel)
        result.paste(rear_cover, (rod.width + front_cover.width + barrel.width, (result_height - rear_cover.height) // 2), rear_cover)
        
        # Добавляем текст (длину гильзы и штока)
        draw = ImageDraw.Draw(result)
        text = f"Гильза: {barrel_length} мм, Шток: {rod_length} мм"
        font_path = "/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf"
        font = ImageFont.truetype(font_path, 38)
        draw.text((10, 10), text, fill="black", font=font)
        
        # Сохраняем изображение
        result.save('pneumatic_cylinder_drawing.png')
        
        # Отображаем результат в метке
        label_result.config(text=f"Чертеж создан! Гильза: {barrel_length} мм, Шток: {rod_length} мм\nИзображение сохранено как 'pneumatic_cylinder_drawing.png'")
    except Exception as e:
        label_result.config(text=f"Ошибка: {str(e)}")

# Создаем главное окно
root = tk.Tk()
root.title("Приложение для чертежей пневмоцилиндров")
root.geometry("500x400")

# Метка и поле ввода для длины гильзы
label_barrel = tk.Label(root, text="Введите длину гильзы (мм):", font=("Arial", 12))
label_barrel.pack(pady=5)

entry_barrel = tk.Entry(root, width=10)
entry_barrel.pack(pady=5)

# Метка и поле ввода для длины штока
label_rod = tk.Label(root, text="Введите длину штока (мм):", font=("Arial", 12))
label_rod.pack(pady=5)

entry_rod = tk.Entry(root, width=10)
entry_rod.pack(pady=5)

# Кнопка для создания чертежа
button_create = tk.Button(root, text="Создать чертеж", command=create_drawing)
button_create.pack(pady=20)

# Метка для отображения результата
label_result = tk.Label(root, text="", font=("Arial", 12))
label_result.pack(pady=10)

# Запуск главного цикла программы
root.mainloop()
