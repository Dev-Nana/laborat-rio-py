import math

capacidade = int(input())   
alunos = int(input())   

num_viagens = math.ceil(alunos / (capacidade - 1))

print(num_viagens)