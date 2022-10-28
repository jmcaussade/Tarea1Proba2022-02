import pandas as pd

file = pd.read_csv("StudentsPerformance.csv")
file.rename(columns ={"math score" : "c1"}, inplace = True)
file.rename(columns ={"reading score" : "c2"}, inplace = True)
file.rename(columns ={"writing score" : "c3"}, inplace = True)

Math = file["c1"]
Reading = file["c2"]
Writing = file["c3"]
Mmean = Math.mean() 
Mmode = Math.mode() 
Mmedian = Math.median()
Mdesvstd = Math.std()
print("Mean", Mmean)
print("Mode", Mmode[0])
print("Median", Mmedian)
print("Dstd", Mdesvstd)
