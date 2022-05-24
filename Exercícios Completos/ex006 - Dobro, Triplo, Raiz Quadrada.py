# Exercício Python 006: Crie um algoritmo que leia um número e mostre o seu dobro, triplo e raiz quadrada.

n = int(input('Digite um número: '))

print('O drobro de {} vale {}.'.format(n,(n * 2)))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, (n * 3), n, pow(n, (1/2))))

"""d = (n * 2)
t = (n * 3)
rq = (n ** (1/2))
print('O drobro de {} vale {}.'.format(n,(n * 2)))
print('O triplo de {} vale {}.\nA raiz quadrada de {} é igual a {:.2f}.'.format(n, t, n, rq))"""
