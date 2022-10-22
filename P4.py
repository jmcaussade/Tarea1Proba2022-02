import pandas as pd
import sqldf
import math
from tabulate import tabulate
from pydoc import plain
from turtle import color


def Data(column, fname, cname):
    Min = column.min()
    print("Min", Min)
    Max = column.max()
    print("Max", Max)
    Range = Max - Min
    print("Range", Range)
    Shape = column.shape
    Shape = Shape[0]
    print("Shape",Shape)
    Ni = round(1 + 3.32*math.log(Shape,10))
    print("Ni", Ni)

    #Ni = round(Ni,3)
    #print("Ni", Ni)
    Width = round(Range/Ni,10)
    print("Width", Width)
    NewRange = Ni*Width
    print("NewRange", NewRange)
    F = 0
    Fr = 0
    Fp = 0
    ListData = []
    Low = Min
    print("Low", Low)
    High = Min + Width
    print("High", High)
    i = 0
    NewMax = Min + NewRange
    print("NewMax", NewMax)
    while i < Ni:
        print("\nRound ", i)
        print("High", High)
        print("Low", Low)
        List = []
        L = str(round(Low, 3))
        H = str(round(High, 3))
        Interval = str("[" + L + " - " + H + "]")
        q = f"""SELECT * FROM {fname} WHERE {Low} <= {cname} AND {cname} < {High}"""
        #q = f"""SELECT * FROM {fname} WHERE {Low} < {cname} """
        #q = f"""SELECT * FROM Math WHERE {Low} < c1 AND c1 < {High}"""
        n = sqldf.run(q)

        counter = 0
        #print(n)
        count = n.shape[0]
        print("Count",count)

        aux = count/Shape
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
Reading = file["c2"]
Writing = file["c3"]
###############################
#M = Data(Math)

M = Data(Math, "Math", "c1")
#R = Data(Reading, "Reading", "c2")
#W = Data(Writing, "Writing", "c3")

#### TABLE ##############
heads = ["Interval", "f", "fr", "fr%", "F", "Fr", "Fr%"]

print("               ################### MATH TEST SCORES ####################")
print(tabulate((M), headers = heads, tablefmt = "pretty"))

""" print("               ################### READING TEST SCORES ####################")
print(tabulate((R), headers = heads, tablefmt = "pretty")) """

""" print("               ################### WRITING TEST SCORES ####################")
print(tabulate((W), headers = heads, tablefmt = "pretty")) """

