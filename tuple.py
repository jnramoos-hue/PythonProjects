# Tuple são imutáveis



halogenios = ('F', 'Cl', 'Br', 'I', 'At')
gases_nobres = ('He', 'Ne', 'Ar', 'Xe', 'Kr', 'Rn')
elementos = halogenios + gases_nobres
t1 = (5,2,6,8,4,5,6,4,4,0,12,22,3,4,5)
print(halogenios[-2])
print(elementos)
print(t1.count(5))
print(halogenios[0:2])
print('Cl' in halogenios)
print('Fe' in halogenios)
print(sum(t1))
print(max(t1))
print(min(t1))

#Operações não disponiveis em tuplas: .sort(), .reverse(), .pop()....
# for elemento in elementos:
#     print(f'Elementos químicos: {elemento}')
#
# grupo17 = list(halogenios)
# grupo17[0] = 'H'
# print(grupo17)

grupo1 = ['Li', 'Na', 'K', 'Rb', 'Cs']
alcalinos = tuple(grupo1)
print(type(alcalinos))

print(sorted(alcalinos))
# print(alcalinos.sort())







