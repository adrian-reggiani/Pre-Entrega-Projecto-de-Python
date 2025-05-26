productos = []
option = 0

def ingresar_Producto():
    nombre = input(' Ingresa nombre del producto: ')
    categoria = input( ' Ingresa la categoria del producto: ')
    precio = int(input( ' Ingresa el precio del producto: \n'))
    
    print( f'Se ha ingresado el siguiente producto:\n - Nombre del Producto: {nombre} \n - Categoria del Producto: {categoria} \n - Precio del Producto: {precio}\n')
    print(' Se regresa al menu anterior \n')
    
    productos.append({
        'nombre':  nombre,
        'categoria': categoria,
        'precio': precio
    })
    return  0

def mostrar_producto():
    print(productos,'\n')
    return 0

def menu():
    print ( '1 - Ingresar Producto' )
    print ( '2 - Mostrar Producto' )
    print ( '3 - Buscar Prducto' )
    print ( '4 - Eliminar Producto' )
    print ( '5 - Salir\n' )

    





while option != 5: 

    menu()
   
    option = int(input(' Ingrese la opcion deseada luego presione la tecla Enter: '))

    match option:
        case 1:
            option = ingresar_Producto()
        case 2:
            option = mostrar_producto()
        case 3:
            print ( 'Buscar Prducto')
        case 4:
            print ( 'Eliminar Producto')
        case 5:
            print ( 'Saliendo del programa...')
            
