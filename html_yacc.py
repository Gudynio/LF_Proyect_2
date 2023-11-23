        # PARTE 2: ANALISIS GRAMATICAL (PARSING) USANDO YACC
# DE LA ENTRADA YA TOKENIZADA CON LEX 

import ply.yacc as yacc
from html_lex import tokens


precedence = (
    (
        'SBL',
        'SBR',
        'keyId',
        'IdValue',
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
    'S : SBL A '
    print(p[1]+'ola')


def p_keyId(p):
    'A : keyId B'
    p[0] = p[1]
    print(p[0]+'  ADIOS')


def p_SBR(p):
    'B : SBR C'
    p[0] = p[1]
    print(p[0]+'  ADIOS')

def p_end(p):
    'C : '
    p[0] = ""


# Error rule for syntax errors
def p_error(p):
    print("Syntax error in input!")
    print(p)




# Build the parser
parser = yacc.yacc()


while True:
   try:
       s = input('Valid expression: > ')
   except EOFError:
       break
   if not s: continue
   result = parser.parse(s)
   print("result: ", result)
