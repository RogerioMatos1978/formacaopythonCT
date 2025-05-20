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


