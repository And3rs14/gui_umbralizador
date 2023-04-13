import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk


class MyApp:
    def __init__(self, master):
        self.master = master

        self.master.geometry("1000x700")
        
        
        self.label_original = Label(self.master)
        self.label_bw = Label(self.master)
        self.label_r = Label(self.master)
        self.label_g = Label(self.master)
        self.label_b = Label(self.master)


        self.label_original.place(relwidth=0.40, relheight=0.5, relx=0.25)

        self.label_bw.place(relwidth=0.40, relheight=0.5, relx=0.25, rely=0.5)
        self.label_r.place(relwidth=0.35, relheight=0.33, relx=0.65)
        self.label_g.place(relwidth=0.35, relheight=0.33, relx=0.65, rely=0.33)
        self.label_b.place(relwidth=0.35, relheight=0.33, relx=0.65, rely=0.66)


        # Crear el botón contenedor
        self.controlBox = Label(self.master, bg='#2E4970', fg='white', bd=0)
        self.controlBox.place(relwidth=0.25, relheight=1)

        self.boton_cargar = Button(self.controlBox, text="Cargar imagen", command=self.cargar_imagen)
        self.boton_cargar.place(relx=0.2)

        # Crear los controles
        self.control1 = create_control(self.controlBox, 0, 0.2, 1, 0.09, 'Gris', '0')
        self.control2 = create_control(self.controlBox, 0, 0.4, 1, 0.09, 'ROJO', '0')
        self.control3 = create_control(self.controlBox, 0, 0.6, 1, 0.09, 'VERDE', '0')
        self.control4 = create_control(self.controlBox, 0, 0.8, 1, 0.09, 'AZUL', '0')
    

    
    def cargar_imagen(self):
        self.ruta = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo",
                                               filetypes=(("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp"), ("Todos los archivos", "*.*")))
        print(self.ruta)
        # adrees = 'imagenes/IMG_20221007_001919_861.jpg'
        self.original_image = cv2.imread(self.ruta)

        # Open and identify the image
        self.image = Image.open(self.ruta)
  
        # Create a copy of the image and store in variable
        self.img_copy = self.image.copy()

        # Redimensionar imagen para mostrarla en el canvas
        if self.original_image.shape[1] > 400 or self.original_image.shape[0] > 400:
            relacion = min(400 / self.original_image.shape[1], 400 / self.original_image.shape[0])
            self.original_image = cv2.resize(self.original_image, (int(self.original_image.shape[1] * relacion), int(self.original_image.shape[0] * relacion)))


        self.bw = cv2.cvtColor(self.original_image, cv2.COLOR_BGR2GRAY)
       

        # Obtener las bandas RGB
        b, g, r = cv2.split(self.original_image)

        r = cv2.resize(r, (200, 200))
        g = cv2.resize(g, (200, 200))
        b = cv2.resize(b, (200, 200))

        # Convertir imágenes a formato PIL y luego a PhotoImage para mostrarlas en las etiquetas
        self.img_original = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(self.original_image, cv2.COLOR_BGR2RGB)))
        self.img_bw = ImageTk.PhotoImage(image=Image.fromarray(self.bw))
        self.img_r = ImageTk.PhotoImage(image=Image.fromarray(r))
        self.img_g = ImageTk.PhotoImage(image=Image.fromarray(g))
        self.img_b = ImageTk.PhotoImage(image=Image.fromarray(b))
        
        
        # Mostrar las imágenes en las etiquetas
        # self.label_original.config(text="Imagen original",bg='#FF00FB', fg='white', bd=0, image = self.background_image)
        
        self.label_original.bind('<Configure>',self.resize_background)

        # self.label_original.bind('<Configure>', lambda e: self.resize_background(e, self.original_image, self.label_original))


        self.label_bw.config(text="Imagen blanco y negro",bg='#67D7E5', fg='white', bd=0, image = self.img_bw)
        self.label_r.config(text="Banda Roja", bg='#FA3004', fg='white', bd=0, image = self.img_r)
        self.label_g.config(text="Banda Verde", bg='#00FF13', fg='white', bd=0, image = self.img_g)
        self.label_b.config(text="Banda Azul", bg='#0013FF', fg='white', bd=0, image = self.img_b)

        # image_label = ttk.Label(
        #     root,
        #     image=photo,
        #     text='Python',
        #     compound='top'
        # )
        print(type(self.label_b))

    def resize_background(self, event):
    
        # Get the new width and height for image
        new_width = event.width 
        new_height = event.height
        
        # Resize the image according to new dimensions
        self.image = self.img_copy.resize((new_width, new_height))

        # Define new image using PhotoImage function
        self.background_image = ImageTk.PhotoImage(self.image)

        # Change image in the label

        self.label_original.config(text="Imagen original",bg='#FF00FB', fg='white', bd=0, image = self.background_image)

        # self.background.configure(image=self.background_image)

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


# Ejecutar la aplicación
root = Tk()
app = MyApp(root)
root.mainloop()
