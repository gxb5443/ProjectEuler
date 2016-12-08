#! python

current = 1
last = 0
sum = 0
while True:
    if current>4000000:
        break
    if current % 2 == 0:
        sum += current
    next=current + last
    last = current
    current = next

print(sum)
