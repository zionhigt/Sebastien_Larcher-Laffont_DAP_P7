# Inspired by https://gist.github.com/dongr0510/fd163ed5e80ae61dba998868ea262328#file-top_down_knapsack-py

import csv

if __name__ == "__main__":
    
    def solve_knapsack(gains, weights, max_weight):
      # Creation d'un tableau à deux dimensions pour la mémorisation, tout les éléments sont initialisé a -1
        memories_array = [[-1 for x in range(max_weight+1)] for y in enumerate(gains)]
        return knapsack_recursive(memories_array, gains, weights, max_weight, 0)


    def knapsack_recursive(memories_array, gains, weights, max_weight, current_index):

        # Vérifications de base
        if max_weight <= 0 or current_index >= len(gains):
            return 0

        # Si on a déja un sous problème similaire, on retourne ce resultat depuis la memoire
        if memories_array[current_index][max_weight] != -1:
            return memories_array[current_index][max_weight]

        gain_1 = 0
        # Appel recursif après avoir choisi l'élément à l'index courant
        # Si l'élément entre dans le sac sans contrainte
        if weights[current_index] <= max_weight:
            gain_1 = gains[current_index] + knapsack_recursive(
            memories_array, gains, weights, max_weight - int(weights[current_index]), current_index + 1)

        # Appel récursif après avoir trouver l'élément courant
        gain_2 = knapsack_recursive(
            memories_array, gains, weights, max_weight, current_index + 1)

        memories_array[current_index][max_weight] = max(gain_1, gain_2)
        return memories_array[current_index][max_weight]

    def data_config(data):
        items = []
        for key in data.keys():
            d = data[key]
            items.append({
                "name": key,
                "weight": d["cost"],
                "value": round(d["cost"] * d["gain"], 3)
            })
        return items


    with open('dataset1_Python+P7.csv', newline="") as data_file:
        DATA = [dict(data) for data in csv.DictReader(data_file)]

        gains = [float(d["value"]) for d in DATA]
        weights = [float(d["weight"]) for d in DATA]
        max_weight = 500
        res = solve_knapsack(gains, weights, max_weight)
        print(res)