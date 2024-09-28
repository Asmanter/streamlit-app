import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageDraw, ImageFont

# Функция для создания текста на изображении
def add_text_to_image(image, text, position, font_path, font_size, color="black"):
    draw = ImageDraw.Draw(image)
    font = ImageFont.truetype(font_path, font_size)
    draw.text(position, text, fill=color, font=font)

# Функция для генерации изображения гильзы
def generate_barrel_image():
    try:
        barrel_length = int(entry.get())  # Получаем длину гильзы из поля ввода
        if barrel_length > 0:
            # Загрузка изображений
            front_cover = Image.open('front_cover.png').convert('RGBA')
            rear_cover = Image.open('rear_cover.png').convert('RGBA')
            barrel = Image.open('barrel.png').convert('RGBA')
            rod = Image.open('rod.png').convert('RGBA')
            output_file = 'pneumatic_cylinder_with_text_on_barrel.png'
            
            # Путь к шрифту
            font_path = "C:\\Windows\\Fonts\\arial.ttf"
            
            if barrel_length > 100:
                # Используем специальное изображение для больших гильз
                barrel_big = Image.open('barrel_big.png').convert('RGBA')
                image_with_text = barrel_big.copy()
                
                # Добавляем текст
                text = f"{barrel_length}"
                add_text_to_image(image_with_text, text, (1401, 655), font_path, 38)
                
                # Сохраняем изображение
                image_with_text.save(output_file)
                print(f"Saved big barrel image to {output_file}")
            else:
                # Изменяем размер гильзы
                new_barrel = barrel.resize((round(barrel_length * 8.3), barrel.height))
                
                # Создаем новое изображение для результата
                result = Image.new('RGBA', (
                    rod.width + front_cover.width + new_barrel.width + rear_cover.width,
                    max(front_cover.height, new_barrel.height, rear_cover.height, rod.height)
                ), (255, 255, 255, 0))

                # Вычисляем вертикальные смещения для выравнивания элементов
                barrel_y_position = (result.height - new_barrel.height) // 2
                front_cover_y_position = (result.height - front_cover.height) // 2
                rear_cover_y_position = (result.height - rear_cover.height) // 2
                rod_y_position = (result.height - rod.height) // 2

                # Вставляем элементы
                result.paste(rod, (0, rod_y_position), rod)
                result.paste(front_cover, (rod.width, front_cover_y_position), front_cover)
                result.paste(new_barrel, (rod.width + front_cover.width, barrel_y_position), new_barrel)
                result.paste(rear_cover, (rod.width + front_cover.width + new_barrel.width, rear_cover_y_position), rear_cover)
                
                # Добавляем текст
                text = f"{barrel_length}"
                text_x_position = rod.width + front_cover.width + (new_barrel.width // 2) - 25
                text_y_position = barrel_y_position + new_barrel.height - 58
                add_text_to_image(result, text, (text_x_position, text_y_position), font_path, 38)
                
                # Сохраняем изображение
                result.save(output_file)
                print(f"Saved result image with text to {output_file}")
            
            messagebox.showinfo("Успех", f"Изображение гильзы длиной {barrel_length} мм создано.")
        else:
            messagebox.showerror("Ошибка", "Длина гильзы должна быть больше 0.")
    except ValueError:
        messagebox.showerror("Ошибка", "Введите корректное числовое значение.")

# Создание интерфейса
root = tk.Tk()
root.title("Генератор изображений гильзы")

label = tk.Label(root, text="Введите длину гильзы (мм):")
label.pack()

entry = tk.Entry(root)
entry.pack()

button = tk.Button(root, text="Создать изображение", command=generate_barrel_image)
button.pack()

root.mainloop()
