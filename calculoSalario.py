import math
import decimal

def round_up(x, place=2):
    context = decimal.getcontext()
    # get the original setting so we can put it back when we're done
    original_rounding = context.rounding
    # change context to act like ceil()
    context.rounding = decimal.ROUND_CEILING

    rounded = round(decimal.Decimal(str(x)), place)
    context.rounding = original_rounding
    return float(rounded)

salarioBruto = 811.4

tempoSalario = 12
salariosRecebidos = 5
tempoRestante = tempoSalario-salariosRecebidos

taxaBanco = 50

salarioReal = salarioBruto - taxaBanco

motherboard = 549
gabinete = 357
cpu = 699
fonte = 265
ram = 370
gpu = 952.45

componentes = [motherboard, gabinete, cpu, fonte, ram, gpu]
comprados = [gpu]
faltaComprar = [componente for componente in componentes if componente not in comprados]

totalRestante = 0 
totalCompleto = motherboard + gabinete + cpu + fonte + ram + gpu
for i in faltaComprar:
    totalRestante += i

#54 caracteres na maior linha

imposto1 = 0
imposto2 = 0

precoReal = totalCompleto
precoReal2 = totalRestante

guardar1 = precoReal / math.ceil(precoReal/salarioReal)
guardar2 = precoReal2 / math.ceil(precoReal2/salarioReal)

calculos = f'''
****************************************************** -- ******************************************************
Salário mensal bruto: {salarioBruto}                            -- Salário mensal bruto: {salarioBruto}
Salário total bruto: {salarioBruto * tempoSalario}                            -- Salário total bruto: {salarioBruto*tempoSalario}
Taxa do banco: {taxaBanco}                                      -- Taxa do banco: {taxaBanco}
Taxa do banco total: {taxaBanco * tempoSalario}                               -- Taxa do banco total: {taxaBanco*tempoSalario}
Salário mensal líquido: {salarioReal}                          -- Salário mensal líquido: {salarioReal}
Salário total líquido: {salarioReal * tempoSalario}                          -- Salário total líquido: {salarioReal*tempoSalario}

Salário total bruto restante: {tempoRestante * salarioBruto}                   -- Salário total bruto restante: {tempoRestante*salarioBruto}
Taxa do banco total restante: {tempoRestante * taxaBanco}                      -- Taxa total do banco restante: {tempoRestante*taxaBanco}
Salário total líquido restante: {tempoRestante * salarioReal}                 -- Salário total líquido restante: {tempoRestante*salarioReal}

Preço total: {totalCompleto}                                   -- Preço total: {totalRestante}
Meses para comprar: {math.ceil(totalCompleto/salarioReal)}                                  -- Meses para comprar: {math.ceil(totalRestante/salarioReal)}
Quanto economizar por mês: {round_up(guardar1)}                      -- Quanto economizar por mês: {round_up(guardar2)}

Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar1)}                -- Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar2)}
Quanto pode gastar por mês líquido: {round_up(salarioReal - guardar1)}              -- Quanto pode gastar por mes líquido: {round_up(salarioReal - guardar2)}

Dinheiro total após a compra: {round_up(tempoRestante * salarioReal - precoReal)}                  -- Dinheiro total após a compra: {round_up(tempoRestante * salarioReal - precoReal2)}

*************************Com GPU********************** -- *************************Sem GPU*************************
'''
print(calculos)
input()
