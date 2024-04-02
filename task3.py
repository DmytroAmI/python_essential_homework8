import json
import pickle

data = ["item1, item2, item3", "item4, item5"]

# pickle
with open("data.txt", "wb") as file:
    pickle.dump(data, file)

with open("data.txt", "rb") as file:
    data_pickle = pickle.load(file)
print(data_pickle)

# json
data_json = json.loads(json.dumps(data_pickle))
with open("output.json", "w") as file:
    json.dump(data_json, file)

with open("output.json", "r") as file:
    data_j = json.load(file)
print(data_j)
