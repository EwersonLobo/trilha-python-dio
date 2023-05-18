conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}
# .issubset nos diz se os elemento de um conjuto estão contido no segundo conjunto que está no paramentro
resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)
