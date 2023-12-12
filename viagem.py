
distancia = 430   #km
eficienciaCarro = 15 #Km/L
tanqueCarro = 47  #L
precoGasolina = 5 #Reais

carroDia = 110.95 #Reais
taxa = 1.12       #em porcentagem
condutorJovem = 29.95
viagemDias = 2
quantPessoas = 4

quantLitros = distancia / eficienciaCarro
quantLitrosIdaVinda = quantLitros * 2
quantLitrosComprar = quantLitros - tanqueCarro
quantLitrosComprarIdaVinda = quantLitrosIdaVinda - tanqueCarro
custoLitros = quantLitros * precoGasolina
custoLitrosIdaVinda = quantLitrosIdaVinda * precoGasolina

aluguelCarro = (carroDia+condutorJovem) * viagemDias * taxa

precoPorPessoa = aluguelCarro/quantPessoas

precoTotalPorPessoa = custoLitrosIdaVinda/quantPessoas + precoPorPessoa

print(f'Preço do aluguel do carro: {aluguelCarro}\nPreço do aluguel por pessoa: {precoPorPessoa}')
if quantLitrosComprarIdaVinda > 0:
    print(f'Quantos litros vai gastar: {quantLitrosComprarIdaVinda}')
    print(f'Custo total de gasolina: {custoLitrosIdaVinda}')
if quantLitrosComprarIdaVinda < 0:
    print(f'Quantos litros vai sobrar: {quantLitrosComprarIdaVinda*-1}')
print(f'Custo total pra cada pessoa: {precoTotalPorPessoa}')