from tkinter import *
from tkinter import ttk

window = Tk()
frame_app = Frame(window, width=400, height=600, bg="blue")
frame_app.pack()

# Widgets dentro del contender APP
frame_navbar = Frame(frame_app, width=400, height=100)
frame_navbar.grid(row=0, column=0)
frame_title = Frame(frame_app, width=400, height=150)
frame_title.grid(row=1, column=0)
frame_options = Frame(frame_app, width=400, height=500)
frame_options.grid(row=2, column=0)

# Widgets dentro del contender OPTIONS
frame_food = Frame(frame_options, width=350, height=350, bg="#d48df0")
frame_food.place(x=25, y=30)
# frame_drinks = Frame(frame_options, width=350, height=200, bg="#eba2a2")
# frame_drinks.place(x=25, y=380)

label_correo = Label(frame_food, 
              text="CORREO",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_correo.place(x=20, y=5)
caja_correo = Entry(frame_food, width=40) 
caja_correo.place(x=20, y=50)

label_pwd = Label(frame_food, 
              text="CONTRASENA",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_pwd.place(x=20, y=85)
caja_pwd = Entry(frame_food, width=40) 
caja_pwd.place(x=20, y=130
label_edad = Label(frame_food, 
              text="EDAD",
              font=("Calibri", "22", "bold"),
              fg="white",
              bg="#d48df0")
label_edad.place(x=20, y=160)
caja_edad = Entry(frame_food, width=40) 
caja_edad.place(x=20, y=200)


# Widgets dentro del contender NAVBAR
title = Label(frame_navbar, 
              text="Menú",
              font=("Calibri", "14"))
title.place(x=320, y=40)

# Widgets dentro del contender TITLE
title1 = Label(frame_title, 
              text="¡Bienvenido(a)!", 
              font=("Calibri", "22", "bold"),
              justify=LEFT)
title1.place(x=25, y=10)
title2 = Label(frame_title, 
              text="¿Quieres ser parte de nuestra \ncomunidad?", 
              font=("Calibri", "18"),
              justify=LEFT)
title2.place(x=25, y=50)

#def validar_datos(): 
    #caja_correo.delete()
    #caja_pwd.delete()
    #caja_edad.delete()
    
#boton_registrar = Button(frame_food, text="Registro", bg="#17abab",font=("Tahoma",12), width=30, height=2, command=validar_datos).place(x=20, y=200)

window.mainloop()