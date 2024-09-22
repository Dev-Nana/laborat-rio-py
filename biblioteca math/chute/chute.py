valor = int(input())
chute1 = int(input())
chute2 = int(input())

intervalo1 = abs(valor - chute1)
intervalo2 = abs(valor - chute2)

if intervalo1 > intervalo2:
    print("segundo")
elif intervalo1 == intervalo2:
    print("empate")
else:
    print("primeiro")
