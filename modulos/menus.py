administrador = ["Registro usuarios", "Gestion de usuarios", "Salir"]
registroUsuario = ["nombre", "direccion", "telefono", "antiguedad en años", "servicios contratados"]
categorizarUsuario = ["cliente nuevo", "cliente regular", "cliente leal"]

historialUsuarios = ["Registro y almacenamiento de servicios utilizados por cada usuario",
                     "Seguimiento de las interacciones de los usuarios con la empresa, como consultas de servicio al cliente, reclamaciones y sugerencias"]

promociones = [categorizarUsuario[0],
               categorizarUsuario[1],
               categorizarUsuario[2]]

servicios = ["Internet de Fibra Optica", "planes pospago", "planes prepago", "salir"]
reportes = ["cantidad usuarios por servicios", "servicio mas vendido", "servicio de un usuario"]

def showMenu (list):
    for i in enumerate(list, start=1):
        print (i)