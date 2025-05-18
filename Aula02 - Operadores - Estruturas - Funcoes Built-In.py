"""
Os Booleanos são valores lógicos que podem ser apenas True ou False.
Eles surgem quando fazemos comparações entre valores ou avaliamos
condições em estruturas como if, sendo fundamentais para o
controle de fluxo de qualquer aplicação em Python.

1. Visão Geral

Sempre que usamos operadores de comparação (==, >, < etc.),
o resultado será um valor booleano: True ou False. Em instruções if,
Python decide o bloco a ser executado com base nesses resultados.
"""
# 2. Comparações e Condições
# Qualquer comparação entre valores retorna True ou False. Por exemplo:

print(10 > 9)   # True
print(10 == 9)  # False
print(10 < 9)   # False

# Em um if, o Python utiliza o resultado booleano para decidir qual caminho seguir:

a = 200
b = 33

if b > a:
    print("b é maior que a")
else:
    print("b NÃO é maior que a")

# 3. Avaliando Valores com bool()
# A função bool() converte praticamente qualquer valor para True ou False. Exemplos:

print(bool("Hello"))   # True
print(bool(15))        # True

x = "Hello"
y = 15
print(bool(x))  # True
print(bool(y))  # True

# 4. Valores que Retornam True
# Quase todo valor em Python será True se tiver algum tipo de conteúdo. Exemplos:
#
# Strings não vazias, como "Cubo Três" e "Python"
# Números diferentes de zero, ex: 10, -1
# Coleções (listas, tuplas, dicionários) que contenham elementos

print(bool("Cubo Três"))       # True
print(bool("Python"))          # True
print(bool(123))               # True
print(bool(["excel", "power bi"]))  # True

# 5. Valores que Retornam False
# Alguns poucos casos resultam em False, principalmente valores vazios ou inexistentes:
#
# 0 (inteiro zero)
# "" (string vazia)
# Coleções vazias como (), [], {}
# None e o próprio False

print(bool(False))  # False
print(bool(None))   # False
print(bool(0))      # False
print(bool(""))     # False
print(bool(()))     # False
print(bool([]))     # False

# 6. Sobrescrita de Métodos e Objetos Personalizados
# Dependendo de como uma classe é implementada, ela pode ser avaliada como False
# quando seu método __len__() retornar 0. Se o método __len__() retornar um valor maior, a avaliação se torna True.

class Pedido:
    def __init__(self):
        self.itens = []

    def adicionar_item(self, item):
        self.itens.append(item)

    def remover_item(self, item):
        self.itens.remove(item)

    def __len__(self):
        return len(self.itens)


# Exemplo de uso
pedido = Pedido()
print(len(pedido))        # 0
print(bool(pedido))       # False (pois __len__ é 0)

pedido.adicionar_item("Pipoca")
print(len(pedido))        # 1
print(bool(pedido))       # True  (pois __len__ agora é 1)

# 7. Funções que Retornam Boolean
# Você pode criar funções que retornam True ou False conforme alguma condição,
# e utilizá-las para facilitar o controle de fluxo no código.

def verifica_maioridade(idade):
    return idade >= 18

idade = int(input("Digite sua idade: "))
if verifica_maioridade(idade):
    print("Você é maior de idade")
else:
    print("Você NÃO é maior de idade")

# 8. Funções Internas para Verificação
# O Python traz diversas funções que retornam valores booleanos,
# como isinstance(), para verificar se um objeto é de determinado tipo.

x = 200
print(isinstance(x, int))  # True

"""
Em Python, operadores são utilizados para realizar operações em variáveis e valores. 
Eles podem somar, comparar, verificar identidade, entre outros. 
A escolha do operador certo permite que você crie códigos mais expressivos e eficientes.

1. Introdução
Existem diversos grupos de operadores em Python, dentre eles:

1. Operadores Aritméticos
2. Operadores de Atribuição
3. Operadores de Comparação
4. Operadores Lógicos
5. Operadores de Identidade
6. Operadores de Pertinência
7. Precedência de Operadores (ordem de avaliação)
Um exemplo simples de operador aritmético é +, que realiza a soma de valores:
"""
print(10 + 5)  # Exibe 15


# 2. Operadores Aritméticos
# Usados com números para operações matemáticas comuns:

