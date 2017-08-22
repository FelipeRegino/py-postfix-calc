import sys
import re

def main():
    x = 0
    entrada = []
    while x!="=":
        x = input("Digite um numero ou um operador(+|-|*|/). Digite '=' para fazer o calculo: ")
        if x!="=":
            entrada.append(x)
    verify(entrada)
    getResult(entrada)

def verify(entrada):
    firstTest(entrada)
    secondTest(entrada)

def firstTest(entrada):
    entrada = ''.join(entrada)
    entrada += '='
    pattern = re.compile("^[0-9]{2}[0-9+\-*\/]*=$")
    m = pattern.match(entrada)
    if m == None:
        print ("Cadeia Inválida: insira caracteres válidos [números e +-*/")
        sys.exit(2)

def secondTest(entrada):
    val = 0
    for i in entrada:
        if i in ['+','-','/','*']:
            val -= 1
        elif int(i) in range(9):
            val += 1
    if val != 1:
        print("Cadeia Inválida: Número de números e simbolos está errado")
        sys.exit(3)

def getResult(entrada):
    numbers = []

    for item in entrada:
        if item == "*" or item == "+" or item == "-" or item == "/":
            if len(numbers) < 2:
                print("Cadeia Inválida: Posições inadequadas dos caracteres")
                sys.exit(4)
            numbers[-2] = calc(item, numbers[-2], numbers[-1])
            numbers.remove(numbers[-1])
        else:
            numbers.append(int(item))
    print(numbers[-1])

def calc(operator, n1, n2):
    if operator == "*":
        return n1*n2
    elif operator == "+":
        return n1+n2
    elif operator == "-":
        return n1-n2
    elif operator == "/":
        if n2 == 0:
            print ("Cadeia Inválida: Não é possível dividir por 0")
            sys.exit(1)
        return n1/n2

main()
