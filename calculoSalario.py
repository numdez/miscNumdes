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
surplus = 0

salarioReal = salarioBruto - taxaBanco
salarioCondo = salarioReal - contaCondo
salarioCerto = salarioReal - contaCondo - contaSky

motherboard = 370
gabinete = 210
cpu = 576
fonte = 280
ram8 = 99.52
impostoRam8 = 20.38
totalRam8 = round_up(ram8 + impostoRam8)
ram16 = 143.13
impostoRam16 = 29.33
totalRam16 = round_up(ram16 + impostoRam16)
ram = round_up(ram8 + impostoRam8 + ram16 + impostoRam16)
gpu = 952.45

componentes = [motherboard, gabinete, cpu, fonte, totalRam8, totalRam16, gpu]
comprados = [gpu, cpu, gabinete]
faltaComprar = [componente for componente in componentes if componente not in comprados]


totalRestante = 0 
totalCompleto = motherboard + gabinete + cpu + fonte + totalRam8 + totalRam16 + gpu
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

Mês atual = {contaCondo2} + {contaSky2}
Total mês atual = {contaCondo2 + contaSky2}
Resto = {surplus}
'''
print(calculos)

pcDict = {
    "Pente de 16GB": totalRam16,
    "Fonte 600W": 280,
    "Placa mãe": 380
}

val = input()
try:
    taxaCancelada = int(val)
except:
    pass

while(val != 'n'):

    if taxaCancelada > 0:
        taxaBanco = 0
        salarioBruto += taxaCancelada
        taxaCancelada = 0
    if usoCheque < 0:
        usoCheque = abs(usoCheque)
    
    duasContas = contaCondo + contaSky
    duasContasEx = f"{contaCondo} + {contaSky}"
    zeroContas = contaCondo2 + contaSky2
    zeroContasEx = f"{contaCondo2} + {contaSky2}"

    surplus = round_up(salarioBruto - (faturaAtual + duasContas + usoCheque + taxaBanco))
    livreCartao += faturaAtual
    if not list(pcDict):
        comprar = 0
        compravel = 'Tudo já foi comprado'
    for k in list(pcDict):
        if pcDict[k] < surplus + livreCartao:
            compravel = f'{k} por {pcDict[k]}'
            comprar = pcDict[k]
            del pcDict[k]
            break
        else:
            compravel = "nada"
            comprar = 0
    
    livreCartao -=  comprar

    if compravel == 'Tudo já foi comprado':
        printar = f''' 
Próximo mês = {faturaAtual} + {duasContasEx} + {usoCheque} + {taxaBanco} - {salarioBruto}
Total próximo mês = {salarioBruto - (faturaAtual + duasContas + taxaBanco + usoCheque)}
Resto = {surplus} + {round_up(livreCartao)} livre no cartão ao fim do mês
Peças compráveis = {compravel}
'''
    else:
        printar = f''' 
Próximo mês = {faturaAtual} + {duasContasEx} + {usoCheque} + {taxaBanco} - {salarioBruto}
Total próximo mês = {salarioBruto - (faturaAtual + duasContas + taxaBanco + usoCheque)}
Resto = {surplus} + {round_up(livreCartao)} livre no cartão ao fim do mês
Peças compráveis = {compravel}
Peças faltando = {list(pcDict.items())}
    '''
    print(printar)
    salarioBruto = 811.4
    faturaAtual = proximaFatura(aParcela, aFaltam, bParcela, bFaltam, cParcela, cFaltam, comprar)
    if usoCheque > 0 and faturaAtual + duasContas + taxaBanco + usoCheque > salarioBruto:
        usoCheque = pagaChequeComCheque(usoCheque, chequeEspecial)
    elif usoCheque > 0 and surplus >= usoCheque:
        usoCheque -= salarioBruto
        if usoCheque <= 0:
            usoCheque = 0
    
    aParcela = 58.06
    aFaltam -= 1
    bParcela = 191.90
    bFaltam -= 1
    cParcela = 22.15
    cFaltam -= 1
    if surplus < 0 and surplus >= -300:
        usoCheque = surplus
    elif surplus > 0:
        usoCheque = 0
        salarioBruto += surplus
    
    val = input()
    try:
        taxaCancelada = int(val)
    except:
        pass
# %%
