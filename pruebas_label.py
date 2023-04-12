from tkinter import *
root = Tk()
root.geometry("1000x700")


btn_relheight = Label(root, text="Controles")
btn_relheight.place(relwidth=0.25, relheight=1)

label1 = Label(btn_relheight,bg='#2E4970', fg='white', bd=0)
label1.place(rely=0.2, relwidth=1,relheight=0.09)


label = Label(label1, text='Gris')
label.place(relx=0,rely=0.30, relwidth=0.1)

slider = Scale(label1, from_=0, to=255, tickinterval=51, orient=HORIZONTAL)
slider.place(relx=0.15, relwidth=0.6)

e1 = Entry(label1)
e1.place(relx=0.8,rely=0.30,relwidth=0.15)
e1.insert(0, '0')

# =============================0
label1 = Label(btn_relheight,bg='#2E4970', fg='white', bd=0)
label1.place(rely=0.4, relwidth=1,relheight=0.09)


label = Label(label1, text='ROJO')
label.place(relx=0,rely=0.30, relwidth=0.1)

slider = Scale(label1, from_=0, to=255, tickinterval=51, orient=HORIZONTAL)
slider.place(relx=0.15, relwidth=0.6)

e1 = Entry(label1)
e1.place(relx=0.8,rely=0.30,relwidth=0.15)
e1.insert(0, '0')
# =============================0

# =============================0
label1 = Label(btn_relheight,bg='#2E4970', fg='white', bd=0)
label1.place(rely=0.6, relwidth=1,relheight=0.09)


label = Label(label1, text='VERDE')
label.place(relx=0,rely=0.30, relwidth=0.1)

slider = Scale(label1, from_=0, to=255, tickinterval=51, orient=HORIZONTAL)
slider.place(relx=0.15, relwidth=0.6)

e1 = Entry(label1)
e1.place(relx=0.8,rely=0.30,relwidth=0.15)
e1.insert(0, '0')
# =============================0

# =============================0
label1 = Label(btn_relheight,bg='#2E4970', fg='white', bd=0)
label1.place(rely=0.8, relwidth=1,relheight=0.09)


label = Label(label1, text='AZUL')
label.place(relx=0,rely=0.30, relwidth=0.1)

slider = Scale(label1, from_=0, to=255, tickinterval=51, orient=HORIZONTAL)
slider.place(relx=0.15, relwidth=0.6)

e1 = Entry(label1)
e1.place(relx=0.8,rely=0.30,relwidth=0.15)
e1.insert(0, '0')
# =============================0


root.mainloop()