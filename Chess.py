N = int(input())
for i in range(N):
    x, y = list(map(int, input().split(' ')))
    if (x + y) % 2 == 0:
        print("BLACK")
    else:
        print("WHITE")