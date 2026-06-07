# Trocar valores entre duas variáveis.

var1 = 62
var2 = 31
#
# var1, var2 = var2, var1
#
# print(f'var1 = {var1} e var2 = {var2}')

# Operador condicional ternário
# menor = var1 if var1 < var2 else var2
# print(f'Menor valor: {menor}')
# print(f'Menor valor: {(var2, var1)[var1 < var2]}')

# Generators

# valores = [1,3,5,7,9,11,13,15]
# quadrados = (item ** 2 for item in valores)
# print(quadrados)
# for valor in quadrados:
#     print(valor)

# Função enumerate()
# bebidas = ['café', 'chá', 'água', 'Suco', 'Refrigerante']
# for i, item in enumerate(bebidas):
#     print(f'índice: {i}, Item: {item}')

# temparatudas = [-1, 10, 5, -3, 8, 4, -2, -5, 7]
# total = 0
#
# for i, t, in enumerate(temparatudas):
#     if t < 0:
#         print(f'A temperatura em {i} é negativa, com {t}ºC.')

# Gerenciamento de contexto com with

try:
    a = open('frutas.txt', 'r', encoding='utf-8')
    print(a.read())
except IOError:
    print('Could not open the file.')
else:
    a.close()

with open('frutas.txt', 'r', encoding='utf-8') as a:
    for linha in a:
        print(linha, end='')



