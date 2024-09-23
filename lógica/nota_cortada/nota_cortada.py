b = int(input())  
t = int(input())   
h = 70
c = 160

nota = c * h
area = (b+t) * h/2

if area == nota/2:
    print("0")
elif area > nota/2:
    print("1")
else:
    print("2")