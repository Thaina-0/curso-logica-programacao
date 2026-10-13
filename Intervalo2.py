N = int(input())
contf = 0
contd = 0

for i in range(N):
    num = int(input())
    if num >= 10 and num <= 20:
        contd += 1
    elif num < 10 or num > 20:
        contf += 1

print(f"{contd} in\n{contf} out")


#A primeira linha da entrada contém um valor inteiro N (N < 10000),
#que indica o número de casos de teste.
#Cada caso de teste a seguir é um valor inteiro X (-107 < X <107).