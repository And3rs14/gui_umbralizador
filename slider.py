from tkinter import *

def create_control(root, relx, rely, relwidth, relheight, text, default):
    # Crear el marco contenedor
    container = Label(root)
    container.place(relx=relx, rely=rely, relwidth=relwidth, relheight=relheight)
    
    # Crear la etiqueta
    label = Label(container, text=text)
    label.place(relx=0, rely=0.3, relwidth=0.1)
    
    # Crear el control deslizante
    slider = Scale(container, from_=0, to=255, tickinterval=51, orient=HORIZONTAL)
    slider.place(relx=0.15, relwidth=0.6)
    
    # Crear la entrada
    entry = Entry(container)
    entry.place(relx=0.8, rely=0.3, relwidth=0.15)
    entry.insert(0, default)
    
    return container, slider, entry

# Crear la raíz de la aplicación
root = Tk()
root.geometry("1000x700")

# Crear el botón contenedor
btn_relheight = Label(root, bg='#2E4970', fg='white', bd=0)
btn_relheight.place(relwidth=0.25, relheight=1)

# Crear los controles
control1 = create_control(btn_relheight, 0, 0.2, 1, 0.09, 'Gris', '0')
control2 = create_control(btn_relheight, 0, 0.4, 1, 0.09, 'ROJO', '0')
control3 = create_control(btn_relheight, 0, 0.6, 1, 0.09, 'VERDE', '0')
control4 = create_control(btn_relheight, 0, 0.8, 1, 0.09, 'AZUL', '0')

btn_relx=Label(root, text="Imagen original", bg='#FF00FB', fg='white', bd=0)
btn_relx.place(relwidth=0.40, relheight=0.5, relx=0.25)

btn_rely=Label(root, text="Imagen blanco y negro", bg='#67D7E5', fg='white', bd=0)
btn_rely.place(relwidth=0.40, relheight=0.5,relx=0.25, rely=0.5)
# 35
btn_rely=Label(root, text="Banda Roja", bg='#FA3004', fg='white', bd=0)
btn_rely.place(relwidth=0.35, relheight=0.33,relx=0.65)

btn_rely=Label(root, text="Banda Verde", bg='#00FF13', fg='white', bd=0)
btn_rely.place(relwidth=0.35, relheight=0.33,relx=0.65, rely=0.33)

btn_rely=Label(root, text="Banda Azul", bg='#0013FF', fg='white', bd=0)
btn_rely.place(relwidth=0.35, relheight=0.33,relx=0.65, rely=0.66)



# Ejecutar la aplicación
root.mainloop()