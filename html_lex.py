    # PARTE 1: TOKENIZAR LA ENTRADA USANDO LEX
import ply.lex as lex

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import re

with open('JSONTEST.json') as doc1: 
    text = doc1.read()     # por default se abre como sólo lectura doc = open("Data/Example1.txt", 'r') 
    
doc1.close() # qué pasa si abrimos y no cerramos el archivo?

# Paso 1: Proporcione una lista de tokens que defina
# todos los posibles nombres de token que puede producir
# el lexer.
# La lista de tokens también es utilizada YACC
# para identificar terminales.

tokens = (  
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
)

# Paso 2. Cada token se especifica escribiendo una regla
# de expresión regular, mediante declaraciones que usan
# un prefijo especial *t_* para indicar que define un token.

# Definición de tokens simples:

t_SBL = r"\["
t_SBR = r"\]"
t_keyId= r"\"id\":[ ]*"
t_idValue=r"[0-9]+"
t_idNombre=r"\"name\":[ ]*"
t_valueNombre="\"[A-Z][A-Z,a-z,á-ú]+[ ]*[A-Z][A-Z,a-z,á-ú]+\""
t_idEmail=r"\"email\":[ ]*"
t_valueEmail=r"\"[A-Z,a-z,0-9]*@[A-Z,a-z,\.]*\""
t_idTelefono=r"\"phone\":[ ]*"
t_valueTelefono=r"\"\([0-9]*\)[ ,0-9]*\""
t_text=r'.+'



# Definición de tokens que incluye código para
# complementar, por ejemplo, para la definición de número,
# se incluye su conversión a entero (para este caso):

##def t_NUMBER(t):
##    r'\d+'
##    t.value = int(t.value)
##    return t


# Para incluir caracteres a ignorar, en este caso,
# tabuladores y espacios.
t_ignore  = ' \t'


# Para el manejo de errores en las entradas
def t_error(t):
    #print('Illegal character', t.value[0])
    t.lexer.skip(1)


# Paso 3. Crear el objeto tipo lex (el tokenizador)

lexer = lex.lex()

# Hasta aquí se requiere sólo para tokenizar antes del parseo.


# DE AQUI EN ADELANTE ES PARA VALIDAR ESTE SCRIPT

# # Paso 4. Definir o solicitar la entrada al usuario
# # Se define una cadena de entrada, para este ejemplo.
# # data puede ser una cadena obtenida de un archivo o directamente
# # dada por un usuario desde la línea de comandos.


input_str = text


print('Para terminar introduce ENTER --- ')
 ##
 ### Paso 5. Usar el objeto tipo lex para tokenizar la entrada
 ### Hacer que el objeto tipo lex identifique en la cadena de
 ### entrada los tokens definidos.
 ##
if input_str != '':
    lexer.input(input_str)
 ##
 ### los tokens quedan en la variable lexer de tipo objeto Lexer,
 ### y se puede acceder a esos elementos de la siguiente manera:
 ##
for tok in lexer:
    valx=1
    print(tok)
 ##
 ### La salida de cada tok tiene el siguiente formato:
 ### LexToken(type of token, token, line number, position)
