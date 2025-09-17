#1 criar uma tupla com as letras A, C, D, E, F, G, H, I, K, L, M, N, P, Q, R, S, T, V, W, Y 
Letras = ('A', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'W', 'Y')
print("Exercício 1")
#a- Conte e imprima o número de elementos contidos na tupla criada.
print(f"letra a:\n{len(Letras)}")

#b- Verifique e imprima se o aminoácido Serina (S) pertence à tupla. 
print("letra b:")
if "S" in Letras:
    print("pertence")
if not "S" in Letras:
    print("nao pertence")

#c-  Crie uma segunda tupla contendo os elementos Prolina (P), Glicina (G), Asparagina (N), Tirosina (Y), Valina (V) e Triptofano (W).
SegundaTupla = ('P', 'G', 'N', 'Y', 'V', 'W')

#d- Some as tuplas construídas e imprima o resultado.
TerceiraTupla = Letras + SegundaTupla
print(f"letra d:\n{TerceiraTupla}")

#e- Conte a ocorrência dos elementos Glicina (G), Asparagina (N) e Cisteína (C)
#Como não sei qual das duas tuplas era pra contar, fiz as duas, sendo a primeira a versão sem a adição e a segunda com.
print("contagem do G")
print(Letras.count('G'))
print(TerceiraTupla.count('G'))

print("contagem do N")
print(Letras.count('N'))
print(TerceiraTupla.count('N'))

print("contagem do C")
print(Letras.count('C'))
print(TerceiraTupla.count('C'))

#f- Retorne a posição do primeiro elemento Asparagina (N).
print("letra f")
print(Letras.index('N'))
print(TerceiraTupla.index('N'))

#g- Retorne os 5 últimos elementos da tupla.
#Novamente, como não sei qual das tuplas, fiz das duas
print("letra G")
print(Letras[-5::])
print(TerceiraTupla[-5::])