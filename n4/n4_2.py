import math
import tkinter as tk


def draw(shader, width, height):
    image = bytearray((0, 0, 0) * width * height)
    for y in range(height):
        for x in range(width):
            pos = (width * y + x) * 3
            color = shader(x / width, y / height)
            normalized = [max(min(int(c * 255), 255), 0) for c in color]
            image[pos:pos + 3] = normalized
    header = bytes(f'P6\n{width} {height}\n255\n', 'ascii')
    return header + image


def main(shader):
    # Чёрный фон
    root = tk.Tk()
    root.configure(bg='black')
    label = tk.Label(root, borderwidth=0)
    img = tk.PhotoImage(data=draw(shader, 1024, 1024))
    label.pack()
    label.config(image=img)
    tk.mainloop()


def shader(x, y):
    # Вычисляем расстояние от центра для красного круга
    dx1 = x - 0.5
    dy1 = y - 0.5
    distance1 = math.sqrt(dx1 * dx1 + dy1 * dy1) * 2
    radius1 = 0.2

    # Вычисляем расстояние от центра со смещением для зеленого круга
    dx2 = x - 0.48
    dy2 = y - 0.48
    distance2 = math.sqrt(dx2 * dx2 + dy2 * dy2) * 2
    radius2 = 0.2

    # Используем расстояния для создания градиента
    r = 1 - pow(6 * distance1, 2) if distance1 < radius1 else 0
    g = 1 - pow(6 * distance2, 2) if distance2 < radius2 else 0
    b = 0

    return r, g, b


main(shader)
