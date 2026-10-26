# Aquellos tipos de Python que admiten ser recorridos usando <for>* se conocen como ITERABLES
# Entre ellos se encuentran los strings, las listas y las tuplas, entre otros. Nosotros nos concentraremos fundamentalmente
# en los primeros dos.
#
# En general, podemos pensar a estos tipos iterables como objetos compuestos por elementos "más pequeños":
# Los strings, por ejemplo, están conformados por caracteres. Como Python no distingue entre caracteres individuales y strings
# más largos, estos caracteres no son otra cosa que strings de longitud 1.

# Como dijimos anteriormente, usamos <for> para recorrer objetos iterables. La sintaxis (estructura general) es
# for <VARIABLE> in <ITERABLE>:
#   <BLOQUE>

string_ejemplo = "Soy un string muy feliz"
# En el ejemplo siguiente, como hasta el momento no existe la variable <caracter>, Python la crea.
# <caracter> ciclará todos los posibles valores (caracteres) de <string_ejemplo>, haciendo para cada uno de ellos lo que
# sea que hayamos escrito en el bloque interno.
for caracter in string_ejemplo:
    print(caracter)         # En este caso, lo único que hacemos es mostrar por pantalla cada caracter

print(caracter)             # Al terminar el <for>, la variable usada para recorrer el iterable "sobrevive", es decir, puede seguir siendo usada
                            # En este caso, guarda el último valor que le fue asignado (la z)

# Si bien lo que hacemos dentro de un for suele estar relacionado con la variable que usamos para recorrer el iterable, nada impide que
# este no sea el caso. En el ejemplo siguiente, calculamos la cantidad de caracteres que conforman al string anterior sin hacer uso de <len>.

longitud = 0
for caracter in string_ejemplo:
    longitud = longitud + 1

print(string_ejemplo, 'tiene longitud', longitud)

# Cuando queremos indicar que la variable de recorrido no va a ser usada, es convención llamarla '_'. Este es un nombre de variable "normal"
# (es decir, puede ser leída y escrita como cualquier otra), pero suele reservarse para este caso.
for _ in range(5):          # <range> es otro tipo iterable
    print("Ja", end='')     # Escribimos JaJaJaJaJa

# Si bien solemos usar <for> para hacer recorridas "completas" (es decir, de principio a fin) y recurrimos al <while> 
# cuando creemos que podemos encontrar una situación que amerite hacer lo contrario, podemos 
# interrumpir el proceso haciendo uso de <break>. 
# 
# En este ejemplo, vamos a tratar de detectar si este string contiene un signo '$'. Si es así, no seguimos revisándolo.
for c in 'No tengo $ para comprar pavadas':
    if c == '$':
        break
else:
    print('Esto no va a ocurrir')       # ESTO RARA VEZ SE USA: se puede colocar una sentencia <else> luego de un <for>. Su contenido se
                                        # ejecuta ÚNICAMENTE si el <for> termina normalmente, es decir, no mediante el uso de un <break>.
                                        # Incluyo este ejemplo únicamente por completitud, pero insisto en que no es algo que necesiten saber.
