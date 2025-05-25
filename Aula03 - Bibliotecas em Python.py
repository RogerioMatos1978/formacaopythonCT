# Bibliotecas em Python
# Em Python, chamamos de “bibliotecas” ou “módulos” os conjuntos de código que oferecem
# funcionalidades específicas, já prontas para uso. Elas podem fazer parte da biblioteca
# padrão (instalada por padrão com o Python) ou ser de terceiros, desenvolvidas e distribuídas pela comunidade.

# 1. Biblioteca Padrão

# A biblioteca padrão do Python inclui diversos módulos úteis para tarefas comuns,
# como manipular arquivos, trabalhar com expressões regulares, acessar bancos de dados e muito mais. Destacamos aqui alguns exemplos populares:
#
# 1. math – Funções matemáticas, como seno, cosseno, logaritmo, etc.
# 2. statistics – Ferramentas estatísticas básicas (média, mediana, variância, etc.).
# 3. random – Geração de números aleatórios e escolhas randômicas.
#  Essas bibliotecas já vêm instaladas com o Python, prontas para uso imediato.
# Exemplo usando 'math' para cálculos
import math

angulo = math.radians(45)       # Converte 45° para radianos
print(math.sin(angulo))         # Calcula seno de 45°

# Exemplo usando 'statistics' para análise simples
import statistics

dados = [10, 20, 20, 30, 40, 40, 40]
print(statistics.mean(dados))   # Média
print(statistics.median(dados)) # Mediana

# Exemplo usando 'random' para gerar valores
import random

numero_aleatorio = random.randint(1, 100) # Inteiro entre 1 e 100
print(numero_aleatorio)

lista_nomes = ["Ana", "Bruno", "Carla", "Daniel"]
print(random.choice(lista_nomes))  # Escolhe um nome aleatório

# 2. Formas de Importar

# Existem diferentes maneiras de importar módulos e funções em Python.
# Isso pode alterar a forma como chamamos as funções e variáveis no código.
# import nome_do_modulo
# Importa todo o módulo e, ao chamar suas funções ou variáveis, é preciso qualificar com o nome do módulo.
import math

resultado = math.sqrt(16)  # sqrt está em math
print(resultado)

# from nome_do_modulo import nome_do_objeto
# Importa apenas o que você especificar, permitindo chamar diretamente sqrt sem precisar do prefixo math.
import math as m

print(m.sqrt(25))   # Usando 'm' em vez de 'math'

# from nome_do_modulo import * (não recomendado)
# Importa tudo do módulo, sem precisar do prefixo.
# Contudo, pode gerar conflitos de nome e dificultar a leitura do código, além de torná-lo menos previsível.
# Geralmente, preferimos import math ou from math import algo para manter o código mais organizado e explícito.
from math import *

print(sin(1), cos(1), sqrt(9))

# 3. Bibliotecas de Terceiros (PyPI)
# O Python Package Index (PyPI) é o repositório oficial de bibliotecas e pacotes criados pela comunidade.
# Para instalar uma biblioteca de terceiros, normalmente usamos o pip (Python package installer):
# pip install nome-da-biblioteca
# Em IDEs como o PyCharm, você pode instalar módulos clicando no ícone de lâmpada ou usando o
# gerenciador de pacotes (File > Settings > Project > Python Interpreter).

# Por exemplo, para fazer requisições HTTP, podemos usar a biblioteca requests:
import requests

resposta = requests.get("https://google.com")
print(resposta.status_code)

# Outro exemplo é a biblioteca tabulate, que formata dados em tabelas de texto:
from tabulate import tabulate

dados = [
    ["Ana", 25],
    ["Bruno", 30],
    ["Carla", 22]
]
cabecalho = ["Nome", "Idade"]

print(tabulate(dados, headers=cabecalho, tablefmt="grid"))
"""
Há milhares de bibliotecas disponíveis no PyPI, cobrindo áreas como ciência de dados, 
aprendizado de máquina, desenvolvimento web, interface gráfica e muito mais.
Em resumo, as bibliotecas fornecem funcionalidades prontas que agilizam o desenvolvimento. 
A biblioteca padrão do Python já é bastante rica, enquanto o PyPI oferece uma 
infinidade de pacotes adicionais para quase qualquer necessidade."""

