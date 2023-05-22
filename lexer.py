import ply.lex as lex
import re

tokens = ['IDENTIFICADOR', 'NUMERO', 'SUMA', 'RESTA', 'MULTIPLICACION', 'DIVISION',
          'ASIGNACION', 'DIFERENTE', 'MENOR', 'MENORI', 'MAYOR', 'MAYORI', 'PARENTESISI',
          'PARENTESISD', 'COMA', 'PUNTOCOMA', 'PUNTO', 'ACTUALIZAR']

palabrasReservadas = ['INICIAR', 'FINALIZAR', 'SI', 'ENTONCES', 'SINO', 'MIENTRAS', 'HACER', 'LLAMAR', 'CONSTANTE', 'VARIABLE', 'ENTERO', 'PROCEDIMIENTO', 'FUERA', 'DENTRO']

tokens = tokens + palabrasReservadas

t_ignore = '\t'
t_SUMA = r'\+'
t_RESTA = r'\-'
t_MULTIPLICACION = r'\*'
t_DIVISION = r'/'
t_ASIGNACION = r'='
t_DIFERENTE = r'<>'
t_MENOR = r'<'
t_MENORI = r'<='
t_MAYOR = r'>'
t_MAYORI = r'>='
t_PARENTESISI = r'\('
t_PARENTESISD = r'\)'
t_COMA = r','
t_PUNTOCOMA = r';'
t_PUNTO = r'\.'
t_ACTUALIZAR = r':='

def t_IDENTIFICADOR(t):

    r'[a-zA-Z_][a-zA-Z0-9_]*'
    if t.value.upper() in palabrasReservadas:

        t.value = t.value.upper()
        t.type = t.value

    return t

def t_newline(t):

    r'\n+'
    t.lexer.lineno += len(t.value)

def t_ccode_nonspace(t):

    r'\s+'
    pass

def t_COMENTARIO(t):

    r'\$.*'
    pass

def t_NUMERO(t):

    r'\d+'
    t.value = int(t.value)
    return t

def t_error(t):

    print("¡CARACTER ILEGAL!: '%s'" % t.value[0])
    t.lexer.skip(1)


analizador = lex.lex()
