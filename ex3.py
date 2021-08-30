import math
val_tinta = 107.00
vol_tinta = 3.6
cob_tinta = vol_tinta*3


a = float(input("Digite o comprimento da parede: "))
b = float(input("Digite a largura da parede: "))
m = a*b
qtd_lata = math.ceil(m/cob_tinta)
val_total = qtd_lata * val_tinta

print("em uma parede de {:.2f}m², podemos usar {} latas de tinta, com um valor total de {:.3f} reais."
      .format(m, qtd_lata, val_total))


