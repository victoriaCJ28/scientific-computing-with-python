# Número de discos
NUMBER_OF_DISKS = 5

# Las torres A, B y C representadas como listas (A empieza con todos los discos)
A = list(range(NUMBER_OF_DISKS, 0, -1))  # Discos del más grande (abajo) al más pequeño (arriba)
B = []  # Torre auxiliar
C = []  # Torre destino

def move(n, source, auxiliary, target):
    if n <= 0:
        return  # Caso base: no hay discos que mover

    # Paso 1: mover n-1 discos desde la torre origen a la torre auxiliar
    # Esto se hace recursivamente, usando la torre destino como auxiliar temporal
    move(n - 1, source, target, auxiliary)

    # Paso 2: mover el disco más grande (el número n) directamente a la torre destino
    target.append(source.pop())

    # Mostrar el estado actual de las torres
    print(A, B, C, '\n')

    # Paso 3: mover los n-1 discos que están en la torre auxiliar a la torre destino
    # Esto se hace recursivamente, usando la torre origen como auxiliar
    move(n - 1, auxiliary, source, target)

# Llamada inicial para mover todos los discos de A a C usando B como auxiliar
move(NUMBER_OF_DISKS, A, B, C)
