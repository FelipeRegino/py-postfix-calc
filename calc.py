def main():
    x = 0
    entrada = []
    while x!="=":
        x = input("Digite um numero ou um operador(+|-|*|/). Digite '=' para fazer o calculo: ")
        if x!="=":
            entrada.append(x)
    getResult(entrada)

def getResult(entrada):
    numbers = []

    for item in entrada:
        if item == "*" or item == "+" or item == "-" or item == "/":
            numbers[-2] = calc(item, numbers[-1], numbers[-2])
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
        return n1/n2

main()
