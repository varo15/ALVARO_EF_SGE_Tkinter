import tkinter as tk
from tkinter import ttk

root = tk.Tk()
root.config(width=300, height=200)
root.title("Titulo de la ventana")
#Crear el Frame
frame = ttk.Frame(root)

# Crear Label
label = ttk.Label(root, text="Etiqueta")
#Posicionar la etiqueta
label.place(x=10, y=10)

# Crear caja de texto.
entry = ttk.Entry(root)
# Posicionarla en la ventana.
entry.place(x=50, y=50)

# Crear campo Text
T = tk.Text(root, height=2, width=30)
entry.place(x=70, y=70)
T.insert(tk.END, "Just a text Widget\nin two lines\n")


frame.mainloop() #Fin Frame
root.mainloop() #Fin root
