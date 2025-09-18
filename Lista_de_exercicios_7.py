#1. Um problema comum em bioinformática estrutural é a comparação entre estruturas moleculares.
#Nesse exercício, alinhamos estruturalmente dois resíduos de glicina (amarela e roxa - Figura 1) e
#apresentamos as coordenadas tridimensionais (x, y, z) (Tabelas 1 e 2). Considerando estas tabelas de
#coordenadas x, y, z dos átomos dos dois resíduos de glicina, calcule o RMSD (Root Mean Square Deviation)
#entre elas segundo a equação:

#Equação 1 - RMSD (Considere N=4 que é o número de átomos).
'''
ATOMO x y z
N 108.304 100.827 67.992
CA 108.477 100.389 69.362
C 109.907 100.555 69.817
O 110.821 100.799 69.027

ATOMO x y z
N 107.670 101.359 70.074
CA 108.477 100.389 69.362
C 109.513 101.011 68.450
O 110.667 100.572 68.425
'''

#2. Em biologia molecular, o conteúdo GC (guanina e citosina) é o percentual de bases nitrogenadas em uma
#molécula de DNA ou RNA que são guanina ou citosina (dentre as quatro bases possíveis). Para as seguintes
#sequências calcule usando os operadores vistos em aula o percentual de conteúdo GC, imprimindo os resultados:
Sequência_A= "ATGATCTCGTAATTAACCGGAATTTTGGGCC"
#Saída esperada: 41.93
print("Sequencia A")
percentualA = (Sequência_A.count("GC") / len(Sequência_A)) * 100
print(f"Percentual: {percentualA}")

Sequência_B = "GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA"
#Saída esperada: 44.44
print("Sequencia B")
PercentualB = (Sequência_B.count("GC") / len(Sequência_B)) * 100
print(f"percentual B {PercentualB}")