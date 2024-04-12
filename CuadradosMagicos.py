def sumaFila(cuadrado, i):
    j = 0
    suma = 0
    while j < len(cuadrado):
        suma = suma + cuadrado[i][j]
        j += 1
    return suma



def sumaColumna(cuadrado, j):
    i = 0
    suma = 0
    while i < len(cuadrado):
        suma = suma + cuadrado[i][j]
        i += 1
    return suma


def sumaColumnas(cuadrado, numeroMagico):
    j = 0
    i = 0
    suma = 0
    
    while j < len(cuadrado):
        suma = 0
        while i < len(cuadrado):
            suma = suma + cuadrado[i][j]
            i += 1
        if suma == numeroMagico :
            i = 0
            j += 1
            
        else : break
    return suma


def sumaDiagonales(cuadrado, numeroMagico):
    i = 0
    j = 0
    suma = 0
    while i < len(cuadrado): ##primera diagonal, de izquierda a derecha
        suma = suma + cuadrado[i][j]
        i += 1
        j += 1
    if suma == numeroMagico: ## diagonal opuesta
        suma = 0
        i = 0
        j = j - 1
        while i < len(cuadrado):
            suma = suma + cuadrado[i][j]
            i += 1
            j = j - 1

    return suma

def no_esta_en_matriz(i, matriz):
    for fila in matriz:
        for elemento in fila:
            if elemento == i:
                return False
    return True

def esCuadradoMagico(cuadrado, numeroMagico):
    res = True
    i = 0
    if sumaDiagonales(cuadrado, numeroMagico)== numeroMagico and sumaColumnas(cuadrado, numeroMagico)== numeroMagico:
        while i < len(cuadrado) and res == True:
            if sumaFila(cuadrado,i) == numeroMagico:
                res = True
            else : 
                res = False
            i = i+ 1
            
    else :
        res = False    
    return res


def magiCuadrado (n):

    cuadrado = [[0] * n for _ in range(n)]
    numeroMagico = ((n * n * n) + n)//2
    
    def backtrack(i, j):
        
        if i == n and j == n and esCuadradoMagico(cuadrado, numeroMagico):
            return 1
        contador=0
    
        ## siempre que no tenga que cambiar de fila hago esto, pero cuando llego a la ultima columna cambio el if
        if j < n - 1 :
            for u in range (1 , n*n + 1):
                if sumaFila(cuadrado, i) + u <= numeroMagico and sumaColumna(cuadrado, j) + u <= numeroMagico :
                    if no_esta_en_matriz(u, cuadrado):
                        cuadrado[i][j] = u
                        contador += backtrack(i , j +1)
                        cuadrado [i][j] = 0
        elif j == n-1 and i < n-1: ##cuando llego a la ultima columna, si no estoy en la ultima fila hago esto 
            for m in range (1 , n*n + 1):
                if sumaFila(cuadrado,i) + m == numeroMagico and no_esta_en_matriz(m, cuadrado) and sumaColumna(cuadrado, j) + m <= numeroMagico :
                        cuadrado[i][j] = m
                        
                        contador += backtrack(i+1, 0)

                        cuadrado [i][j] = 0
            
        elif i == n-1: ## cuando estoy en el ultimo lugar de la matriz
                for h in range (1 , n*n + 1):
                    if sumaFila(cuadrado,i) + h == numeroMagico and no_esta_en_matriz(h, cuadrado)and sumaColumna(cuadrado, j) + h == numeroMagico :
                        
                        cuadrado[i][j] = h
                        contador += backtrack(i+1, j+1)
                        cuadrado[i][j] = 0
                        

                return contador     

            
        return contador    
        
        
    return backtrack(0, 0)
        
print (magiCuadrado(3))








