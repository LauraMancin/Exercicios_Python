soma = 0
quantidade = 0

for c in range(1, 7):

  número = int(input(f'Digite o valor {c}: '))

  if número % 2 == 0:

    soma += número
    quantidade += 1
    
print(f'Você informou {quantidade} números pares e a soma deles é {soma}.')