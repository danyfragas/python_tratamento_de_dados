# exercício 13: Escreva um programa que pergunte a quantidade de Km percorridos por um carro
# alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo
# que o carro custa R$60 por dia e R$0,15 por Km rodado.

k = float(input('Km percorridos: '))
d = int(input('Dias alugado: '))
total = (k*0.15) + (d*60)
print('O total a pagar é: R$ {}'. format(total))