# Operador	Nome	Exemplo
# +	Adição	x + y
# -	Subtração	x - y
# *	Multiplicação	x * y
# /	Divisão	x / y
# %	Resto da Divisão	x % y
# **	Exponenciação	x ** y
# //	Divisão de Inteiro	x // y

print(7 % 2)    # 1 (resto de 7 / 2)
print(2 ** 3)   # 8

# 2. Operadores Aritméticos
# Usados com números para operações matemáticas comuns:

# Operador	Nome	Exemplo
# +	Adição	x + y
# -	Subtração	x - y
# *	Multiplicação	x * y
# /	Divisão	x / y
# %	Resto da Divisão	x % y
# **	Exponenciação	x ** y
# //	Divisão de Inteiro	x // y

print(7 % 2)    # 1 (resto de 7 / 2)
print(2 ** 3)   # 8

# 4. Operadores de Comparação
# Usados para comparar dois valores e retornar um resultado booleano (True ou False):

# Operador	Nome	Exemplo
# ==	Igual	x == y
# !=	Diferente	x != y
# >	Maior que	x > y
# <	Menor que	x < y
# >=	Maior ou igual	x >= y
# <=	Menor ou igual	x <= y
a = 10
b = 5
print(a == b)   # False
print(a > b)    # True
print(a <= b)   # False

# 5. Operadores Lógicos
# Servem para combinar condições e retornar um resultado booleano:
#
# and — Retorna True se ambas as expressões forem verdadeiras
# or — Retorna True se pelo menos uma expressão for verdadeira
# not — Inverte o resultado, retornando False se a expressão for verdadeira
x = 10
print(x > 5 and x < 15)   # True (ambas são verdadeiras)
print(x < 5 or x < 12)    # True (pelo menos uma é verdadeira)
print(not(x < 20))        # False (pois x < 20 é True, e not True = False)

# 6. Operadores de Identidade
# Verificam se duas variáveis são, de fato, o mesmo objeto em memória:
#
# is — Retorna True se as variáveis apontam para o mesmo objeto
# is not — Retorna True se não apontarem para o mesmo objeto
a = [1, 2, 3]
b = a
c = [1, 2, 3]

print(a is b)      # True  (ambas referem-se à mesma lista)
print(a is c)      # False (c é outra lista, mesmo que com itens iguais)

print(a is not b)  # False
print(a is not c)  # True

# 7. Operadores de Pertinência
# Verificam se uma sequência existe em outro objeto (string, lista, tupla etc.):
#
# in — Retorna True se o valor estiver contido na sequência
# not in — Retorna True se o valor não estiver contido
frutas = ["maçã", "banana", "uva"]
print("banana" in frutas)      # True
print("laranja" not in frutas)  # True

texto = "Python é divertido"
print("diver" in texto)         # True
print("php" in texto)           # False

# 8. Precedência de Operadores
# Determina a ordem em que as operações são realizadas. As operações entre parênteses têm maior precedência, seguidas por exponenciação, depois multiplicação/divisão, e assim por diante. Operadores de mesma precedência são avaliados da esquerda para a direita.
#
# Precedência	Operadores
# Mais alto	( ) (Parênteses)
#           ** (Exponenciação)
#           *, /, //, % (Multiplicação, Divisão, Divisão de Inteiro e Resto)
#           +, - (Adição e Subtração)
#           ==, !=, >, <, >=, <=, is, is not, in, not in (Comparações, Identidade e Pertinência)
#           not (Negação Lógica)
#           and (Conjunção Lógica)
# Mais baixo	or (Disjunção Lógica)
# Exemplos de uso da precedência:

# Sem parênteses, avaliado da esquerda para a direita
print(6 + 3 - 6 + 3)  # 6

# Alterando ordem com parênteses
print(6 + 3 - (-6 + 3))  # 12

# Parênteses usados em cada trecho
print((6 + 3) - (6 + 3))  # 0

# Outro exemplo:
print(100 + 5 * 3)  # 115, multiplicação antes da soma

# Mesma precedência, segue da esquerda para a direita
print(5 + 4 - 7 + 3)  # 5

# 9. Bônus - Operações com Strings
# Alguns operadores aritméticos também podem ser utilizados em strings:

# + para concatenação.
texto1 = "Olá, "
texto2 = "Mundo!"
resultado = texto1 + texto2
print(resultado)  # "Olá, Mundo!"

# * para repetição.
mensagem = "Python "
repeticoes = 3
print(mensagem * repeticoes)  # "Python Python Python "

 # Funções Built-in Básicas
