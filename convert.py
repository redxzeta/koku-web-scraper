import json

# making the name short
def dot_split(word):
    if word.count("・") < 2:
        return word
    else:
        return "・".join(word.split("・", 2)[:2])


with open('kokuItems.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

kokuList = []

for i in data:
    parent_name = i["name"]
    nickname = dot_split(parent_name)
    # print(nickname)
    parent = {
        "_id": f"{parent_name}",
        "name": parent_name,
        "nickname": str(nickname)
    }
    category = i["categories"]
    categories = []

    for j in category:
        child_title = j['title']
        category_items = j["items"]
        child = {
            "_id": f"{parent_name}_{child_title}",
            "title": child_title
        }

        item_list = []
        for k in category_items:
            item = k['title']
            item_type = False
            if 'type' in k:
                item_type=k['type']
            category_item = {
                "_id": f"{child_title}_{item}",
                "title": f"{item}",
                "type": item_type
            }
            item_list.append(category_item)
        child.update({"items": item_list})
        categories.append(child)
    parent.update({"categories": categories})
    kokuList.append(parent)
    # x = requests.post(f"{url}/{parent_name}", json = parent) //posting to backend
    # print(x)

with open('formatted.json', 'w', encoding='utf-8') as outfile:
    json.dump(kokuList, outfile, ensure_ascii=False, indent=4)
