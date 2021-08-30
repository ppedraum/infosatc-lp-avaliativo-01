val_premio = float(input("VALOR TOTAL DO PRÊMIO: "))
imposto = val_premio*0.07
val_real = val_premio - imposto

val_g1 = 0.46*val_real 
val_g2 = 0.32*val_real 
val_g3 = val_real - (val_g1 + val_g2)

print("-----------------------------------")
print("VALOR TOTAL DO PRÊMIO = {:.2f}".format(val_premio))
print("VALOR DO IMPOSTO = {:.2f}".format(imposto))
print("VALOR REAL (MENOS IMPOSTO) = {:.2f}".format(val_real))
print("PRÊMIO GANHADOR 1 = {:.2f}".format(val_g1))
print("PRÊMIO GANHADOR 2 = {:.2f}".format(val_g2))
print("PRÊMIO GANHADOR 3 = {:.2f}".format(val_g3))
print("-----------------------------------")