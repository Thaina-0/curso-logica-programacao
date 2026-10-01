N = int(input())

for i in range(N):
    linha = input().split()
    n1 = int(linha[0])
    n2 = int(linha[1])

    if n1 < 0 or n2 == 0:
        print(f"divisao impossivel")
    else: 
        divisao = n1/n2
        print(divisao)

 #A entrada contém um número inteiro N. 
 #Este N será a quantidade de pares de valores inteiros (X e Y) que serão lidos em seguida.