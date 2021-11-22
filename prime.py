n=int(input("Enter the number till you want to check: "))
primes = []
for i in range (2, n+1):
    for j in range(2, i):
        if i%j == 0:
            break
    else:
        primes.append(i)
print(n, "->", primes)