"""
O Python possui diversas funções nativas (built-in) que facilitam o desenvolvimento. 
Elas executam tarefas comuns, como encontrar valores máximos e mínimos, 
somar itens de uma coleção, medir o comprimento de estruturas, entre outros. 
Vamos ver algumas das principais funções embutidas.
"""
# 1. len()
#  Retorna o número de itens em um objeto. Serve para listas, tuplas, strings, sets, dicionários, etc.
# Caso seja chamado em um dicionário, retornará a quantidade de chaves presentes.
# Exemplo com lista
animais = ["cachorro", "gato", "tigre"]
print(len(animais))  # 3

# Exemplo com string
texto = "Python"
print(len(texto))     # 6

# 2. sum()
# Soma todos os elementos de um objeto iterável (listas, tuplas, etc.). É bastante útil para somatórios rápidos.
# Lembre-se de que os itens devem ser numéricos, caso contrário ocorrerá um erro.
numeros = [10, 20, 5]
resultado = sum(numeros)
print(resultado)  # 35

# Também é possível usar um valor inicial
resultado_com_inicial = sum(numeros, 100)
print(resultado_com_inicial)  # 135

# 3. max() e min()
# Retornam, respectivamente, o maior e o menor valor de um iterável.
# Também funcionam ao passar vários argumentos separados por vírgula.
#  Se a lista (ou conjunto) estiver vazia, um erro será gerado.
#  Caso queira evitar isso, valide antes se o iterável possui elementos.
valores = [3, 10, 1, 7, 4]
print(max(valores))  # 10
print(min(valores))  # 1

# Podemos utilizar diretamente:
print(max(2, 5, 8, 1))  # 8
print(min(2, 5, 8, 1))  # 1

# 4. range()
# Gera uma sequência de números. É frequentemente usado em laços de repetição (for),
# mas também pode ser convertido para lista, por exemplo.

for i in range(3):
    print(i)
# Saída: 0, 1, 2

print(list(range(2, 5)))
# Converte para lista: [2, 3, 4]

print(list(range(1, 10, 2)))
# Início = 1, Fim = 10, Passo = 2 -> [1, 3, 5, 7, 9]

# 5. abs()
# Retorna o valor absoluto de um número.
# Usado para sempre obter a distância de zero.

print(abs(-10))  # 10
print(abs(3.5))  # 3.5

# 6. round()
# Arredonda um número para o inteiro mais próximo. R
# ecebe um parâmetro opcional para determinar quantas casas decimais manter.
# O comportamento de round() em casos de .5 pode variar dependendo do contexto,
# geralmente usando o arredondamento “para o par” (banker's rounding).

print(round(3.2))         # 3
print(round(3.6))         # 4
print(round(3.14159, 2))   # 3.14

# 7. type()
# Retorna o tipo do objeto passado como argumento,
# permitindo verificar se algo é int, str, list, etc.

print(type(10))           #
print(type("Python"))     #
print(type([1, 2, 3]))    #

# -----------------------------------------------------------------------------------
# 8. enumerate()
#  Transforma um iterável em um objeto que gera pares de índice,
#  valor, útil para loops com contadores.

animais = ["cachorro", "gato", "tigre"]
for indice, animal in enumerate(animais):
    print(indice, animal)

# Saída:
# 0 cachorro
# 1 gato
# 2 tigre

# -----------------------------------------------------------------------------------
# 9. zip()
# Combina elementos de várias coleções (listas, tuplas, etc.) em grupos.
# Ideal para percorrer vários iteráveis em paralelo.

nomes = ["Ana", "Bruno", "Carla"]
idades = [25, 30, 22]

for nome, idade in zip(nomes, idades):
    print(nome, idade)

# Saída:
# Ana 25
# Bruno 30
# Carla 22

# -----------------------------------------------------------------------------------
# 10. input()
# Lê dados do usuário via terminal. Retorna uma string.
# É comumente usada para criar interatividade em scripts.
# Essas funções nativas são apenas uma pequena parte da extensa biblioteca de
# funcionalidades que o Python traz por padrão.
# Ao longo do curso vamos conhecendo novas funções.
nome = input("Digite seu nome: ")
print("Olá,", nome)

# Sempre retorna string, então para converter em número, por exemplo:
idade = int(input("Digite sua idade: "))
print("Você tem", idade, "anos.")

