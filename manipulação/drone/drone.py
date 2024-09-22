a = int(input())
b = int(input())
c = int(input())
h = int(input())
l = int(input())

if ((a <= h and b <= l) or (a <= h and b <= l)):
    print("S")
elif ((a <= h and c <= l) or (a <= h and c <= l)):
    print("S")
elif ((c <= h and b <= l) or (c <= h and b <= l)):
    print("S")
else:
    print("N")
