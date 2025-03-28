num1 = int(input("Digite um número maior que zero e menor que mil: "))
centena = (num1 // 100)
dezena = (num1 // 10) % 10
unidade = (num1 % 10)
soma = centena + dezena + unidade
print(soma)
 