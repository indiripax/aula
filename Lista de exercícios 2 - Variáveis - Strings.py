#Exercicio 1
TNF = "VRSSSRTPSDKPVAHVVANPQAEGQLQWLNRRANALLANGVELRDNQLVVPSEGLYLIYSQVLFKGQGCPSTHVLLTHTISRIAVSYQTKVNLLSAIKSPCQRETPEGAEAKPWYEPIYLGGVFQLEKGDRLSAEINRPDYLLFAESGQVYFGIIAL"

#a- Retorne o tamanho da sequência.
print(len(TNF))

#b- Realize a contagem da ocorrência de um sequência de leucinas (LL).
leucina= TNF.count("LL")
print(leucina)

#c- Encontre na sequência as posições ocupadas por duas glicinas (GG) e duas argininas (RR).
print(TNF.index("GG"))

print(TNF.index("RR"))

#d- Retorne os 100 primeiros aminoácidos da sequência.
print(TNF[0:99])

#e- Substitua o trecho da sequência com a ocorrência de 3 serinas e 1 arginina (SSSR) por alaninas.
NovoTNF = TNF.replace("SSSR", "AAAA")
print(NovoTNF)

#f- Quebre a sequência no local onde a substituição foi realizada.

#estou com dpuvida se era isso mesmo que era pra ser feito
print(NovoTNF.split("AAAA"))

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
letrasmm = text

#3
insulin_signal = "MALWMRLLPLLALLALWGPDPAAA"

#a- Retorne o tamanho da sequência apresentada.
print(len(insulin_signal))

#b- Quebre a sequência no trecho “LLALLALWG".

#Não entendi o que foi pedido aqui nem na outra:
OutraSequencia = insulin_signal.split("LLALLAWG")
print(OutraSequencia)
MaisUmaSequencia = "LLALLAWG"

#c- Concatene as sequências resultantes obtendo a seguinte sequência final MALWMRLLPPDPAAA.
SequenciaFinal = "MALWMRLLPPDPAAA"
print(insulin_signal + SequenciaFinal)

#d- Substitua o trecho "DPAAA" por “LLALL”.
substituicao = (insulin_signal.replace("DPAAA", "LLALL"))
print(substituicao)

#4- Com base na sequência de DNA GATGGAACTTGACGTAAACCTATATT retorne a sequência de RNA correspondente sendo a mesma GAUGGAACUUGACGUAAACCUAUAUU
DNA = "GATGGAACTTGACGTAAACCTATATT"
RNA = DNA.replace("G", "C")("A", "U")("C", "G")("U", "A")
print(RNA)