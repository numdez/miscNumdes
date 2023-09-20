
cpf = input("Insira o cpf: ")
cpf = [int(x) for x in str(cpf)]
if len(cpf) < 11:
    print('CPF INVÁLIDO - NÃO POSSUI 11 DÍGITOS')
else:  
    ordem1 = [10, 9, 8, 7, 6, 5, 4, 3, 2]
    ordem2 = [11, 10, 9, 8, 7, 6, 5, 4, 3, 2]
    digito1 = 0
    digito2 = 0

    for i in range(9):
        digito1 += float(cpf[i] * ordem1[i]) 
    
    digito1 = float(digito1 * 10 % 11)
    
    if digito1 == 10:  #gambiarra pra resto com mais de 1 dígito
        digito1 = 0

    for i in range(10):
        digito2 += cpf[i] * ordem2[i]

    digito2 = digito2 * 10 % 11
    
    if digito2 == 10:  #gambiarra pra resto com mais de 1 dígito
        digito2 = 0

    print(digito1, digito2)
    print(cpf[-2], cpf[-1])

    if digito1 == cpf[-2] and digito2 == cpf[-1]:
        print('CPF VÁLIDO')
    else:
        print('CPF INVÁLIDO - DÍGITOS INCORRETOS')

