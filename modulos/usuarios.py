import corefile as core
import menus as menu
import develper.solicitudInfoValida as infoValida


usuarios = core.loadData(**core.data)["miMovistar"]["usuarios"]
id = len(usuarios)
idNuevo = id+1



def seleccionarServiciosContratados():
    cantidadServiciosUsuario = input(f"Ingrese la cantidad de servicios contratados por el cliente\n-->")
    cantidadServiciosUsuario = infoValida.datoInt(cantidadServiciosUsuario, "cantidad de servicios")
    #edit
    agregarServicios = "s"
    while agregarServicios == "s":  
        servicios = []
        for i in range(1, cantidadServiciosUsuario+1, 1):
            contador_i = i =+ 1
            print("\nServicios disponibles\n")
            opcionServicio = input(f'{menu.showMenu(menu.servicios)}\nSeleccione una opcion\n-->')
            opcionServicio = infoValida.datoInt(opcionServicio, "servicios contratados")
            if opcionServicio == 1:
                servicios.append("Internet de Fibra Optica")
            elif opcionServicio == 2:
                servicios.append("planes pospago")
            elif opcionServicio == 3:
                servicios.append("planes prepago")
            elif opcionServicio == 4:
                agregarServicios = "n"
            else:
                print("Kha")
            if contador_i == cantidadServiciosUsuario:
                break
    print(servicios)
    return servicios
    
    



def agregarUsuario(id):
    nombre = infoValida.datoStr(input("ingrese nombre"), "nombre")
    direccion = infoValida.datoStr(input("ingrese nombre"), "direccion")
    telefono = infoValida.datoInt(input("ingrese nombre"), "direccion")
    antiguedad = infoValida.datoInt(input("ingrese nombre"), "antiguedad")
    usuario = {
        idNuevo:{
            "id":idNuevo,
            "Nombre":nombre,
            "direccion":direccion,
            "telefono":telefono,
            "antiguedad en años":antiguedad,
            # "servicios contratados":seleccionarServiciosContratados(),
        }
    }


agregarUsuario(id)

