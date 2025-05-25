# Documentação | Métodos de Strings
# Documentação de Métodos de String em Python
# Aqui você encontrará uma visão completa dos principais métodos de string no Python, c
# obrindo definições, sintaxes, parâmetros e exemplos práticos.
# ste conteúdo foi organizado para facilitar seu aprendizado e uso no dia a dia.

# 1. Índice de Métodos
# Categoria	Métodos
# Conversão de Caixa	capitalize(), casefold(), lower(), upper(), swapcase(), title()
# Verificação	isalnum(), isalpha(), isascii(), isdecimal(), isdigit(), isidentifier(), islower(), isnumeric(), isprintable(), isspace(), istitle(), isupper()
# Busca e Localização	find(), rfind(), index(), rindex(), startswith(), endswith()
# Substituição e Formatação	format(), format_map(), replace(), translate(), maketrans()
# Divisão e União	split(), rsplit(), splitlines(), join()
# Strip e Alinhamento	strip(), lstrip(), rstrip(), center(), ljust(), rjust(), zfill()
# Outros	partition(), rpartition(), count(), encode(), expandtabs()

# 2. Conversão de Caixa
# capitalize()
# Definição
# Converte o primeiro caractere da string para maiúsculo e o restante para minúsculo.

# Sintaxe
# string.capitalize()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
frase = "cubo três e laennder"
print(frase.capitalize())   # "Cubo três e laennder"

curso = "ESCOLA DE DADOS"
print(curso.capitalize())   # "Escola de dados"

saudacao = "olá, mundo!"
print(saudacao.capitalize())# "Olá, mundo!"

cores = "vermelho e AZUL"
print(cores.capitalize())   # "Vermelho e azul"

# ----------------------------------------------------------------------------------------------------------------------------
# casefold()
#
# Definição
# Converte a string para letras minúsculas de forma mais "agressiva" do que lower(), muito útil em comparações case-insensitive.
#
# Sintaxe
# string.casefold()
#
# Parâmetros
# Não possui parâmetros.

# Exemplos
texto = "Cubo Três"
print(texto.casefold())       # "cubo três"

msg = "OLÁ, MUNDO!"
print(msg.casefold())         # "olá, mundo!"

palavra = "Laennder"
print(palavra.casefold())     # "laennder"

frase_mista = "EsCoLa De DaDoS"
print(frase_mista.casefold()) # "escola de dados"

# ------------------------------------------------------------------------------
# lower()
#
# Definição
# Converte todos os caracteres alfabéticos da string para minúsculo.
#
# Sintaxe
# string.lower()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
msg = "Olá, Mundo! Cubo Três"
print(msg.lower())       # "olá, mundo! cubo três"

titulo = "LAENNDER EM PYTHON"
print(titulo.lower())    # "laennder em python"

frase = "EScola DE DAdos"
print(frase.lower())     # "escola de dados"

print("".lower())        # ""

# -------------------------------------------------------------------------------------------------
# upper()
#
# Definição
# Converte todos os caracteres alfabéticos da string para maiúsculo.
#
# Sintaxe
# string.upper()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos

texto = "python"
print(texto.upper())           # "PYTHON"

msg = "Olá, Mundo! Cubo Três"
print(msg.upper())             # "OLÁ, MUNDO! CUBO TRÊS"

frase = "escola de dados"
print(frase.upper())           # "ESCOLA DE DADOS"

print("".upper())              # ""

# swapcase()
#
# Definição
# Converte letras maiúsculas em minúsculas e vice-versa.
#
# Sintaxe
# string.swapcase()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("Python".swapcase())     # "pYTHON"
print("CUBO três".swapcase())  # "cubo TRÊS"
print("Olá, Mundo!".swapcase())# "oLÁ, mUNDO!"
print("LAennder123".swapcase())# "laENNDER123"

# title()
# Definição
# Converte o primeiro caractere de cada palavra para maiúsculo e o restante para minúsculo.
#
# Sintaxe
# string.title()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("cubo três e escola de dados".title())  # "Cubo Três E Escola De Dados"
print("laennder EM python".title())           # "Laennder Em Python"
print("ola, mundo!".title())                  # "Ola, Mundo!"
print("VERMELHO E AZUL".title())              # "Vermelho E Azul"


# 3. Verificação
# isalnum()
# Definição
# Retorna True se todos os caracteres da string forem alfanuméricos (letras e números).
#
# Sintaxe
# string.isalnum()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
# print("CuboTrês".isalnum())    # True (sem espaços e sem caracteres especiais)
print("EscolaDeDados2023".isalnum())  # True
print("Olá, Mundo!".isalnum()) # False (possui pontuação)
print("Python_3".isalnum())    # False (possui underscore)

