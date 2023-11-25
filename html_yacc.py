# PARTE 2: ANALISIS GRAMATICAL (PARSING) USANDO YACC
# DE LA ENTRADA YA TOKENIZADA CON LEX 

#Se importan los elementos del Yacc 
import ply.yacc as yacc
#Se obtienen los tokesn del archivo lex
from html_lex import tokens
#Se importan los elementos para poder generar el CVS
import csv
from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"
#Se importa el modulo que permite la evalucion de expresiones regulares
import re

#Se abre el archivo JSON de donde se obtiene la información
with open('CV-json.json') as doc1: 
    # por default se abre como sólo lectura doc = open("Data/Example1.txt", 'r')
    text = doc1.read()     
# Se cierra el documento 
doc1.close() 

#Se establecen los tokens que se usaran
precedence = (
    (
        'SBL',
        'SBR',
        'keyId',
        'idValue',
        'idNombre',
        'valueNombre',
        'idEmail',
        'valueEmail',
        'idTelefono',
        'valueTelefono',
        'text'
    ),
)

#Se crean las listas donde guardaremos los datos que extraeremos del JSON
titles=['ID','NAME','EMAIL','PHONE']
ids=[]
names=[]
emails=[]
phones=[]

#Se generan las reglas 
def p_start(p):
    'S : SBL A SBR'
    p[0]=p[1]

def p_nodeA_A(p):
    'A : B keyId idValue B idNombre valueNombre B idEmail valueEmail B idTelefono valueTelefono B A'
    p[0] = p[1]
    ids.insert(0,p[3])
    names.insert(0,p[6])
    emails.insert(0,p[9])
    phones.insert(0,p[12])

def p_nodeA_B(p):
    'A : B keyId idValue B idNombre valueNombre B idEmail valueEmail B idTelefono valueTelefono B'
    p[0] = p[1]
    ids.insert(0,p[3])
    names.insert(0,p[6])
    emails.insert(0,p[9])
    phones.insert(0,p[12])

def p_nodeB_B(p):
    'B : text B'
    p[0] = p[1]

def p_nodeB(p):
    'B : text'
    p[0] = p[1]

def p_end(p):
    'B : '
    p[0] = ""


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")


# Build the parser
parser = yacc.yacc()

x=0
while x==0:
   try:
       s = text
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   x=1


# Combinar las listas de datos en una lista de tuplas
combined_data = list(zip(ids, names, emails, phones))

# Nombre del archivo CSV
csv_file = 'output.csv'

# Escribir el archivo CSV
with open(csv_file, 'w', newline='') as file:
    writer = csv.writer(file)
    
    # Escribir la cabecera
    writer.writerow(titles)
    
    # Escribir los datos
    writer.writerows(combined_data)

print(f'Se ha creado el archivo CSV: {csv_file}')