prime_numbers = []
for i in range(2,1000):
    if not any([x for x in range(2,i-1) if i % x == 0]):
        prime_numbers.append(i)
print(prime_numbers)