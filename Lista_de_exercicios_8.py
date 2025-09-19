#Para os exercícios desta lista, considere a seguinte lista de sequências e faça programas em Python que execute as tarefas descritas abaixo:

Sequencia_A = "LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK"
Sequencia_B = "KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS"
Sequencia_C = "CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR"

#1. Imprima apenas as sequências com 80 ou mais aminoácidos.
print("1:")

if len(Sequencia_A) >= 80:
    print(f"Sequência_A")

if len(Sequencia_B) >= 80:
    print(f"Sequência_B")

if len(Sequencia_C) >= 80:
    print(f"Sequência_C")

#2. Imprima apenas as sequências cujo tamanho seja maior que a média de tamanho das sequências.
print("2:")

media = (len(Sequencia_A) + len(Sequencia_B) + len(Sequencia_C)) / 3

if len(Sequencia_A) > media:
    print(F"Sequência A é maior que a média")
if len(Sequencia_B) > media:
    print(f"Sequencia B é maior que a média")
if len(Sequencia_C) > media:
    print(f"Sequencia C é maior que a média")
else:
    print("Nenhuma sequencia é maior que a média")

#3. Imprima apenas as sequências que possuam pelo menos uma histidina (H) e nenhuma prolina (P).
print("3:")

if "H" in Sequencia_A and "P" not in Sequencia_A:
    print(f"Sequência_A")
if "H" in Sequencia_B and "P" not in Sequencia_B:
    print(f"Sequência_B")
if "H" in Sequencia_C and "P" not in Sequencia_C:
    print(f"Sequência_C")
else:
    print("nenhuma das sequencias correspondem aos requisitos")

#4. Identifique e imprima a maior dentre as três sequências a seguir.
print("4:")

AG = len(Sequencia_A)
BG = len(Sequencia_B)
CG = len(Sequencia_C)

if len(Sequencia_A) > len(Sequencia_B) and len(Sequencia_A) > len(Sequencia_C):
    print("Sequência A")
elif len(Sequencia_B) > len(Sequencia_A) and len(Sequencia_B) > len(Sequencia_C):
    print("Sequência B")
else:
     print("Sequência C")


#5. Imprima as três sequências em ordem crescente de tamanho.
print("5:")

