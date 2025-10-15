lista=[]  
for c in range(1, 6):
    
    peso=float(input('Peso da {}ª pessoa: '.format(c)))
    lista+=[peso]   

print('')
print('O Maior peso foi:', max(lista))  
print('O Menor peso foi:', min(lista))  