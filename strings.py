# Todo lo que empieza con un numeral (#) es un comentario y no es interpretado por Python.
# Comentá / descomentá las líneas que quieras y ejecutá el programa 

# Las cadenas de caracteres (strings) son el tipo de dato que usamos
# para representar texto arbitrario, es decir, cuyo contenido -en principio-
# puede ser cualquier cosa: números, nombres, símbolos aleatorios...
string1 = 'Esto es una cadena de caracteres'
string2 = "Esto es otra cadena de caracteres"



# PRINT

# La función <print(...)> nos permite mostrar información a través de la consola.
# Acepta prácticamente cualquier tipo de parámetro y muestra una representación en texto del dato introducido.
print('Hola!')  # Imprimimos el literal 'Hola!'
print(string1)  # Imprimimos el contenido de la variable <string1>
print('El contenido de la variable string2 es', string2, ". INCREIBLE!!!")  # Podemos separar entre comas tantos parámetros como queramos (inclusive 0)
# Por defecto, print separa los parámetros ingresados con una coma y termina la salida con un salto de línea (un "ENTER").
# Podemos cambiar ese comportamiento usando los PARÁMETROS OPCIONALES sep y end, que, DE SER USADOS, deben aparecer al final de la lista.
print(1 , 'Escuela', True, ("Esto se llama", "Tupla"), sep='-_-', end='TERMINE!!\n')    # \n se considera un solo símbolo (caracter), y simboliza un salto de línea.



# INPUT

# Podemos usar la función <input(...)> para leer texto provisto por el usuario.
# Al invocarla, el programa se pausa hasta que se presione ENTER en la consola. Lo que se haya escrito se vuelve el valor retornado por la función.
entrada = input()
print(entrada)
# Podemos combinar print e input en una sola línea de código. No obstante, es desprolijo y difícil de seguir.
print(input("Decí lo que quieras! "))   # input acepta un string para mostrar como guía al usuario.



# INDEXADO

w = 'palabra'
# La notación [i] nos permite acceder al símbolo (i+1)-ésimo de un string.
print(w[0]) # Así, acá w[0] nos muestra 'p', el primer (1) caracter de 'palabra'
print(w[3]) # w[3] nos muestra el cuarto, 'a'
# print(w[25]) # Los índices que superan la longitud del string no están permitidos. Si descomentás esta línea, el programa va a arrojar un error
print(len(w))  # La función <len(...)> nos permite saber cuál es la longitud de un string.
print(w[len(w) - 1])    # De este modo, SIEMPRE el último caracter de w se encontrará en la posición [len(w) - 1]
print(w[-1])    # Alternativamente, los índices negativos comienzan del final, por lo que w[-1] produce la misma salida que lo anterior

# También podemos generar un string nuevo (es decir, el original no es modificado) indicando un rango de la forma w[a:b]. Esto resultará en el substring contenido en w desde la posición a
# (inclusive) hasta la posición b (no incluida).
# De omitir cualquiera de los dos (a o b), se asume 0 para el primero y len(w) - 1 para el segundo.
w1 = w[0:len(w)]        # w1 va a ser igual a w
w2 = w[0: 4]            # Desde la posición 0 a la 3 (4 no incluido), "pala"
w3 = w[3:5]             # Desde la posición 3 a la 4 (5 no incluido), "ab"
w4 = w[:6]              # Desde la posición 0 a la 5
w5 = w[4:]              # Desde la posición 4 al final
w6 = w[:]               # Desde el inicio hasta el final. Nuevamente, igual a w
print(w1, w2, w3, w4, w5, w6)



# Comparación

# De la misma manera que comparamos números, Python permite, además del símbolo == para verificar si dos cadenas son iguales,
# emplear los símbolos <, >, <= y >= para comparar el orden lexicográfico de dos expresiones. El resultado de la comparación es un valor booleano,
# True o False

print("alabarda" < "hola")
print("palabra" == w)
print("Araucaria" > "Brócoli")
print("a" > "A")                # Hay que tener cuidado con ciertas consideraciones, como qué va antes, si las mayúsculas o las minúsculas
# Para no preocuparnos por eso, podemos generar un string nuevo únicamente en minúsculas (o mayúsculas) y comparar esos resultados.
palabra1 = "GMmnQp"
palabra2 = "GmfnJS"
# En este ejemplo, nos gustaría que la comparación resulte en que palabra 2 está antes que palabra 1, pero como palabra2 contiene un M mayúscula
# que se considera anterior a la m minúscula, palabra 1 resulta anterior.
print (palabra2 < palabra1)
print(palabra2.lower() < palabra1.lower())  # El método* <lower()> crea un string nuevo a partir del original, completamente en minúsculas.
