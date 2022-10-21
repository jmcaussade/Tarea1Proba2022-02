import pandas as pd
import sqldf
import math


file = pd.read_csv("StudentsPerformance.csv")
file.rename(columns ={"math score" : "c1"}, inplace = True)
#print(list(file))
Math = file["c1"]
#print(Math)


def Data(column):
    Min = column.min()
    Max = column.max()
    Range = Max - Min
    Shape = column.shape
    Ni = round(1 + 3.32*math.log(Shape[0],10), 6)
    Width = Range/Ni
    NewRange = Ni*Width
    ListInterval = []
    ListCount = []
    Low = 0
    High = Width
    i = 0
    while i < Ni:
        L = str(round(Low, 3))
        H = str(round(High, 3))
        Interval = str("[" + L + " - " + H + "]")
        ListInterval.append(Interval)
        q = f"""SELECT * FROM Math WHERE {Low} < c1 AND c1 < {High}"""
        n = sqldf.run(q)
        count = n.shape[0]
        ListCount.append(count)
        Low+=Width
        High+=Width
        i+=1

    ListData = [ListInterval, ListCount]
    return ListData



x = Data(Math)
print(x)
