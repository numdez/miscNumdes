# %%
# tudo
import math
import decimal
from os import system

def clear():
    system('cls')

def round_up(x, place=2):
    context = decimal.getcontext()
    # get the original setting so we can put it back when we're done
    original_rounding = context.rounding
    # change context to act like ceil()
    context.rounding = decimal.ROUND_CEILING

    rounded = round(decimal.Decimal(str(x)), place)
    context.rounding = original_rounding
    return float(rounded)

def proximaFatura(aParcela, aFaltam, bParcela, bFaltam, cParcela, cFaltam, extra):
    nextFatura = 0
    if aFaltam > 0:
        nextFatura += aParcela
    if bFaltam > 0:
        nextFatura += bParcela
    if cFaltam > 0:
        nextFatura += cParcela
    if extra > 0:
        nextFatura += extra
    return nextFatura

def pagaChequeComCheque(usoCheque, chequeEspecial):
    usoCheque = chequeEspecial - usoCheque
    return usoCheque

clear()

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

salarioBruto = 811.4
chequeEspecial = 300

tempoSalario = 12
salariosRecebidos = 5
tempoRestante = tempoSalario-salariosRecebidos

taxaCancelada = 0
taxaBanco = 50
contaSky = 130
contaCondo = 300

contaSky2 = 0
contaCondo2 = 0

surplus = 0

salarioReal = salarioBruto - taxaBanco
salarioCondo = salarioReal - contaCondo
salarioCerto = salarioReal - contaCondo - contaSky

motherboard = 350 + 24
gabinete = 210
cpu = 576
fonte600w = 280 + 31
fonte650w = 288 + 34
ram8 = 99.52
impostoRam8 = 20.38
totalRam8 = round_up(ram8 + impostoRam8)
ram16 = 143.13
impostoRam16 = 29.33
totalRam16 = round_up(ram16 + impostoRam16)
ram = round_up(ram8 + impostoRam8 + ram16 + impostoRam16)
gpu = 952.45

componentes = [motherboard, gabinete, cpu, fonte650w, totalRam8, totalRam16, gpu]
comprados = [gpu, cpu, gabinete]
faltaComprar = [componente for componente in componentes if componente not in comprados]

totalRestante = 0 
totalCompleto = motherboard + gabinete + cpu + fonte650w + totalRam8 + totalRam16 + gpu
for i in faltaComprar:
    totalRestante += i

#54 caracteres na maior linha

imposto1 = 0
imposto2 = 0

precoReal = totalCompleto
precoReal2 = totalRestante

guardar1 = precoReal / math.ceil(precoReal/salarioReal)
guardar2 = precoReal2 / math.ceil(precoReal2/salarioReal)

guardarCondo = precoReal2 / math.ceil(precoReal2/salarioCondo)
guardarCerto = precoReal2 / math.ceil(precoReal2/salarioCerto)

calculos = f'''
****************************************************** -- ******************************************************
Salário mensal bruto: {salarioBruto}                            -- Salário mensal bruto: {salarioBruto}                            -- Salário mensal bruto: {salarioBruto}
Salário total bruto: {salarioBruto * tempoSalario}                            -- Salário total bruto: {salarioBruto*tempoSalario}                            -- Salário total bruto: {salarioBruto*tempoSalario}
Taxa do banco: {taxaBanco}                                      -- Taxa do banco: {taxaBanco}                                      -- Taxa do banco: {taxaBanco}
Taxa do banco total: {taxaBanco * tempoSalario}                               -- Taxa do banco total: {taxaBanco*tempoSalario}                               -- Taxa do banco total: {taxaBanco*tempoSalario}
Salário mensal líquido: {salarioCerto}                          -- Salário mensal líquido: {salarioCondo}                          -- Salário mensal líquido: {salarioReal}
Salário total líquido: {math.ceil(salarioCerto * tempoSalario)}                            -- Salário total líquido: {math.ceil(salarioCondo*tempoSalario)}                            -- Salário total líquido: {salarioReal*tempoSalario}

Salário total bruto restante: {tempoRestante * salarioBruto}                   -- Salário total bruto restante: {tempoRestante*salarioBruto}                   -- Salário total bruto restante: {tempoRestante*salarioBruto}
Taxa do banco total restante: {tempoRestante * taxaBanco}                      -- Taxa total do banco restante: {tempoRestante*taxaBanco}                      -- Taxa total do banco restante: {tempoRestante*taxaBanco}
Salário total líquido restante: {math.ceil(tempoRestante * salarioCerto)}                   -- Salário total líquido restante: {math.ceil(tempoRestante*salarioCondo)}                   -- Salário total líquido restante: {tempoRestante*salarioReal}

Preço total: {math.ceil(precoReal2)}                                       -- Preço total: {math.ceil(totalRestante)}                                       -- Preço total: {math.ceil(totalRestante)}
Meses para comprar: {math.ceil(precoReal2/salarioCerto)}                                  -- Meses para comprar: {math.ceil(totalRestante/salarioCondo)}                                  -- Meses para comprar: {math.ceil(totalRestante/salarioReal)}
Quanto economizar por mês: {round_up(guardarCerto)}                       -- Quanto economizar por mês: {round_up(guardarCondo)}                       -- Quanto economizar por mês: {round_up(guardar2)}

Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardarCerto)}                -- Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardarCondo)}                -- Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar2)}
Quanto pode gastar por mês líquido: {round_up(salarioCerto - guardarCerto)}               -- Quanto pode gastar por mes líquido: {round_up(salarioCondo - guardarCondo)}                -- Quanto pode gastar por mes líquido: {round_up(salarioReal - guardar2)}

*************************Tudo************************* -- ***********************Condomínio********************* -- *************************Nada*************************

Janeiro = {contaCondo} + {contaSky}
Total janeiro = {contaCondo + contaSky}
Resto = {surplus}
'''
print(calculos)



