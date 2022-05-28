# Exercício Python 013: Faça um algoritmo que leia o salário de um funcionário e mostre seu
# novo salário, com 15% de aumento.

v = float(input('Qual é o salário do funcionário? R$'))
a = (v+(v * 0.15))
print('Um funcionário que ganhava R${:.2F}, com 15% de aumento, passa a receber R${:.2F}'.format(v, a))
