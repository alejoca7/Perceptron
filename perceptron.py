# perceptron.py

# Importación de bibliotecas
import numpy as np
import sqlite3

# Definición de la clase Perceptron
class Perceptron:
    def __init__(self):
        # Inicialización de los pesos y el sesgo
        self.w = None
        self.b = None
        # Conexión a la base de datos SQLite
        self.conn = sqlite3.connect('perceptron_data.db')
        self.cursor = self.conn.cursor()
        # Creación de la tabla si no existe
        self.create_table()

    # Método para crear la tabla en la base de datos
    def create_table(self):
        self.cursor.execute('''CREATE TABLE IF NOT EXISTS perceptron_data (
                                id INTEGER PRIMARY KEY,
                                weights TEXT,
                                bias REAL
                            )''')
        self.conn.commit()

    # Método para hacer predicciones
    def predict(self, x):
        net = np.dot(self.w, x) + self.b
        return np.where(net >= 0, 1, 0)

    # Método para entrenar el perceptrón
    def train(self, x, y, lr):
        self.w = np.zeros(x.shape[1])
        self.b = 0

        for _ in range(1000):  
            for i in range(len(x)):
                x_i = x[i]
                y_i = y[i]

                net = np.dot(self.w, x_i) + self.b
                y_hat = self.predict(x_i)

                error = y_i - y_hat

                self.w += lr * error * x_i
                self.b += lr * error

        # Insertar pesos y sesgo en la base de datos
        weights_str = ', '.join(map(str, self.w))
        self.cursor.execute("INSERT INTO perceptron_data (weights, bias) VALUES (?, ?)", (weights_str, self.b))
        self.conn.commit()

    # Método para cerrar la conexión a la base de datos
    def __del__(self):
        self.conn.close()