# isalpha()
# Definição
# Retorna True se todos os caracteres da string forem letras.
#
# Sintaxe
# string.isalpha()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("Laennder".isalpha())     # True
print("Escola3".isalpha())      # False (contém dígito)
print("CUBOTRÊS".isalpha())     # True
print("".isalpha())             # False (string vazia)

# isascii()
# Definição
# Retorna True se todos os caracteres na string forem ASCII (intervalo 0 a 127).
#
# Sintaxe
# string.isascii()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("Ola Mundo".isascii())   # True
print("Cubo Três".isascii())   # False (caractere 'é' não é ASCII)
print("Python3.9".isascii())   # True
print("∑".isascii())           # False

# isdecimal()
# Definição
# Retorna True se todos os caracteres na string forem decimais (0-9).
#
# Sintaxe
# string.isdecimal()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("123".isdecimal())       # True
print("2023".isdecimal())      # True
print("3.14".isdecimal())      # False (ponto)
print("٢٥".isdecimal())        # True (dígito árabe para 25)

# isdigit()
# Definição
# Retorna True se todos os caracteres na string forem dígitos (inclui caracteres como "²", "½" etc.).
#
# Sintaxe
# string.isdigit()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("123".isdigit())         # True
print("Cubo3".isdigit())       # False
print("½".isdigit())           # True (caractere de fração)
print("٢٥".isdigit())          # True (dígitos árabes)

# isidentifier()
# Definição
# Retorna True se a string for um identificador válido em Python (nome de variável, por exemplo).
#
# Sintaxe
# string.isidentifier()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("cubo_tres".isidentifier())   # True
print("3laennder".isidentifier())   # False (inicia com dígito)
print("Python".isidentifier())      # True
print("def".isidentifier())         # True, mas é palavra reservada

# islower()
# Definição
# Retorna True se todos os caracteres alfabéticos da string estiverem em minúsculo.
#
# Sintaxe
# string.islower()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("cubo três".islower())   # True
print("Laennder".islower())    # False
print("python2023".islower())  # True (dígitos não afetam)
print("".islower())            # False (vazia)

# isnumeric()
# Definição
# Retorna True se todos os caracteres forem numéricos (incluindo dígitos, frações, subscritos etc.).
#
# Sintaxe
# string.isnumeric()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("1234".isnumeric())    # True
print("⅕".isnumeric())       # True (caractere de fração)
print("Cubo3".isnumeric())   # False (letras)
print("٢٥".isnumeric())      # True (dígitos árabes)


# isprintable()
# Definição
# Retorna True se todos os caracteres da string forem imprimíveis ou se a string estiver vazia.
#
# Sintaxe
# string.isprintable()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("Olá, Mundo!".isprintable())  # True
print("Cubo Três\nLaennder".isprintable()) # False (\n não é imprimível)
print("   ".isprintable())         # True (espaços são imprimíveis)
print("".isprintable())            # True (vazia)

# isspace()
# Definição
# Retorna True se todos os caracteres da string forem espaços em branco (espaço, tab, nova linha etc.).
#
# Sintaxe
# string.isspace()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("   ".isspace())     # True
print("\n\t".isspace())    # True
print(" Laennder ".isspace())  # False (possui texto)
print("".isspace())        # False

# istitle()
# Definição
# Retorna True se cada palavra na string começar com letra maiúscula e as demais letras estiverem em minúsculo.
#
# Sintaxe
# string.istitle()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("Cubo Três Laennder".istitle()) # True
print("Escola de Dados".istitle())    # False ("de" não está capitalizado)
print("Olá, Mundo!".istitle())        # True
print("PYTHON".istitle())             # False

# isupper()
# Definição
# Retorna True se todos os caracteres alfabéticos da string estiverem em maiúsculo.
#
# Sintaxe
# string.isupper()
#
# Parâmetros
# Não possui parâmetros.
#
# Exemplos
print("CUBO TRÊS".isupper())   # True
print("Olá, Mundo!".isupper()) # False
print("PYTHON3".isupper())     # True (dígitos não influenciam)
print("".isupper())            # False


# 4. Busca e Localização
# find()
# Definição
# Retorna o índice da primeira ocorrência de uma substring na string. Retorna -1 se não for encontrada.
#
# Sintaxe
# string.find(value[, start[, end]])
#
# Parâmetros
# value: substring a ser encontrada.
# start (opcional): índice inicial da busca.
# end (opcional): índice final da busca.
# Exemplos
texto = "Olá, Mundo! Olá, Mundo! Escola de Dados"
print(texto.find("Mundo"))      # 5
print(texto.find("Mundo", 6))   # 17
print(texto.find("Python"))     # -1 (não encontrado)

frase2 = "Laennder, Cubo Três, Laennder"
print(frase2.find("Laennder", 1)) # 18

