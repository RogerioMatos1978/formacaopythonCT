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