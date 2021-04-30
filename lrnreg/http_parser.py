#!/usr/bin/env python3
import urllib.request
import re

quit = ''
while quit.lower() != 'n':
    print("Where should we search?")
    url = input()
    print("Great! So we'll try to open this url " + str(url) + " to search for the phrase:")
    searchFor = input()
    searchMe = urllib.request.urlopen(url).read().decode("utf-8")

    if re.search(searchFor, searchMe):
        print("Found a match!  Would you like to try again? Y/N")
        quit = input()
    else:
        print("No match!  Would you like to try again? Y/N")
        quit = input()

