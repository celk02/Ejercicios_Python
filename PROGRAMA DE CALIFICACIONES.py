clasificacion= int(input("Ingresar un numero entre una clasificaciones (0-100): "))

if clasificacion >= 90 and clasificacion <= 100:
    print("Clasificacion A")
elif clasificacion >= 80 and clasificacion <= 89:
    print("Clasificacion B")
elif clasificacion >= 70 and clasificacion <= 79:
    print("Clasificacion C")
elif clasificacion >= 60 and clasificacion <= 69:
    print("Clasificacion D")
elif clasificacion >= 0 and clasificacion <= 59:
    print("Clasificacion F")