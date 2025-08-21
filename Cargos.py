cargo = input('Insira o seu Cargo: ').capitalize().strip()
dia = input('Insira o dia que deseja vizualizar: ').capitalize().strip()

if cargo == 'Gerente':
    if dia == 'Segunda' or dia == 'Terça' or dia == 'Quarta' or dia == 'Quinta' or dia == 'Sexta' or dia == 'Sábado':
        print('Acesso Válido')
    else:
        print('Acesso Inválido')
elif cargo == 'Analista':
    if dia == 'Segunda' or dia == 'Terça' or dia == 'Quarta' or dia == 'Quinta' or dia == 'Sexta':
        print('Acesso Válido')
    else:
        print('Acesso Inválido')
elif cargo == 'Estagiário':
    if dia == 'Segunda' or dia == 'Quarta' or dia == 'Sexta':
        print('Acesso Válido')
    else:
        print('Acesso Inválido')
else:
    print('Cargo Negado')
