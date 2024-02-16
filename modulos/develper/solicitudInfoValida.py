def datoInt(opcionInt, motivo):
    while True:
        try:
            opcionInt = int(opcionInt)
            if opcionInt == "":
                raise ValueError("El valor no puede ser vacío")
            break
        except ValueError as e:
            print(f"Opción inválida:")
            opcionInt = input(f"Ingrese un nuevo valor para {motivo}\n")
    return opcionInt

def datoFloat(opcionFloat, motivo):
    while True:
        try:
            opcionFloat = float(opcionFloat)
            if opcionFloat == "":
                raise ValueError("El valor no puede ser vacío")
            break
        except ValueError as e:
            print(f"Opción inválida:")
            opcionFloat = input(f"Ingrese un nuevo valor para {motivo}")
    return opcionFloat

def datoStr(opcionTexto, motivo):
    while True:
        try:
            opcionTexto = str(opcionTexto)
            if opcionTexto == "":
                raise ValueError("El valor no puede ser vacío")
            break
        except ValueError as e:
            print(f"Opción inválida: {e}")
            opcionTexto = input("Ingrese un nuevo valor: ")

    return opcionTexto
        
# requerirDato=input("escriba algo")
# datoInt(requerirDato, "Prueba")