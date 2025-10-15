from datetime import date
atual = date.today().year

nascimento = int(input('Ano de nascimento: '))
idade = atual - nascimento

if idade == 18:
    print('Você JÁ PODE se alistar!')

elif idade < 18:
    saldo = 18 - idade
    print(f'Ainda faltam {saldo} ano(s) para o alistamento!')

else:
    saldo = idade - 18
    print(f'Você já deveria estar alistado há {saldo} ano(s)!')
    ano = atual - saldo
    print(f'Seu alistamento foi em {ano}')