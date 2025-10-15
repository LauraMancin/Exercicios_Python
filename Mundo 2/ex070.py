total = 0.0
menor = ' '
barato = 0.0
cont = 0

while True:
    nome = str(input('Nome do produto: '))
    preco = float(input('Preço do produto: R$ '))

    if preco > 1000:
        cont += 1

    if menor == ' ' or preco < barato:
        menor = nome
        barato = preco

    total += preco
    opc = ' '

    while opc not in 'SN':
        opc = str(input('Quer continuar (S/N): ')).strip().upper()[0]
        
    if opc == 'N':
        break

print('=' * 50)
print(f'Valor total da compra: R$ {total:.2f}')
print(f'Total de produtos por mais de R$ 1000,00: {cont}')
print(f'Nome do produto mais barato: {menor}, valor: R$ {barato:.2f}')
print('=' * 50)

