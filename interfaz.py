from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


# from tkinter import *      
# root = Tk()      
# canvas = Canvas(root, width = 300, height = 300)      
# canvas.pack()      
# img = PhotoImage(file="C:/Users/Anderson/Pictures/Captura de pantalla 2023-02-07 123437.png")      
# canvas.create_image(20,20, anchor=NW, image=img)

# mainloop()  

# Función para cargar la imagen
def cargar_imagen():
    # Abrir el cuadro de diálogo para seleccionar un archivo
    ruta = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo",
        filetypes=(("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp"), ("Todos los archivos", "*.*")))
    print(ruta)
    # Cargar la imagen utilizando la biblioteca Pillow
    imagen = Image.open(ruta)

    # Redimensionar la imagen si es demasiado grande para el canvas
    ancho, alto = imagen.size
    if ancho > 400 or alto > 400:
        relacion = min(400 / ancho, 400 / alto)
        imagen = imagen.resize((int(ancho * relacion), int(alto * relacion)), Image.LANCZOS)

    img = ImageTk.PhotoImage(imagen)
    # Agregar la imagen al canvas
    canvas_imagen.create_image(20, 20, anchor=NW, image=img)

    # Actualizar la ventana
    ventana.update()

# Crear la ventana principal
ventana = Tk()
ventana.title("Cargar imagen")

# Crear el botón para cargar la imagen
boton_cargar = Button(ventana, text="Cargar imagen", command=cargar_imagen)
boton_cargar.pack()

# Crear el canvas para mostrar la imagen
canvas_imagen = Canvas(ventana, width=400, height=400)
canvas_imagen.pack()

# Ejecutar la aplicación
ventana.mainloop()
