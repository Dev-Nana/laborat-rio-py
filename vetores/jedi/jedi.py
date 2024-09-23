numero = int(input())
indice = 0
todas = []

while indice < numero:
    lutas = int(input())
    todas.append(lutas)
    indice += 1
    
metade = numero // 2
jedi = todas[:metade]
sith = todas[metade:]

if sum(jedi) == sum(sith):
    print("Empate")
elif sum(jedi) > sum(sith):
    print("Jedi")
else:
    print("Sith")
    
