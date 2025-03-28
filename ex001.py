nota1 = float(input("Digite a nota da prova um: "))
nota2 = float(input("Digite a nota da prova dois: "))
nota3 = float(input("Digite a nota da propva três: "))

media1 = (nota1 + nota2 + nota3) / 3
print(media1)

if media1 >= 6:
        print("Parabéns, você foi arovado")
else:
    print("Reprovado")