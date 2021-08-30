#30
val_br = float(input("Digite um valor monetário em reais: "))
cot_us = float(input("Digite a cotação atual do dólar: "))
val_us = val_br*cot_us
data_atual = date.today()
print("R${:.2f} = US${:.2f} ({})".format(val_br, val_us, data_atual.strftime("%d/%m/%Y"))) 