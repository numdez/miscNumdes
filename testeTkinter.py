import math
import decimal
import tkinter as tk

from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


def round_up(x, place=2):
    context = decimal.getcontext()
    original_rounding = context.rounding
    context.rounding = decimal.ROUND_CEILING

    rounded = round(decimal.Decimal(str(x)), place)
    context.rounding = original_rounding
    return float(rounded)

salarioBruto = 811.4

tempoSalario = 12
salariosRecebidos = 1
tempoRestante = tempoSalario-salariosRecebidos

taxaBanco = 50

gastosMensais = 0
descontos = 53.17
descontos2 = 10.41 + 53.17 + 11.49

salarioReal = salarioBruto - taxaBanco - gastosMensais

precoAlvo = 1832.70 + 62.90
precoAlvo2 = 1947.89 + 91.41 + 62.90

importacao = True

#54 caracteres na maior linha

imposto1 = 0
imposto2 = 0

taxaImportacao = 0

if importacao == True:
    imposto1 = precoAlvo * taxaImportacao
    imposto2 = precoAlvo2 * taxaImportacao

precoReal = precoAlvo + imposto1 - descontos
precoReal2 = precoAlvo2 + imposto2 - descontos2

guardar1 = precoReal / math.ceil(precoReal/salarioReal)
guardar2 = precoReal2 / math.ceil(precoReal2/salarioReal)

totalSalario = salarioReal * tempoSalario

percentualGasto1 = precoReal / totalSalario
percentualGasto2 = precoReal2 / totalSalario 

app = tk.Tk()
app.title("Teste Interface VR")

label128 = ttk.Label(app, text='MEK Foto Store').grid(row=0, column=1)

label256 = ttk.Label(app, text='All In One Store').grid(row=0, column=4)

vr128 = ScrolledText(app, width=54, height=28)
vr128.insert(tk.INSERT, f'''Salário mensal bruto: {salarioBruto}   
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
Imposto: {round_up(imposto1)} 

Meses para pagar imposto (se for taxado): {math.ceil(imposto1/salarioReal)} 
Preço com imposto: {round_up(precoReal)}
Meses para pagar tudo: {math.ceil(precoReal/salarioReal)}
Quanto economizar por mês: {round_up(guardar1)}

Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar1)}
Quanto pode gastar por mês líquido: {round_up(salarioReal - guardar1)}

Dinheiro gasto na compra: {round_up(precoReal)}
Percentual do salário gasto: {round_up(percentualGasto1*100)}%
Dinheiro total após a compra: {round_up(tempoRestante * salarioReal - precoReal)} 
Percentual do salário restante: {round_up(100-percentualGasto1*100)}%

''')
vr128.grid(row=3, column=1)

separator = ttk.Separator(app, orient="vertical")
separator.grid(row=2, column=4)

vr256 = ScrolledText(app, width=54, height=28)
vr256.insert(tk.INSERT, f'''Salário mensal bruto: {salarioBruto}   
Salário total bruto: {salarioBruto * tempoSalario}  
Taxa do banco: {taxaBanco}   
Taxa do banco total: {taxaBanco * tempoSalario} 
Salário mensal líquido: {salarioReal}  
Salário total líquido: {salarioReal * tempoSalario}  

Salário total bruto restante: {tempoRestante * salarioBruto}  
Taxa do banco total restante: {tempoRestante * taxaBanco}  
Salário total líquido restante: {tempoRestante * salarioReal}  

Preço no site: {precoAlvo2}  
Meses para comprar: {math.ceil(precoAlvo2/salarioReal)} 
Imposto: {round_up(imposto2)} 

Meses para pagar imposto (se for taxado): {math.ceil(imposto2/salarioReal)} 
Preço com imposto: {round_up(precoReal2)}
Meses para pagar tudo: {math.ceil(precoReal2/salarioReal)}
Quanto economizar por mês: {round_up(guardar2)}

Quanto pode gastar por mês bruto: {round_up(salarioBruto - guardar2)}
Quanto pode gastar por mês líquido: {round_up(salarioReal - guardar2)}

Dinheiro gasto na compra: {round_up(precoReal2)}
Percentual do salário gasto: {round_up(percentualGasto2*100)}%
Dinheiro total após a compra: {round_up(tempoRestante * salarioReal - precoReal2)}
Percentual do salário restante: {round_up(100-percentualGasto2*100)}%
''')
vr256.grid(row=3, column=4)

app.eval('tk::PlaceWindow . center')

app.mainloop()
