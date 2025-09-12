#Exercicio 1
TNF = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

#a- Retorne o tamanho da sequência.
print(len(TNF))

#b- Realize a contagem da ocorrência de um sequência de leucinas (LL).
leucina= TNF.count("LL")
print(leucina)

#c- Encontre na sequência as posições ocupadas por duas glicinas (GG) e duas argininas (RR).
tam = len(TNF)
for i in (0,tam -1):
    if TNF[i] == "G":
        if TNF[i+1] == "G":
            print(i)

for i in (0, tam -1)
    if TNF[i] == "R"
        if TNF[i+1] =="r"
            print(i)

#d- Retorne os 100 primeiros aminoácidos da sequência.
print(TNF[0:99])

#e- Substitua o trecho da sequência com a ocorrência de 3 serinas e 1 arginina (SSSR) por alaninas.


#f- Quebre a sequência no local onde a substituição foi realizada.

#Exercicio 2
text= "As proteínas são cadeias polipeptídicas formadas pela ligação peptídica entre resíduos de aminoácidos. Existem 20 tipos de aminoácidos comumente encontrados nos seres vivos. A esses aminoácidos, foram atribuídas abreviações de 3 letras e símbolos de 1 letra. As abreviações de 3 letras são bastante evidentes consistindo nas três primeiras letras do se nome."

#a-  Passe todo o texto para letras maiúsculas. 
maiusculo = text.upper()
print(maiusculo)

#b- Passe todo o texto para letras minúsculas.
minusculo = text.lower()
print(minusculo)

#c- Passe cada primeira letra de palavra em maiúsculo.
maiusculo1 = text.title()
print(maiusculo1)

#d- Transforme as letras maiúsculas em minúsculas e vice-versa.
letrasmm = text.

#3
insulin_signal = "MALWMRLLPLLALLALWGPDPAAA"

#a- Retorne o tamanho da sequência apresentada.
print(len(insulin_signal))

#b- Quebre a sequência no trecho “LLALLALWG".


#c- Concatene as sequências resultantes obtendo a seguinte sequência final MALWMRLLPPDPAAA.
SequenciaFinal = "MALWMRLLPPDPAAA"
print(insulin_signal + SequenciaFinal)

#d- Substitua o trecho "DPAAA" por “LLALL”.


#4- Com base na sequência de DNA GATGGAACTTGACGTAAACCTATATT retorne a sequência de RNA correspondente sendo a mesma GAUGGAACUUGACGUAAACCUAUAUU
DNA = "GATGGAACTTGACGTAAACCTATATT"
