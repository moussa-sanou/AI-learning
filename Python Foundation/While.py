from datetime import datetime
# While loop
''' With the while loop we can execute a set of statements as long as a condition is true '''

CurrentTime = datetime.now().second + 2
print(CurrentTime)

wait_until = (datetime.now().second + 2) % 60

while datetime.now().second != wait_until:
    pass
print(f'We are at {wait_until} seconds!')

wait_until = (datetime.now().second + 2) % 60
while True:
    if datetime.now().second == wait_until:
        print(f'We are at {wait_until} seconds!')
        break

while True:
    if datetime.now().second == wait_until:
        continue
    break
print(f'We are at {wait_until} seconds!')

