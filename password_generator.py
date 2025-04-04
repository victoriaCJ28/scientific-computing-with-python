import re               # Módulo para trabajar con expresiones regulares
import secrets          # Módulo para generar números aleatorios seguros
import string           # Módulo que contiene cadenas predefinidas como letras y dígitos

def generate_password(length=16, nums=1, special_chars=1, uppercase=1, lowercase=1):
    """
    Genera una contraseña aleatoria segura que cumple con ciertos requisitos mínimos:
    - length: longitud total de la contraseña
    - nums: cantidad mínima de dígitos numéricos
    - special_chars: cantidad mínima de caracteres especiales
    - uppercase: cantidad mínima de letras mayúsculas
    - lowercase: cantidad mínima de letras minúsculas
    """

    # Define los diferentes conjuntos de caracteres posibles
    letters = string.ascii_letters              # a-z y A-Z
    digits = string.digits                      # 0-9
    symbols = string.punctuation                # Caracteres especiales como !@#$%

    # Combina todos los caracteres posibles en una sola cadena
    all_characters = letters + digits + symbols

    while True:
        password = ''
        
        # Genera una contraseña aleatoria tomando caracteres al azar del conjunto completo
        for _ in range(length):
            password += secrets.choice(all_characters)

        # Lista de restricciones que deben cumplirse, con sus respectivos patrones regex
        constraints = [
            (nums, r'\d'),                          # Dígitos (0-9)
            (special_chars, fr'[{symbols}]'),       # Caracteres especiales
            (uppercase, r'[A-Z]'),                  # Letras mayúsculas
            (lowercase, r'[a-z]')                   # Letras minúsculas
        ]

        # Verifica que se cumplan todas las restricciones utilizando expresiones regulares
        if all(
            constraint <= len(re.findall(pattern, password))  # ¿Hay suficientes coincidencias del patrón?
            for constraint, pattern in constraints
        ):
            break  # Si cumple todas las restricciones, termina el bucle y conserva la contraseña
    
    return password  # Devuelve la contraseña generada

# Punto de entrada del script si se ejecuta directamente
if __name__ == '__main__':
    new_password = generate_password()  # Llama a la función con los valores por defecto
    print('Generated password:', new_password)  # Imprime la contraseña generada
