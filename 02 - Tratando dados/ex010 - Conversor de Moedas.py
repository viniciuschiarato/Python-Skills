# Exercício Python 010: Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e
# mostre quantos dólares ela pode comprar.

f = float(input('Quanto dinheiro você tem na carteira? R$'))
d = 3.27
c = (f/d)
print('Com R${:.2f} você pode comprar US${:.2f}'.format(f, c))
