from administracion_inventario import mostrar_productos, modificar_tabla, hacer_devolucion
import sqlite3

def protocolo_cliente(intencion):
    if intencion == '1':
        print('estos son las categorias de productos que tenemos: ')
        mostrar_productos("SELECT {} FROM Productos WHERE cantidad > 1".format('tipo'))
        tipo = input('cual categoría te interesa: ')
        mostrar_productos("SELECT * FROM Productos WHERE cantidad > 1 AND tipo = '{}'".format(tipo))
        id = input('ingresa el id del producto que te interesa: ')
        print('el producto es: ')
        mostrar_productos("SELECT * FROM Productos WHERE cantidad > 1 AND id = '{}'".format(id))
        print('pidele a un vendedor que verifique la compra')
        print('Gracias por comprar aquí')
        protocolo_vendedor('3', id)
    if intencion == '2':
        id = input('cual es el id producto que quieres devolver: ')
        hacer_devolucion(id)
    
def protocolo_vendedor(intencion, id):
    if intencion == '1':
        print('estos son los productos que tenemos: ')
        mostrar_productos("SELECT * FROM Productos")
        intencion = input('qué quieres hacer hoy:\n inserta\n (1) si quieres agregar algun producto,\n (2) si quieres eliminar algún producto, \n (3) si quiere modificar algún producto ya existente\n')
        modificar_tabla(intencion)    
    if intencion == '3':
        conn = sqlite3.connect('tienda.db')
        cursor = conn.cursor()
        cantidad_row = cursor.execute("SELECT cantidad FROM productos WHERE id = ?", (id,)).fetchone()
        if cantidad_row is not None:
            cantidad = int(cantidad_row[0])
            mostrar_productos('UPDATE productos SET cantidad = {} WHERE id = {}'.format(cantidad -1, id))
            conn.commit()
            conn.close()
        else:
            print('El producto con el ID {} no existe en la tabla de productos'.format(id))