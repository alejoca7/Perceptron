import sqlite3

def conectar_base_datos():
    # Conectar a la base de datos (creará el archivo si no existe)
    return sqlite3.connect('pesos.db')

def crear_tabla_pesos(conn):
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS pesos (
                       operacion TEXT,
                       peso_1 REAL,
                       peso_2 REAL,
                       sesgo REAL
                   )''')

def insertar_pesos(conn, operacion, peso_1, peso_2, sesgo):
    cursor = conn.cursor()
    cursor.execute('INSERT INTO pesos VALUES (?, ?, ?, ?)', (operacion, peso_1, peso_2, sesgo))
    conn.commit()

def cerrar_conexion(conn):
    conn.close()

# Paso 1: Conectar a la base de datos
conn = conectar_base_datos()

# Paso 2: Crear una tabla para almacenar los pesos
crear_tabla_pesos(conn)

# Paso 3: Insertar los pesos en la tabla
operacion = "AND"
peso_1 = 0.5
peso_2 = 0.8
sesgo = -0.2
insertar_pesos(conn, operacion, peso_1, peso_2, sesgo)

# Paso 4: Cerrar la conexión a la base de datos
cerrar_conexion(conn)
