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

def firstTest(entrada):
    entrada = ''.join(entrada)
    entrada += '='
    pattern = re.compile("^[0-9]{2}[0-9+\-*\/]*=$")
    m = pattern.match(entrada)
    if m != None:
        print("pegou")
    else:
        print("nao pegou")
    sys.exit()

def getResult(entrada):
    numbers = []

    for item in entrada:
        if item == "*" or item == "+" or item == "-" or item == "/":
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
