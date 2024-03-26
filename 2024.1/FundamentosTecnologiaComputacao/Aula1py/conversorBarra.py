'''
Criar um algoritmo em python que leia o comprimento de uma barra em centímetros e exiba seu comprimento convertido em:
- Polegadas
- Pés

1 polegada = 2,54 cm = 0,08 pés
'''

# Entrada
barra = float(input("Digite o comprimento da barra em cm: "))

# Processamento
polegadas = barra / 2.54
pes = polegadas * 0.08

#Saída
print (f"O comprimento da barra em polegadas é {polegadas}")
print (f"O comprimento da barra em polegadas é {pes}")