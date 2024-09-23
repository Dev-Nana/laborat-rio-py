n = int(input())

raiz = 0

while raiz * raiz < n:
    raiz += 1
    if (raiz * raiz) == n:
        print("sim")
if (raiz * raiz) != n or n == 0:
    print("nao")