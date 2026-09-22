totC = 0
totR = 0
totS = 0
totCB = 0

N = int(input())

for i in range(N):
    Linha = input().split()
    num = int(Linha[0])
    letra = Linha[1]

    totCB += num

    if letra == 'C':
        totC += num
    elif letra == 'R':
        totR += num
    elif letra == 'S':
        totS += num

PC = (totC / totCB) * 100
PR = (totR / totCB) * 100
PS = (totS / totCB) * 100

print(f"Total: {totCB} cobaias")
print(f"Total de coelhos: {totC}")
print(f"Total de ratos: {totR}")
print(f"Total de sapos: {totS}")
print(f"Percentual de coelhos: {PC:.2f} %")
print(f"Percentual de ratos: {PR:.2f} %")
print(f"Percentual de sapos: {PS:.2f} %")


#A primeira linha de entrada contém um valor inteiro N que indica os vários casos//
#de teste que vem a seguir. Cada caso de teste contém um inteiro Quantia (1 ≤ Quantia ≤ 15) 
#que representa a quantidade de cobaias utilizadas e um caractere Tipo ('C', 'R' ou 'S'),
#indicando o tipo de cobaia (R:Rato S:Sapo C:Coelho).