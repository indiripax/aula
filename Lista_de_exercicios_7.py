#1. Um problema comum em bioinformática estrutural é a comparação entre estruturas moleculares.
#Nesse exercício, alinhamos estruturalmente dois resíduos de glicina (amarela e roxa - Figura 1) e
#apresentamos as coordenadas tridimensionais (x, y, z) (Tabelas 1 e 2). Considerando estas tabelas de
#coordenadas x, y, z dos átomos dos dois resíduos de glicina, calcule o RMSD (Root Mean Square Deviation)
#entre elas segundo a equação:

#Equação 1 - RMSD (Considere N=4 que é o número de átomos).

Glicina_1 = { "N":(108.304, 100.827, 67.992), "CA":(108.477, 100.389, 69.362), "C":(109.907, 100.555, 69.817), "O":(110.821, 100.799, 69.027)}

Glicina_2 = { "N":(107.670, 101.359, 70.074), "CA":(108.477, 100.389, 69.362), "C":(109.513, 101.011, 68.450), "O":(110.667, 100.572, 68.425)}

print("Exercício 1")

soma = 0

for key in Glicina_1:
    soma += (Glicina_1[key][0]-Glicina_2[key][0])**2 + (Glicina_1[key][1]-Glicina_2[key][1])**2 + (Glicina_1[key][2]-Glicina_2[key][2])**2
    
RMSD = ((1/len(Glicina_1))* soma )**0.5
print(f"RMSD= {RMSD}")

#2. Em biologia molecular, o conteúdo GC (guanina e citosina) é o percentual de bases nitrogenadas em uma
#molécula de DNA ou RNA que são guanina ou citosina (dentre as quatro bases possíveis). Para as seguintes
#sequências calcule usando os operadores vistos em aula o percentual de conteúdo GC, imprimindo os resultados:
print("Exercício 2:")

Sequência_A = "ATGATCTCGTAATTAACCGGAATTTTGGGCC"
#Saída esperada: 41.93
print("Sequencia A")
percentual = ((Sequência_A.count("G") + Sequência_A.count("C")) / len(Sequência_A)) * 100
print(f"Percentual: {percentual:.2f}")

Sequência_B= "GGCCTTAAGTTTAACCCGGAATTTAAAGGCCCCAAA"
#Saída esperada: 44.44
print("Sequencia B")
percentuals = ((Sequência_B.count("G") + Sequência_B.count("C")) / len(Sequência_B)) * 100
print(f"Percentual: {percentuals:.2f}")