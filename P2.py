import pandas as pd
import sqldf
from matplotlib import pyplot as plt


def Data(fname, cname):
    GroupList = []
    #Group A
    #print("\n Group A")
    q1 = f"""SELECT {cname} FROM {fname} WHERE g = "group A" """
    n1 = sqldf.run(q1)
    #print(n1)
    A = n1[cname].tolist()
    #print(A)
    
    #Group B
    #print("\n Group B")
    q2 = f"""SELECT {cname} FROM {fname} WHERE g = "group B" """
    n2 = sqldf.run(q2)
    #print(n2)
    B = n2[cname].tolist()
    #print(B)

    #Group C
    #print("\n Group C")
    q3 = f"""SELECT {cname} FROM {fname} WHERE g = "group C" """
    n3 = sqldf.run(q3)
    #print(n3)
    C = n3[cname].tolist()
    #print(C)

    #Group D
    #print("\n Group D")
    q4 = f"""SELECT {cname} FROM {fname} WHERE g = "group D" """
    n4 = sqldf.run(q4)
    #print(n4)
    D = n4[cname].tolist()
    #print(D)

    #Group E
    #print("\n Group E")
    q5 = f"""SELECT {cname} FROM {fname} WHERE g = "group E" """
    n5 = sqldf.run(q5)
    #print(n5)
    E = n5[cname].tolist()
    #print(E)

    GroupList = [A, B, C, D, E]

    return GroupList


file = pd.read_csv("StudentsPerformance.csv")
file.rename(columns ={"math score" : "c1"}, inplace = True)
file.rename(columns ={"reading score" : "c2"}, inplace = True)
file.rename(columns ={"writing score" : "c3"}, inplace = True)
file.rename(columns ={"race/ethnicity" : "g"}, inplace = True)


Math = file[["c1", "g"]]
Reading = file[["c2", "g"]]
Writing = file[["c3", "g"]]




x = Data("Math", "c1")

plt.boxplot([x[0], x[1], x[2], x[3], x[4]])
plt.show()


