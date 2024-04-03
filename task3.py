import json
import pickle

data = ["предмет1, item2, item3", "item4, item5"]

# pickle
with open("data.pickle", "wb") as file:
    pickle.dump(data, file)

with open("data.pickle", "rb") as file:
    data_pickle = pickle.load(file)
print(data_pickle)

# json
data_json = json.loads(json.dumps(data_pickle))
with open("output.json", "w", encoding="utf-8") as file:
    json.dump(data_json, file, ensure_ascii=False, indent=4)

with open("output.json", "r", encoding="utf-8") as file:
    data_j = json.load(file)
print(data_j)
