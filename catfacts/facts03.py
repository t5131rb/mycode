#!/usr/bin/env python3
"""Alta3 Research | Author: RZFeeser@alta3.com"""

# imports always go at the top of your code
import requests

def main():
    """Run time code"""
    ## create r, which is our request object
    data = requests.get('https://api.open-notify.org/atros.json')

    for date in data["near_earth_objects"]:
        for ast in data["near_earth_objects"][date]:
            if ast.get("is_potentially_hazardous_asteroid"):
                num_hazard += 1
    print(num_hazard)

main()
