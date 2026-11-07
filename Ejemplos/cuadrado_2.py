# Dibuja un cuadrado con lado de longitud <largo_lado>
def dibujar_cuadrado(largo_lado):
    for i in range(largo_lado):
        es_renglon_interno = (i > 0) and (i < largo_lado - 1) 
        if es_renglon_interno:
            dibujar_renglon_interno(largo_lado)
        else:
            dibujar_renglon_extremo(largo_lado)
        print()
        

def dibujar_renglon_interno(largo):
    for i in range(largo):
        print('*' if (i == 0 or i + 1 == largo) else ' ', end='')

def dibujar_renglon_extremo(largo):
    print('*' * largo, end='')

dibujar_cuadrado(7)