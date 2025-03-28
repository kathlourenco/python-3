lado1 = float(input("Digite o valor do lado do triangulo: "))
lado2 = float(input("Digite o valor do segundo lado do triangulo: "))
lado3 = float(input("Digite o valor do terceiro lado do triangulo: "))

if lado1 == lado2 == lado3:
    print("É um triangulo equilátero! ")
if lado1 > lado2 == lado3:
    print("É um triangulo isósceles! ")
if lado1 > lado2 > lado3 or lado2 > lado3 > lado1 or lado3> lado1 > lado2:
    print("É um triangulo escaleno! ")