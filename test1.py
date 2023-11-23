from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import re

with open('CV-Json.json') as doc1: 
    text = doc1.read()     # por default se abre como sólo lectura doc = open("Data/Example1.txt", 'r') 
    
doc1.close() # qué pasa si abrimos y no cerramos el archivo?

nombre = re.compile(r"\"name\": \"[A-Z,a-z, ]*\"")
matchesNames = nombre.findall(text)

correo = re.compile(r"\"email\": \"[A-Z,a-z,0-9]*@[A-Z,a-z,\.]*\"")
matchesEmail = correo.findall(text)

trabajo = re.compile(r"\"position\": \"[A-Z,a-z, ]*\"")
matchesPositions = trabajo.findall(text)

if(matchesEmail!=0):
    for i in range(len(matchesEmail)):
        print('CV '+ str(i+1))
        print(matchesNames[i])
        print(matchesEmail[i])
        print(matchesPositions[i])
        print('\n')
else:
    print('not found!')

