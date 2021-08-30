from datetime import date
""" #6
c = float(input("Digite uma temperatura em celcius: "))
f = c*(9/5) + 32
print("f = {}*(9/5) + 32 ----> f = {} ºF".format(c, f) ) """

""" #11
m = float(input("Digite uma velocidade em metros por segundo: "))
k = m*3.6
print("{:.2f}m/s = {:.2f}km/h".format(m, k)) """

""" #14
g = float(input("Digite um ângulo em graus: "))
r = (g*3.14)/180
print("{:.2f}º = {:.2f}rad".format(g, r)) """

""" #19
l = float(input("Digite um volume em litros: "))
m = l/(10**3)
print("{:.2f}l = {:.3f}m³".format(l, m)) """

""" #21
l = float(input("Digite uma massa em libras: "))
k = l*0.45
print("{:.2f}lb2 = {:.2f}kg".format(l, k)) """

""" #23
m = float(input("Digite uma distância em metros: "))
j = m/0.91
print("{:.2f}m = {:.2f}yd".format(m, j)) """

""" #25
a = float(input("Digite uma área em acres: "))
m = a*4048.58
print("{:.2f}ac = {:.2f}m²".format(a, m)) """

""" #26
m = float(input("Digite uma distância em metros quadrados: "))
h = m*(1/10**4)
print("{:.2f}m² = {:.4f}ha".format(m, h)) """

""" #28
n = [float(input("Digite um número: ")),
     float(input("Digite outro número: ")), 
     float(input("Digite outro número: "))]
q = n[0]**2 + n[1]**2 + n[2]**2
print("{:.2f}² + {:.2f}² + {:.2f}² = {:.2f}".format(n[0], n[1], n[2], q)) """

""" #29
n = [float(input("Digite a nota 1: ")),
     float(input("Digite a nota 2: ")), 
     float(input("Digite a nota 3: ")),
     float(input("Digite a nota 4: "))]
q = (n[0] + n[1] + n[2] + n[3])/4
print("({:.2f} + {:.2f} + {:.2f} + {:.2f})/4 = {:.2f}/4 = {:.2f}".format(n[0], n[1], n[2], n[3],
                                                                       n[0]+n[1]+n[2]+n[3],
                                                                       q)) """

#30
val_br = float(input("Digite um valor monetário em reais: "))
cot_us = float(input("Digite a cotação atual do dólar: "))
val_us = val_br*cot_us
data_atual = date.today()
print("R${:.2f} = US${:.2f} ({})".format(val_br, val_us, data_atual.strftime("%d/%m/%Y")))


