#29
n = [float(input("Digite a nota 1: ")),
     float(input("Digite a nota 2: ")), 
     float(input("Digite a nota 3: ")),
     float(input("Digite a nota 4: "))]
q = (n[0] + n[1] + n[2] + n[3])/4
print("({:.2f} + {:.2f} + {:.2f} + {:.2f})/4 = {:.2f}/4 = {:.2f}".format(n[0], n[1], n[2], n[3],
                                                                       n[0]+n[1]+n[2]+n[3],
                                                                       q)) 