# A menudo tomamos decisiones o llevamos a cabo acciones dependiendo de se alguna condición particular
# se cumple o no. Esto puede ocurrir o no, sin otras opciones entre medio.

# Por ejemplo, imaginemos que sólo podemos sacar los residuos reciclables los días martes. En ese caso, sólo lo haremos 
# si el día actual es martes, y evitaremos hacerlo cualquier otro. Notemos cómo no es posible que un día sea "medio martes" o "un poco jueves";
# es martes o no es martes.

# En el contexto de la lógica, estos valores binarios (sí o no, prendido o apagado, ...) se representan mediante <Verdadero> y <Falso>,
# y llamamos a este tipo de valores Booleanos, en honor a George Bool, padre del álgebra computacional moderna. Dichos valores se encuentran
# representados de una manera u otra en todos los lenguajes de programación, y nos permiten ejecutar código de manera condicional, es decir, dependiendo
# de algún factor que determinemos.

# Del mismo modo que al trabajar con números contamos con los literales 1, 2, 3, ..., en Python contamos con los literales
# <True> y <False> (¡noten las mayúsculas!), representando los valores Verdadero y Falso, respectivamente.

v1 = True
v2 = False

print('v1:', v1)
print('v2:', v2)

# Generalmente no se opera directamente con estos valores, sino que estos se derivan como resultado de la evaluación (el cálculo)
# de expresiones más complejas. Esto último es importante: por enredadas que parezcan ciertas expresiones, si su resultado es booleano,
# esto quiere decir que sólo puede ser Verdadero o Falso.

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# OPERADORES DE COMPARACIÓN

# Una de las maneras más comunes de obtener un resultado booleano es haciendo uso de los <Operadores de Comparación>, que son usados
# sobre dos expresiones (generalmente del mismo tipo). Estos son:
#   - ==        Igual
#   - !=        Desigual
#   - <         Menor
#   - <=        Menor o igual
#   - >         Mayor
#   - >=        Mayor o igual

n = 5
print(f'¿Es {n} menor que diez?\t', n < 10)
# Este caso cómo loss operadores de comparación tienen menor prioridad que los aritméticos (en este caso, suma)
print(f'Si sumo 4 a {n}, ¿el resultado es menor que 2?', n + 4 < 2)
print(f'¿Es {n} igual a {n}?', n == n)
print(f'¿Y al doble de {n}, {n*2}?', n == 2 * n)
print(f'Como {n} = {2 * n} es falso, {n} ≠ {2 * n} tiene que ser {n != 2 * n}')
print(f'Como es cierto que {n} < 10, también debe serlo {n} ≤ 10: {n <= 10}')

# --------------------------------------------------------------------------------------------------------------------------------------------------------------

# OPERADORES LÓGICOS

# Existen tres operadores que funcionan exclusivamente sobre valores booleanos, y cuyo resultado también es booleano. En lógica, se conocen como
# <Y>, <O> y <NO> (o negación), y en Python están representados por las palabras <and>, <or> y <not>.

# <or> y <and> son operadores binarios (aplican sobre dos operandos, como la suma), mientras que 
# <not> es unario (como poner un menos delante de un número).

# En los siguientes ejemplos, las letras A y B representan expresiones booleanas arbitrarias.

# - or
#   A or B es verdadero cuando A, B o los dos a la vez son verdaderos.
print('3 es mayor que 2183123 o es igual a 3:', 3 > 2183123 or 3 == 3)  # los operadores lógicos tienen menor prioridad que los de comparación
#   Como consecuencia de lo anterior, A or B es falso únicamente cuando tanto A como B son falsos.
print('3 es mayor que diez o 3 es distinto a 3:', 3 > 2183123 or 3 != 3)

