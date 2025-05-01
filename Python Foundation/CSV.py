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

with open('10_02_us.csv', 'r') as f:
    reader = list[csv.reader(f, delimiter='\t')]
    for row in reader[1:]:
        print(row)