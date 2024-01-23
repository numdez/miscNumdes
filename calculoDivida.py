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


meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

salarioBruto = 811.4
chequeEspecial = 300

taxaCancelada = 0
taxaBanco = 50
contaSky = 130
contaCondo = 300
contaSky2 = 0
contaCondo2 = 0

motherboard = 350 + 24
moboCartao = 411 + 24
gabinete = 210
cpu = 576
fonte600w = 280 + 31
f600wCartao = 329.5 + 31
fonte650w = 288 + 34
f650wCartao = 339 + 34
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

surplus = 0
maxCartao = 1100
livreCartao = 0
faturaAtual = 458.90
usoCheque = 178.58
aParcela = 58.06
aFaltam = 2
bParcela = 191.90
bFaltam = 3
cParcela = 22.15
cFaltam = 10

duasContas = contaCondo + contaSky
duasContasEx = f"({contaCondo} + {contaSky})"
zeroContas = contaCondo2 + contaSky2
zeroContasEx = f"{contaCondo2} + {contaSky2}"

pcDict = {
    "Pente de 16GB": totalRam16,
    "fonte 650W": fonte650w,
    "Placa mãe": motherboard
}
pcCartao = {
    "Pente de 16GB": totalRam16,
    "fonte 650W": f650wCartao,
    "Placa mãe": moboCartao
}


avulso = 0
entrada = 's'
contLacos = 0
cont = 1



entrada = input(f"Quanto entrou em {meses[cont]}? ")
try:
    avulso = float(entrada)
except:
    pass

while(entrada != 'n'):
    # CONSERTAR O CALCULO DE SALDO DISPONIVEL NO CARTÃO, DEVE SER ADICIONADO À FATURA ATUAL E RETIRADO DO LIVRECARTAO
    compravel = []
    comprar = 0
    virgula = ''
    contLacos = 0
    comprando = ''
    cartaoOuPix = []

    pagar = round_up(faturaAtual + usoCheque + duasContas)
    pagarEx = f'{faturaAtual} + {usoCheque} + {duasContasEx}'
    usoCheque = 0
    montante = salarioBruto + avulso
    avulso = 0
    resto = round_up(montante - pagar)
    livreCartao += faturaAtual
    if resto < 0 and resto >= -300:
        usoCheque = round_up(abs(resto))
        resto = 0
    elif resto < -300:
        resto += 300
        usoCheque = 300
    else:
        avulso = resto

    for i in list(pcDict):
        if contLacos > 0 and contLacos < len(list(pcDict)) and compravel:
            virgula = ', '
        if pcDict[i] <= avulso:
            compravel.append(f'{virgula}{i} por {pcDict[i]}')
            avulso -= pcDict[i]
            cartaoOuPix.append('no pix')
            del pcDict[i]
            del pcCartao[i]
        contLacos += 1

    for i in list(pcCartao):
        if contLacos > 0 and contLacos < len(list(pcCartao)) and compravel:
            virgula = ', '
        if pcCartao[i] <= livreCartao:
            compravel.append(f'{virgula}{i} por {pcCartao[i]}')
            livreCartao -= pcCartao[i]
            cartaoOuPix.append('no cartão')
            del pcCartao[i]
            del pcDict[i]    
        contLacos += 1

    if not pcDict or not pcCartao:
        compravel = 'Tudo foi comprado'
        comprar = 0

    if compravel and compravel != 'Tudo foi comprado':
        print(compravel, cartaoOuPix)
        for i in range(len(compravel)):
            comprando += f'{compravel[i]} {cartaoOuPix[i]}'

    livreCartao = round_up(livreCartao)
    printar = f'''Tanto que deve pagar: {pagar}
Tanto que tem para pagar: {montante}
Tanto que sobrou: {resto}
Tanto que usou do cheque especial: {usoCheque}
Tanto que tem livre no cartão: {livreCartao}
Pode comprar: {comprando}
Falta comprar: {list(pcDict)}

'''
    print(printar)
    aParcela = 58.06
    aFaltam -= 1
    bParcela = 191.90
    bFaltam -= 1
    cParcela = 22.15
    cFaltam -= 1
    faturaAtual = round_up(proximaFatura(aParcela, aFaltam, bParcela, bFaltam, cParcela, cFaltam, comprar))
    cont += 1
    if cont == 12:
        cont = 0
    entrada = input(f"Quanto entrou em {meses[cont]}? ")
    try:
        avulso += float(entrada)
    except:
        pass
    
    
