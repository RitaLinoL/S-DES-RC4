q = 353
a = 3

def calcularY(x):
    if(x<q):
        Y = (a ** x ) % q
        return Y
    else:
        print("Valor inválido para X")
        return -1

        
def calcularK(y, x):
    if(y > 0):
        K = (y ** x) % q
        return K
    else:
        print("Valor inválido para Y")
        return -1