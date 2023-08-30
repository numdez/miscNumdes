import math

salarioBruto = 811.4

tempoSalario = 12
salariosRecebidos = 1
tempoRestante = tempoSalario-salariosRecebidos

taxaBanco = 50

salarioReal = salarioBruto - taxaBanco

precoAlvo = 1908.54
precoAlvo2 = 2168.82

importacao = True

#54 caracteres na maior linha

imposto1 = 0
imposto2 = 0

taxaImportacao = 0.6

if importacao == True:
    imposto1 = precoAlvo * taxaImportacao
    imposto2 = precoAlvo2 * taxaImportacao

precoReal = precoAlvo + imposto1
precoReal2 = precoAlvo2 + imposto1

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

Preço no site: {precoAlvo}                                 -- Preço no site: {precoAlvo2}
Meses para comprar: {math.ceil(precoAlvo/salarioReal)}                                  -- Meses para comprar: {math.ceil(precoAlvo2/salarioReal)}
Imposto: {imposto1}                                      -- Imposto: {imposto2}

Meses para pagar imposto (se for taxado): {math.ceil(imposto1/salarioReal)}            -- Meses para pagar imposto (se for taxado): {math.ceil(imposto2/salarioReal)}
Preço com imposto: {precoReal}                  -- Preço com imposto: {precoReal2}
Meses para pagar tudo: {math.ceil(precoReal/salarioReal)}                               -- Meses para pagar tudo: {math.ceil(precoReal2/salarioReal)}
Quanto economizar por mês: {guardar1}                    -- Quanto economizar por mês: {guardar2}

Quanto pode gastar por mês bruto: {salarioBruto - guardar1}   -- Quanto pode gastar por mês bruto: {salarioBruto - guardar2}
Quanto pode gastar por mês líquido: {salarioReal - guardar1} -- Quanto pode gastar por mes líquido: {salarioReal - guardar2}

Dinheiro total após a compra: {tempoRestante * salarioReal - precoReal}                 -- Dinheiro total após a compra: {tempoRestante * salarioReal - precoReal2}

************************128G************************** -- ************************256G**************************
'''

print(calculos)
