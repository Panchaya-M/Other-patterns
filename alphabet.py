rows = int(input("Enter number of rows: "))

for i in range(0, rows):
    for j in range(rows - 1, i, -1):
        print("A", end='')
    print("+", end='')
    for l in range(i):
        if l==i-1: 
          print('E'*(2*l+1), end='')
          print('+', end='')
    for k in range(i + 1, rows):
        print("B", end='')
    print('\r')

for i in range(1,rows):
  for j in range(i):
    print('C', end='')
  print('+', end='')
  for l in range(rows-1,i,-1):
    print('E', end='')
    # if l==0: print("+", end='')
  for l in range(i+1,rows):
    if l != rows-1:
        print('E', end='')
    if l == rows-1: 
        print('+', end='')
  for k in range(i):
    print('D', end='')
  print('\r')