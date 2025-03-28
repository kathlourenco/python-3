media = float(input("informe sua media: "))
faltas = int(input("Quantidade de faltas: "))

if media >= 6:
    if faltas <= 20:
        print("Aprovado")
    else:
        print("Reprovado por faltas")
else:
    print("Reprovado or média")
