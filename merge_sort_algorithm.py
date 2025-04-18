def merge_sort(array):
    # Caso base: si el arreglo tiene 1 o 0 elementos, ya está ordenado
    if len(array) <= 1:
        return

    # Encontrar el punto medio del arreglo
    middle_point = len(array) // 2

    # Dividir el arreglo en dos mitades
    left_part = array[:middle_point]
    right_part = array[middle_point:]

    # --- INICIO DE LA RECURSIÓN ---
    # Llamada recursiva para ordenar la mitad izquierda
    merge_sort(left_part)

    # Llamada recursiva para ordenar la mitad derecha
    merge_sort(right_part)
    # --- FIN DE LA RECURSIÓN ---
    # En este punto, left_part y right_part están ordenados por separado

    # Inicializar índices para left_part, right_part y el arreglo original
    left_array_index = 0
    right_array_index = 0
    sorted_index = 0

    # Mezclar los elementos ordenados de left_part y right_part en array
    while left_array_index < len(left_part) and right_array_index < len(right_part):
        # Comparar el elemento actual de cada mitad y poner el menor en array
        if left_part[left_array_index] < right_part[right_array_index]:
            array[sorted_index] = left_part[left_array_index]
            left_array_index += 1
        else:
            array[sorted_index] = right_part[right_array_index]
            right_array_index += 1
        sorted_index += 1

    # Copiar los elementos restantes de left_part (si hay)
    while left_array_index < len(left_part):
        array[sorted_index] = left_part[left_array_index]
        left_array_index += 1
        sorted_index += 1

    # Copiar los elementos restantes de right_part (si hay)
    while right_array_index < len(right_part):
        array[sorted_index] = right_part[right_array_index]
        right_array_index += 1
        sorted_index += 1


# Ejecución del programa principal
if __name__ == '__main__':
    # Lista de números a ordenar
    numbers = [4, 10, 6, 14, 2, 1, 8, 5]

    print('Unsorted array: ')
    print(numbers)

    # Llamada a merge_sort que modifica la lista en su lugar
    merge_sort(numbers)

    print('Sorted array: ' + str(numbers))
