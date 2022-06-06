# Exercício Python 011: Faça um programa que leia a largura e a altura de uma parede em metros,
# calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro
# de tinta pinta uma área de 2 metros quadrados.

l = float(input('Largura da parede: '))
a = float(input('Altura da parede: '))
m2 = (l * a)
rendimento = 2
t = (m2 / rendimento)
print('Sua parede tem a dimensão de {:.2f} x {:.2f} e sua área e de {:.0f}m².'.format(l, a, m2))
print('Para pintar essa parede, você precisará de {:.2f}l. de tinta.'.format(t))
