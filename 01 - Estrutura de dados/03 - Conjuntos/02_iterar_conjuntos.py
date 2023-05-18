carros = {"gol", "celta", "palio"} #Declarando o Set

for carro in carros: # percorrento o Set
    print(carro)

for indice, carro in enumerate(carros): # percorrendo o set e enumerando as posição dos elementos
    print(f"{indice}: {carro}")
