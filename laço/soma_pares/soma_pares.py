a = int(input())
b = int(input())

if a > b:
    print("invalido")
else:
    soma = 0
    while a <= b:
        if a % 2 == 0:
            soma = soma + a
        a = a + 1
    print(soma)