from conversor import*

cm=int(input("Digite a medida em cm: "))
pol=cm_pol(cm)
print("o valor " +str(cm)+ " em centímetros corresponde a " +str(pol)+ " valor em polegadas\n")

file = open('resultados da conversão.txt', 'a')
file.write("O valor " +str(cm)+ " em centímetros corresponde a " +str(pol)+ " valor em polegadas\n")
file.close()