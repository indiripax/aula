#Em um experimento de docking molecular utilizando três ferramentas diferentes, foram obtidos os três três conjuntos de RMSD da tabela abaixo. Considerando os valores desta tabela, crie os 3 conjuntos usando variáveis do tipo conjunto em Python.
 
ferramenta1= {1.9, 1.8, 5.7, 1.6, 5.8, 1.7, 9.6, 5.9, 9.5, 6.5, 6.2, 1.1, 4.4, 3.5, 2.9, 4.7, 4.6, 5.2, 5.3}
ferramenta2= {4.7, 3.6, 6.2, 7.1, 7, 5.6, 5.7, 3.4, 3.3, 2.1, 3.8, 3.9, 5, 5.1, 1.9, 9.5, 1.0, 1.3, 5.4}
ferramenta3= {2.2, 3.3, 5.1, 3, 3.7, 9.1, 8.8, 8.5, 2, 4.1, 6.1, 4.9, 1.1, 0.5, 0.8, 3.2, 6.9, 9.3, 9.5}

#A seguir, codifique em Python as seguintes tarefas: 
#a) Verifique as diferenças entre os conjuntos (1,2) (1,3) e (2,3)  

diferenca1_2 = ferramenta1.difference(ferramenta2)

diferenca1_3 = ferramenta1.difference(ferramenta3)

diferenca2_3 = ferramenta2.difference(ferramenta3)

print("letra a:")
print(f"diferenca 1,2 {diferenca1_2}")
print(f"diferenca 1,3 {diferenca1_3}")
print(f"diferenca 2,3 {diferenca2_3}")

#b) Retorne as intersecções entre (1,2) (1,3) e (2,3)  
intersection1_2 = ferramenta1.intersection(ferramenta2)

intersection1_3 = ferramenta1.intersection(ferramenta3)

intersection2_3 = ferramenta2.intersection(ferramenta3)

print("letra b:")
print(f"intercessao 1,2 {intersection1_2}")
print(f"intercessao 1,3 {intersection1_3}")
print(f"intercessao 2,3 {intersection2_3}")

#c) Insira todos os elementos do conjunto 2 e 3 no conjunto 1 
ferramenta1.update(ferramenta2, ferramenta3)
print("letra c:")
print(f"conjunto 1 {ferramenta1}")

#d) Retorne o tamanho do conjunto formado pela tarefa (c)
print("letra d:")
print(f"tamanho do conjunto {len(ferramenta1)}")


#Exercício 2:
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
    print("A e D são disjuntos")
else:
    print("A e D não são disjuntos")

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
  print("C não é subconjunto de B")

#d) Acrescente os elementos 18, 23, 25, 63 no conjunto D
acrescente = D.update({18, 23, 25, 63})
print(f"letra d:\n{D}")