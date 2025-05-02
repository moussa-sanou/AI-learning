import csv

with open('10_02_us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    for row in reader:
        print(row)

print('---------' * 10)

with open('10_02_us.csv', 'r') as f:
    reader = csv.reader(f, delimiter='\t')
    next(reader)
    for row in reader:
        print(row)

print('---------' * 10)

with open('10_02_us.csv', 'r') as f:
    reader = list(csv.reader(f, delimiter='\t'))
    for row in reader[1:]:
        print(row)
print('---------' * 10)

# Filtering data
with open('10_02_us.csv', 'r') as f:
    data = csv.reader(f, delimiter='\t')

primes = []
for number in range(2, 99999):
    for factor in range(2, int(number**0.5)):
        if number % factor == 0:
            break
    else:
        primes.append(number)

# Writing
with open('10_02_ma_prime.csv', 'w') as f:
    writer = csv.writer(f)
    for row in data:
        writer.writerow([row['place name'], row['county']])