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


M = Data("Math", "c1")
R = Data("Reading", "c2")
W = Data("Writing", "c3")

sub = file[["g", "c1", "c2", "c3"]]
#sub["prom"] = ((sub["c1"] + sub["c2"] + sub["c3"])/3)
sub["prom"] = (sub.iloc[:, [1, 2, 3]].sum(axis=1))/3
X = Data("sub", "prom")

#MATH
G1 = plt.figure("Gráfico 1: BoxPlots prueba Matematicas",figsize = (10, 10))
plt.title("Puntajes prueba Matematicas")
plt.xlabel("Grupos")
plt.ylabel("Puntaje")
plt.boxplot([M[0], M[1], M[2], M[3], M[4]], labels = ("A", "B", "C", "D", "E"))
plt.show()

#Reading
G2 = plt.figure("Gráfico 2: BoxPlots prueba Lectura",figsize = (10, 10))
plt.title("Puntajes prueba Lectura")
plt.xlabel("Grupos")
plt.ylabel("Puntaje")
plt.boxplot([R[0], R[1], R[2], R[3], R[4]], labels = ("A", "B", "C", "D", "E"))
plt.show()

#Writing
G3 = plt.figure("Gráfico 3: BoxPlots prueba Escritura",figsize = (10, 10))
plt.title("Puntajes prueba Escritura")
plt.xlabel("Grupos")
plt.ylabel("Puntaje")
plt.boxplot([W[0], W[1], W[2], W[3], W[4]], labels = ("A", "B", "C", "D", "E"))
plt.show()

#Promedio pruebas
G4 = plt.figure("Gráfico 4: BoxPlots promedio pruebas por grupo",figsize = (10, 10))
plt.title("Promedio pruebas")
plt.xlabel("Grupos")
plt.ylabel("Puntaje")
plt.boxplot([X[0], X[1], X[2], X[3], X[4]], labels = ("A", "B", "C", "D", "E"))
plt.show()