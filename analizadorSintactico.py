import ply.yacc as yacc
import re

from lexer import tokens

precedencia = (

    ('right', 'IDENTIFICADOR', 'LLAMAR', 'INICIAR', 'SI', 'MIENTRAS'),
    ('right', 'PROCEDIMIENTO'),
    ('right', 'VARIABLE'),
    ('right', 'ASIGNACION'),
    ('right', 'ACTUALIZAR'),
    ('left', 'DIFERENTE'),
    ('left', 'MENOR', 'MENORI', 'MAYOR', 'MAYORI'),
    ('left', 'SUMA', 'RESTA'),
    ('left', 'MULTIPLICACION', 'DIVISION'),
    ('left', 'PARENTESISI', 'PARENTESISD')

)

def p_program(p):

    '''program : block'''
    print("program")
    #p[0] = program(p[1], "program")

def p_block(p):

    '''block : constDecl varDecl procDecl statement'''
    print("block")

def p_constDecl(p):

    '''constDecl : CONSTANTE constAssignmentList PUNTOCOMA'''
    #p[0] = constDecl(p[2])
    print("constDecl")

def p_constDeclEmpty(p):

    '''constDecl : empty'''
    #p[0] = null()
    print("null")

def p_constAssignmentListA(p):

    '''constAssignmentList : IDENTIFICADOR ASIGNACION NUMERO'''
    print("constAssignmentList A")

def p_constAssignmentListB(p):

    '''constAssignmentList : constAssignmentList COMA IDENTIFICADOR ASIGNACION NUMERO'''
    print("constAssignmentList B")

def p_varDecl(p):

    '''varDecl : VARIABLE IDENTIFICADOR PUNTOCOMA'''
    print("varDecl")

def p_varDeclEmpty(p):

    '''varDecl : empty'''
    print("null")


def p_identListA(p):

    '''identList : IDENTIFICADOR'''
    print("identList A")

def p_identListB(p):

    '''identList : identList COMA IDENTIFICADOR'''
    print("identList B")

def p_procDecl(p):

    '''procDecl : procDecl PROCEDIMIENTO IDENTIFICADOR PUNTOCOMA block PUNTOCOMA'''
    print("procDecl")

def p_procDeclEmpty(p):

    '''procDecl : empty'''
    print("null")

def p_statementA(p):

    '''statement : IDENTIFICADOR ACTUALIZAR expression'''
    print("statement A")

def p_statementB(p):

    '''statement : LLAMAR IDENTIFICADOR'''
    print("statement B")

def p_statementC(p):

    '''statement : INICIAR statementList FINALIZAR'''
    print("statement C")

def p_statementD(p):

    '''statement : SI condition ENTONCES statement'''
    print("statement D")

def p_statementE(p):

    '''statement : MIENTRAS condition HACER statement'''
    print("statement E")

def p_statementEmpty(p):

    '''statement : empty'''
    print("null")

def p_statementListA(p):

    '''statementList : statement'''
    print("statementList A")

def p_statementListB(p):

    '''statementList : statementList PUNTOCOMA statement'''
    print("statementList B")

def p_condition(p):

    '''condition : expression relation expression'''
    print("condition")

def p_relationA(p):

    '''relation : ASIGNACION'''
    print("relation A")

def p_relationB(p):

    '''relation : DIFERENTE'''
    print("relation B")

def p_relationC(p):

    '''relation : MENOR'''
    print("relation C")

def p_relationD(p):

    '''relation : MAYOR'''
    print("relation D")

def p_relationE(p):

    '''relation : MENORI'''
    print("relation E")

def p_relationF(p):

    '''relation : MAYORI'''
    print("relation F")

def p_expressionA(p):

    '''expression : term'''
    print("expression A")

def p_expressionB(p):

    '''expression : addingOperator term'''
    print("expression B")

def p_expressionC(p):

    '''expression : expression addingOperator term'''
    print("expression C")

def p_termA(p):

    '''term : factor'''
    print("term A")

def p_termB(p):

    '''term : term multiplyingOperator factor'''
    print("term B")

def p_addingOperatorA(p):

    '''addingOperator : SUMA'''
    print("addingOperator A")

def p_addingOperatorB(p):

    '''addingOperator : RESTA'''
    print("addingOperator B")

def p_multiplyingOperatorA(p):

    '''multiplyingOperator : MULTIPLICACION'''
    print("multiplyingOperator A")

def p_multiplyingOperatorB(p):

    '''multiplyingOperator : DIVISION'''
    print("multiplyingOperator B")

def p_factorA(p):

    '''factor : IDENTIFICADOR'''
    print("factor A")

def p_factorB(p):

    '''factor : NUMERO'''
    print("factor B")

def p_factorC(p):

    '''factor : PARENTESISI expression PARENTESISD'''
    print("factor C")

def p_empty(p):

    '''empty :'''
    pass

def p_error(p):

    print("¡ERROR DE SINTAXIS!", p)
    print("ERROR EN LA LÍNEA: " + str(p.lineno))

analizadorS = yacc.yacc()

cadena = "CONSTANTE t = 4;"

resultado = analizadorS.parse(cadena)

print(resultado)