pcDict = {
    "Pente de 16GB": totalRam16,
    "fonte 650W": fonte650w,
    "Placa mãe": motherboard
}

usoChequeProx = 0
val = input('Dinheiro extra recebido: ')
try:
    taxaCancelada = int(val)
except:
    pass

maxCartao = 1100
livreCartao = 31
faturaAtual = 427.91
usoCheque = 178.58
aParcela = 58.06
aFaltam = 1
bParcela = 191.90
bFaltam = 2
cParcela = 22.15
cFaltam = 9


contMes = 0
compravel = []
comprar = 0
comprando = ''

while(val != 'n'):

    
    entradas = surplus   
    contMes += 1
    if contMes == 12:
        contMes = 0

    if taxaCancelada > 0 and contMes > 1:
        taxaBanco = 0
        entradas += taxaCancelada
        taxaCancelada = 0
    elif taxaCancelada > 0:
        entradas += taxaCancelada
        taxaCancelada = 0
    if usoCheque < 0:
        usoCheque = abs(usoCheque)
    
    usoChequePassado = usoCheque

    duasContas = contaCondo + contaSky
    duasContasEx = f"{contaCondo} + {contaSky}"
    zeroContas = contaCondo2 + contaSky2
    zeroContasEx = f"{contaCondo2} + {contaSky2}"
    

    surplus = round_up(salarioBruto + entradas - (faturaAtual + duasContas + usoChequePassado + taxaBanco))
    livreCartao += faturaAtual

    if not list(pcDict):
        comprar = 0
        compravel.append('Tudo já foi comprado')

    cont = 0
    for k in list(pcDict):
        if cont > 0:
            virgula = ', '
        if cont == 0 or cont == 3:
            virgula = ''
        if pcDict[k] < surplus + livreCartao:
            compravel.append(f'{virgula}{k} por {pcDict[k]}')
            comprar += pcDict[k]
            print(compravel)
            del pcDict[k]
            print(pcDict)
        else:
            compravel.append("nada")
            comprar = 0
        cont += 1

    for i in range(len(compravel)):
        if compravel[i] == 'Tudo já foi comprado' or compravel == 'Tudo já foi comprado':
            comprando = 'Tudo já foi comprado'
        elif compravel[i] == 'nada' and i == 0:
            comprando = 'nada'
        elif compravel[i] == 'nada' and i != 0:
            break
        else:
            comprando +=  compravel[i]
            
    if surplus > 0 and comprar > 0:
        backCompra = comprar
        comprar -= surplus
        surplus = comprar - backCompra
        if surplus < 0:
            surplus = 0
        if comprar < 0:
            comprar = 0
        livreCartao -= comprar
    else:
        livreCartao -=  comprar

    if surplus < 0 and surplus > -300:
        resto = f'Cheque especial usado = {abs(surplus)}\nResto = 0'
    elif surplus < -300:
        resto = f'Cheque especial usado = 300\nFaltando = {round_up(abs(surplus)-300)}'
    else:
        resto = f'Resto = {surplus}'
        usoCheque = 0

    if not list(pcDict):
        printar = f'''
{meses[contMes]} = {salarioBruto} + {entradas} - {faturaAtual} - {duasContasEx} - {usoChequePassado} - {taxaBanco} 
Total {meses[contMes].lower()} = {round_up(salarioBruto + entradas - (faturaAtual + duasContas + taxaBanco + usoChequePassado))}
{resto}
Peças compráveis = {comprando}
Livre no cartão = {round_up(livreCartao)}
'''
    else:
        printar = f'''
{meses[contMes]} = {salarioBruto} + {entradas} - {faturaAtual} - {duasContasEx} - {usoChequePassado} - {taxaBanco}
Total {meses[contMes].lower()} = {round_up(salarioBruto + entradas - (faturaAtual + duasContas + taxaBanco + usoChequePassado))}
{resto}
Peças compráveis = {comprando}
Livre no cartão = {round_up(livreCartao)}
Peças faltando = {list(pcDict.items())}
    '''
    print(printar)
    salarioBruto = 811.4
    faturaAtual = round_up(proximaFatura(aParcela, aFaltam, bParcela, bFaltam, cParcela, cFaltam, comprar))
    
    compravel = []
    comprando = ''

    aParcela = 58.06
    aFaltam -= 1
    bParcela = 191.90
    bFaltam -= 1
    cParcela = 22.15
    cFaltam -= 1
    
    val = input('Dinheiro extra recebido: ')
    try:
        taxaCancelada = int(val)
    except:
        pass

# %%
