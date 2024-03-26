'''
Escreva o algritmo de uma calculadora que faça e demonstre todas as operações básicas a partir de dois números fornecidos pelo usuário
'''

# MINI CALCULADORA DE INTEIROS: +, -, *, **, /, // e % = 5 Aritméticos
print ("MINI CALCULADORA DE INTEIROS:")
n1 = int(input("n1: "))
n2 = int(input("n2: "))
print (f"ADIÇÃO: N1 + N2 + {n1} + {n2} = {n1 + n2}")
print (f"SUBTRAÇÃO: N1 - N2 = {n1} - {n2} = {n1 - n2}")
print (f"MULTIPLICAÇÃO: N1 * N2 = {n1} * {n2} = {n1 * n2}")
print (f"DIVISÃO: N1 / N2 = {n1} / {n2} = {n1 / n2}")
print (f"DIV (QUOCIENTE INT): N1 div N2 = {n1} // {n2} = {n1 // n2}")
print (f"MOD (RESTO INT): N1 mod N2 = {n1} % {n2} = {n1 % n2}")
print (f"POTENCIAÇÃO: N1 ** N2 = {n1} ** {n2} = {n1 ** n2}")
print (f"RADICIAÇÃO: N1 ** (1/N2) = {n1} ** { 1/n2 } = {n1 ** (1/n2)}")