peso = float(input( ' Digite seu peso: ' ))

altura = float(input( ' Digite sua altura: ' ))

IMC = peso / altura ** 2

print (f'Seu IMC é igual a: {IMC:.1f}')

if IMC <= 18.5:
    print('Você está abaixo do peso!')

elif IMC <= 25:
    print('Você está no seu peso ideal!')

elif IMC <= 30:
    print ('Você está com sobrepeso!')

elif IMC <= 40:
    print ('Você está obeso!')

else:
    print ('Você está com obesidade mórbida!')