# rfind()
# Definição
# Busca a substring e retorna o índice da última ocorrência. Retorna -1 se não for encontrada.
#
# Sintaxe
# string.rfind(value[, start[, end]])
#
# Parâmetros
# value: substring a ser buscada.
# start (opcional)
# end (opcional)
# Exemplos
texto = "banana"
print(texto.rfind("a"))       # 5
print(texto.rfind("an"))      # 3
print(texto.rfind("x"))       # -1
print(texto.rfind("a", 0, 3)) # 1 (entre índices 0 e 2)

frase = "Cubo Três, Laennder, Cubo Três"
print(frase.rfind("Cubo Três")) # índice da última ocorrência

# index()
# Definição
# Retorna o índice da primeira ocorrência de uma substring, lançando ValueError se não encontrada. É semelhante a find(), porém gera exceção ao invés de retornar -1.
#
# Sintaxe
# string.index(value[, start[, end]])
#
# Parâmetros
# value: substring a ser encontrada.
# start (opcional)
# end (opcional)
# Exemplos
texto = "Python na Cubo Três"
print(texto.index("Cubo"))  # 10

try:
    print(texto.index("Laennder"))
except ValueError:
    print("Substring não encontrada!")

print(texto.index("n", 2, 8))  # 5

# rindex()
# Definição
# Similar a rfind(), mas retorna ValueError se a substring não for encontrada.
#
# Sintaxe
# string.rindex(value[, start[, end]])
#
# Parâmetros
# value
# start (opcional)
# end (opcional)
# Exemplos
texto = "banana"
print(texto.rindex("a"))   # 5

try:
    print(texto.rindex("x"))
except ValueError:
    print("Substring não encontrada!")

frase = "Cubo Três e Cubo Três"
print(frase.rindex("Cubo"))  # índice da última ocorrência de "Cubo"

# startswith()
# Definição
# Retorna True se a string começar com o valor especificado.
#
# Sintaxe
# string.startswith(value[, start[, end]])
#
# Parâmetros
# value: substring a verificar.
# start (opcional): índice inicial.
# end (opcional): índice final.
# Exemplos
texto = "Cubo Três e Laennder"
print(texto.startswith("Cubo"))   # True
print(texto.startswith("Laennder"))  # False

saudacao = "Olá, Mundo!"
print(saudacao.startswith("Olá"))   # True
print(saudacao.startswith(",", 3))   # True (verifica a partir do índice 3)

# endswith()
# Definição
# Retorna True se a string terminar com o valor especificado.
#
# Sintaxe
# string.endswith(value[, start[, end]])
#
# Parâmetros
# value: substring a verificar.
# start (opcional): índice inicial para verificação.
# end (opcional): índice final para verificação.
# Exemplos
arquivo = "relatorio.pdf"
print(arquivo.endswith(".pdf"))   # True

banner = "Escola de Dados - Cubo Três"
print(banner.endswith("Cubo Três"))         # True
print(banner.endswith("Dados", 0, 17))      # True

saudacao = "Olá, Mundo!"
print(saudacao.endswith("!"))               # True

# endswith()
# Definição
# Retorna True se a string terminar com o valor especificado.
#
# Sintaxe
# string.endswith(value[, start[, end]])
#
# Parâmetros
# value: substring a verificar.
# start (opcional): índice inicial para verificação.
# end (opcional): índice final para verificação.
# Exemplos
arquivo = "relatorio.pdf"
print(arquivo.endswith(".pdf"))   # True

banner = "Escola de Dados - Cubo Três"
print(banner.endswith("Cubo Três"))         # True
print(banner.endswith("Dados", 0, 17))      # True

saudacao = "Olá, Mundo!"
print(saudacao.endswith("!"))               # True

# format_map()
# Definição
# Similar a format(), mas recebe um dicionário (ou map) para formatar a string com chaves correspondentes.
#
# Sintaxe
# string.format_map(mapping)
#
# Parâmetros
# mapping: dicionário ou objeto que contenha as chaves de substituição.
#
# Exemplos
dados = {"nome": "Cubo Três", "curso": "Escola de Dados"}
frase = "Bem-vindo ao {nome}, parte da {curso}!"
print(frase.format_map(dados))

class Map(dict):
    def __missing__(self, key):
        return "N/A"

map_test = Map(nome="Laennder")
print("Olá, {nome} e {amigo}!".format_map(map_test))
# amigo não está definido, retorna "N/A"

coordenadas = {"x": 10, "y": 20}
print("Coordenadas: x={x}, y={y}".format_map(coordenadas))


