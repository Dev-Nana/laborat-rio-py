a = int(input())
b = int(input())

soma = 0

if a > b:
    print("invalido")
else:
    while a <= b:
        if (a % 3 == 0) and (a % 2 == 0):
            soma = soma + a
        a = a + 1
    print(soma)
