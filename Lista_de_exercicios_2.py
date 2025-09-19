#Exercicio 1
TNF = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

print("Exercício 1")
#a- Retorne o tamanho da sequência.
print(f"letra a:\n{len(TNF)}")

#b- Realize a contagem da ocorrência de um sequência de leucinas (LL).
leucina= TNF.count("LL")
print(f"letra b:\n{leucina}")

#c- Encontre na sequência as posições ocupadas por duas glicinas (GG) e duas argininas (RR).
print("letra c:")
print(f"Posição GG: {TNF.index("GG")}")

print(f"Posição de RR: {TNF.index("RR")}")

#d- Retorne os 100 primeiros aminoácidos da sequência.
print(f"Letra d:\n{TNF[0:99]}")

#e- Substitua o trecho da sequência com a ocorrência de 3 serinas e 1 arginina (SSSR) por alaninas.
NovoTNF = TNF.replace("SSSR", "AAAA")
print(f"letra e:\n{NovoTNF}")

#f- Quebre a sequência no local onde a substituição foi realizada.
print(f"letra f:\n{NovoTNF.split("AAAA")}")

#Exercicio 2
print("Exercício 2")
text= "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome."

#a-  Passe todo o texto para letras maiúsculas. 
maiusculo = text.upper()
print(f"letra a:\n{maiusculo}")

#b- Passe todo o texto para letras minúsculas.
minusculo = text.lower()
print(f"letra b\n{minusculo}")

#c- Passe cada primeira letra de palavra em maiúsculo.
maiusculo1 = text.title()
print(f"letra c:\n{maiusculo1}")

#d- Transforme as letras maiúsculas em minúsculas e vice-versa.
letrasmm = text.swapcase()
print(f"letra d:\n{letrasmm}")

#Exercício 3
print("Exercício 3")

insulin_signal = "MALWMRLLPLLALLALWGPDPAAA"

#a- Retorne o tamanho da sequência apresentada.
print(f"letra A:\n{len(insulin_signal)}")

#b- Quebre a sequência no trecho “LLALLALWG".
print(f"letra b:\n{insulin_signal.split("LLALLALWG")}")

#c- Concatene as sequências resultantes obtendo a seguinte sequência final MALWMRLLPPDPAAA.

#aqui há duas maneiras de se fazer:
#da maneira onde eu crio a variável de split:
insulin_signal_split = insulin_signal.split("LLALLALWG")
#e rodando:
# SequenciaFinal = insulin_signal.split("LLALLALWG")[0]+insulin_signal.split("LLALLALWG")[1]

#ou da seguinte maneira:
SequenciaFinal = insulin_signal_split[0] + insulin_signal_split[1]
print(f"letra c:\n{SequenciaFinal}")

#d- Substitua o trecho "DPAAA" por “LLALL”.
substituicao = (insulin_signal.replace("DPAAA", "LLALL"))
print(f"letra d:\n{substituicao}")

#4- Com base na sequência de DNA GATGGAACTTGACGTAAACCTATATT retorne a sequência de RNA correspondente sendo a mesma GAUGGAACUUGACGUAAACCUAUAUU
DNA = "GATGGAACTTGACGTAAACCTATATT"

RNATU = DNA.replace("T", "U")
print(f"Exercício 4\n{RNATU}")

#porém também entendi que 
RNA = ""
for LetraRNA in DNA:
    if LetraRNA == "G":
        RNA += "C"
    elif LetraRNA == "A":
        RNA += "U"
    elif LetraRNA == "C":
        RNA += "G"
    elif LetraRNA == "T":
        RNA += "A"
print(f"Exercício 4 outro entedimento\n{RNA}")
