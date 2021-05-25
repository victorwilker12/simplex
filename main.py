import numpy as np 
F = int(input("Numero de Funções de restrição"))
V = int(input("Numero de Variáveis da Função"))
matriz_func = []
z_function = []
z_function_zero = []
LD = []

Var_F = np.eye(F,dtype=int)
#print(Var_F)
for i in range(F):
	#matriz_func.append([])
	line = []
	print("-------")
	z_function_zero.append(0)
	for j in range(V):
		line.append(int(input('digite a variável ' + str(j+1) +" da " + str(i+1) + "º funcao")))	
	matriz_func.append(line)

matriz_func = np.array(matriz_func)

for i in range(V+F):
	if i < V :
		z_function.append(int(input("digite os valores da Função Objetiva na posição" + str(i) +" : ")))
	elif  i >= V:
		z_function.append(0)
z_function = np.multiply(-1, z_function)



for i in range(F+1):
	if i > 0:
		LD.append(int(input("digite os valores da Coluna do Lado Direito da função " + str(i) + " : ")))
	elif  i == 0:
		LD.append(0)
LD = np.vstack(LD)

matriz = np.concatenate((matriz_func, Var_F), axis=1)
array = np.vstack([z_function, matriz])
array = np.c_[ array,LD]
print(array)

