# Cuando escribimos programas, especialmente a medida
# que crecen en volumen, es deseable dividirlos en unidades
# más manejables. Esto nos permite desarrollarlas, testearlas,
# y mantenerlas de forma separada. La manera principal en la
# que hacemos esto en Python es a través del uso de FUNCIONES.

# Las funciones son grupos de sentencias relacionadas que
# pueden ser llamadas en conjunto, que pueden o no necesitar
# uno o más parámetros, y que pueden o no retornar algún valor.

# El uso de funciones trae aparejadas múltiples ventajas. Para empezar,
# podemos definirlas en un lugar y usarlas en otro (incluso en un
# archivo diferente), tantas veces como queramos. Si más tarde necesitamos modificarlas,
# este cambio va a alcanzar a todos los lugares en los que son llamadas. Como resultado, 
# nuestro código resulta más modular, fácil de entender y de mantener. 
# 
# Adicionalmente, podemos brindarles nombres descriptivos que evidencien fácilmente su intención.

# Su sintaxis es
#   def <nombre_funcion>(<parametro_1>, <parametro_2>, ..., <parametro_n>):
#       <bloque_funcion>
# donde n puede ser cero (es decir, la función puede no llevar parámetros). Los
# parámetros son la información que la función necesita para hacer su trabajo.

# Por ejemplo, si queremos definir una función que calcule el perímetro de un cuadrado dependiendo
# de la medida de uno de sus lados, vamos a necesitar proveerle dicha medida.
def perimetro_cuadrado(lado): 
    return lado * lado             # cuando queremos devolver un valor, usamos la sentencia return <expresion>

print(perimetro_cuadrado(3))
print(perimetro_cuadrado(5))