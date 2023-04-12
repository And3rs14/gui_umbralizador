from tkinter import *
import cv2
from PIL import ImageTk, Image


def create_control(root, relx, rely, relwidth, relheight, text, default):
    # Crear el marco contenedor
    container = Label(root)
    container.place(relx=relx, rely=rely,
                    relwidth=relwidth, relheight=relheight)

    # Crear la etiqueta
    label = Label(container, text=text)
    label.place(relx=0, rely=0.3, relwidth=0.1)

    # Crear el control deslizante
    slider = Scale(container, from_=0, to=255,
                   tickinterval=51, orient=HORIZONTAL)
    slider.place(relx=0.15, relwidth=0.6)

    # Crear la entrada
    entry = Entry(container)
    entry.place(relx=0.8, rely=0.3, relwidth=0.15)
    entry.insert(0, default)

    return container, slider, entry


# Crear la raíz de la aplicación
root = Tk()
root.geometry("1000x700")

# Cargar las imágenes con cv2
# Reemplaza con la ruta de tu imagen
original_image = cv2.imread(
    '/imagenes/Captura de pantalla 2023-02-07 123437.png')
# Reemplaza con la ruta de tu imagen en blanco y negro
bw_image = cv2.imread('/imagenes/Captura de pantalla 2023-02-07 123437.png', 0)
red_image = cv2.imread('/imagenes/Captura de pantalla 2023-02-07 123437.png')
green_image = cv2.imread('/imagenes/Captura de pantalla 2023-02-07 123437.png')
blue_image = cv2.imread('/imagenes/Captura de pantalla 2023-02-07 123437.png')

# Convertir las imágenes a formato compatible con Tkinter
original_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)
original_image = Image.fromarray(original_image)
original_image = ImageTk.PhotoImage(original_image)

bw_image = Image.fromarray(bw_image)
bw_image = ImageTk.PhotoImage(bw_image)

red_image = cv2.cvtColor(red_image, cv2.COLOR_BGR2RGB)
red_image = Image.fromarray(red_image)
red_image = ImageTk.PhotoImage(red_image)

green_image = cv2.cvtColor(green_image, cv2.COLOR_BGR2RGB)
green_image = Image.fromarray(green_image)
green_image = ImageTk.PhotoImage(green_image)

blue_image = cv2.cvtColor(blue_image, cv2.COLOR_BGR2RGB)
blue_image = Image.fromarray(blue_image)
blue_image = ImageTk.PhotoImage(blue_image)

# Crear el botón contenedor
controlBox = Label(root, bg='#2E4970', fg='white', bd=0)
controlBox.place(relwidth=0.25, relheight=1)

# Crear los controles
control1 = create_control(controlBox, 0, 0.2, 1, 0.09, 'Gris', '0')
control2 = create_control(controlBox, 0, 0.4, 1, 0.09, 'ROJO', '0')
control3 = create_control(controlBox, 0, 0.6, 1, 0.09, 'VERDE', '0')
control4 = create_control(controlBox, 0, 0.8, 1, 0.09, 'AZUL', '0')

originalBox = Label(root, text="Imagen original",
                    bg='#FF00FB', fg='white', bd=0)
originalBox.place(relwidth=0.40, relheight=0.5, relx=0.25)

bwBox = Label(root, text="Imagen blanco y negro",
              bg='#67D7E5', fg='white', bd=0)
bwBox.place(relwidth=0.40, relheight=0.5, relx=0.25, rely=0.5)
# 35
redBox = Label(root, text="Banda Roja", bg='#FA3004', fg='white', bd=0)
redBox.place(relwidth=0.35, relheight=0.33, relx=0.65)

greenBox = Label(root, text="Banda Verde", bg='#00FF13', fg='white', bd=0)
greenBox.place(relwidth=0.35, relheight=0.33, relx=0.65, rely=0.33)

blueBox = Label(root, text="Banda Azul", bg='#0013FF', fg='white', bd=0)
blueBox.place(relwidth=0.35, relheight=0.33, relx=0.65, rely=0.66)


# Ejecutar la aplicación
root.mainloop()
