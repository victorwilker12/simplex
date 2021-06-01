import numpy as np 
import numpy.ma as ma
from decimal import Decimal
np.set_printoptions(suppress=True)
np.seterr(divide='ignore', invalid='ignore')
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
		line.append(float(input('digite a variável ' + str(j+1) +" da " + str(i+1) + "º funcao")))	
	matriz_func.append(line)

matriz_func = np.array(matriz_func)

for i in range(V+F):
	if i < V :
		z_function.append(float(input("digite os valores da Função Objetiva na posição" + str(i) +" : ")))
	elif  i >= V:
		z_function.append(0)
z_function = np.multiply(-1, z_function)



for i in range(F+1):
	if i > 0:
		LD.append(float(input("digite os valores da Coluna do Lado Direito da função " + str(i) + " : ")))
	elif  i == 0:
		LD.append(0)
LD = np.vstack(LD)

matriz = np.concatenate((matriz_func, Var_F), axis=1)
matriz = np.vstack([z_function, matriz])
matriz = np.c_[matriz,LD]



print(matriz)


# ------ escolhendo pivos -----

#menor valor da função z
while True:
	min_value_obj = min(matriz[0])



	r_function =[ row[-1] for row in matriz]
	print("ultima coluna =LD ")
	print(r_function)
	print(min_value_obj)

	linha = 0
	col = 0
	#encontrar posição do menor valor da função z 
	for i in range(len(matriz)):
	   	for j in range(len(matriz[i])):
	    		if(matriz[i][j]<matriz[0][col]):
	        		linha = i
	        		col = j

	index_col_pivo = col

	col_pivot = [ row[col] for row in matriz]# coluna pivo 
	print("Coluna pivo:")
	print(col_pivot)
	result_pivo = np.vstack(map(lambda x,y: y/x ,col_pivot,r_function)) #divisão da coluna pela coluna LD 
	result_pivo = np.array(result_pivo)
	result_pivo[0] =0
	min_value_div = min(numero for numero in result_pivo if numero != 0)# encontrando o minimo da divisão para encontrar a linha pivo
	print(matriz)
	print("resultado da divisão do Lado direito pela coluna pivo: ")
	print(result_pivo)
	for i in range(len(result_pivo)):# encontrar index de menor valor apos a divisão
		if result_pivo[i] ==  min_value_div:
			index_line_min_value_div = i
			break

	
	#print(index_line_min_value_div)
	#print(min_value_obj)
	#print('Coluna Pivo: ')
	#print(col_pivot)
	num_pivo =  matriz[index_line_min_value_div][index_col_pivo]
	num_pivo = num_pivo *1.0
	print('Numero selecionado para ser pivo: ')
	print(num_pivo)
	matriz =matriz.astype(np.float)
	for i in range(len(matriz)):
		if index_line_min_value_div == i:
	   		for j in range(len(matriz[i])):
	    			matriz[index_line_min_value_div][j] = matriz[index_line_min_value_div][j]/ num_pivo
	new_line_pivo = matriz[index_line_min_value_div]
	print("Linha pivo: ")
	print(new_line_pivo)

	for i in range(len(matriz)):
		if index_line_min_value_div != i:
	   		for j in range(len(matriz[i])):
	    			matriz[i][j] = (new_line_pivo[j] * (-1.0 * col_pivot[i])) + matriz[i][j]
	print(matriz)
	#verificando se precisa continuar
	verificador = min(matriz[0])
	if verificador >= 0 :
		break
print("\n")
print("--------------------- Solução Ótima ----------------------------")
solution_Z =[ row[-1] for row in matriz]
print("Solução ótima para Z = "+ str(solution_Z[0]))
print("----------------------------------------------------------------")
print("Tabela da Solução")
print(matriz)