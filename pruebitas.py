import cv2
import numpy as np
from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk

class MyApp:
    def __init__(self, master):
        self.master = master

        # Crear etiquetas para mostrar las imágenes
        self.label_original = Label(self.master)
        self.label_bw = Label(self.master)
        self.label_r = Label(self.master)
        self.label_g = Label(self.master)
        self.label_b = Label(self.master)
        self.label_original.pack(side=LEFT)
        self.label_bw.pack(side=LEFT)
        self.label_r.pack(side=LEFT)
        self.label_g.pack(side=LEFT)
        self.label_b.pack(side=LEFT)

        self.boton_cargar = Button(self.master, text="Cargar imagen", command=self.cargar_imagen)
        self.boton_cargar.pack()

    def cargar_imagen(self):
        self.ruta = filedialog.askopenfilename(initialdir="/", title="Seleccionar archivo",
                                               filetypes=(("Archivos de imagen", "*.jpg;*.jpeg;*.png;*.bmp"), ("Todos los archivos", "*.*")))
        self.imagen_original = cv2.imread(self.ruta)
        self.imagen_bw = cv2.cvtColor(self.imagen_original, cv2.COLOR_BGR2GRAY)

        # Redimensionar imagen para mostrarla en la etiqueta
        if self.imagen_original.shape[1] > 400 or self.imagen_original.shape[0] > 400:
            relacion = min(400 / self.imagen_original.shape[1], 400 / self.imagen_original.shape[0])
            self.imagen_original = cv2.resize(self.imagen_original, (int(self.imagen_original.shape[1] * relacion), int(self.imagen_original.shape[0] * relacion)))
            self.imagen_bw = cv2.resize(self.imagen_bw, (int(self.imagen_original.shape[1] * relacion), int(self.imagen_original.shape[0] * relacion)))

        # Obtener las bandas RGB
        b, g, r = cv2.split(self.imagen_original)

        # Redimensionar las bandas para mostrarlas en la etiqueta
        r = cv2.resize(r, (400, 400))
        g = cv2.resize(g, (400, 400))
        b = cv2.resize(b, (400, 400))

        # Convertir imágenes a formato PIL y luego a PhotoImage para mostrarlas en las etiquetas
        self.img_original = ImageTk.PhotoImage(image=Image.fromarray(cv2.cvtColor(self.imagen_original, cv2.COLOR_BGR2RGB)))
        self.img_bw = ImageTk.PhotoImage(image=Image.fromarray(self.imagen_bw))
        self.img_r = ImageTk.PhotoImage(image=Image.fromarray(r))
        self.img_g = ImageTk.PhotoImage(image=Image.fromarray(g))
        self.img_b = ImageTk.PhotoImage(image=Image.fromarray(b))

        # Mostrar las imágenes en las etiquetas
        self.label_original.config(image=self.img_original)
        self.label_bw.config(image=self.img_bw)
        self.label_r.config(image=self.img_r)
        self.label_g.config(image=self.img_g)
        self.label_b.config(image=self.img_b)
        

root = Tk()
app = MyApp(root)
root.mainloop()
