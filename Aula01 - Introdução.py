# 1. O que é Python
# Python é uma linguagem de programação popular, criada por Guido van Rossum e lançada em 1991.
# la é conhecida por sua simplicidade, legibilidade e versatilidade, sendo utilizada em diversas áreas da tecnologia.

# Para que Python é utilizado?
# Python é aplicado em vários contextos, como:
#
# Análise matemática e manipulação de dados
# Desenvolvimento web (lado do servidor)
# Desenvolvimento de software
# Scripting e automação de sistemas

# O que é possível fazer com Python?
# Com Python, você pode:
#
# Integrar sistemas e automatizar processos
# Conectar-se a bancos de dados e manipular arquivos
# Criar aplicações web robustas e interativas
# Desenvolver protótipos rapidamente ou construir aplicações para produção
# Por que escolher Python?
# Python é uma excelente escolha porque:
#
# Funciona em diversas plataformas, como Windows, macOS, Linux e Raspberry Pi
# Possui uma sintaxe simples e intuitiva, que se assemelha à linguagem inglesa
# Permite escrever código de forma mais concisa do que muitas outras linguagens
# É interpretada, o que possibilita testar e prototipar rapidamente
# Suporta múltiplos paradigmas de programação: procedural, orientada a objetos e funcional
# Informações Importantes
# A versão mais recente amplamente utilizada é o Python 3, que traz diversas melhorias e funcionalidades modernas.
# Embora o Python 2 ainda seja encontrado em alguns projetos, ele não recebe novas funcionalidades, apenas atualizações de segurança.
#
# Você pode escrever código Python em um simples editor de texto ou usar ambientes de desenvolvimento integrados (IDEs) como Thonny,
# PyCharm, NetBeans ou Eclipse, que ajudam a gerenciar projetos maiores.

# Sintaxe do Python
# Python foi projetado com foco na legibilidade. Alguns aspectos importantes da sua sintaxe incluem:
#
# Uso de quebras de linha para finalizar comandos, sem necessidade de ponto e vírgula.
# Indentação obrigatória para definir blocos de código, em vez de chaves ({}) usadas em outras linguagens.
# Estrutura de código inspirada na linguagem natural e na matemática, facilitando a compreensão.
# Essa combinação de simplicidade, clareza e flexibilidade faz do Python uma ótima escolha tanto para iniciantes quanto para desenvolvedores experientes.

# 2. Instalação e Verificação
# Instalação e Verificação
# Muitos computadores já possuem Python instalado. Para verificar no Windows, abra o cmd.exe e execute:
#
# python --version
# Se não estiver instalado, você pode baixá-lo gratuitamente em: python.org.

# Seu Primeiro Programa
# Para executar um programa Python, usando o IDLE, crie um arquivo com a extensão .py e escreva o código.
# Por exemplo, crie um arquivo chamado Exemplo01.py com o conteúdo:
print("Olá, Mundo!")

# Em seguida, execute o código, clicando em Run ou pressionando F5. A saída deverá ser:

# Olá, Mundo!

# Você também pode utilizar interpretadores online para testar seu código sem instalar nada.

# Executando o Interpretador Python

# Para testar comandos rapidamente, execute o Python diretamente na linha de comando:

# python
#
# Caso o comando python não funcione, tente:
#
# py
#
# Para sair do interpretador, digite:
#
# exit()

# 3. Sintaxe do Python
# Execução de Código
# Você pode escrever código Python diretamente no interpretador ou em arquivos com a extensão .py e executá-los na linha de comando. Exemplo simples:

print("Olá Mundo!")

# Indentação
# Em Python, a indentação é fundamental para definir blocos de código. Ao contrário de outras linguagens que utilizam chaves,
# Python utiliza espaços em branco para delimitar blocos.
#
# Exemplo correto:

if 7 > 3:
    print("Sete é maior que três!")

# Exemplo com erro de indentação:

if 7 > 3:
print("Sete é maior que três!")

# 4. Comentários em Python
# Comentários são utilizados para explicar o código e são ignorados pelo interpretador. Eles começam com o símbolo #.
#
# Exemplo de comentário:
# Este é um comentário
print("Olá, Mundo!")  # Comentário após o código

# Para comentários de várias linhas, utilize o símbolo # em cada linha ou uma string multilinha não atribuída:

"""
Este é um comentário
de várias linhas.
"""
print("Olá, Mundo!")

 # 5. Variáveis em Python
# Variáveis são contêineres para armazenar dados. Em Python, não é necessário declarar o tipo da variável; ele é definido automaticamente quando um valor é atribuído.

# Exemplo:

idade = 37
nome = "Laennder"
print(idade)
print(nome)

# Você pode converter tipos (casting) usando funções como str(), int() e float():

x = str(3)    # x será '3'
y = int(3)    # y será 3
z = float(3)  # z será 3.0

# Para verificar o tipo de uma variável, utilize a função type():

x = 5
print(type(x))

# Nomes de Variáveis

# Regras para nomes de variáveis:
#
# Devem iniciar com uma letra ou underscore (_).
# Não podem começar com números.
# Podem conter apenas caracteres alfanuméricos e underscores.
# São case-sensitive (diferenciam maiúsculas de minúsculas).
# Não podem ser palavras reservadas do Python.

# Exemplos de nomes válidos:

meunome = "Laennder"
meu_nome = "Laennder"
_meu_nome = "Laennder"
meuNome = "Laennder"
MEUNOME = "Laennder"
meunome2 = "Laennder"

# Exemplos de nomes inválidos:

# 2meunome = "Laennder"
# meu-nome = "Laennder"
# meu nome = "Laennder"

# Atribuição Múltipla
# Python permite atribuir valores a várias variáveis em uma única linha:

x, y, z = "Laennder", "Matheus", "Ketlyn"
print(x)
print(y)
print(z)

# Ou atribuir o mesmo valor a múltiplas variáveis:

x = y = z = "Matheus"
print(x)
print(y)
print(z)

# É possível também desempacotar coleções:

carros = ["Gol", "Onix", "Creta"]
x, y, z = carros
print(x)
print(y)
print(z)

# 6. Saída de Dados
# A função print() é utilizada para exibir variáveis e mensagens na tela.

# Exemplo usando vírgulas (que permite diferentes tipos de dados):
x = "Python"
y = "é"
z = "incrível"
print(x, y, z)

# Exemplo de concatenação de strings:

x = "Cubo Três "
y = "é a "
z = "melhor Escola!"
print(x + y + z)

# Ao combinar strings e números, separe-os por vírgula:
idade = 37
nome = "Laennder"
print(nome, idade)

# É possível utilizar f-strings para criar máscaras nas saídas de dados:
idade = 37
nome = "Laennder"
print(f"Meu nome é {nome} e minha idade é {idade}")

# Por padrão, a função print gera uma quebra de linha ao final, mas é possível substituir esse comportamento.
idade = 37
nome = "Laennder"
print(f"Meu nome é {nome}", end=" ")
print(f"e minha idade é {idade}", end="\n")

# 7. Tipos de Dados em Python
# Python possui diversos tipos de dados embutidos. Nesta aula focamos em 4 tipos primitivos.
#
# Textos: str
# Números: int, float
# Booleanos: bool
# Para obter o tipo de um objeto, utilize a função type():
idade = 37
print(type(idade))

# Ao atribuir um valor a uma variável, o tipo é definido automaticamente:

x = "Olá Mundo"   # str
x = 20            # int
x = 20.5          # float
x = True          # bool

# Para definir explicitamente um tipo, use as funções construtoras:

x = str("Olá Mundo")
x = int(20)
x = float(20.5)
