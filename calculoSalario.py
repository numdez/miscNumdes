import math

salarioBruto = 811.4

tempoSalario = 12
salariosRecebidos = 1
tempoRestante = tempoSalario-salariosRecebidos

taxaBanco = 50

salarioReal = salarioBruto - taxaBanco

precoAlvo = 1908.54

importacao = True

imposto = 0

taxaImportacao = 0.6

if importacao == True:
    imposto = precoAlvo * taxaImportacao

precoReal = precoAlvo + imposto


calculos = f'''
Salário mensal bruto: {salarioBruto}
Salário total bruto: {salarioBruto * tempoSalario}
Taxa do banco: {taxaBanco}
Taxa do banco total: {taxaBanco * tempoSalario}
Salário mensal líquido: {salarioReal}
Salário total líquido: {salarioReal * tempoSalario}

Salário total bruto restante: {tempoRestante * salarioBruto}
Taxa do banco total restante: {tempoRestante * taxaBanco}
Salário total líquido restante: {tempoRestante * salarioReal}

Preço no site: {precoAlvo}
Meses para comprar: {math.ceil(precoAlvo/salarioReal)}
Imposto: {imposto}
Meses para pagar imposto (se for taxado): {math.ceil(imposto/salarioReal)}
Preço com imposto: {precoReal}
Meses para pagar tudo: {math.ceil(precoReal/salarioReal)}
Quanto economizar por mês: {precoReal / math.ceil(precoReal/salarioReal)}

Dinheiro total após a compra: {tempoRestante * salarioReal - precoReal}
'''

print(calculos)