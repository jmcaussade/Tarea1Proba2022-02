import pandas as pd


file = pd.read_csv("StudentsPerformance.csv")
file.rename(columns ={"math score" : "c1"}, inplace = True)
file.rename(columns ={"reading score" : "c2"}, inplace = True)
file.rename(columns ={"writing score" : "c3"}, inplace = True)


Math = file["c1"]
Reading = file["c2"]
Writing = file["c3"]

def Description(fname):
    mean = fname.mean() 
    mode = fname.mode() 
    median = fname.median()
    desvstd = fname.std()
    var = fname.var()
    cvar = var/ abs(mean)
    sesgo = mean - median
    print("Mean", mean)
    print("Mode", mode[0])
    print("Median", median)
    print("Dstd", desvstd)
    print("var", var)
    print("Mcvar", cvar)
    print("Msesgo", sesgo)


Description(Math)
print("##############")
Description(Reading)
print("##############")
Description(Writing)
