from tkinter import *
import tkinter as tk
from tkinter import ttk, messagebox, scrolledtext
from tkinter.ttk import Radiobutton, Button


def crearElementos():
    root = tk.Tk()
    root.geometry("400x500")
    root.title("Titulo de la ventana")

    # Crear Label
    label = ttk.Label(root, text="Introduce un texto:", font=("Arial Bold", 20))
    # Posicionar la etiqueta
    label.place(x=50, y=20)

    # Crear caja de texto.
    entry = ttk.Entry(root)
    entry.place(x=50, y=60)

    # Crear Radio Button
    var = tk.IntVar()
    R1 = Radiobutton(root, text="Option 1", variable=var, value=1)
    R1.pack(anchor=tk.W)
    R1.place(x=50, y=100)

    R2 = Radiobutton(root, text="Option 2", variable=var, value=2)
    R2.pack(anchor=tk.W)
    R2.place(x=50, y=130)

    R3 = Radiobutton(root, text="Option 3", variable=var, value=3)
    R3.pack(anchor=tk.W)
    R3.place(x=50, y=160)

    # Crear CheckButton
    CheckVar1 = tk.IntVar()
    CheckVar2 = tk.IntVar()
    C1 = tk.Checkbutton(root, text="Check 1", variable=CheckVar1, onvalue=1, offvalue=0)
    C1.pack()
    C1.place(x=150, y=100)
    C2 = tk.Checkbutton(root, text="check 2", variable=CheckVar2, onvalue=1, offvalue=0)
    C2.pack()
    C2.place(x=150, y=130)

    # Crear ComboBox
    comboExample = ttk.Combobox(root,
                                values=[
                                    "Enero",
                                    "Febrero",
                                    "Marzo",
                                    "Abril"])
    print(dict(comboExample))
    comboExample.grid(column=0, row=1)
    comboExample.current(0)
    comboExample.place(x=50, y=200)
    print(comboExample.current(), comboExample.get())

    # Crear un Menu
    menubar = tk.Menu(root)
    root.config(menu=menubar)

    filemenu = tk.Menu(menubar, tearoff=0)
    filemenu.add_command(label="Nuevo")
    filemenu.add_command(label="Abrir")
    filemenu.add_command(label="Guardar")
    filemenu.add_command(label="Cerrar")
    filemenu.add_separator()
    filemenu.add_command(label="Salir", command=root.quit)

    editmenu = tk.Menu(menubar, tearoff=0)
    editmenu.add_command(label="Cortar")
    editmenu.add_command(label="Copiar")
    editmenu.add_command(label="Pegar")

    helpmenu = tk.Menu(menubar, tearoff=0)
    helpmenu.add_command(label="Ayuda")
    helpmenu.add_separator()
    helpmenu.add_command(label="Acerca de...")

    menubar.add_cascade(label="Archivo", menu=filemenu)
    menubar.add_cascade(label="Editar", menu=editmenu)
    menubar.add_cascade(label="Ayuda", menu=helpmenu)

    # Crear un Spinbox
    spinner = tk.Spinbox(root, from_=0, to=20)
    spinner.pack()
    spinner.place(x=50, y=230)

    def clicked():
        # Crear MessageBox
        messagebox.showinfo("Alerta", "El boton se ha ejecutado correctamente")
        textBox.insert(INSERT, "Texto: " + str(entry.get()) +
                       "\nSpinner: " + str(spinner.get()) +
                       "\nCombobox: " + str(comboExample.get()) +
                       "\n")

        # Crear un Dialog
        answer = messagebox.askokcancel("Cerar Mensaje", "Quieres cerrar la alerta?")

    # Crear un Boton
    btn = Button(root, text="NO pulses", command=clicked)
    btn.place(x=50, y=270)

    # Crear campo Text
    textBox = scrolledtext.ScrolledText(width=20, height=5)
    textBox.place(x=50, y=310)

    root.mainloop()  # Fin root


crearElementos()
