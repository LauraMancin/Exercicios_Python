print (50 * '-')

#Menu de opções.
escolha = float(input('''TABUADA DIGITAL!
	
Digite [ 1 ] para Multiplicação.
Digite [ 2 ] para Divisão.
Digite [ 3 ] para Subtração.
Digite [ 4 ] para Adição.

Digite o número que representa a sua escolha: '''))

print (50 * '-')


numero = float(input('Agora digite o número que você quer aplicar: '))


if escolha == 1:
    print (50 * '-')
    for laço in range (0, 11):
        print (f'{laço:2} X {numero:2} = {laço * numero:2}')


elif escolha == 2:
    print (50 * '-')
    for laço in range (1, 11):
        print (f'{numero:2} ÷ {laço:2} = {numero / laço:.2f}')


elif escolha == 3:
    print (50 * '-')
    for laço in range (0, 11):
        print (f'{numero:2} - {laço:2} = {numero - laço:2}')


elif escolha == 4:
    print (50 * '-')
    for laço in range (0, 11):
        print (f'{laço:2} + {numero:2} = {laço + numero:2}')


else:
    print ('ERRO! TENTE NOVAMENTE.')