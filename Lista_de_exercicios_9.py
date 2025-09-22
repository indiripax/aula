#1. Escreva um programa que calcule e escreva a tabela de graus Centígrados em função dos graus Farenheit que variem entre 1 e 150 de 1 em 1 conforme a fórmula a seguir
print("Exercício 1")

for i in range(1, 151):
    F = i
    Celcios = 5/9*(F - 32)
    print(f"{F}°F = {Celcios}°C")

#2. Utilizando as estruturas de repetição, verifique se as seguintes sequências são uma sequência de 
DNA = ("A", "G", "T", "C")
RNA = ("U", "C", "A", "G")
PROTEINA = ("A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y")

#ou nenhuma delas (nesse caso, imprima as letras que não fazem parte do alfabeto):

s1 = "ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN"
s2 = "TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT"
s3 = "ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN"

print("Exercicio 2")


#3. Utilizando as estruturas de repetição, gere e imprima a sequência complemento reverso da seguinte sequência de DNA:
print("Exercício 3")
DNA_ = "TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT"
DNA_COMPLEMENTO = ""
for letra in DNA_:
    if letra == "A":
            DNA_COMPLEMENTO += "T"
    elif letra == "T":
        DNA_COMPLEMENTO += "A"
    elif letra == "C":
        DNA_COMPLEMENTO += "G"
    elif letra == "G":
        DNA_COMPLEMENTO += "C"
print(DNA_COMPLEMENTO[::-1])

#4.Escreva um programa que calcule o fatorial de um número recebido como entrada. Lembre-se que o fatorial de um número é igual ao número multiplicado n sucessivamente por n-1, n-2, .. 1. 
#Exemplo: fat(6) = 6 x 5 x 4 x 3 x 2 x 1 = 720.
print("Exercício 4:")

numero = int()
fatorial = 1
for i in range(1, numero + 1):
    fatorial *= i
resultado = print(f"O fatorial de {numero} é {fatorial}.")

#5. Escreva um programa que liste a tabuada (produtos) dos números de 1 a 15.

print("Exercício 5:")

for i in range(1, 16):
    print(f"Tabuada do {i}:")
    for j in range(1, 16):
        print(f"{i} x {j} = {i * j}")
    print()

#6. Considerando a seguinte sequência e tabela de massas (Tabela 1), escreva um programa em Python que calcule a massa molar da sequência:

print("Exercício 6")

Sequencia = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

Massa_aminoacidos = {"A":(71.03711), "C":(103.00919), "D":(115.02694), "E":(129.04259), "F":(147.06841), "G":(57.02146), "H":(137.05891), "I":(113.08406), "K":(128.09496), "L":(113.08406), "M":(131.04049), "N":(114.04293), "P":(97.05276), "Q":(128.05858), "R":(156.10111), "S":(87.03203), "T":(101.04768), "V":(99.06841), "W":(186.07931), "Y":(163.06333)}

sequencia = list(Sequencia)

soma = 0

for aminoacido in sequencia:
    soma += Massa_aminoacidos[aminoacido]

print(f"A massa molar da sequência é {soma:.5f}")

#7. Considerando a Tabela 2 que contem dados de defensinas de plantas, obtenha / calcule e imprima:

pdb = {"3PSM":(1, "A,B", "UniProt", "Q6B519", "KTCENLADTFRGPCFTDGSCDDHCKNKEHLIKGRCRDDFRCWCTRNC", 47, "polipeptide(L)", 5.511),\
    "2NY9": (1, "X", "Uniprot", "Q17027", "ATCDLASGFGVGSSLCAAHCLVKGYRGGYCKNKICHCRDKF", 41, "polypeptide(L)", 4.349),/
    "2NY8": (1, "X", "Uniprot", "Q17027", "ATCDLASGFGVGSSLCAAHCIARRYRGGYCNSKAVCVCRN", 40, "polypeptide(L)", 4.148),/
    "2NZ3": (1, "A", "UniProt", "Q17027", "ATCDLASIFNVNHALCAAHCIARRYRGGYCNSKAVCVCRN", 40, "polypeptide(L)", 4.353),/
    "2E3G": (1, "A", "UniPort", "Q17027", "ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN", 40, "polypeptide(L)", 4.525),/
    "2E3F": (1, "A", "UniPort", "Q17027", "ATCDLASFSSQWVTPNDSLCAAHCIARRYRGGYCNGKRVCVCR", 43, "polypeptide(L)", 4.747)/
    "2E3E": (1, "A", "UniPort", "Q17027", "ATCDLASFSSQWVTPNDSLCAAHCLVKGYRGGYCKNKICHCRDKF", 45, "polypeptide(L)", 5.007)}

#A) a menor sequência e seu comprimento
#B) a maior sequência e seu comprimento
#C) a média entre os comprimentos das sequências
#D) a mediana entre os comprimentos das sequências

#8. Considerando as assinaturas moleculares (fingerprints) hipotéticas das tabelas abaixo, calcule a distância de Tanimoto


batata