nota1 = float(input('Primeira nota:'))
nota2 = float(input('Segunda nota:'))

media = (nota1 + nota2) / 2

if 7 > media >= 5:
    print('O aluno está em RECUPERAÇÃO!')

elif media < 5:
    print('O aluno está REPROVADO!')

else:
    print('O aluno está APROVADO!')