a, b, c = int(input()), int(input()), int(input())
if a + b > c or b + c > a or a + c > b:
    print('Триугольник существует')
else:
    print('Триугольник не существует')