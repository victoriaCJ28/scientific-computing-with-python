text = 'mrttaqrhknsw ih puggrur'  # Texto cifrado
custom_key = 'happycoding'  # Clave para cifrar/descifrar

def vigenere(message, key, direction=1):
    key_index = 0  # Índice para recorrer la clave
    alphabet = 'abcdefghijklmnopqrstuvwxyz'  # Alfabeto usado para cifrado/descifrado
    final_message = ''  # Variable donde se almacenará el mensaje final

    for char in message.lower():  # Convertimos el mensaje a minúsculas para uniformidad

        # Si el carácter no es una letra, se agrega sin modificar
        if not char.isalpha():
            final_message += char
        else:        
            # Se obtiene el carácter de la clave correspondiente
            key_char = key[key_index % len(key)]
            key_index += 1  # Se avanza en la clave

            # Se calcula el desplazamiento basado en el carácter de la clave
            offset = alphabet.index(key_char)
            index = alphabet.find(char)  # Se obtiene la posición del carácter en el alfabeto
            new_index = (index + offset * direction) % len(alphabet)  # Se aplica la transformación
            final_message += alphabet[new_index]  # Se agrega el carácter cifrado/descifrado al mensaje final
    
    return final_message  # Se retorna el mensaje final

def encrypt(message, key):
    return vigenere(message, key)  # Cifrado con la función Vigenère
    
def decrypt(message, key):
    return vigenere(message, key, -1)  # Descifrado invirtiendo la dirección

# Imprimir los valores iniciales
print(f'\nEncrypted text: {text}')
print(f'Key: {custom_key}')

# Descifrar el mensaje
decryption = decrypt(text, custom_key)
print(f'\nDecrypted text: {decryption}\n')
#end
