#Reto semana 6.

mensaje = "Ingrese contraseña (inicia con un número y cinco letras): "
contraseña = input(mensaje)

while True:
    if len(contraseña) != 6:
        print("Contraseña inválida, debe tener 6 caracteres.")
        contraseña = input(mensaje)
    elif not contraseña[0].isdigit():
        print("Contraseña inválida, el primer carácter debe ser un número.")
        contraseña = input(mensaje)
    elif not contraseña[1:6].isalpha():
        print("Contraseña inválida, los siguientes 5 caracteres deben ser letras.")
        contraseña = input(mensaje)
    else:
        print(contraseña, "Es una contraseña válida.")
        break

# Verificación de la contraseña con while
verificacion = input("Ingrese su contraseña nuevamente: ")
while verificacion != contraseña:
    print("Contraseña incorrecta, intente de nuevo.")
    verificacion = input("Ingrese su contraseña nuevamente: ")
   
print("Contraseña correcta.")
print("Fin del programa.")