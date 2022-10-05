def transpuestaVector(a):
    matriz = []
    for i in a:
            matriz.append([i])
    return matriz

def transpuestaMatriz(a):
    matriz = []
    for i in range(len(a)):
        for x in range(len(a[i])):
            if i == 0:
                matriz.append([a[i][x]])
            else:
                matriz[x].append(a[i][x])
    return matriz

def productoVectores(a,b):
    vector = []
    for i in range(len(a)):
        vector.append(producto(a[i], b[i]))
    return vector


def sumaVector(a):
    valorDevolver = a.pop(0)
    while len(a) != 0:
        valorDevolver = suma(valorDevolver, a.pop(0))
    return valorDevolver


def productoMatrices(a, b):
    matriz = []
    for i in range(len(a)):
        p = []
        for j in range(len(b[0])):
            p.append((i, j))
        matriz.append(p)
    transpuesta = transpuestaMatriz(b)
    for i in range(len(matriz)):
        for j in range(len(matriz[i])):
            vector = productoVectores(a[matriz[i][j][0]],transpuesta[matriz[i][j][1]])
            matriz[i][j] = sumaVector(vector)
    return matriz


def productoMatrizPorVector(matriz, vector):
    return productoMatrices(matriz, transpuestaVector(vector))


def consecutiveMultiplicy(matriz, vector, n):
    for i in range(len(matriz)):
        print(matriz[i])
    for x in range(n):
        vector = productoMatrizPorVector(matriz, vector)
    print("----------------" * 2)
    return vector

def suma(a,b):
    cc = (a[0] + b[0])
    ci = (a[1] + b[1])
    num = (cc,ci)
    return num

def producto(a,b):
    cc = ((a[0] * b[0]) - (a[1] * b[1]))
    ci = ((a[0] * b[1]) + (b[0] * a[1]))
    num = (cc, ci)
    return num