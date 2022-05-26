from clases import *

admin=1
invitado=2
print (f"""
{admin})Administracion.
{invitado})Invitado.
""")
seleccion=int (input("SELECCIONE EL USUARIO QUE DESEA INGRESAR: \n"))
if seleccion == admin:
    usuario=input("Ingrese el mail de administracion: \n")
    continuar=True
    print("Bienvenido al menu de Administración.\n")
    while usuario == "lucaslopez@gmail.com" and continuar:
        
        ver_catalogo=1
        agregar_vehiculo=2
        salir=3
        print(f"""
        !Seleccione la acción a realizar:
        {ver_catalogo})Ver Vehículos.
        {agregar_vehiculo})Cargar Vehiculo.
        {salir})Salir.
        """)
        accion=int(input(": \n"))
        if accion == agregar_vehiculo:
            agregar_moto=1
            agregar_auto=2
            agregar_bicicleta=3
            print(f"""
            Seleccione el Vehículo que desea agregar.
            {agregar_moto})Motos.
            {agregar_auto})Autos.
            {agregar_bicicleta})Bicicletas.
            """)
            vehiculo=int(input(": \n"))
            if vehiculo == agregar_moto:
                print("Ingrese los datos de la moto.")
                marca_moto= input("Ingrese la marca: \n")
                modelo_moto=int(input("Ingrese el modelo: \n"))
                precio_moto=int(input("Ingrese el Precio: \n"))
                moto_nueva=Motos(marca_moto,modelo_moto,precio_moto)
                print(moto_nueva.marca,moto_nueva.modelo,moto_nueva.precio)
            elif vehiculo == agregar_auto:
                print("Ingrese los datos del auto.")
                marca_auto=input("ingrese la marca: \n")
                modelo_auto=int(input("Ingrese el modelo: \n"))
                precio_auto=int(input("Ingrese el Precio: \n"))
                auto_nuevo=Auto(marca_auto,modelo_auto,precio_auto)
                print(auto_nuevo.marca,auto_nuevo.modelo,auto_nuevo.precio)
            elif vehiculo == agregar_bicicleta:
                print("Ingrese los datos de la bicicleta.")
                marca_bicicleta=input("ingrese la marca: \n")
                rodado_bicicleta=int(input("Ingrese el rodado: \n"))
                precio_bicicleta=int(input("Ingrese el Precio: \n"))
                bicicleta_nueva=Bicicletas(marca_bicicleta,rodado_bicicleta,precio_bicicleta)
                print(bicicleta_nueva.marca,bicicleta_nueva.rodado,bicicleta_nueva.precio)
        elif accion==ver_catalogo:
            print ("\nCATÁLOGO DE MOTOS:\n")
            print(f"Marca: {honda.marca}\nModelo: {honda.modelo}\nPrecio: {honda.precio}\n")
            print(f"Marca: {motomel.marca}\nModelo: {motomel.modelo}\nPrecio: {motomel.precio}\n")
            print(f"Marca: {moto_nueva.marca}\nModelo: {moto_nueva.modelo}\nPrecio: {moto_nueva.precio}")
            print("\nCATALOGO DE AUTOS:\n")
            print(f"Marca: {vw.marca}\nModelo: {vw.modelo}\nPrecio: {vw.precio}\n")
            print(f"Marca: {ford.marca}\nModelo: {ford.modelo}\nPrecio: {ford.precio}\n")
            print(f"Marca: {auto_nuevo.marca}\nModelo: {auto_nuevo.modelo}\nPrecio: {auto_nuevo.precio}")
            print("\nCATALOGO DE BICICLETAS:\n")
            print(f"Marca: {orbea.marca}\nRodado: {orbea.rodado}\nPrecio: {orbea.precio}\n")
            print(f"Marca: {venzo.marca}\nRodado: {venzo.rodado}\nPrecio: {venzo.precio}\n")
            print(f"Marca: {bicicleta_nueva.marca}\nRodado: {bicicleta_nueva.rodado}\nPrecio: {bicicleta_nueva.precio}")
        elif accion==salir:
            print("Hasta la Próxima.")
            continuar=False
        else:
            print("Opcion no valida")
elif seleccion == invitado:
    print ("\nCATÁLOGO DE MOTOS:\n")
    print(f"Marca: {honda.marca}\nModelo: {honda.modelo}\nPrecio: {honda.precio}\n")
    print(f"Marca: {motomel.marca}\nModelo: {motomel.modelo}\nPrecio: {motomel.precio}\n")
    print("\nCATALOGO DE AUTOS:\n")
    print(f"Marca: {vw.marca}\nModelo: {vw.modelo}\nPrecio: {vw.precio}\n")
    print(f"Marca: {ford.marca}\nModelo: {ford.modelo}\nPrecio: {ford.precio}\n")
    print("\nCATALOGO DE BICICLETAS:\n")
    print(f"Marca: {orbea.marca}\nRodado: {orbea.rodado}\nPrecio: {orbea.precio}\n")
    print(f"Marca: {venzo.marca}\nRodado: {venzo.rodado}\nPrecio: {venzo.precio}\n")
else:
    print("Usuario incorrecto.")