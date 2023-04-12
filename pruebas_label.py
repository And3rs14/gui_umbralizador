from tkinter import *
root = Tk()
root.geometry("500x500")

btn_relheight = Label(root, text="Controles")
btn_relheight.place(relwidth=0.25, relheight=1)

btn_relx=Label(root, text="Imagen original")
btn_relx.place(relwidth=0.40, relheight=0.5, relx=0.25)

btn_rely=Label(root, text="Imagen blanco y negro")
btn_rely.place(relwidth=0.40, relheight=0.5,relx=0.25, rely=0.5)
# 35
btn_rely=Label(root, text="Banda Roja")
btn_rely.place(relwidth=0.35, relheight=0.33,relx=0.65)

btn_rely=Label(root, text="Banda Verde")
btn_rely.place(relwidth=0.35, relheight=0.33,relx=0.65, rely=0.33)

btn_rely=Label(root, text="Banda Azul")
btn_rely.place(relwidth=0.35, relheight=0.33,relx=0.65, rely=0.66)


root.mainloop()