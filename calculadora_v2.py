saida = ''
def adicao(a,b):
    return a + b
def subtracao(a,b):
    return a - b
def multiplicacao(a,b):
    return a * b
def divisao(a,b):
    if(a == 0 or b == 0):
        print("Nao foi possivel realizar a divisao por 0.")
    else:
        return a / b
def calculadora(c,d,operacao):
    if(operacao == "adicao" or operacao == "+"):
        resultado = adicao(c,d)
        return resultado
    elif(operacao == "subtracao" or operacao == "-"):
        resultado = subtracao(c,d)
        return resultado
    elif(operacao == "multiplicacao" or operacao == "*"):
        resultado = multiplicacao(c,d)
        return resultado
    elif(operacao == "divisao" or operacao == "/"):
        resultado = divisao(c,d)
        return resultado
while (saida != "n"):
    x = eval(input("Digite o primeiro numero: "))
    y = eval(input("Digite o segundo numero: "))
    operacao = input("Qual operacao você deseja realizar: ")
    resultado = calculadora(x,y,operacao)
    print("Resultado da operação: " + str(resultado))
    saida = input("Caso deseje fazer outra operação, digite S, se não, digite N. ")
    saida = saida.lower()