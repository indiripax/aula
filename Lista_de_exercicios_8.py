#Para os exercícios desta lista, considere a seguinte lista de sequências e faça programas em Python que execute as tarefas descritas abaixo:

Sequência_A = "LRSSSQNSSDKPVAHVVANHQVEEQLEWLSQRANALLANGMDLKDNQLVVPADGLYLVYSQVLFKGQGCPDYVLLTHTVSLRSSSDK"
Sequência_B = "KPAAHLIGDPSKQNSLLWRANTDRAFLQDGFSLSNNSLLVPTSGIYFVYSQVVFSGKAYSPKATSSPLYLAHEVQLFSS"
Sequência_C = "CPQGKYIHPQNNSICCTKCHKGTYLYNDCPGPGQDTDCRECESGSFTASENHLRHCLSCSKCRKEMGQVEISSCTVDRDTVCGCR"

#1. Imprima apenas as sequências com 80 ou mais aminoácidos.
print("1:")

if len(Sequência_A) >= 80:
    print(f"Sequência_A")

if len(Sequência_B) >= 80:
    print(f"Sequência_B")

if len(Sequência_C) >= 80:
    print(f"Sequência_C")

#2. Imprima apenas as sequências cujo tamanho seja maior que a média de tamanho das sequências.
print("2:")

media = (len(Sequência_A) + len(Sequência_B) + len(Sequência_C)) / 3

if len(Sequência_A) > media:
    print(F"Sequência A é maior que a média")
if len(Sequência_B) > media:
    print(f"Sequencia B é maior que a média")
if len(Sequência_C) > media:
    print(f"Sequencia C é maior que a média")
else:
    print("Nenhuma sequencia é maior que a média")

#3. Imprima apenas as sequências que possuam pelo menos uma histidina (H) e nenhuma prolina (P).
print("3:")

if "H" in Sequência_A and "P" not in Sequência_A:
    print(f"Sequência_A")
if "H" in Sequência_B and "P" not in Sequência_B:
    print(f"Sequência_B")
if "H" in Sequência_C and "P" not in Sequência_C:
    print(f"Sequência_C")
else:
    print("nenhuma das sequencias correspondem aos requisitos")

#4. Identifique e imprima a maior dentre as três sequências a seguir.
print("4:")

AG = len(Sequência_A)
BG = len(Sequência_B)
CG = len(Sequência_C)

#5. Imprima as três sequências em ordem crescente de tamanho.
print("5:")

