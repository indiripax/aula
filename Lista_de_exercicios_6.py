#1. O Protein Data Bank (PDB) é uma base de dados de estruturas de proteínas. Cada entrada da base de
#dados é identificada de por um id de 4 letras / dígitos como por exemplo “1ABC”. Abaixo são apresentados
#ids de estruturas PDBs, juntamente com a a contagem de aminoácidos presentes nessas estruturas.
'''1A8M - 471
1TNR - 283
2AZ5 - 592
1TNF - 471
2TNF - 468
2TUN - 942
4TSV - 150
5TSW - 900
2E7A - 471
6RMJ - 489'''

#a) Construa um dicionário onde os ids PDB sejam as chaves e o número de resíduos de aminoácidos sejam o valor.
print("letra a:")
PDB = {"1A8M": 471, "1TNR": 283, "2AZ5": 592, "1TNF": 471, "2TNF": 468, "2TUN": 942, "4TSV": 150, "5TSW": 900, "2E7A": 471, "6RMJ": 489}

#b) Imprima os valores contidos nos ids 2TNF e 2E7A.
print("letra b:")
print(f"2TNF: {PDB['2TNF']}")
print(f"2E7A: {PDB['2E7A']}")

#c) Verifique e imprima o tamanho do dicionário construído
print("letra c:")
print(f"tamanho do dicionario: {len(PDB)}")

#d) Obtenha e imprima a lista de todas as chaves do dicionário
print("letra d:")
print(f"lista de chaves: {PDB.keys()}")

#e) Obtenha e imprima a lista de todos os valores do dicionário
print("letra e:")
print(f"lista de valores: {PDB.values()}")

#f) Obtenha e imprima uma lista de tuplas com todos os pares chave-valor. Cada dupla será um par ordenado (chave, valor).
print("letra f")
print(f"lista de tuplas: {PDB.items()}")