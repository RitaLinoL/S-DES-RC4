from diffie_hellman import *

Ya = calcularY(97)
Yb = calcularY(233)

print("Ya : ", Ya)
print("Yb: ", Yb)


Ka = calcularK(Yb, 97)

print("K por Yb: ", Ka)

Kb = calcularK(Ya, 233)

print("K por Ya:", Kb)