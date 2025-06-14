# tetrominos.py

def obtener_tetrominos():

    O = [
        [1, 1],
        [1, 1]
    ]

    I = [
        [1],
        [1],
        [1],
        [1]
    ]

    L = [
        [1, 0],
        [1, 0],
        [1, 1]
    ]

    J = [
        [0, 1],
        [0, 1],
        [1, 1]
    ]

    T = [
        [1, 1, 1],
        [0, 1, 0]
    ]

    Z = [
        [1, 1, 0],
        [0, 1, 1]
    ]

    U = [
        [1, 0, 1],
        [1, 1, 1]
    ]

    MAS = [
        [0, 1, 0],
        [1, 1, 1],
        [0, 1, 0]
    ]

    return [O, I, L, J, T, Z, U, MAS]