# replace()
# Definição
# Retorna uma string onde um valor especificado é substituído por outro valor especificado.
#
# Sintaxe
# string.replace(old, new[, count])
#
# Parâmetros
# old: substring a ser substituída.
# new: nova substring.
# count (opcional): número máximo de substituições.
# Exemplos
texto = "Olá, Mundo! Olá, Mundo!"
print(texto.replace("Mundo", "Cubo Três"))
# "Olá, Cubo Três! Olá, Cubo Três!"

print(texto.replace("Olá", "Laennder", 1))
# Substitui apenas a primeira ocorrência

frase = "Python na Escola de Dados"
print(frase.replace("Escola de Dados", "Laennder"))

cores = "vermelho, vermelho, azul"
print(cores.replace("vermelho", "amarelo", 1))

# translate()
# Definição
# Retorna a string traduzida de acordo com a tabela passada, normalmente gerada por maketrans().
#
# Sintaxe
# string.translate(table)
#
# Parâmetros
# table: tabela de tradução obtida via str.maketrans() ou dicionário.
#
# Exemplos
tabela = str.maketrans("aeiou", "12345")
texto = "cubo tres laennder"
print(texto.translate(tabela)) # "c5b4 tr2s l13nnd2r"

# Exemplo com remoção de caracteres
tabela2 = str.maketrans("", "", "!")
saudacao = "Olá, Mundo!!!"
print(saudacao.translate(tabela2)) # "Olá, Mundo"

dic = {ord('C'): 'K', ord('T'): 'D'}
print("Cubo Três".translate(dic))  # "Kubo Drês"

# maketrans()
# Definição
# Retorna uma tabela de tradução que pode ser usada pelo método translate().
#
# Sintaxe
# str.maketrans(x, y=None, z=None)
#
# Parâmetros
# Se x e y forem strings de mesmo tamanho, cria-se um mapeamento de cada caractere de x para o caractere em y.
# z é uma string com caracteres a serem removidos.
# Também pode receber um dicionário de mapeamentos.
# Exemplos
# Exemplo 1: x e y
tabela = str.maketrans("abc", "xyz")
texto = "abcCuboTrês"
print(texto.translate(tabela))  # "xyzCuxoTrês"

# Exemplo 2: usando z para remover
tabela2 = str.maketrans("", "", " ")
texto2 = "Olá, Mundo! Cubo Três"
print(texto2.translate(tabela2)) # "Olá,Mundo!CuboTrês"

# Exemplo 3: dicionário de mapeamento
tabela3 = str.maketrans({ord('E'): '3', ord('D'): 'd'})
print("EscolaDeDados".translate(tabela3)) # "3scoladedados"

# Exemplo 4
tabela4 = str.maketrans("Cubo", "Data")
print("Cubo Três!".translate(tabela4))     # "Data Três!"

# 6. Divisão e União
# split()
#
# Definição
# Divide a string em uma lista, usando um separador especificado. Se não for passado um separador, divide pelos espaços em branco.
#
# Sintaxe
# string.split(separator=None, maxsplit=-1)
#
# Parâmetros
# separator (opcional): separador.
# maxsplit (opcional): número máximo de divisões.
# Exemplos
frase = "Cubo Três Escola de Dados"
print(frase.split())             # ['Cubo', 'Três', 'Escola', 'de', 'Dados']

cores = "vermelho,azul,amarelo"
print(cores.split(","))          # ['vermelho', 'azul', 'amarelo']

texto = "banana"
print(texto.split("a"))          # ['', 'b', 'n', 'n', '']

nome = "Laennder Cubo Três"
print(nome.split(maxsplit=1))    # ['Laennder', 'Cubo Três']

# rsplit()
# Definição
# Divide a string a partir do final, retornando uma lista de substrings. É semelhante a split(), mas pode ser útil quando se especifica o parâmetro maxsplit.
#
# Sintaxe
# string.rsplit(separator=None, maxsplit=-1)
#
# Parâmetros
# separator (opcional): delimitador (padrão é espaço).
# maxsplit (opcional): número máximo de divisões.
# Exemplos
texto = "Cubo Três Laennder Escola de Dados"
print(texto.rsplit())              # ['Cubo', 'Três', 'Laennder', 'Escola', 'de', 'Dados']
print(texto.rsplit(maxsplit=2))    # ['Cubo Três Laennder', 'Escola', 'de Dados']

lista_cores = "vermelho,azul,amarelo,verde"
print(lista_cores.rsplit(",", 1))  # ['vermelho,azul,amarelo', 'verde']
print(lista_cores.rsplit(",", 2))  # ['vermelho,azul', 'amarelo', 'verde']





# String
nome = "Rogerio"
# Toda String é uma Lista
nomeCompleto = """
Meu nome é
Rogerio 
da Silva 
Matos
"""
print(nomeCompleto)

nomes = ["Rogerio", "Alicya" , "Maria", "Matos", "Santos"]
for i in sorted(nomes):
    print(i)


