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

def proximaFatura(aParcela, aFaltam, bParcela, bFaltam, cParcela, cFaltam, extra, extra2, extra3, extra4, acadMes):
    nextFatura = 0
    if aFaltam > 0:
        nextFatura += aParcela
    if bFaltam > 0:
        nextFatura += bParcela
    if cFaltam > 0:
        nextFatura += cParcela
    if extra > 0:
        nextFatura += extra
    if extra2 > 0:
        nextFatura += extra2
    if extra3 > 0:
        nextFatura += extra3
    if extra4 > 0:
        nextFatura += extra4
    nextFatura += acadMes
    return nextFatura

def parcelaCompra(valor, parcelas):
    parcelado = []
    for i in range(parcelas):
        parcelado.append(valor/parcelas)
    return parcelado

meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']


salarioBrutoAtual = 811.4
chequeEspecial = 300
livreCheque = 0

contaSky = 130
contaCondo = 300

motherboard = 338.24
moboCartao = 338.24
gabinete = 210
cpu = 576
fonte600w = 0
'''
fonte650w = 288 + 34
f650wCartao = 339 + 34
'''
fonteAli = 237.92
ram8 = 99.52
impostoRam8 = 20.38
totalRam8 = round_up(ram8 + impostoRam8)
ram16 = 0
impostoRam16 = 0
totalRam16 = round_up(ram16 + impostoRam16)
ram32 = 249.60
impostoRam32 = 51.14
totalRam32 = round_up(ram32 + impostoRam32)
ram = round_up(ram8 + impostoRam8 + ram16 + impostoRam16)
gpu = 952.45

componentes = [motherboard, gabinete, cpu, fonte600w, totalRam16, gpu]
comprados = [gpu, cpu, gabinete, motherboard, totalRam16, fonte600w]
faltaComprar = [componente for componente in componentes if componente not in comprados]

surplus = 0
maxCartao = 1100
livreCartao = 911
faturaAtual = 38.65
saldoAtual = 672.25
usoCheque = 0
aParcela = 16.51
aFaltam = 2
bParcela = 191.90
bFaltam = 0
cParcela = 22.14
cFaltam = 7
acadMes = 0

meta = 0

duasContas = contaCondo + contaSky
duasContasEx = f"({contaCondo} + {contaSky})"

pcDict = {

}
pcCartao = {

}

avulso = 0
entrada = 's'
contLacos = 0
mesAtual = True
cont = 4
contExtra = 0
comprarParcela1 = []
comprarParcela2 = []
comprarParcela3 = []
comprarParcela4 = []

entrada = input(f'Meta a ser alcançada: ')
try:
    meta = float(entrada)
except:
    pass

entrada = input(f"Quanto entrou em {meses[cont]}? ")
try:
    avulso = float(entrada)
except:
    pass

while(entrada != 'n'):
    contExtra += 1
    compravel = []
    comprar = 0
    virgula = ''
    contLacos = 0
    comprando = ''
    cartaoOuPix = []

    pagar = round_up(faturaAtual + usoCheque + duasContas)
    pagarEx = f'{faturaAtual} + {usoCheque} + {duasContasEx}'
    usoCheque = 0
    livreCheque = 0
    montante = salarioBrutoAtual + avulso
    avulso = 0

    if (mesAtual == True):
        montante = saldoAtual
        mesAtual = False

    resto = round_up(montante - pagar)
    livreCartao += faturaAtual

    if resto > 0 and meta > 0:
        if (meta - resto/4) < 0:
            resto -= meta
            meta = 0
        else:
            meta -= resto/4
            resto -= resto/4

    if resto < 0 and resto >= -300:
        usoCheque = round_up(abs(resto))
        livreCheque = chequeEspecial - usoCheque
        resto = 0
    elif resto < -300:
        resto += 300
        usoCheque = 300
        livreCheque = 0
    else:
        livreCheque = chequeEspecial - usoCheque
        avulso = resto

    for i in list(pcDict):
        if contLacos > 0 and contLacos < len(list(pcDict)) and compravel:
            virgula = ', '
        if pcDict[i] <= avulso + livreCheque:
            compravel.append(f'{virgula}{i} por {pcDict[i]}')
            avulso -= pcDict[i]
            if avulso < 0:
                usoCheque = abs(avulso)
                avulso = 0
                livreCheque -= usoCheque
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
            comprar += pcCartao[i]
            cartaoOuPix.append('no cartão')
            del pcCartao[i]
            del pcDict[i]    
        contLacos += 1    

    if compravel and compravel != 'Tudo foi comprado':
        for i in range(len(compravel)):
            comprando += f'{compravel[i]} {cartaoOuPix[i]}'

    livreCartao = round_up(livreCartao)
    printar = f'''Tanto que deve pagar: {pagar} ({faturaAtual} + Cheque Especial Usado + {duasContas})
Tanto que tem para pagar: {montante}
Tanto que sobrou: {resto}
Tanto que usou do cheque especial: {usoCheque}
Tanto que tem livre no cheque especial: {livreCheque}
Tanto que tem livre no cartão: {livreCartao}
Tanto que falta para alcançar a meta: {meta}
Mês: {contExtra}
'''
    """
    Pode comprar: {comprando}
    Falta comprar: {list(pcDict)}
    """
    print(printar)
    if aFaltam > 0:
        aFaltam -= 1
    if bFaltam > 0:
        bFaltam -= 1
    if cFaltam > 0:
        cFaltam -= 1

    if not comprarParcela1:
        comprarParcela1.append(0)
    if not comprarParcela2:
        comprarParcela2.append(0)
    if not comprarParcela3:
        comprarParcela3.append(0)
    if not comprarParcela4:
        comprarParcela4.append(0)

    faturaAtual = round_up(proximaFatura(aParcela, aFaltam, bParcela, bFaltam, cParcela, cFaltam, comprarParcela1[0], comprarParcela2[0], comprarParcela3[0], comprarParcela4[0], acadMes))
    if comprarParcela1:
        comprarParcela1.pop(0)
    if comprarParcela2:
        comprarParcela2.pop(0)
    if comprarParcela3:
        comprarParcela3.pop(0)
    if comprarParcela4:
        comprarParcela4.pop(0)
    
    cont += 1
    if cont == 12:
        cont = 0
    
    entrada = input(f"Quanto entrou em {meses[cont]}? ")
    try:
        avulso += float(entrada)
    except:
        pass
