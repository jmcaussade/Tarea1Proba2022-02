import pandas as pd
import sqldf
import math
from matplotlib import pyplot as plt

#Data managing
file = pd.read_csv("StudentsPerformance.csv")
file.rename(columns ={"math score" : "M"}, inplace = True)
file.rename(columns ={"reading score" : "R"}, inplace = True)
file.rename(columns ={"writing score" : "W"}, inplace = True)
df2 = file.assign(Sum =lambda x: x.M + x.R + x.W)
Data = df2.iloc[:, [0, 5, 6, 7, 8]]

########################### TOP 10 ##############################
### No gender ####
q1 = """SELECT * FROM Data ORDER BY Sum DESC 
LIMIT 10"""
n1 = sqldf.run(q1)
ListIndex1 = n1["index"]
ListData1 = n1["Sum"]

## Female ###
q2 = """SELECT * FROM Data WHERE gender = "female" ORDER BY Sum DESC 
LIMIT 10"""
n2 = sqldf.run(q2)
ListIndex2 = n2["index"]
ListData2 = n2["Sum"]

## Male ###
q3 = """SELECT * FROM Data WHERE gender = "male" ORDER BY Sum DESC 
LIMIT 10"""
n3 = sqldf.run(q3)
ListIndex3 = n3["index"]
ListData3 = n3["Sum"]

########################### Bottom 10 #####################
### No gender ####
q4 = """SELECT * FROM Data ORDER BY Sum ASC 
LIMIT 10"""
n4 = sqldf.run(q4)
ListIndex4 = n4["index"]
ListData4 = n4["Sum"]


### female ####
q5 = """SELECT * FROM Data WHERE gender = "female" ORDER BY Sum ASC 
LIMIT 10"""
n5 = sqldf.run(q5)
ListIndex1 = n5["index"]
ListData5 = n5["Sum"]

### male ####
q6 = """SELECT * FROM Data WHERE gender = "male" ORDER BY Sum ASC 
LIMIT 10"""
n6 = sqldf.run(q6)
ListIndex1 = n6["index"]
ListData6 = n6["Sum"]

########### Graficos ################
ListX = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]


########### Top 10 #######################
###### All Genders #############
G1 = plt.figure("Top 10 All genders",figsize = (10, 10))
plt.title("Top All genders ", fontsize = 25)
plt.xlabel("positiongit", fontsize = 20)
plt.ylabel("Score", fontsize=20)
plt.plot(ListX, ListData1)
plt.legend(["All Genders"])

###### Female #############
G1 = plt.figure("Top 10 Female",figsize = (10, 10))
plt.title("Top 10 Female", fontsize = 25)
plt.xlabel("position", fontsize = 20)
plt.ylabel("Score", fontsize=20)
plt.plot(ListX, ListData2)
plt.legend(["Female"])

###### Male #############
G1 = plt.figure("Top 10 Male",figsize = (10, 10))
plt.title("Top 10 Male", fontsize = 25)
plt.xlabel("position", fontsize = 20)
plt.ylabel("Score", fontsize=20)
plt.plot(ListX, ListData3)
plt.legend(["Male"])

########### Worst 10 ########################
########### ALL Genders #############
G1 = plt.figure("Worst 10 All genders",figsize = (10, 10))
plt.title("Worst 10 All genders ", fontsize = 25)
plt.xlabel("position", fontsize = 20)
plt.ylabel("Score", fontsize=20)
plt.plot(ListX, ListData4)
plt.legend(["All Genders"])

###### Female #############
G1 = plt.figure("Worst 10 Female",figsize = (10, 10))
plt.title("Worst 10 Female", fontsize = 25)
plt.xlabel("position", fontsize = 20)
plt.ylabel("Score", fontsize=20)
plt.plot(ListX, ListData5)
plt.legend(["Female"])

###### Male #############
G1 = plt.figure("Worst 10 Male",figsize = (10, 10))
plt.title("Worst 10 Male", fontsize = 25)
plt.xlabel("position", fontsize = 20)
plt.ylabel("Score", fontsize=20)
plt.plot(ListX, ListData6)
plt.legend(["Male"])
plt.show()