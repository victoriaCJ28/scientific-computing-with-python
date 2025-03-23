def verify_card_number(card_number):
    # Inicializamos la suma de los dígitos en posiciones impares
    sum_of_odd_digits = 0
    
    # Invertimos el número de la tarjeta para facilitar los cálculos
    card_number_reversed = card_number[::-1]
    
    # Extraemos los dígitos en posiciones impares (contando desde 0 en la lista invertida)
    odd_digits = card_number_reversed[::2]

    # Sumamos los dígitos impares directamente
    for digit in odd_digits:
        sum_of_odd_digits += int(digit)

    # Inicializamos la suma de los dígitos en posiciones pares
    sum_of_even_digits = 0
    
    # Extraemos los dígitos en posiciones pares
    even_digits = card_number_reversed[1::2]
    
    for digit in even_digits:
        number = int(digit) * 2  # Multiplicamos por 2 los dígitos en posición par
        if number >= 10:  # Si el resultado es mayor o igual a 10, sumamos sus dígitos
            number = (number // 10) + (number % 10)
        sum_of_even_digits += number
    
    # Calculamos el total de ambas sumas
    total = sum_of_odd_digits + sum_of_even_digits
    print(total)  # Imprimimos el total calculado
    
    # La tarjeta es válida si el total es múltiplo de 10
    return total % 10 == 0

def main():
    card_number = '4111-1111-4555-1142'  # Número de tarjeta de prueba
    
    # Creamos una tabla de traducción para eliminar guiones y espacios
    card_translation = str.maketrans({'-': '', ' ': ''})
    
    # Aplicamos la traducción para obtener solo los dígitos de la tarjeta
    translated_card_number = card_number.translate(card_translation)

    # Verificamos si el número de tarjeta es válido
    if verify_card_number(translated_card_number):
        print('VALID!')
    else:
        print('INVALID!')

# Ejecutamos la función principal
main()
