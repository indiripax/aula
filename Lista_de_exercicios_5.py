#Dados os seguintes conjuntos
print("Exercício 2")
A = {3, 6, 9, 12, 15, 18, 21, 24, 28, 27} 
B = {2, 6, 8, 10, 14, 16, 18, 20, 22, 24} 
C = {2, 6, 10, 18, 20} 
D = {1, 30, 5, 11, 17, 16, 22, 26} 

#Codifique em Python as variáveis que os representam e realize as seguintes tarefas: 

#a) Verifique a interseção e diferença entre o conjunto A e B.
print("letra a:")
print(f"intercessão {A.intersection(B)}")
print(f"diferença {A.difference(B)}")

#b) Verifique se o conjunto A e B são disjuntos ao conjunto D
print("letra b:")
if A.isdisjoint(D):
    print("A e B são disjuntos")
else:
    print("A e B não são disjuntos")

if B.isdisjoint(D):
    print("B e D são disjuntos")
else:
    print("B e D não são disjuntos")

#c) Retorne se o conjunto C é subconjunto de A e B
print("letra c:")
if C.issubset(A):
  print("C é subconjunto de A")
else:
  print("C não é subconjunto de A")

if C.issubset(B):
  print("C é subconjunto de B")
else:
  print("C não é subconjunto de B"

#d) Acrescente os elementos 18, 23, 25, 63 no conjunto D
acrescente = D.update({18, 23, 25, 63})
print(f"letra d:\n{D}")