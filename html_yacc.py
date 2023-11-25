        # PARTE 2: ANALISIS GRAMATICAL (PARSING) USANDO YACC
# DE LA ENTRADA YA TOKENIZADA CON LEX 

import ply.yacc as yacc
from html_lex import tokens

from IPython.core.interactiveshell import InteractiveShell
InteractiveShell.ast_node_interactivity = "all"

import re

with open('JSONTEST.json') as doc1: 
    text = doc1.read()     # por default se abre como sólo lectura doc = open("Data/Example1.txt", 'r') 
    
doc1.close() # qué pasa si abrimos y no cerramos el archivo?

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


def p_start(p):
    'S : SBL A'
    p[0]=p[1]
    print(p[0])
    print(p)


def p_nodeA(p):
    'A : text B'
    p[0] = p[1]
    print(p[0])

def p_nodeB_text(p):
    'B : text B'
    p[0] = p[1]
    print(p[0])

def p_nodeB_keyId(p):
    'B : keyId C'
    p[0] = p[1]
    print(p[0])

def p_nodeB_SBR(p):
    'B : SBR M'
    p[0] = p[1]
    print(p[0])

def p_nodeC(p):
    'C : idValue D'
    p[0] = p[1]
    print(p[0])

def p_nodeD(p):
    'D : text E'
    p[0] = p[1]
    print(p[0])

def p_nodeE_text(p):
    'E : text E'
    p[0] = p[1]
    print(p[0])

def p_nodeE(p):
    'E : idNombre F'
    p[0] = p[1]
    print(p[0])

def p_nodeF(p):
    'F : valueNombre G'
    p[0] = p[1]
    print([0])

def p_nodeG(p):
    'G : text H'
    p[0] = p[1]
    print([0])

def p_nodeH_text(p):
    'H : text H'
    p[0] = p[1]
    print([0])

def p_nodeH(p):
    'H : idEmail I'
    p[0] = p[1]
    print([0])

def p_nodeI(p):
    'I : valueEmail J'
    p[0] = p[1]
    print([0])

def p_nodeJ(p):
    'J : text K'
    p[0] = p[1]
    print([0])

def p_nodeK_text(p):
    'K : text K'
    p[0] = p[1]
    print([0])

def p_nodeK(p):
    'K : idTelefono L'
    p[0] = p[1]
    print([0])

def p_nodeL(p):
    'L : valueTelefono A'
    p[0] = p[1]
    print([0])

def p_end(p):
    'M : '
    p[0] = ""


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)


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
   print("result: ", result)
   x=1