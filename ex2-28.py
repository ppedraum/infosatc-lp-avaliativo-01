#28
n = [float(input("Digite um número: ")),
     float(input("Digite outro número: ")), 
     float(input("Digite outro número: "))]
q = n[0]**2 + n[1]**2 + n[2]**2
print("{:.2f}² + {:.2f}² + {:.2f}² = {:.2f}".format(n[0], n[1], n[2], q))