"""
This is the program for covid_19 API.
Author: Gurleen Kaur
Date: 08-08-2021
"""
import requests
import json

url = "https://api.covid19india.org/v4/min/timeseries.min.json"

response = requests.get(url)

data = json.loads(response.text)
keys = data.keys()

states = []
i = 0
print("~" * 20)
print("Enter:")
for key in keys:
    print(f"{i} for {key}")
    i += 1
    states.append(key)
print("~" * 20)

choice = int(input("Select the state or UT where you'd like to see data about covid cases:"))
i = 0

date = input("Enter date (yyyy-mm-dd):")
print(f"Cases of {states[choice]} on {date} are:")
cases = data[states[choice]]["dates"][date]

print()
print("~" * 70)
for key, value in cases.items():
    print(f"{key} : {value}")
print("~" * 70)

l = []
print()
my_choice = int(input("Do you want to see total cases till now of:{states[choice]}:\nEnter 1(Yes)||0(No):"))

if my_choice == 1:
    print(f"Total cases till now of:{states[choice]}")
    for key, value in data[states[choice]]["dates"].items():
        print(key, value)
        l.append(data[states[choice]]["dates"][key]["total"]["confirmed"])

    print()
    print(f"Total confirmed cases in {states[choice]} are {l[len(l) - 1]}")
elif my_choice == 0:
    print("Successful exit.")
else:
    print("Enter a valid choice!")
