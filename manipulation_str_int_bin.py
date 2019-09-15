'''Neste script estao implementadas funcoes de manipulacao de strings, inteiros e binarios'''
__version__:"1.0"
__author__:"Alice Barros & Rita Lopes"


def listInt_to_listBin(list_int):
  '''Funcao para conversao de lista de inteiros para lista de binarios
  :param list_int: lista de inteiros a ser convertido em lista de binarios
  :type list_int: list()
  :return list_bin: lista de binarios correspondentes a lista de inteiros
  :rtype list_bin: list()
  '''
  list_bin = list()
  for num in list_int:
    list_bin.append(str(bin(num))[2:].zfill(8))
  return list_bin


def string_to_listInt(text):
  '''Funcao para conversão de string para list de inteiros de acordo com a tabela ascii
  :param text: string a ser convertida em lista
  :type text: str
  :return text_int: lista de inteiros correspondente ao texto enviado
  :rtype text_int: list()
  '''
  text_int = list()
  for letter in text:
    text_int.append(ord(letter));
  return text_int



def listInt_to_string(text_int):
  '''Funcao para conversao de list de inteiros para string de acordo com a tabela
  :param text_int: lista de inteiros a ser convertida em texto 
  :type text_int: list
  :return text: texto a ser retorndo
  :rtype text_int: str
  '''
  text = list()
  for number in text_int:
    text.append(chr(number));
  return text

