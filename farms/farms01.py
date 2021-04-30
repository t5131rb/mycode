#!/usr/bin/env python3
# create a list of strings
farms = [{"name": "NE Farm", "agriculture": ["sheep", "cows", "pigs", "chickens", "llamas", "cats"]},
         {"name": "W Farm", "agriculture": ["pigs", "chickens", "llamas"]},
         {"name": "SE Farm", "agriculture": ["chickens", "carrots", "celery"]}]
# loop across the list called vendors
for a in farms[0]["agriculture"]:
        print(a)

choice = input("""
Choose a farm (1, 2, 3):
1 = NE Farm
2 = W Farm
3 = SW Farm
""")

for x in farms[choice]["agriculture"]:
    print(x)

for alldict in farms:
    if choice in alldict["name"]
        for x in alldict["agriculture"]:
            print(x["agriculture"])

ag = ["carrots","celery"]
for alldict in farms:
    if choice in alldict["name"]
        for x in alldict["agriculture"]:
            if x not in ag
            print(x["agriculture"])

