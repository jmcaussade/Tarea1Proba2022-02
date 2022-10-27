import pandas as pd
import sqldf
import math
from tabulate import tabulate
from matplotlib import pyplot as plt



def Data(column, fname, cname):
    print("Data :",fname, "\n")
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
    High = round(Min + Width,3)
    print("High", High)
    i = 0
    NewMax = round(Min + NewRange,3)
    print("NewMax", NewMax)
    while i < Ni:
        if i < Ni-1:
            print("\nRound ", i)
            print("High", High)
            print("Low", Low)
            List = []
            L = str(round(Low, 3))
            H = str(round(High, 3))
            Interval = str("[" + L + " - " + H + "]")
            q = f"""SELECT * FROM {fname} WHERE {Low} <= {cname} AND {cname} < {High}"""

            n = sqldf.run(q)

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

        else:
            print("\nRound ", i)
            print("High", High)
            print("Low", Low)
            List = []
            L = str(round(Low, 3))
            H = str(round(High, 3))
            Interval = str("[" + L + " - " + H + "]")
            q = f"""SELECT * FROM {fname} WHERE {Low} < {cname} AND {cname} <= {NewMax}"""

            n = sqldf.run(q)

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
    print("\nFIN\n")
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
R = Data(Reading, "Reading", "c2")
W = Data(Writing, "Writing", "c3")

########### CODE ###############
#print(M)
def Graph(list):
    ListInterval = []
    i = 0
    while i <len(list):
        s = list[i][0]
        s = s.replace("[","")
        s = s.replace("]","")
        s = s.replace(" ","")
        s = s.split("-")
        #print("s", s)
        #print("i", i)
        ListInterval.append(float(s[0]))
        i+=1

    s = list[i-1][0]
    s = s.replace("[","")
    s = s.replace("]","")
    s = s.replace(" ","")
    s = s.split("-")
    #print("s", s)
    ListInterval.append(float(s[1]))
    #print(ListInterval)
    return ListInterval

#Graph(M)

#### TABLE ##############
heads = ["Interval", "f", "fr", "fr%", "F", "Fr", "Fr%"]

print("               ################### MATH TEST SCORES ####################")
print(tabulate((M), headers = heads, tablefmt = "pretty"))

print("               ################### READING TEST SCORES ####################")
print(tabulate((R), headers = heads, tablefmt = "pretty"))

print("               ################### WRITING TEST SCORES ####################")
print(tabulate((W), headers = heads, tablefmt = "pretty"))

###### GRAPH ##############

D = Math["c1"]
F = Reading["c2"]
G = Writing["c3"]



#MATH
G1 = plt.figure("Gráfico 1: Histograma prueba Matematicas",figsize = (10, 10))
bins = Graph(M)
plt.title("Histograma prueba Matematicas")
plt.xlabel("Score")
plt.ylabel("Frecuencia absoluta")
plt.xticks(bins)
plt.hist(D, bins, facecolor='b', alpha=0.7, edgecolor='k', linewidth=1)
#READING
G2 = plt.figure("Gráfico 2: Histograma prueba Lectura",figsize = (10, 10))
bins2 = Graph(R)
plt.title("Histograma prueba Lectura")
plt.xlabel("Score")
plt.ylabel("Frecuencia absoluta")
plt.xticks(bins2)
plt.hist(F, bins2, facecolor='r', alpha=0.7, edgecolor='k', linewidth=1)
#WRITING
G3 = plt.figure("Gráfico 3: Histograma prueba Escritura",figsize = (10, 10))
bins3 = Graph(W)
plt.title("Histograma prueba Escritura")
plt.xlabel("Score")
plt.ylabel("Frecuencia absoluta")
plt.xticks(bins3)
plt.hist(G, bins3, facecolor='g', alpha=0.7, edgecolor='k', linewidth=1)

#plt.show()


