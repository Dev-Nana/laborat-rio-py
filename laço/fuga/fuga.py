H, P, F, D = map(int, input().split())

h = (H-F)/D
p = (P-F)/D

if h < 0:
  h += 16
if p < 0:
  p += 16

if h < p:
  print('S')
else:
  print('N')