#!/usr/bin/env python3

## create dictionary

Ali = {"name":{"birth":"Cassius Clay","current":"Muhammad Ali"},
        "contact":{"phone":"333-444-5555","email":"thebest@boxing.com"},
        "favorites":{"number":56,"food":{"baked chicken":3.5,"mac and cheese":4.5,"spinach":2,"green peas":2},
            "drink":{"adult":["none"],"nonadult":["Mr. Champ soda"]}}}

foodList = Ali.get('favorites').get('food').keys()
foodCost = Ali.get('favorites').get('food').values()

totalCost = 0
for fCost in foodCost:
    totalCost += fCost

totalCost2 = sum(foodCost)


print("The Champ's favorite foods are:\n")
print(foodList)
print("The cost of The Champ's favorite meal is ")
print(totalCost2)

