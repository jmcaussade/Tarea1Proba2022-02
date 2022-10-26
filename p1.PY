import pandas as pd
import sqldf
import math
from matplotlib import pyplot as plt

#Data managing
file = pd.read_csv("StudentsPerformance.csv")
file.rename(columns ={"math score" : "Math"}, inplace = True)
file.rename(columns ={"reading score" : "Reading"}, inplace = True)
file.rename(columns ={"writing score" : "Writing"}, inplace = True)
df2 = file.assign(Sum =lambda x: x.Math + x.Reading + x.Writing)
Data = df2.iloc[:, [0, 5, 6, 7, 8]]

########################### TOP 10 ##############################
### No gender ####
q1 = """SELECT * FROM Data ORDER BY Sum DESC 
LIMIT 10"""
n1 = sqldf.run(q1)

## Female ###
q2 = """SELECT * FROM Data WHERE gender = "female" ORDER BY Sum DESC 
LIMIT 10"""
n2 = sqldf.run(q2)

## Male ###
q3 = """SELECT * FROM Data WHERE gender = "male" ORDER BY Sum DESC 
LIMIT 10"""
n3 = sqldf.run(q3)


########################### Bottom 10 #####################
### No gender ####
q4 = """SELECT * FROM Data ORDER BY Sum ASC 
LIMIT 10"""
n4 = sqldf.run(q4)

### female ####
q5 = """SELECT * FROM Data WHERE gender = "female" ORDER BY Sum ASC 
LIMIT 10"""
n5 = sqldf.run(q5)

### male ####
q6 = """SELECT * FROM Data WHERE gender = "male" ORDER BY Sum ASC 
LIMIT 10"""
n6 = sqldf.run(q6)

########### Graficos ################

########### Top 10 #######################
###### All Genders #############
n1.plot(x="index", y=["Math", "Reading", "Writing"], kind="bar", title="Top 10 All genders")

###### Female #############
n2.plot(x="index", y=["Math", "Reading", "Writing"], kind="bar", title="Top 10 female")

###### Male #############
n3.plot(x="index", y=["Math", "Reading", "Writing"], kind="bar", title="Top 10 male")

########### Worst 10 ########################
########### ALL Genders #############
n4.plot(x="index", y=["Math", "Reading", "Writing"], kind="bar", title="Worst 10 All genders")

###### Female #############
n5.plot(x="index", y=["Math", "Reading", "Writing"], kind="bar", title="Worst 10 female")

###### Male #############
n6.plot(x="index", y=["Math", "Reading", "Writing"], kind="bar", title="Worst 10 male")


plt.show()