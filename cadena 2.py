nombres= input("ingresar tu nombre: ")
apellidos= input("ingresa tus apellidos: ")

nombre_completo= nombres + " " + apellidos
print(f"nombre_completo: {nombre_completo} ")

vocales= "aeiou"
vocales1= "AEIOU"
letra_z= ""


for w in nombre_completo:
    if w in vocales:
        letra_z += "z"
    elif w in vocales1:
        letra_z += "Z"    
    else:
        letra_z += w
print(f"vocales remplazadas por 'z': {letra_z}")
    

letras= "Jose"
nombre_reversa= " "
for a in letras:
    nombre_reversa =  a + nombre_reversa
print(nombre_reversa)




