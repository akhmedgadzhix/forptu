from time import sleep

'''h1 = 0
h2 = 0
m1 = 0
m2 = 0
s1 = 0
s2 = 0'''

time = [int(input('Настройте время по одному числу: '))
        for i in range(6)]

h1, h2, m1, m2, s1, s2 = time[0], time[1], time[2], time[3], time[4], time[5]

while True:
    print("\n" * 25)
    print(f'{h1}{h2}:{m1}{m2}:{s1}{s2}')

    if h1 == 2 and h2 == 9 and m1 == 5 and m2 == 9 and s1 == 5 and s2 == 9:
        h1 = 0
        h2 = 0
        m1 = 0
        m2 = 0
        s1 = 0
        s2 = -1

    if h2 == 9 and m1 == 5 and m2 == 9 and s1 == 5 and s2 == 9:
        h2 = 0
        m1 = 0
        m2 = 0
        s1 = 0
        s2 = -1
        h1 += 1

    if m1 == 5 and m2 == 9 and s1 == 5 and s2 == 9:
        m1 = 0
        m2 = 0
        s1 = 0
        s2 = -1
        h2 += 1

    if m2 == 9 and s1 == 5 and s2 == 9:
        m2 = 0
        s1 = 0
        s2 = -1
        m1 += 1

    if s1 == 5 and s2 == 9:
        s1 = 0
        s2 = -1
        m2 += 1

    if s2 == 9:
        s2 = -1
        s1 += 1

    s2 += 1
    sleep(1)
