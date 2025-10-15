while True:
    sexo = str(input("Qual o seu sexo(Digite M ou F): ")).upper().strip()[0]
    
    if sexo not in "MF":
        print("Opção invalida. Digite M ou F")

    else:
        print("Muito obrigado")
        break