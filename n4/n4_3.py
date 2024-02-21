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


def rotate_point(point, origin, angle):
    ox, oy = origin
    px, py = point

    qx = ox + math.cos(angle) * (px - ox) - math.sin(angle) * (py - oy)
    qy = oy + math.sin(angle) * (px - ox) + math.cos(angle) * (py - oy)

    return qx, qy


def main(shader):
    root = tk.Tk()
    root.configure(bg='black')
    label = tk.Label(root, borderwidth=0)
    img = tk.PhotoImage(data=draw(shader, 512, 512))
    label.pack()
    label.config(image=img)
    tk.mainloop()


def shader(x, y):
    r = math.sqrt((x - 0.5)**2 + (y - 0.5)**2)
    theta = math.atan2(y - 0.5, x - 0.5)

    mouth_angle = math.pi / 6
    eye_x, eye_y, eye_r = 0.6, 0.2, 0.09

    bow1_x, bow1_y, radius1 = 0.95, 0.3, 0.09
    bow2_x, bow2_y, radius2 = 0.95, 0.7, 0.09
    bow3_x, bow3_y, radius3 = 0.09, 0.16, 0.04

    triangle1_v1, triangle1_v2, triangle1_v3 = (0.09, 0.16), (0.03, 0.1), (0.15, 0.1)
    triangle2_v1, triangle2_v2, triangle2_v3 = (0.09, 0.16), (0.03, 0.22), (0.15, 0.22)

    angle = math.radians(45)

    triangle1_v1 = rotate_point(triangle1_v1, triangle1_v1, angle)
    triangle1_v2 = rotate_point(triangle1_v2, triangle1_v1, angle)
    triangle1_v3 = rotate_point(triangle1_v3, triangle1_v1, angle)

    triangle2_v1 = rotate_point(triangle2_v1, triangle2_v1, angle)
    triangle2_v2 = rotate_point(triangle2_v2, triangle2_v1, angle)
    triangle2_v3 = rotate_point(triangle2_v3, triangle2_v1, angle)

    b1 = ((x - triangle1_v2[0]) * (triangle1_v1[1] - triangle1_v2[1]) - (y - triangle1_v2[1]) * (
                triangle1_v1[0] - triangle1_v2[0])) < 0.0
    b2 = ((x - triangle1_v3[0]) * (triangle1_v2[1] - triangle1_v3[1]) - (y - triangle1_v3[1]) * (
                triangle1_v2[0] - triangle1_v3[0])) < 0.0
    b3 = ((x - triangle1_v1[0]) * (triangle1_v3[1] - triangle1_v1[1]) - (y - triangle1_v1[1]) * (
                triangle1_v3[0] - triangle1_v1[0])) < 0.0

    if (b1 == b2) and (b2 == b3):
        return 1, 0, 0

    b1 = ((x - triangle2_v2[0]) * (triangle2_v1[1] - triangle2_v2[1]) - (y - triangle2_v2[1]) * (
                triangle2_v1[0] - triangle2_v2[0])) < 0.0
    b2 = ((x - triangle2_v3[0]) * (triangle2_v2[1] - triangle2_v3[1]) - (y - triangle2_v3[1]) * (
                triangle2_v2[0] - triangle2_v3[0])) < 0.0
    b3 = ((x - triangle2_v1[0]) * (triangle2_v3[1] - triangle2_v1[1]) - (y - triangle2_v1[1]) * (
                triangle2_v3[0] - triangle2_v1[0])) < 0.0

    if (b1 == b2) and (b2 == b3):
        return 1, 0, 0
    if ((x - eye_x)**2 + (y - eye_y)**2) < eye_r**2:
        return 0, 0, 0

    if ((x - bow3_x)**2 + (y - bow3_y)**2) < radius3**2:
        return 1, 0, 0

    if -mouth_angle < theta < mouth_angle and r < 0.5:
        return 0, 0, 0
    elif r < 0.5:
        if ((x - bow1_x)**2 + (y - bow1_y)**2) < radius1**2 or ((x - bow2_x)**2 + (y - bow2_y)**2) < radius2**2:
            return 1, 0, 0
        return 1, 1, 0
    else:
        return 0, 0, 0


main(shader)
