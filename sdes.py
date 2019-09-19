'''Este modulo contem as funcoes relacionadas com o algoritmo de criptografia S-DES
__version__: "1.0"
__author__: "Alice Barros & Rita Lopes"
'''

'''
Geração das chaves K1 e K2:
K1:
Key() -> 10 bits
Permutação de 10 bits
Divide a chave permutada em 2 metades (Right and Left)
Rotação á esquerda (o primeiro elemento passa a ser o último e os elementos seguintes passam para frente/esquerda)
Faz uma permutação de 8 bits com os 10 elementos depois de ter feito a rotação a esquerda,
Resultando em K1 (subchave 1) -> Return K1

K2:
Pega o Resultado da 1º Rotação à esquerda e faz: 
: Rotação dupla à esquerda (o primeiro elemento passa a ser o último e os elementos seguintes passam para frente/esquerda (2x))
: Permutação de 8 bits com os 10 bits/elementos formados depois da concatenação dos bits após a rotação dupla
Resultando em K2 (subchave 2) -> Return K2
'''

# P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
# P8 = [6, 3, 7, 4, 8, 5, 10, 9]


"""
def rotacao_a_esquerda(esq, direita):
	first_esq = esq[0]
	esq[0] = esq[1]
	esq[1] = esq[2]
	esq[2] = esq[3]
	esq[3] = first_esq
	
	first_dir = direita[0]
	direita[0] = direita[1]
	direita[1] = direita[2]
	direita[2] = direita[3]
	direita[3] = first_dir

	return esq, direita
"""

def shift(four):
	rotation_result = []
	#for i in four:
	first_four = four[0]
	four[0] = four[1]
	four[1] = four[2]
	four[2] = four[3]
	four[3] = first_four
	rotation_result = [four[0], four[1], four[2], four[3]]

	return rotation_result

def gerando_subchave_k1(K):
	P10 = [3, 5, 2, 7, 4, 10, 1, 9, 8, 6]
	P8 = [6, 3, 7, 4, 8, 5, 10, 9]

	''' 
	permutando K de acordo com P10
	gerando new_K = permutação de K com P10
	separa os 5 primeiros bits dos 5 últimos bits
	esq = 5 primeiros bits & direita = 5 ultimos bits
	# rotacao_a_esquerda(esq, direita)
	shift(esq)
	shift(direita)

	## result_rotacao1 = esq + direita ~concatenação de esq com direita~
	
	permuta result_rotacao1 com P8
	gerando a subchave K1 = resultado da permutação result_rotacao1 com P8
	'''
	return K1

def gerando_subchave_k2(esq, direita):
	P8 = [6, 3, 7, 4, 8, 5, 10, 9]

	'''
	for i in range(0,3):
		# result_rotacao_esq2 = rotacao_a_esquerda() -> pega a esq e a direita e rotaciona 2x
		rotacao_esq2 = shift(esq)-> pega a esq e rotaciona 2x
		rotacao_dir2 = shift(direita) --> pega a direita e rotaciona 2x
		resultado_rotacao2 = rotacao_esq2 + rotacao_dir2
	permuta resultado_rotacao2 com P8,
	gerando a subchave K2 = resultado da permutação resultado_rotacao2 com P8	
	'''
	return K2


"""
GERANDO AS SUBCHAVES:

Key --> P10 -- Shift -|-- > P8 --> K1
					            |
Key --> P10 -- Shift -|-- > Double Shift -- P8 --> K2

K1 = P8(Shift(P10(Key)))
K2 = P8(Shift(Shift(P10(Key))))


	|=========================================================================================|
			  Dados:
	  	IP -> Permutação Inicial (Initial Permutation)
		  Fk -> Função Complexa que envolve SUBSTITUIÇÃO E PERMUTAÇÃO dependente da chave K1
  		SW (switch), onde o da esquerda(L) passa a ser o da direita(R) e vice-versa
	  	Fk -> Função Complexa que envolve SUBSTITUIÇÃO E PERMUTAÇÃO dependente da chave K2
		  IP_inversa -> função Inversa da Permutação Inicial
	|=========================================================================================|


CIFRANDO O TEXTO:

texto claro -- > IP -- Fk -- SW -- Fk -- IP_inversa -- > texto cifrado

DECIFRANDO O TEXTO:

texto cifrado -- > IP_inversa -- Fk -- SW -- Fk -- IP -- > texto claro

"""

def IP (texto_plano):
	PI = [2, 6, 3, 1, 4, 8, 5, 7]

	# P_Inicial = Permutação inicial dos 8 bits do texto plano (processados) com o PI

	return PI


# Fk é feito 2 vezes
def Fk(R, subchave):




	return

def SW(L, R):
	return R, L

def IP_inversa():
	PI_inverso = [4, 1, 3, 5, 7, 2, 8, 6]

	# P_Final = Permutação final dos 8 bits processados com o PI_inverso

	return P_Final


texto_claro = open()
texto_cifrado = IP_inversa(Fk(SW(Fk(IP(texto_claro)))))
print (texto_cifrado)
print("\n")
texto_decifrado = IP_inversa(Fk(SW(Fk(IP(texto_cifrado)))))
print(texto_decifrado)