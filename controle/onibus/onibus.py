capacidade = int(input())
passageiros = 0

while passageiros < capacidade * 2:
    movimentacao = int(input())
    
    passageiros += movimentacao
    
    if passageiros == 0:
        print("vazio")
    elif passageiros < capacidade:
        print("ainda cabe")
    elif passageiros >= capacidade * 2:
        print("hora de partir")
    else:
        print("lotado")