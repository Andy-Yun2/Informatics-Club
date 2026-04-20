shoes = list(input().strip())
r = 0

for shoe in shoes:
    if shoe.capitalize() == 'R':
        r += 1

if r == 0:
    print("Maybe Dorothy is in Kansas.")
elif r == 1:
    print("Hop along Dorothy and find that other shoe.")
else:
    print("Dorothy is in the classroom.")
