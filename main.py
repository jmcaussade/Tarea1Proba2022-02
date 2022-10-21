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
    Width = Max - Min
    q = """SELECT * FROM Math WHERE c1 == NULL"""
    n = sqldf.run(q)
    print(n)


    return 0



Data(Math)



#b = f"""SELECT Average FROM {string} WHERE Year == {y}"""
#        Data = pysqldf(b)
