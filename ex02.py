media = float(input("informe sua media: "))
faltas = int(input("Quantidade de faltas: "))

if media >= 6 and faltas <= 20:
    print("Aluno aprovado")
elif media >= 6 and faltas > 20:
    print("Reprovado por falta")
else:
    print("Reprovado por média")

