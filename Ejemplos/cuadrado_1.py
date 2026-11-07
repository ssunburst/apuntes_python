# Dibuja un cuadrado con lado de longitud <largo_lado>
def dibujar_cuadrado(largo_lado):
    for i in range(largo_lado):
        dibujar_renglon(largo_lado,                          # El largo del renglón es igual a la cantidad de renglones a dibujar
                            (i > 0) and (i < largo_lado - 1) # Un renglón es interno si está entre el segundo y el anteúltimo, inclusive
                        )


# Dibuja un renglón individual del cuadrado de longitud <largo>. 
# Si <es_renglon_interno> es verdadero, los puntos internos son espacios en lugar de asteriscos.
def dibujar_renglon(largo, es_renglon_interno):
    for i in range(largo):
        simbolo = '*'       # Asumimos que el símbolo a dibujar es un asterisco
        es_punto_interno = (i > 0) and (i < largo - 1)  # Un punto es interno si está entre el segundo y el anteúltimo, inclusive

        if es_renglon_interno and es_punto_interno:     # Cambiamos de símbolo solo si se trata de un renglón interno Y estoy dibujando
            simbolo = ' '                               # Un punto interno

        print(simbolo, end='')                          # Sea cual sea el símbolo, lo dibujamos sin saltar de línea
    print()                                             # Una vez que terminamos con el renglón, saltamos de línea


dibujar_cuadrado(10)