# check_database.py

# Importación de la biblioteca
import sqlite3

# Función para revisar la base de datos y mostrar su contenido
def check_database():
    # Conexión a la base de datos
    conn = sqlite3.connect('perceptron_data.db')
    cursor = conn.cursor()

    # Ejecutar una consulta para ver todos los registros en la tabla perceptron_data
    cursor.execute("SELECT * FROM perceptron_data")
    rows = cursor.fetchall()

    # Mostrar los resultados
    for row in rows:
        print("ID:", row[0])
        print("Pesos:", row[1])
        print("Sesgo:", row[2])
        print()

    # Cerrar la conexión
    conn.close()

# Condición para ejecutar la función check_database solo si este archivo se está ejecutando directamente
if __name__ == "__main__":
    check_database()