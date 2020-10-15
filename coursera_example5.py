start, end = 524, 10508
sum = 0

for num in range(start, end+1):
    if num % 2 == 0:
        sum = sum + num

print(sum)
