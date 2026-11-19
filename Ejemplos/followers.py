# Para que el programa funcione correctamente, debe contarse con los archivos
# following.json y followers_1.json presentes en la misma carpeta. 
# Los mismos deben obtenerse desde las opciones de Instagram.

# Agregamos funcionalidad que nos permite trabajar con información
# en formato json
import json

# Abrimos e interpretamos el archivo de seguidores
# Guardamos su contenido en una variable llamada followers_data
with open("followers_1.json", encoding='utf-8') as f:
    followers_data = json.load(f)

# Abrimos e interpretamos el archivo de seguidos
# Guardamos su contenido en una variable llamada following_data
with open("following.json", encoding='utf-8') as f:
    following_data = json.load(f)

# La diferencia entre las dos maneras suguientes de procesar la información
# se debe a cómo está estructurado cada archivo.

# Tomamos del contenido de sólo el contenido de seguidores que
# nos importa (los nombres de usuario) y los almacenamos en un conjunto
followers = {
    item["string_list_data"][0]["value"] for item in followers_data
}

# Tomamos del contenido de sólo el contenido de seguidos que
# nos importa (los nombres de usuario) y los almacenamos en un conjunto
following = {
    item['title']
    for item in following_data['relationships_following']
}

# La diferencia entre ambos conjuntos nos da qué usuarios seguidos
# no está entre nuestros seguidores.
# sorted es una función que genera una lista ordenada con el resultado.
difference = sorted(following - followers)

# Imprimimos los nombres de usuario del resultado, uno por uno.
for username in difference:
    print(username)

# Si el programa se ejecuta por fuera del IDE (por ejemplo, haciéndole doble click),
# el mismo se cierra una vez que finaliza. La llamada a input() siguiente "congela"
# la pantalla con los resultados
input()