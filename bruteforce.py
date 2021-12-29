import json

class Tree:
    def __init__(self, data):
        self.data = data

    def make_schema(self):
        # O(2^data.len)
        nodes_count = 2**len(self.data)
        str_schema = bin(nodes_count - 1)[2:]
        schemas = []
        print("Prepare schemas")
        for i in range(nodes_count):
            current_binary = format(i, '0' + str(len(str_schema)) + 'b')
            schemas.append(current_binary)
        return schemas
        
    def get_combinaisons(self):
        values = self.get_value_from_map()
        print("Combine results")
        combinaisons = map(lambda x:
            [
                x[0],
                sum(map(lambda y: y["weight"], x[1])),
                sum(map(lambda y: y["value"], x[1]))
            ],
            values
         )
        return combinaisons

    def get_items_from_schemas(self, schemas):
        return [self.data[i] for i in range(len(schemas)) if schemas[i] == "1"]

    def get_value_from_map(self, mapping=None):
        if mapping is None:
            mapping = self.make_schema()
        print("Get values")
        results = [(schema, self.get_items_from_schemas(schema)) for schema in mapping]
        return results

    
class Bag:
    def __init__(self, max_weight, tree):
        self.max_weight = max_weight
        self.tree = tree

    def out_of_constraint(self):
        print("Get posible combinaisons")
        combinaisons = self.tree.get_combinaisons()
        print("Get content can be into")
        filtered_combinaisons = list(filter(lambda x: x[1] <= self.max_weight, combinaisons))
        filtered_combinaisons.sort(key=lambda x: (-x[2], x[1]))
        return filtered_combinaisons

    def get_best_content(self):
        best = self.out_of_constraint()[0]
        return {
            "actions": self.tree.get_items_from_schemas(best[0]),
            "amount": best[1],
            "full_gain": best[2]
        }


if __name__ == "__main__":

    def data_config(data):
        items = []
        print("Configure data")
        for key in data.keys():
            d = data[key]
            items.append({
                "name": key,
                "weight": d["cost"],
                "value": round(d["cost"] * d["gain"], 3)
            })
        return items


    with open('./data.json', "rb") as data_file:
        data = json.load(data_file)
        DATA = data_config(data)
        posibility_tree = Tree(DATA)
        bag = Bag(500, posibility_tree)
        best_content = bag.get_best_content()
        print("Meilleurs investisments")
        print("\nACTION \t\t| COST \t\t| GAIN\n")
        actions_table = [f"{action['name']} \t| {'0'*(2 - len(str(action['weight'])))}{action['weight']}€/1 \t| {action['value']}€/2ans" for action in best_content["actions"]]
        print("\n".join(actions_table))
        print(f"\nTotal investisement: {best_content['amount']}€ \t| Total gain: {best_content['full_gain']}€")

        # print("\n\nTest mode :")
        # test_base = [best_content['full_gain'] < combi[2] for combi in bag.out_of_constraint()]
        # print("Error: "+ str(True in test_base))