mass = [i for i in range(1_000_000)]

target = 999_999

for num in range(len(mass)):
    if target == mass[num]:
        print(num)

