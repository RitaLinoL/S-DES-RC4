from rc4 import rc4


chave = input("Chave: ")

texto = input("Texto: ")

texto_enc = rc4(texto, chave)
print("Resultado da encriptação: ", texto_enc)

print("-------------")
print("Resultado da decriptação: ", rc4(texto_enc, chave))




