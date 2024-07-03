# Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

# Solicita ao usuário que insira dois números
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

# Solicita ao usuário que escolha a operação
print("Escolha a operação:")
print("1. Adição")
print("2. Subtração")
print("3. Multiplicação")
print("4. Divisão")
operacao = input("Digite o número da operação desejada (1/2/3/4): ")

# Realiza a operação escolhida
if operacao == "1":
    resultado = num1 + num2
    operacao_str = "adição"
elif operacao == "2":
    resultado = num1 - num2
    operacao_str = "subtração"
elif operacao == "3":
    resultado = num1 * num2
    operacao_str = "multiplicação"
elif operacao == "4":
    if num2 != 0:
        resultado = num1 / num2
        operacao_str = "divisão"
    else:
        resultado = "indefinido (não é possível dividir por zero)"
else:
    resultado = "Operação inválida"
    operacao_str = "nenhuma"

# Exibe o resultado da operação
if operacao in ["1", "2", "3", "4"] and not (operacao == "4" and num2 == 0):
    print(f"O resultado da {operacao_str} entre {num1} e {num2} é: {resultado}")
else:
    print(resultado)
