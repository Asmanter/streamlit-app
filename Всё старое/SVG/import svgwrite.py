import svgwrite
import tkinter as tk
from tkinter import messagebox, filedialog
import os

def generate_barrel_image():
    try:
        barrel_length = int(entry.get())  # Получаем длину гильзы из поля ввода
        if barrel_length > 0:
            # Создаем новый SVG-файл
            dwg = svgwrite.Drawing('pneumatic_cylinder.svg', profile='tiny')

            # Пути к SVG-файлам деталей
            front_cover_path = 'front_cover.svg'
            rear_cover_path = 'rear_cover.svg'
            barrel_path = 'barrel.svg'
            rod_path = 'rod.svg'

            # Проверяем, существуют ли файлы
            if not all(os.path.exists(path) for path in [front_cover_path, rear_cover_path, barrel_path, rod_path]):
                messagebox.showerror("Ошибка", "Не найдены все SVG файлы.")
                return

            # Вставляем переднюю крышку
            front_cover = dwg.image(href=front_cover_path, insert=(100, 100), size=("60px", "60px"))
            dwg.add(front_cover)

            # Вставляем заднюю крышку
            rear_cover = dwg.image(href=rear_cover_path, insert=(100 + barrel_length + 60, 100), size=("60px", "60px"))
            dwg.add(rear_cover)

            # Вставляем гильзу и изменяем её длину
            barrel = dwg.rect(insert=(130, 70), size=(f'{barrel_length}px', '60px'), fill='lightgreen', stroke='black', stroke_width=2)
            dwg.add(barrel)

            # Вставляем шток
            rod = dwg.image(href=rod_path, insert=(50, 90), size=("80px", "20px"))
            dwg.add(rod)

            # Добавляем текст (длину гильзы)
            dwg.add(dwg.text(f'{barrel_length} мм', insert=(130 + barrel_length // 2, 150), font_size='20px', fill='black'))

            # Путь для сохранения файла
            output_file = filedialog.asksaveasfilename(defaultextension=".svg", filetypes=[("SVG files", "*.svg"), ("All files", "*.*")])
            if output_file:
                dwg.saveas(output_file)
                print(f"Файл сохранён по адресу: {output_file}")
                messagebox.showinfo("Успех", f"Изображение гильзы длиной {barrel_length} мм создано и сохранено.")
            else:
                messagebox.showerror("Ошибка", "Не удалось сохранить изображение.")
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


print(f"Файл сохранён по адресу: {output_file}")
