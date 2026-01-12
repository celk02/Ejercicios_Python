print("MÁQUINA EXPENDEDORA DE BEBIDAS")
print(""" Bebidas:
      1 = CocaCola
      2 = Agua
      3 = Sprite
      4 = Pepsi
      5 = Monster """)


opcion = int(input("Elige una bebida (1-5): "))


match opcion:
    case 1:
        print("Seleccionaste: CocaCola")
    case 2:
        print("Seleccionaste: Agua")
    case 3:
        print("Seleccionaste: Sprite")
    case 4:
        print("Seleccionaste: Pepsi")
    case 5:
        print("Seleccionaste: Monster")
    case _:
        print(f"No existe una bebida con el numero {opcion}")
