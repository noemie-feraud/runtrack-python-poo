# a = 10
# b = a
# b = 20
# print(a)

# list1 = [1, 2, 3]
# list2 = list1
# list2.append(4)
# print(list1)

# def do_something(number1, number2):
#     number1 += 10
#     number2 += 50

# number1 = 15
# number2 = 20

# do_something(number1, number2)

# print(number1)
# print(number2)

# def add_pokemon(pokemon_list, id, name):
#     pokemon_list[id] = name

# pokemons  = {
#     "144" : "bulbizare",
#     "145" : "carapuce",
#     "147" : "salamèche",
# }

# add_pokemon(pokemons, "148", 'rondoudou')
# print(pokemons)

# class Voiture:
#     def __init__(self, marque):
#         self.marque = marque
# v1 = Voiture("Tesla")
# v2 = v1
# v2.marque = "BMW"
# print(v1.marque)

import copy
list1 = [1, 2, 3]
list2 = copy.copy(list1)
list2.append(4)
print(list1)