#exercício 1

NCBI = ["AAY66821.1", "AAY66759.1", "AAY66711.1", "AAY66706.1", "AAY66703.1", "AAY66697.1", "AAY66696.1", "AAY66682.1", "AAY66647.1", "AAY66625.1", "AAY66623.1", "AAY66620.1", "AAY66619.1", "AAY66616.1", "AAY66609.1", "AAY66607.1", "AAY66586.1", "AAY66564.1", "AAY66562.1", "AAY66561.1", "AAY66558.1", "AAY66544.1", "AAY66542.1", "AAY66539.1", "AAY66538.1", "AAY66537.1", "AAY66536.1", "AAY66512.1", "AAY66496.1", "AAM93627.1", "AAM93626.1", "AAY66506.1", "AAM93587.1", "AAY66811.1", "AAY66620.1", "AAY66555.1", "AAY66707.1", "AAM93653.1", "AAY66608.1", "AAY66700.1", "AAY66646.1", "AAY66809.1", "AAK97814.1", "AAK97810.1", "AAY66594.1", "AAY66685.1", "AAY66571.1", "AAY66865.1"]

# a) Crie uma lista com esses identificadores, obtenha e imprima tamanho da lista criada.
print(len(NCBI))

#b) Verifique a presença dos seguintes identificadores: AAY66682.1,  AAY66504.1, AAY66640.1, AAY66562.1, AAY66816.1

if "AAY66682.1" in NCBI:
    print("AAY66682.1 pertence")
if not "AAY66682.1" in NCBI:
    print("AAY66682.1 nao pertence")

if "AAY66504.1" in NCBI:
    print("AAY66504.1 pertence")
if not "AAY66504.1" in NCBI:
    print("AAY66504.1 nao pertence")

if "AAY66640.1" in NCBI:
    print("AAY66640.1 pertence")
if not "AAY66640.1" in NCBI:
    print("AAY66640.1 nao pertence")

if "AAY66562.1" in NCBI:
    print("AAY66562.1 pertence")
if not "AAY66562.1" in NCBI:
    print("AAY66562.1 nao pertence")

if "AAY66816.1" in NCBI:
    print("AAY66816.1 pertence")
if not "AAY66816.1" in NCBI:
    print("AAY66816.1 nao pertence")

#c) Obtenha e imprima o elemento presente na posição 10 da lista

print(NCBI[10])

#d) Insira os identificadores nas posições indicadas e imprima a lista final: AAY66967.1 posição 11; AAY66880.1 posição 21; AAY66874.1 posição 16

#e) Verifique o elemento na posição 8 e em seguida o retire da lista e imprima a lista final.  


#