import pandas as pd
import sqldf
import math
from tabulate import tabulate
from pydoc import plain
from turtle import color


def Data(column):
    Min = column.min()
    Max = column.max()
    Range = Max - Min
    Shape = column.shape
    Ni = round(1 + 3.32*math.log(Shape[0],10), 6)
    Width = Range/Ni
    NewRange = Ni*Width
    F = 0
    Fr = 0
    Fp = 0
    ListData = []
    Low = 0
    High = Width
    i = 0
    while i < Ni:
        List = []
        L = str(round(Low, 3))
        H = str(round(High, 3))
        Interval = str("[" + L + " - " + H + "]")
        #q = f"""SELECT * FROM Math WHERE {Low} < {cname} AND {cname} < {High}"""
        q = f"""SELECT * FROM Math WHERE {Low} < c1 AND c1 < {High}"""
        n = sqldf.run(q)
        count = n.shape[0]

        aux = count/Shape[0]
        fr = round(aux, 4)
        fp = round(fr*100, 4)
        F+=count
        Fr+= round(fr,3)
        Fp+= round(fp,3)

        List.append(Interval)
        List.append(count)
        List.append(fr)
        List.append(fp)
        List.append(F)
        List.append(Fr)
        List.append(Fp)

        ListData.append(List)
        Low+=Width
        High+=Width
        i+=1
    return ListData


#Data managing
file = pd.read_csv("StudentsPerformance.csv")
file.rename(columns ={"math score" : "c1"}, inplace = True)
file.rename(columns ={"reading score" : "c2"}, inplace = True)
file.rename(columns ={"writing score" : "c3"}, inplace = True)

Math = file["c1"]
""" Reading = file["c2"]
Writing = file["c3"] """
M = Data(Math)
""" R = Data(Reading)
W = Data(Writing) """

#### TABLE ##############
heads = ["Interval", "f", "fr", "fr%", "F", "Fr", "Fr%"]

print("               ################### MATH TEST SCORES ####################")
print(tabulate((M), headers = heads, tablefmt = "pretty"))

""" print("               ################### READING TEST SCORES ####################")
print(tabulate((R), headers = heads, tablefmt = "pretty")) """

""" print("               ################### WRITING TEST SCORES ####################")
print(tabulate((W), headers = heads, tablefmt = "pretty")) """

