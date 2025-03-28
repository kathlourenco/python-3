a = float(input("Digite um número: "))
b = float(input("Digite outro número: "))

print("1 - soma")
print("2 - subtração")
print("3 - multiplicação")
print("4 - divisão")
opcao = int(input("Escolha uma das opções acima: "))

if opcao == 1:
    print(f"O resultado da soma é: {a + b}")
elif opcao == 2:
    print(f"Resultado da subtração é {a - b}")
elif opcao == 3:
    print(f"O resultado da multiplicação é {a * b}")
elif opcao == 4:
    if b != 0:
        print(f"O resultado da divisão é {a / b}")
    else:
        print("Não é possível fazer uma divisão por zero")
else:
    print("Opção inválida")

