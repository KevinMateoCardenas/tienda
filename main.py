from logica_tienda import protocolo_cliente, protocolo_vendedor
from administracion_inventario import crear_tablas_datos
import getpass

print('Hola tú debes ser el dueño ¿Cómo estás? para terminar la interacción tu rol debe ser 0')
clave = getpass.getpass('ingrese la clave del inventario ')
intencion = '2'
id = None
while intencion != '0':
    crear_tablas_datos()

    if intencion == '1':
        intencion = input('qué quieres hacer hoy:\n inserta\n (1) si quieres comprar algun producto,\n (2) si quieres devolver algún producto\n')
        id = protocolo_cliente(intencion)

    elif intencion == '2':
        intencion = input('qué quieres hacer hoy:\n inserta\n (1) si quieres modificar el inventario,\n (2) revisar las devoluciones\n (3) si quieres verificar una compra\n')
        contraseña = getpass.getpass('ingrese la clave ')
        if contraseña == clave:
            print('contraseña correcta')
            protocolo_vendedor(intencion,id)
        else:
            print('contraseña incorrecta')

    print('Hola ¿Cómo estás?')
    intencion = input('Cual es tu rol:\n inserta \n(1) si eres cliente,\n (2) si eres vendedor\n')