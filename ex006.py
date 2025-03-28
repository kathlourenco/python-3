horas = int(input('Digite as horas: '))
minutos = int(input('Digite os minutos: '))


if horas >= 0 and horas <= 23 and minutos >=0 and minutos <= 59:
    print('horas e minutos validos')
else:
    print("Horas e minutos inválidos")
