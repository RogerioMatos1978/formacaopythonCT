from operator import invert

# Dicionario é formado por chave e valor
carro = {"modelo": "Mustang" , "marca": "Ford", "ano": 1964 }

print(carro["modelo"])

# Lista com Dicionario
carros = [
    {"modelo": "Mustang", "marca": "Ford", "ano": 1964},
    {"modelo": "Creta", "marca": "Hyndai", "ano": 2020},
    {"modelo": "Fusca", "marca": "Wolksvagem", "ano": 1945},
]
print(carros[1])

# Dicionario
usuario = {
    "id" :10,
    "nome": "Rogerio",
    "acessos": ["biblioteca", "cafeteria", "banheiro"],
    "premium": True
}
print(type(usuario["acessos"]))
print(usuario["acessos"])

# Função dict
usuario2 = dict( nome="Rogerio", idade=47, premium=True)
print(usuario2)

# Python - List Comprehension
quadrados = {
    n: n**2 for n in range(11)
}
print(quadrados)

# Loop for em dicionario pegando key values items
carro2 = {"modelo": "Mustang" , "marca": "Ford", "ano": 1964 }

print(carro2.values())
print(carro2.items())
print(carro2.keys())

for i in carro2:
    print(i)

for valor in carro2.values():
    print(valor)

for key, valor in carro2.items():
    print(f"O valor da chave '{key}' é '{valor}'")

# O in olha para o identificador
if 'cor' in carro2:
    print((carro['cor']))
else:
    print('Carro Transparente')

# usar o get para pegar o valor
print(carro2.get("cor", "Transparente"))

# inserir valores no dicionario
carro2.update({'cor': "Azul", "blindado": True})
print(carro2)

# inserir valores no dicionario
carro2 |= { 'motor':2.0, 'combustivel': 'Gasolina'}
print(carro2)

# Remover do dicionario com o pop
carro2.pop("cor")
print(carro2)

# Remover do dicionario como del
del carro2["motor"]
print(carro2)

# Pegar o tamento do dicionario
print(len(carro2))

# deletar tudo do dicionario
#carro2.clear()
#print(carro2)

inventario = {
    "id": 1,
    "tags": ['promoção', 'pramocinha'],
    "disponivel": True,
    "preco": 9.97
}
print(len(inventario))

# Copiar completo um dicionario para outro
inventario2 = inventario.copy()
print(inventario2)

# Acessando a chave tags e adicionado outro valor
inventario2['tags'].append('desconto')


# --------------------------------------------
import copy
tags = ['promoção', 'pramocinha']

original = {
    "id": 1,
    "tags": tags ,
    "disponivel": True,
    "preco": 9.97
}

copia = copy.deepcopy(original)
copia['tags'].append('desconto')

print(copia)


familaMatos = {
    "pai": {"nome": "Rogerio", "idade": 47, "cores_favoritas": ['azul','amarelo']},
    "mae": {"nome": "Maria", "idade": 45, "cores_favoritas": ['azul','amarelo']},
    "filha": {"nome": "Alicya", "idade": 19, "cores_favoritas": ['azul','amarelo']},
    "filho": {"nome": "Rogerio", "idade": 15, "cores_favoritas": ['azul','amarelo']},

}

print(familaMatos['mae']['idade'])

for posicao, membro in familaMatos.items():
    print(f"{posicao}: o nome é {membro['nome']}")

# ----------------------------------------------
temperaturas = {"seg": 30, "ter": 27,"qua": 25,"qui": 16,"sex": 22,"sab": 45,"do": 38, }

quentes = { dia: temp for dia, temp in temperaturas.items() if temp > 27}

print(quentes)

quentes2 = {}

for dia, temp in temperaturas.items():
    if temp > 27:
        quentes2 |= {dia: temp}
print(quentes2)

#------------------------------
json_trocado ={
    "rogerio.matos@gmail.com": 1,
    "mariamatos@gmail.com": 2
}

json_correto ={ valor: chave for chave, valor in json_trocado.items()}

print(json_correto)
print(json_correto[2])

# ------------------------
nomes = [
    'Laender', 'Edson','Fabricio','Flavio','Giselle','Guilherme',
    'Jefrey', 'João','Julio','Leonor','Matheus','Olavo', 'Rogerio'
]
nomes_agrupados = {}
for nome in nomes:
    print(nome[0])

for nome in nomes:
    #nomes_agrupados.setdefault(nome[0], []).append(nome)
    if nome[0] in nomes_agrupados:
        nomes_agrupados[nome[0]].append(nome)
    else:
        nomes_agrupados[nome[0]] = [nome]

print(nomes_agrupados)
print(len(nomes_agrupados))
print(len(nomes_agrupados['L']))

# ------------------------------------------
from collections import Counter
nomes = [
    'Laender', 'Edson','Fabricio','Flavio','Giselle','Guilherme',
    'Jefrey', 'João','Julio','Leonor','Matheus','Olavo', 'Rogerio',
    'Laender', 'Edson', 'Fabricio', 'Flavio', 'Giselle','Guilherme',
    'Jefrey', 'João', 'Julio', 'Leonor', 'Matheus', 'Olavo', 'Rogerio',
    'Laender', 'Edson', 'Fabricio', 'Flavio', 'Giselle','Guilherme',
    'Jefrey', 'João', 'Julio', 'Leonor', 'Matheus', 'Olavo', 'Rogerio',
]

contagem = {}
for nome in nomes:
    if nome in contagem:
        contagem[nome] +=1
    else:
        contagem[nome] = 1

contagem2 = {}
for nome in nomes:
    contagem2.setdefault(nome, 0)
    contagem2[nome] += 1

contagem3 = {}
for nome in nomes:
    contagem3.setdefault(nome, []).append(nome)

resultado = { chave: len(valor) for chave, valor in contagem3.items()}


print(contagem)
print(contagem2)
print(resultado)
print(Counter(nomes))

nome = "Rogerio da Silva Matos"
freq = Counter(nome)
print(freq)
