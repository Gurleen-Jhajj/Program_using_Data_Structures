"""
Program to represent COVID 19 data using data structures.
author: Gurleen Kaur
date: 21-07-2021
"""
covid19_data={}

Punjab = {"Confirmed":598455,"Active":899,"Recovered":581312,"Deceased":16244,"Tested":12000000}

Maharashtra = {"Confirmed":6229596, "Active":94593, "Recovered":6000911, "Deceased":130753, "Tested":46000000}

Haryana = {"Confirmed":769605, "Active":784, "Recovered":759213, "Deceased":9608, "Tested":11000000}

covid19_data["Punjab"] = Punjab
covid19_data["Maharashtra"] = Maharashtra
covid19_data["Haryana"] = Haryana

Punjab_Districts={}

Ludhiana={"confirmed":87249,"Active":104,"Recovered":85052,"Deceased":2093}

Jalandhar={"confirmed":63023,"Active":102,"Recovered":61432,"Deceased":1489}

Sangrur={"confirmed":15668,"Active":21,"Recovered":14780,"Deceased":867}

Punjab_Districts["Ludhiana"]=Ludhiana
Punjab_Districts["Jalandhar"]=Jalandhar
Punjab_Districts["Snagrur"]=Sangrur

covid19_data["Punjab"]["Districts"]=Punjab_Districts

for keys in covid19_data.keys():
    print(keys,":",covid19_data[keys])


