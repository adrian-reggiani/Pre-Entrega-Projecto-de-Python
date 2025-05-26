#Variables, listas ...

productos = [
    {
        'nombre':  'A23',
        'categoria': 'Telefono',
        'precio': '100000'
    },
     {
        'nombre':  'S24',
        'categoria': 'Telefono',
        'precio': '500000'
    },
    {
        'nombre':  'S23',
        'categoria': 'Telefono',
        'precio': '700000'
    } 
]
   
opcion = 0

#Funciones

def ingresar_Producto():
    nombre = input(' Ingresa nombre del producto: ')
    categoria = input( ' Ingresa la categoria del producto: ')
    precio = int(input( ' Ingresa el precio del producto:'))
    
    print( 
          f'Se ha ingresado el siguiente producto:\n' 
          f'- Nombre del Producto: {nombre} \n'
          f'- Categoria del Producto: {categoria} \n'
          f'- Precio del Producto: {precio}\n'
          )
    
    print( 'Volviendo al Menu... \n')
    
    productos.append({
        'nombre':  nombre,
        'categoria': categoria,
        'precio': precio
    })
    return  0

def mostrar_Producto():
    
    for i, producto in enumerate(productos):
        print('\n'
            f'Producto numero: {i + 1} '
            f'\n Nombre del producto: {producto['nombre']}'
            f'\n Categoria del producto: {producto['categoria']}'
            f'\n Precio del producto: $ {producto['precio']}'
            '\n'
            )
    
    print( 'Volviendo al Menu... \n')
    return 0

def buscar_Producto():
    bsc_Producto = input('Ingrese el nombre del producto: ').strip()
    
    for i, producto in enumerate(productos):
        if producto['nombre'] == bsc_Producto:
            print('\n\nPRODUCTO EXISTE! \n\n'
            
            f"Producto numero: {i + 1}\n"
            f"Nombre del producto: {producto['nombre']}\n"
            f"Categoria del producto: {producto['categoria']}\n"
            f"Precio del producto: $ {producto['precio']}\n"
            )
            return 0
    print('PRODUCTO NO EXISTE! \n\n')
    return 0

def eliminar_Producto():
    # El sistema debe permitir eliminar un producto de la lista, identificándolo por su posición (número) en la lista.-
    
    idProducto=int(input('Ingrese el numero del registro del producto: '))
    for i, producto in enumerate(productos):
        if i == idProducto:
            eliminado = productos.pop(i -1) # Esto es por si ingresan el 1 asi se busca el 0
            print(f"Producto eliminado: {eliminado} \n")
            print(f"Productos restante en la lista {productos} \n")
                  
    return 0
            
    
def menu():
    print ( '1 - Ingresar Producto' )
    print ( '2 - Mostrar Producto' )
    print ( '3 - Buscar Prducto' )
    print ( '4 - Eliminar Producto' )
    print ( '5 - Salir\n' )

# Programa

while opcion != 5: 

    menu()
   
    opcion = int(input(' Ingrese la opcion deseada luego presione la tecla Enter: '))

    match opcion:
        case 1:
            opcion = ingresar_Producto()
        case 2:
            opcion = mostrar_Producto()
        case 3:
            opcion = buscar_Producto()
        case 4:
            opcion = eliminar_Producto()
        case 5:
            print ( 'Saliendo del programa...')
            
