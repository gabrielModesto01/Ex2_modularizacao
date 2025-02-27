from minhasoperacoes import operacoes
from minhasoperacoes import utils

op = input("Escolha qual operação (+, -, *, /) deseja realizar: ")
a = float(input("Digite o primeiro número: "))
b = float(input("Digite o segundo número: "))

if op == "+":
    resultado = operacoes.soma(a, b)
elif op == "-":
    resultado = operacoes.subtracao(a, b)
elif op == "*":
    resultado = operacoes.multiplicacao(a, b)
elif op == "/":
    resultado = operacoes.divisao(a, b)
else:
    resultado = print("Operação inválida")

break

utils.exibir_resultado(op, resultado)