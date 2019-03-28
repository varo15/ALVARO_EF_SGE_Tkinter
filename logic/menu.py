import tkinter as tk
from tkinter import ttk
from tkinter.ttk import Radiobutton

root = tk.Tk()
root.config(width=300, height=400)
root.title("Titulo de la ventana")
# Crear el Frame
frame = ttk.Frame(root)

# Crear Label
label = ttk.Label(root, text="Etiqueta")
# Posicionar la etiqueta
label.place(x=50, y=20)

# Crear caja de texto.
entry = ttk.Entry(root)
# Posicionarla en la ventana.
entry.place(x=50, y=50)

# Crear campo Text


# Crear un Boton
button = ttk.Button(root, text = "Boton")
button.place(x=50, y=100)

# Crear Radio Button
var = tk.IntVar()
R1 = Radiobutton(root, text="Option 1", variable=var, value=1)
R1.pack(anchor =tk.W)
R1.place(x=50, y=150)

R2 = Radiobutton(root, text="Option 2", variable=var, value=2)
R2.pack(anchor =tk.W)
R2.place(x=50, y=170)

R3 = Radiobutton(root, text="Option 3", variable=var, value=3)
R3.pack(anchor =tk.W)
R3.place(x=50, y=190)

frame.mainloop()  # Fin Frame
root.mainloop()  # Fin root
