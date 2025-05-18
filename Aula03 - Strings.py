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

def Letras(letras):
    s = 'enter'
    while s != "":
        s = input("Letra: ")
        if s != "":
            ch = s[0]
            letras.append(ch)
    return
def Inverte(letras, inverso):
    n = len(letras)
    for i in range(n-1,-1,-1):
        inverso.append(letras[i])
    return

letras = []
inverso = []
Letras(letras)
print(letras)
Inverte(letras, inverso)
print(inverso)
