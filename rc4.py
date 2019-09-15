'''Este modulo contem as funcoes relacionadas com o algoritmo de criptografia RC4'''
__version__:"1.0"
__author__:"Alice Barros & Rita Lopes"



from manipulation_str_int_bin import * 
#importacao de funcoes para manipulacao de string, inteiros e binarios, que foram implementadas em arquivo separado


def inicializacao_vetor(K):
  '''  Funcao de inicializao do vetor de estados e vetor temporario
  :param K: chave com tamanho entre 1 e 256 bytes (8 a 2048 bits)
  :return S: vetor de estados de 256 posições com valores iguais às posições 
  :return T: vetor temporario para armazenar os bytes da chave K
  :rtype S: vetor de inteiros
  :rtype T: vetor de inteiros
  '''
  T = []
  S = []

  for i in range(0,256):
      S.append(i) # adiciona/insere os valores de i à/ao lista/vetor S
      T.append( K [i % len(K)]) # caso o tamanho da chave K for 256, inicializar T = K, caso K for menor T é inicializado com valores repetidos ciclicamente de K
  return S, T

def swap(a , b):
  ''' Função de troca de valores a por b
  :param a: segundo retorno 
  :param b: primeiro retorno
  '''
  return b, a

def permutacao_inicial(S, T):
  '''
  Função para permutação dos valores do vetor de estado seguindo expressão matemática dependente do vetor temporário gerado a partir da chave
  :param S: vetor de estado
  :param T: vetor temporário
  :type S: list()
  :type T: list()
  :return S: vetor de estado com a nova permutação 
  :rtype: list()
  '''
  j = 0 #inicializa variável indice 
  for i in range (0, 256):
    j = ((j + S[i] + int(T[i]))% 256) # modifica valor de j para valor dependente da soma dos vetores de estado e temporário na mesma posição e ao valor de j no ciclo anterior 
    S[i], S[j] = swap(S[i], S[j]) # 
  return S 


def geracao_fluxo(texto_entrada, S):
  '''
  Função que percorre todos os elementos de S trocando-os de posição por outro byte em S de acordo com expressão matemática dependente do próprio S, e utiliza a operação lógica XOR (Ou exclusivo) para gerar uma nova configuração de texto utilizando o texto de entrada (que pode ser o texto claro ou criptografado) e S.
  :param texto_entrada : lista com inteiros que passarão pelo processo de geração de texto 
  :param S: vetor de estado, com a permutação inicial
  :type texto_entrada: vetor de inteiros
  :type S: vetor de inteiros
  :return texto_saida: texto ou criptografado ou texto claro (descriptografado), depende do texto de entrada
  :rtype texto_saida: vetor de inteiros
  '''
    
  i, j = 0, 0
  texto_saida = list() #vetor para armazenar saida

  for l in range (0, len(texto_entrada)):
    i = (i + 1) % 256 #indice principal de S
    j = (j + S[i]) % 256 # indice de S dependente do valor de S no indice principal
   
    S[i], S[j] = swap(S[i], S[j]) # permutação dos valores do vetor de estado

    t = (S[i] + S[j]) % 256 # expressão para gerar indice de S 
    k = S[t] # valor de S a ser usado na operação XOR
    texto_saida.append( k ^ texto_entrada[l]) # valor após realização da operação XOR entre uma posição do vetor de estado e do texto de entrada
  return texto_saida


def rc4(texto_entrada, chave):
  '''
  Função principal que a partir de um texto e uma chave, criptografa ou descriptografa texto usando o algoritmo RC4
  :param texto_entrada : string com texto a ser criptografado ou descriptografado
  :param chave: chave a ser utilizada no processo (criptografia ou descriptografia)
  :type texto_entrada : string
  :type chave: string
  :return texto_saida: texto ou criptografado ou claro (descriptografado), depende do texto de entrada
  :rtype: string
  '''

  chave_int = string_to_listInt(chave) # conversão da chave de string para lista de inteiros

  S, T = inicializacao_vetor(chave_int) # chamada de função para inicialização de S e T a partir da chave
  S = permutacao_inicial(S,T) # permutação do vetor de estado

  texto_entrada_int = string_to_listInt(texto_entrada) # conversão do texto de string para uma lista de inteiros de acordo com a tabela ascii

  texto_saida_int = geracao_fluxo(texto_entrada_int, S) # chamada de função de geração de fluxo com o valor enviado pelo usuário e o vetor de estado gerado a partir da chave enviada pelo usuário
  texto_saida = listInt_to_string(texto_saida_int) # conversão do texto de lista de inteiros para string

  return texto_saida
