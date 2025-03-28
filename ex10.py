salario = float(input("Digite o salário fixo: "))
vendas = float(input("Digite o valor total das vendas: "))
comissao1 = (vendas * 3) / 100
comissao2 = 45 + ((vendas - 1500) * 5) / 100
if vendas <= 1500:
    print(f"O salário será {salario + comissao1}")
elif vendas > 1500:
    print(f"O salário será {salario + comissao2 }")