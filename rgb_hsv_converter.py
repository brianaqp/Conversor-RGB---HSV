import math
def rgb_to_hsv(r, g, b):
    r = r / 255
    g = g / 255
    b = b / 255
    max_color = max(r, g, b)
    min_color = min(r, g, b)
    diff = max_color - min_color
    # Calculo del Hue
    if max_color == min_color:
        h = 0
    elif max_color == r:
        h = (60 * (g - b) / diff + 360) % 360
    elif max_color == g:
        h = (60 * (b - r) / diff + 120) % 360
    elif max_color == b:
        h = (60 * (r - g) / diff + 240) % 360

    # Calculo de la S
    if max_color == 0:
        s = 0
    else:
        s = (diff / max_color) * 100

    v = max_color * 100
    return h, s, v


def hsv_to_rgb (h,s,v):
        chroma = v/100 * s/100
        x = chroma * (1-abs((h/60.0) % 2 - 1))
        m = v/100 - chroma
        r, g, b = 0.0, 0.0, 0.0
        if 0 <= h < 60:
            r_, g_, b_ = chroma, x, 0
        elif 60 <= h < 120:
            r_, g_, b_ = x, chroma, 0
        elif 120 <= h < 180:
            r_, g_, b_ = 0, chroma, x
        elif 180<= h < 240:
            r_, g_, b_ = 0, x, chroma
        elif 240 <= h < 300:
            r_, g_, b_ = x, 0 , chroma
        elif 300 <= h < 360:
            r_, g_, b_ = chroma, 0, x

        r, g, b = (r_ + m)*255, (g_ + m)*255, (b_ + m)*255
        return r, g, b

print("El primer valor de prueba sera un RGB a HSV de (143, 74, 23)\nque da como resultado lo siguiente: ")
print(rgb_to_hsv(143, 74, 23))
print("Al convertir de regreso este HSV a RGB, da el mismo valor de entrada inicial: ")
print(hsv_to_rgb(25,83,56))


print("\nSegunda prueba:\nValor de entrada: RGB(200, 200, 100), a HSV:")
r, g, b = 200, 200, 100
h, s, v = rgb_to_hsv(r, g, b)
print(rgb_to_hsv(200,200,100))
print("Convertir ahora el HSV a RGB: ")
print(hsv_to_rgb(h, s, v))

