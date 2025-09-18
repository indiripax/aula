#1. Escreva um programa que calcule e escreva a tabela de graus Centígrados em função dos graus Farenheit que variem entre 1 e 150 de 1 em 1 conforme a fórmula a seguir
print("Exercício 1")
F = 100
Celcios = 5/9*(F - 32)

print(Celcios)

#2. Utilizando as estruturas de repetição, verifique se as seguintes sequências são uma sequência de 
DNA = {"A", "G", "T", "C"}
RNA = {"U", "C", "A", "G"}
PROTEÍNA = {"A", "C", "D", "E", "F", "G", "H", "I", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "Y"} 

#ou nenhuma delas (nesse caso, imprima as letras que não fazem parte do alfabeto):
s1 = "ATCDLASKWNWNHTLCAAHCIARRYRGGYCNSKAVCVCRN"
s2 = "TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT"
s3 = "ATCBDLASKWXWNHTLCAAHCIARRYRGGYCNSJAVCVCRN"

#3. Utilizando as estruturas de repetição, gere e imprima a sequência complemento reverso da seguinte sequência de DNA:
print("Exercício 3")
DNA = "TATTAACCGGGTTTAAACTAGCATGCATGATTAACCAGTACATCTTTT"
DNA_COMPLEMENTO = ""
for letra in DNA:
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

#5. Escreva um programa que liste a tabuada (produtos) dos números de 1 a 15.

#6. Considerando a seguinte sequência e tabela de massas (Tabela 1), escreva um programa em Python que calcule a massa molar da sequência:
#VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL

#7. Considerando a Tabela 2 que contem dados de defensinas de plantas, obtenha / calcule e imprima:

#A) a menor sequência e seu comprimento
#B) a maior sequência e seu comprimento
#C) a média entre os comprimentos das sequências
#D) a mediana entre os comprimentos das sequências

#8. Considerando as assinaturas moleculares (fingerprints) hipotéticas das tabelas abaixo, calcule a distância de Tanimoto
