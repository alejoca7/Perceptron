# gui.py

# Importación de bibliotecas
import tkinter as tk
from tkinter import messagebox
import subprocess  # Importar el módulo subprocess
import numpy as np
from perceptron import Perceptron

# Función para evaluar la entrada del usuario
def evaluate(perceptron, x1, x2):
    x_new = np.array([int(x1), int(x2)])
    result = perceptron.predict(x_new)
    messagebox.showinfo("Resultado", f"El resultado es: {result}")

# Función para entrenar el perceptrón
def train_perceptron(operation_var):
    perceptron = create_perceptron(operation_var.get())
    messagebox.showinfo("Entrenamiento", "El perceptrón ha sido entrenado exitosamente.")

# Función para imprimir los pesos y el sesgo del perceptrón
def print_weights(operation_var):
    perceptron = create_perceptron(operation_var.get())
    if perceptron.w is not None and perceptron.b is not None:
        messagebox.showinfo("Pesos y Sesgo", f"Pesos: {perceptron.w}\nSesgo: {perceptron.b}")
    else:
        messagebox.showinfo("Pesos y Sesgo", "El perceptrón no está entrenado.")

# Función para crear la interfaz gráfica
def create_form():
    root = tk.Tk()
    root.title("Perceptrón")
    root.geometry("300x200")

    frame = tk.Frame(root, bg="#f0f0f0")
    frame.pack(expand=True, fill="both")

    label_operation = tk.Label(frame, text="Seleccione la operación:", bg="#f0f0f0", font=("Helvetica", 12))
    label_operation.grid(row=0, column=0, columnspan=2, pady=5)

    operation_var = tk.StringVar()
    operation_var.set("AND")

    radio_and = tk.Radiobutton(frame, text="AND", variable=operation_var, value="AND", font=("Helvetica", 10))
    radio_and.grid(row=1, column=0, padx=10)
    radio_or = tk.Radiobutton(frame, text="OR", variable=operation_var, value="OR", font=("Helvetica", 10))
    radio_or.grid(row=1, column=1, padx=10)

    label_x1 = tk.Label(frame, text="x1:", bg="#f0f0f0", font=("Helvetica", 10))
    label_x1.grid(row=2, column=0, padx=10)
    entry_x1 = tk.Entry(frame)
    entry_x1.grid(row=2, column=1, padx=10)

    label_x2 = tk.Label(frame, text="x2:", bg="#f0f0f0", font=("Helvetica", 10))
    label_x2.grid(row=3, column=0, padx=10)
    entry_x2 = tk.Entry(frame)
    entry_x2.grid(row=3, column=1, padx=10)

    button_train = tk.Button(frame, text="Entrenar", command=lambda: train_perceptron(operation_var), bg="#4CAF50", fg="white", font=("Helvetica", 10))
    button_train.grid(row=4, column=0, pady=10, padx=10, sticky="we")

    button_evaluate = tk.Button(frame, text="Evaluar", command=lambda: evaluate(create_perceptron(operation_var.get()), entry_x1.get(), entry_x2.get()), bg="#008CBA", fg="white", font=("Helvetica", 10))
    button_evaluate.grid(row=4, column=1, pady=10, padx=10, sticky="we")

    button_weights = tk.Button(frame, text="Mostrar Pesos y Sesgo", command=lambda: print_weights(operation_var), bg="#f44336", fg="white", font=("Helvetica", 10))
    button_weights.grid(row=5, columnspan=2, pady=10, padx=10, sticky="we")

    button_show_db = tk.Button(frame, text="Mostrar Base de Datos", command=show_database, bg="#FFA500", fg="white", font=("Helvetica", 10))
    button_show_db.grid(row=6, columnspan=2, pady=10, padx=10, sticky="we")

    root.mainloop()

# Función para mostrar la base de datos
def show_database():
    subprocess.run(["python", "check_database.py"])

def create_perceptron(operation):
    perceptron = Perceptron()
    if operation == "AND":
        x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y = np.array([0, 0, 0, 1])
    elif operation == "OR":
        x = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
        y = np.array([0, 1, 1, 1])
    else:
        raise ValueError("Operación no válida")

    perceptron.train(x, y, lr=0.1)
    
    return perceptron

# Llamar a la función principal que crea la interfaz gráfica
create_form()