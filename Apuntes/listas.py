# Las listas nos permiten almacenar una secuencia de objetos en una única unidad de memoria.

# Generalmente creamos listas usando su expresión literal, [e0, e1, e2, ..., en], donde e0 es el elemento 
# en el índice 0, e1 el que está en la 1, y así sucesivamente.

frutas = ["Manzana", "Banana", "Pera", "Uva", "Kiwi", "Tortuga"]

# Las listas son un tipo secuencia, tal como los strings. En consecuencia, muchas de las cosas que podemos hacer con
# ellas nos van a resultar familiares.

print(len(frutas))      
print(f'El elemento en la posición 2 (el tercero) de la lista frutas es {frutas[0]}.')

# print(f"Si descomento esto que trata de acceder a {frutas[45]} el programa explota. No me puedo pasar de largo.")

for fruta in frutas:
    print(fruta, end=' ')

print(frutas[1:4])
print(frutas[::2])  # ¿Qué es esto?
print(frutas[:])    # ¿Qué estoy haciendo de manera muy simple?

# Podemos crear una lista a partir de cualquier ITERABLE usando la función* list(<iterable>).

letras_individuales = list("abcdefg")
print(letras_individuales)

numeros_pares_de_2_a_16 = list(range(2, 17, 2))
print(numeros_pares_de_2_a_16)

# También podemos usar la "suma" y el "producto" para combinar o extender listas.

quince_ceros = [0] * 15
print(quince_ceros)

letras_y_numeros = ['a', 'b', 'c'] + [1, 2, 3]
print(letras_y_numeros)

# Este último ejemplo, además, nos muestra que las listas pueden contener elementos de diferente tipo.
# Sin embargo, generalmente (aunque ciertamente no siempre) se trata de mantener su contenido consistente.

lista_chancha = ["Soy un string", 1, 3.5, {"¿Qué soy?"}, {"nombre": "carlos", "edad": 145}, (1, range(2, 90)), ["una", "lista", "dentro", "de", "otra"]]
# Antes de descomentar la linea de abajo, tratá de adivinar cuál va a ser su salida.
print(len(lista_chancha))

# Independientemente de su tipo, cada elemento de una lista (cada "cosa" separada por una coma), sin importar si es un tipo "simple" (como un número) o "compuesto"
# (como otra lista) cuenta como uno (1) al momento de calcular su longitud.


print()
print()

# MUTABILIDAD

# La diferencia fundamental entre las listas y otros iterables (en particular, los strings) es que PUEDEN SER MODIFICADAS a través de varias operaciones.

# 1. Inserción
# Las listas proveen dos métodos destinados a agregar elementos a una lista existente.

l = []                              # Creo una lista vacía (longitud 0)
l.append("primer elemento")         # El método append agrega el elemento pasado por parámetro AL FINAL de la lista sobre la cual es llamado
l.append("segundo elemento")         
print(l)

l.insert(1, "ahora yo soy el segundo elemento") # insert coloca el elemento dado antes del que ocupa la posición indicada
                                                # En efecto, esto no hace más que agregarlo precisamente en ese lugar.
print(l)

l.insert(45, "¿qué está pasando?")              # curiosamente, nos podemos pasar de largo con el índice.
print(l)                                        # ¿cuál fue el resultado?

# Como vimos anteriormente, podemos "sumar" listas. Como probablemente se imaginan, y de forma similar a lo que ocurre con strings, esto
# resulta en la creación de una lista nueva que es la concatenación de las dos involucradas en la operación. En el ejemplo siguiente, la lista apuntada
# por la variable b no es modificada.

a = [1, 2, 3]
b = a
a = a + [4, 5, 6]

print(a)
print(b)
print("¿Es a igual a b?:", "Sí" if a == b else "No")

print()
# SIN EMBARGO, y posiblemente de forma contraintuitiva, NO OCURRE LO MISMO si usamos el operador <+=>. 

c = ['a', 'b', 'c']
d = c
c += ['e', 'f', 'g']
print(c)
print(d)
print("¿Es c igual a d?:", "Sí" if c == d else "No")

# Este es un excelente momento para decir que Python considera que dos listas son iguales si tienen la misma longitud y son iguales elemento a elemento 
# (primero con primero, segundo con segundo). Pará, ¿no es acaso eso una definción recursiva?

print('\n')

# 2. Inclusión
# Podemos verificar si un elemento se encuentra dentro de una lista usando el operador <in>. Cuando hablamos de verificar, nos referimos a obtener una respuesta
# por sí o por no; en nuestro lenguaje, True or False

if "Tortuga" in frutas:
    print("Sí, este es el lugar donde esperaba encontrar una tortuga.")

if "Lechuza" not in frutas:
    print("Claramente no hay lugar para una lechuza en un listado de frutas.")

# <in> funciona mirando si existe algún elemento igual al dado dentro de la lista (de hecho, funciona con iterables en general, no únicamente con listas (PROBALO!!!)).
# Nuevamente nos encontramos ante el interrogante de qué significa que dos objetos sean iguales. Afortunadamente, no es algo de lo que se tengan que preocupar por el momento;
# con la intuición basta.

print('\n')

# 3. Borrado
# Una forma de eliminar elementos de una lista es usando el método pop(), al que puede proveersele un índice de manera opcional.

print(f"c antes del borrado: {c}\nLongitud actual: {len(c)}")
c.pop()     # Por defecto, se elimina el último elemento.
# No sólo se elimina un elemento, sino que también se reduce la longitud de la lista para que no quede un espacio "vacío".
print(f"c después del borrado: {c}\nLongitud actual: {len(c)}")

c.pop(2)
print(f"c después de borrar el elemento en el índice 2: {c}\nLongitud actual: {len(c)}")

# c.pop(15)   # Proveer un índice fuera de rango provoca un error

# Alternativamente, podemos usar el método remove para eliminar la PRIMERA APARICIÓN del elemento que indiquemos.
# Esto es util si no conocemos de antemano en qué índice se encuentra, o siquiera si está ahí en absoluto.

print('\n')

import random   # 1) No le presten atención a esto  2) Hacer un import a mitad de código es una chanchada

lista_misteriosa = []
for _ in range(random.randint(15, 25)):                  # Le agregamos una cantidad aleatoria entre 15 y 25 de elementos
    lista_misteriosa.append(random.randint(0, 20))      # Los elementos también son aleatorios. En este caso, números entre 0 y 20

print('La lista misteriosa resultante es', lista_misteriosa)

# Si quisiéramos asegurarnos que el número 15 no se encuentra en la lista, podemos hacer lo siguiente:

while 15 in lista_misteriosa:
    lista_misteriosa.remove(15)

print('La lista misteriosa, ahora libre de la influencia maligna del número 15:', lista_misteriosa)
