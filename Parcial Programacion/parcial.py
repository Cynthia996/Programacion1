import json
import requests


def get_docs(ruta):
    req = requests.get(ruta)
    if req.status_code == 200:
        dic = json.loads(req.text)
        return dic


def get_charter_by_id(id):
    data = get_docs("https://swapi.dev/api/people/"+str(id))
    return data

def get_all_sw_characters():
    sw_data = []
    data = get_docs("https://swapi.dev/api/people/") 
    while(data["next"]is not None):
        for personaje in data["results"]:
            sw_data.append(personaje)
        data = get_docs(data["next"])
    return sw_data

from random import randint
sw_data = get_charter_by_id
num1 = randint(1,83)
num2 = randint(1,83)

personaje1 =get_charter_by_id(num1)
personaje2 =get_charter_by_id(num2)

print(personaje1)
print(personaje2)

#EJERCICIO 1
#a)
if(personaje1["height"]) > (personaje2["height"]):
    print ("El personaje mas alto es",personaje1["name"],"la altura es", personaje1["height"])

else:
    print ("El personaje mas pesado es",personaje2["name"],"la altura es", personaje2["height"])

#b)
if(personaje1["mass"]) > (personaje2["mass"]):
    print ("El personaje mas pesado es",personaje1["name"],"la altura es", personaje1["mass"])

else:
    print ("El personaje mas pesado es",personaje2["name"],"la altura es", personaje2["mass"])

#c)
 
if len(personaje1['films']) > len(personaje2['films']):
    print ("El personaje que hizo mas peliculas es",personaje1["name"])
else:
    print ("El personaje que hizo mas peliculas es",personaje2["name"])

#d)
if (personaje1 == "Yoda" or personaje2 == "Grievous"):
    print(personaje1)
    print(personaje2)
else:
    print("El personaje no es Yoda ni Grievous")


#Ejercicio 2
sw_data = []

while(urlbase['next'] is not None):
    for doc in urlbase['results']:
        sw_data.append(doc)
    urlbase = consultar_personajes(urlbase['next'])


def nombre (item):
    return (item['name'])

sw_data.sort(key=nombre)

for index, character in enumerate(sw_data):
    
    print(character['name'], character['species'], character['homeworld'])

#b)
for personaje in sw_data:
    if(len(personaje["films"]) == 6):
        print(personaje["name"])

#EJERCICIO 3
from random import randint 

lista =[]
for i in range(0,78):
    num1 = randint(1,78)
    lista.append(num1)

lista.sort()

print("El Menor es",lista[0])
print("El Mayor es:",lista[77])

print(lista)


for lista in range(0,78):
    if(lista % 2 == 0):
        print(lista)