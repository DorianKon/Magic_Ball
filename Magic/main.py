import tkinter as tk
from PIL import Image, ImageTk
import random

# Создание основного окна
root = tk.Tk()
root.title("Магический шар")
root.geometry("800x800+500+0")  # Установка фиксированного размера окна
root.minsize(800, 700)
root.maxsize(850, 850)

# Путь к изображению и иконке
image_path = r"E:\Python\MY_PROJECT\Magic_Ball\112_1_5.png"
icon_path = r"E:\Python\MY_PROJECT\Magic_Ball\213.png"

# Загрузка и установка иконки окна
icon_image = Image.open(icon_path)
photo = ImageTk.PhotoImage(icon_image)
root.iconphoto(False, photo)

# Загрузка основного изображения
original_image = Image.open(image_path)
magic_ball_photoimage = ImageTk.PhotoImage(original_image)


# Функция для получения ответа магического шара
def get_magic_ball_answer():
    answers = ["Бесспорно", "Можешь быть уверен в этом", "Пока неясно, попробуй снова", "Спроси позже", "Даже не думай",
               "Мой ответ — нет", "Весьма сомнительно", "Мне кажется - да", "Вероятнее всего", "Никаких сомнений",
               "Хорошие перспективы", "Об этом лучше не говорить", "Да", "Нет",
               "Сконцентрируйся и спроси опять", "Весьма сомнительно"]
    return random.choice(answers)


# Функция для плавного появления текста
def fade_in_text(canvas, text_id, final_color, steps=10, delay=100):
    """
    Анимация плавного появления текста на канвасе.
    :param canvas: объект канваса Tkinter, на котором отображается текст
    :param text_id: идентификатор текстового объекта на канвасе
    :param final_color: конечный цвет текста
    :param steps: количество шагов анимации
    :param delay: задержка в миллисекундах между шагами анимации
    """

    # Функция, выполняющая один шаг анимации
    def animate(step):
        r, g, b = final_color
        intermediate_color = (
            int(r * step / steps),
            int(g * step / steps),
            int(b * step / steps)
        )
        canvas.itemconfig(text_id, fill="#%02x%02x%02x" % intermediate_color)
        if step < steps:
            canvas.after(delay, animate, step + 1)

    animate(0)


# Функция, вызываемая при нажатии на область канваса для получения ответа
def on_ask_button_click(event=None):
    answer = get_magic_ball_answer()
    canvas.delete("answer_text")  # Удаление предыдущего текста ответа, если он есть

    # Координаты треугольника
    points = [405, 460, 480, 330, 330, 330]

    # Расчет позиции для текста (примерно в центре треугольника)
    text_x = sum([points[i] for i in range(0, len(points), 2)]) / 3
    text_y = sum([points[i] for i in range(1, len(points), 2)]) / 3

    # Сдвигаем текст вверх на несколько пикселей
    offset_y = 5  # Например, поднимаем текст на 15 пикселей вверх
    text_y -= offset_y  # Уменьшаем Y, чтобы поднять текст вверх

    # Расчет максимальной ширины текста
    max_text_width = max(points[::2]) - min(points[::2]) - 45  # Вычитаем 45 пикселей для отступов

    # Создание текста с переносом, центрированием и сдвигом вверх
    text_id = canvas.create_text(text_x, text_y, text=answer, width=max_text_width, tag="answer_text", fill="white",
                                 font=('Arial', 12, 'bold'), justify="center")

    # Плавное появление текста
    fade_in_text(canvas, text_id, (255, 255, 255))  # Белый цвет в RGB


# Создание канваса для рисования
canvas = tk.Canvas(root, width=800, height=800, bg="white")
canvas.pack(fill=tk.BOTH, expand=True)

# Отображение масштабированного изображения
image_on_canvas = canvas.create_image(magic_ball_photoimage.width() / 2, magic_ball_photoimage.height() / 2,
                                      image=magic_ball_photoimage)

# Отображение изображения
image_on_canvas = canvas.create_image(400, 400, image=magic_ball_photoimage)

# Создание треугольной "кнопки" и её позиционирование по центру
points = [405, 460, 480, 330, 330, 330]
triangle = canvas.create_polygon(points, fill="black", outline="white")

# Привязка обработчика клика к треугольнику
canvas.tag_bind(triangle, '<Button-1>', on_ask_button_click)

root.mainloop()
