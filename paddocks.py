

def mean(list):
    data = list
    num = [int(x) for x in data.split()]
    n = sum(num) / len(num)
    return n

unh = 0
numof = 0
resow = 0

for _ in range(3):
    s = input()
    means = mean(list(map(int, input().split())))
    if means >= 12:
        numof += 1
        unh += 1
    elif means >= 25 and numof == 3:
        resow += 1
    else:
        health = 1

if unh == 3:
    print("unhealthy")
elif resow == 1:
    print("resow")
elif health == 1:
    print("healthy")

