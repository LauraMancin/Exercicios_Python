num = int(input('Digite um valor: '))

maior = num
soma = num
cont = 1
opc = str(input('Gostaria de continuar (s/n)? '))

while opc in 'sS':
    num = int(input('Digite um valor: '))
    soma += num
    cont += 1

    if num > maior:
        maior = num
        
    opc = str(input('Gostaria de continuar (s/n)? '))

print(f'Média dos valores digitados: {soma/cont}')
print(f'Maior valor digitado: {maior}')