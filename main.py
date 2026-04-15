import random
import string
import secrets
print("------- BIENVENIDO - GENERADOR DE CONTRASEÑAS -------")

def generar_password(longitud, tipo):
    letras = string.ascii_letters
    numeros = string.digits
    simbolos = string.punctuation
    
    print(f"Elegiste el tipo {tipo}")  
    if tipo == "1":
        caracteres = numeros
        print("---SOLO NÚMEROS---")
    elif tipo =="2":
        caracteres = letras
        print("---SOLO LETRAS---")
    elif tipo == "3":
        caracteres = letras + numeros + simbolos
        print("---COMPLETA---")
    else:
        print("Opción inválida")
        return None
    #crea la contraseña
    password = "".join(secrets.choice(caracteres))
    for _ in range(longitud):
        password += random.choice(caracteres)
    return password #puente del generar_password al main


def main():
    todas_las_pass = []
    while True:
        try: 
            #pide cantidad de caracteres           
            entrada = input("ingrese la longitud de la contraseña(o salir para terminar):")
            if entrada.strip().lower() == "salir":
                print("\n-------Contraseñas generadas ------")
                for i, p in enumerate(todas_las_pass, 1):
                    print(f"{i}. {p}")
                break
            
            #pide tipo de contraseña
            print("""Elegí el tipo de contraseña:
                    1 - Solo números
                    2 - Solo letras
                    3 - Completa (Letras, numeros y símbolos)""")
            tipo = input("Opción :")
            
            longitud = int(entrada) #transforma la entrada en entero
            if longitud <= 4:
                print("La contraseña es corta e insegura ingresa un número mayor a 4")
                continue
            
            password = generar_password(longitud, tipo )
            if password is None:
                continue
            print(f"Contraseña generada: {password}")
            todas_las_pass.append(password)
            
            if longitud < 8 :
                print("Advertencia , se recomienda utilizar al menos 8 caracteres")
        except ValueError:
            print("Error: ingresaste una letra o un caracter no válido. Ingresa un número válido:")


if __name__ == "__main__":
    main()