''''
Escreva um algoritmo que converta o valor em real para Dolar, Euro e Libra
'''

# Entrada
real = float(input("Digite o valor em Real: "))

# Processamento
dolar = real / 4.97
euro = real / 5.39
libra = real / 6.29

# Saída
print (f"O valor em dolar é {dolar : .2f}")
print (f"O valor em euro é {euro : .2f}")
print (f"O valor em libra é {libra : .2f}")