valor = input()
horas = input()

valor = float(valor)
horas = float(horas)

vh = valor * horas

IR = vh * (11/100)
INSS = vh * (8/100)
SL = (vh - IR) - INSS
TD = IR + INSS

print("{x:.1f}".format(x=IR))
print("{x:.1f}".format(x=INSS))
print("{x:.1f}".format(x=SL))
print("{x:.1f}".format(x=TD))
