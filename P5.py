import pandas as pd


file = pd.read_csv("StudentsPerformance.csv")
file.rename(columns ={"math score" : "c1"}, inplace = True)
file.rename(columns ={"reading score" : "c2"}, inplace = True)
file.rename(columns ={"writing score" : "c3"}, inplace = True)


Math = file["c1"]
Reading = file["c2"]
Writing = file["c3"]

def Description(fname):
    sum = 0
    mean = fname.mean() 
    mode = fname.mode() 
    median = fname.median()
    desvstd = fname.std()
    var = fname.var()
    cvar = var/ abs(mean)
    sesgo = mean - median
    largo = Math.shape[0]
    i = 0
    while i < largo:
        resta = Math[i] - mean
        #print("Math[i]: ", Math[i], " Mean: ", mean)
        #print("resta", resta)
        p2 = resta**3
        #print("p2",p2)
        sum+=p2
        #print("sum", sum)
        i+=1
    p3 = (var**3)*(largo - 1)
    #print("p3 ", p3)
    p4 = 1/p3
    #print("p4", p4)
    cs = "{:f}".format(p4 * sum)
    print("Media:", mean)
    print("Moda", mode[0])
    print("Mediana:", median)
    print("Desviacion Estandar:", desvstd)
    print("Varianza:", var)
    print("Coeficiente Variacion:", cvar)
    print("Sesgo:", sesgo)
    if float(cs) < 0:
        print("Coeficiente Pearson:", cs)
        print("la curva es asimetrica hacia la izquierda")
    elif float(cs)  == 0:
        print("Coeficiente Pearson:", cs)
        print("la curva es simetrica ")
    else:
        print("Coeficiente Pearson:", cs)
        print("la curva es asimetrica hacia la derecha")




print("###### Prueba Matematica ############")
Description(Math)
print("\n####### Prueba Lectura ########")
Description(Reading)
print("\n######## Prueba Escritura ########")
Description(Writing)
