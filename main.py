import os
import modulos.menus as menu
import modulos.develper.solicitudInfoValida as infoValida
import modulos.corefile as core

while True:
    print("Welcome to Mi movistar")
    opcion = input(f"{menu.showMenu(menu.administrador)}\n")
    opcion = infoValida.datoInt(opcion, "iniciar")
    if (opcion == 1):
        print("has seleccionado opcion 1")
    if (opcion == 2):
        print("has seleccionado opcion 2")
    if (opcion == 3):
        print("has seleccionado opcion 3")
        break