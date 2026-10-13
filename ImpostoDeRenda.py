salario = float(input())

imposto = 0.0

if salario <= 2000.00:
    print("Isento")
else:
    if salario > 4500.00:
        # Calcula 28% sobre o que passa de 4500
        imposto += (salario - 4500.00) * 0.28
        # Adiciona o máximo das faixas anteriores
        imposto += (1500.00 * 0.18) + (1000.00 * 0.08)
        
    elif salario > 3000.00:
        # Calcula 18% sobre o que passa de 3000
        imposto += (salario - 3000.00) * 0.18
        # Adiciona o máximo da faixa de 8%
        imposto += (1000.00 * 0.08)
        
    elif salario > 2000.00:
        # Calcula 8% sobre o que passa de 2000
        imposto += (salario - 2000.00) * 0.08

    print(f"R$ {imposto:.2f}")


#A entrada contém apenas um valor de ponto flutuante, com duas casas decimais.