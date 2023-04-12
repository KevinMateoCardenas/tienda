import sqlite3
from datetime import datetime

def crear_tablas_datos():
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            nombre TEXT NOT NULL,
            cantidad INTEGER NOT NULL DEFAULT 0,
            descripcion TEXT,
            precio FLOAT,
            fecha_actualizacion DATE NOT NULL
        )
    ''')

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS productos_devueltos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            cantidad INTEGER NOT NULL DEFAULT 0
        )
    ''')
    # Confirmación de cambios y cierre de la conexión
    conn.commit()
    conn.close()

def mostrar_productos(query):
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    conn.close()

def insertar_producto(tipo, nombre, cantidad, descripcion, precio):
    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()
    producto = (None, tipo, nombre, cantidad, descripcion, precio, datetime.now())
    cursor.execute("INSERT INTO productos VALUES (?, ?, ?, ?, ?, ?, ?)", producto)
    conn.commit()
    conn.close()

def modificar_tabla(intencion):

    conn = sqlite3.connect('tienda.db')
    cursor = conn.cursor()

    if intencion == '1':
        tipo = input('inserte el tipo del producto ')
        nombre = input('inserte el nombre del producto ')
        cantidad = input('inserte la cantidad de producto disponible ')
        descripcion = input('inserte la descripcion del producto ')
        precio = input('inserte el precio del producto ')
        insertar_producto(tipo, nombre, cantidad, descripcion, precio)
    
    if intencion == '2':
        id = int(input('inserte el id del producto '))
        cursor.execute('DELETE FROM productos WHERE id = ?', (id,))
        conn.commit()
    
    if intencion == '3':
        id = int(input('inserte el id del producto '))
        campo = input('inserte el campo que quiere modificar (tipo, nombre, cantidad, descripcion, precio) ')
        modificacion = input('inserte la modificación ')

        if campo == 'precio':
            modificacion = float(modificacion)
        elif campo == 'cantidad':
            modificacion = int(modificacion)
        cursor.execute('UPDATE productos SET {} = ? WHERE id = ?'.format(campo), (modificacion, id))
        conn.commit()

    conn.close()

def hacer_devolucion(id):
    try:
        conn = sqlite3.connect('tienda.db')
        cursor = conn.cursor()
        cantidad = int(cursor.execute("SELECT cantidad FROM productos WHERE id = ?", (id,)).fetchone()[0])
        cursor.execute('UPDATE productos SET cantidad = ? WHERE id = ?', (cantidad + 1, id))
        conn.commit()
        conn.close()
    except Exception as E:
        print('devolución no exitosa ', E)
