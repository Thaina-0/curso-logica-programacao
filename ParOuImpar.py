N = int(input())

for i in range(N):
    Num = int(input())
    if Num > 0 and Num % 2 == 0:
        print(f"EVEN POSITIVE")
    elif Num > 0 and Num % 2 != 0:
        print(f"ODD POSITIVE")
    elif Num < 0 and Num % 2 == 0:
        print(f"EVEN NEGATIVE")
    elif Num < 0 and Num % 2 != 0:
        print(f"ODD NEGATIVE")
    elif Num == 0:
        print(f"NULL")

#A primeira linha da entrada contém um valor inteiro N(N < 10000)
#que indica o número de casos de teste. Cada caso de teste a seguir
#é um valor inteiro X (-107 < X <107).