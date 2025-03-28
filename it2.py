num1 = int(input("Digite um número: "))
num2 = int(input("Digite outro número: "))
dif1 = num1 -num2
dif2 = num2 -num1

if num1 > num2:
    print(f"O maior número é {num1} e a diferença entre eles é {dif1}")
else:
    print(f"O maior número é {num2} e a diferença entre eles é {dif2}")