l = int(input())

letra = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

if 1 <= l <= 26:
    print(letra[l - 1])
elif l > 26:
    n = (l - 1) % 26  
    print(letra[n])
else:
    print("joguem de novo")
