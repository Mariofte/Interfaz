# test_inputs.py
import tkinter as tk

root = tk.Tk()
root.geometry("300x400")

# Input normal
tk.Label(root, text="Nombre:").pack()
entry_nombre = tk.Entry(root)
entry_nombre.pack()

# Input contraseña
tk.Label(root, text="Contraseña:").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# Leer el valor
def leer():
    print(entry_nombre.get())
    print(entry_pass.get())

tk.Button(root, text="Leer", command=leer).pack()

root.mainloop()