def inicializacao_vetor(K):
    T = list()
    S = list()
    for i in range(0,256):
        S.append(i)
        T.append( K [i % len(K)])
    return S, T

def swap(a , b):
    return b,a


def permutacao_inicial(S, T):
    j = 0
    for i in range (0, 256):
        j = ((j + S[i] + int(T[i]))% 256)
        print(S[i], S[j])

        S[i], S[j] = swap(S[i], S[j])

        print(S[i], S[j])

S, T = inicializacao_vetor("00001010")

permutacao_inicial(S,T)
print(S)
print(T)