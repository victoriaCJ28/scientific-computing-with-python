text = 'Hello Zaira'  # Texto original a cifrar
shift = 3  # Número de posiciones a desplazar

def caesar(message, offset):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Definimos el alfabeto usado en el cifrado
    encrypted_text = ''  # Variable para almacenar el texto cifrado

    for char in message.lower():  # Convertimos el mensaje a minúsculas para mantener uniformidad
        if char == ' ':  # Si el carácter es un espacio, lo mantenemos igual
            encrypted_text += char
        else:
            index = alphabet.find(char)  # Encontramos la posición del carácter en el alfabeto
            new_index = (index + offset) % len(alphabet)  # Calculamos la nueva posición desplazada
            encrypted_text += alphabet[new_index]  # Agregamos el nuevo carácter cifrado
    
    # Imprimimos el texto original y el cifrado
    print('plain text:', message)
    print('encrypted text:', encrypted_text)

# Cifrar con desplazamiento de 3 posiciones
caesar(text, shift)

# Cifrar con desplazamiento de 13 posiciones (cifrado ROT13)
caesar(text, 13) 
