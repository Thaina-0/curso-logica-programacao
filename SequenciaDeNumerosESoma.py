while True:
    Linha = input().split()
    N = int(Linha[0])
    M = int(Linha[1])

    if N <= 0 or M <= 0:
        break
    if N > M:
        aux = M
        M = N
        N = aux

    Sum = 0
    Result_Sequencia = ""
    for i in range (N, M+1):
        Sum += i
        Result_Sequencia += str(i) + " "
    
    print(f"{Result_Sequencia}Sum={Sum}")

    #O arquivo de entrada contém um número não 
    #determinado de valores M e N. A última linha 
    #de entrada vai conter um número nulo ou negativo.