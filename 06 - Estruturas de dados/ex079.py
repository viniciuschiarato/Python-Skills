# Exercício Python 079: Crie um programa onde o usuário possa digitar vários valores numéricos e
# cadastre-os em uma lista. Caso o número já exista lá dentro, ele não será adicionado.
# No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""lista = list()
continuar = entrada = 0
while True:
    entrada = (int(input('Digite um valor: ')))
    if entrada not in lista:
        lista.append(entrada)
        print('Valor adicionado com sucesso!')
    else:
        print('Valor digitado já consta na lista')
    continuar = str(input('Quer continuar? [S/N]:')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Resposta inválida. Quer continuar? [S/N]:')).strip().upper()[0]
    if continuar == 'N':
        break
print(sorted(lista))"""

números = list()
while True:
    n = int(input('Digite um número: '))
    if n not in números:
        números.append(n)
        print('Valor adicionado com sucesso...')
    else:
        print('Valor duplicado! Não vou adicionar...')
    r = str(input('Quer continuar? [S/N]: '))
    if r in 'Nn':
        break
números.sort()
print(f'Você digitou os valores {números}')




