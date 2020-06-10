import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from PIL import Image


First_state = input("Enter the first state 1")
name_1 = First_state.replace(' ','_')+".csv"
file_name_1 = name_1+".csv"

data = pd.read_csv(file_name_1)
print(data)
count_row = data.shape[0]
#print(count_row)
count_column = data.shape[1]
recovery = []
recovery_percent = []
active = []
active_percent = []
dead = []
dead_percent = []

#print(data.iloc[4,3])

for i in range(count_row):
    if(data.iloc[i,1] !=0 and (i != 37)):
        recovery.append(int(data.iloc[i,3]))
        recovery_percent.append(int(data.iloc[i,3])/int(data.iloc[i,1]))
        active.append(int(data.iloc[i,2]))
        active_percent.append(int(data.iloc[i,2])/int(data.iloc[i,1]))
        dead.append(int(data.iloc[i,4]))
        dead_percent.append(int(data.iloc[i,4])/int(data.iloc[i,1]))

#print(recovery)
#print(recovery_percent)
#Recovery ka 
final_list_1 = [] 
  
for i in range(0, 3):  
    max1 = 0
      
    for j in range(len(recovery)):      
        if recovery[j] > max1: 
            max1 = recovery[j]; 
              
    recovery.remove(max1); 
    final_list_1.append(max1)

for i in range(3):
    temp = final_list_1[i]
    for j in range(count_row):
        if(data.iloc[j,3] == temp):
            print("Top "+str(i+1)+" in recoveries are "+str(data.iloc[j,0]))

#Recovery Percentage ka
final_list_2 = [] 
  
for i in range(0, 3):  
    max2 = 0
      
    for j in range(len(recovery_percent)):      
        if recovery_percent[j] > max2: 
            max2 = recovery_percent[j]; 
              
    recovery_percent.remove(max2); 
    final_list_2.append(max2)
print(final_list_2)

for i in range(3):
    temp = final_list_2[i]
    print(temp)
    for j in range(count_row):
        if(int(data.iloc[j,1]) !=0):
            if((int(data.iloc[j,3])/int(data.iloc[j,1])) == temp):
                print("Top "+str(i+1)+" in recoveries percentage are "+str(data.iloc[j,0]))

#Active kaa
final_list_3 = [] 
  
for i in range(0, 3):  
    max3 = 0
      
    for j in range(len(active)):      
        if active[j] > max3: 
            max3 = active[j]; 
              
    active.remove(max3); 
    final_list_3.append(max3)

for i in range(3):
    temp = final_list_3[i]
    for j in range(count_row):
        if(data.iloc[j,2] == temp):
            print("Top "+str(i+1)+" in active are "+str(data.iloc[j,0]))

#Active_Precentage
final_list_4 = [] 
  
for i in range(0, 3):  
    max4 = 0
      
    for j in range(len(active_percent)):      
        if active_percent[j] > max4: 
            max4 = active_percent[j]; 
              
    active_percent.remove(max4); 
    final_list_4.append(max4)

for i in range(3):
    temp = final_list_4[i]
    for j in range(count_row):
        if(int(data.iloc[j,1]) != 0):
            if((int(data.iloc[j,2])/int(data.iloc[j,1])) == temp):
                print("Top "+str(i+1)+" in active percentage are "+str(data.iloc[j,0]))

#Death
final_list_5 = [] 
  
for i in range(0, 3):  
    max5 = 0
      
    for j in range(len(dead)):      
        if dead[j] > max5: 
            max5 = dead[j]; 
              
    dead.remove(max5); 
    final_list_5.append(max5)

for i in range(3):
    temp = final_list_5[i]
    for j in range(count_row):
        if(data.iloc[j,4] == temp):
            print("Top "+str(i+1)+" in death are "+str(data.iloc[j,0]))

#Death Percentage
final_list_6 = [] 
  
for i in range(0, 3):  
    max6 = 0
      
    for j in range(len(dead_percent)):      
        if dead_percent[j] > max6: 
            max6 = dead_percent[j]; 
              
    dead_percent.remove(max6); 
    final_list_6.append(max6)

for i in range(3):
    temp = final_list_6[i]
    for j in range(count_row):
        if(int(data.iloc[j,1]) != 0):
            if((int(data.iloc[j,4])/int(data.iloc[j,1])) == temp):
                print("Top "+str(i+1)+" in death percentage are "+str(data.iloc[j,0]))



Place_1 = input("Enter the first district you want to compare")
#This is 2 States and 2 district wala code
place_1_row = data[data["state/ut"] == Place_1]
row_1 = [int(place_1_row["cnfrmd"]),int(place_1_row["actv"]),int(place_1_row["rcvd"]),int(place_1_row["dcsd"])]

Second_state = input("Enter the second state 2")
name_2 = Second_state.replace(' ','_')+".csv"
file_name_2 = name_2+".csv"

data_1 = pd.read_csv(file_name_2)
Place_2 = input("Enter the second district you want to compare")

place_2_row = data_1[data_1["state/ut"] == Place_2]
row_2 = [int(place_2_row["cnfrmd"]),int(place_2_row["actv"]),int(place_2_row["rcvd"]),int(place_2_row["dcsd"])]

print(row_1)
print(row_2)

x_axis = ["Total","Active","Recov","Death"]
x_pos = [i for i, _ in enumerate(x_axis)]
plt.legend()
plt.bar(x_pos,row_1,label=Place_1,color='red')
plt.bar(x_pos,row_2,label=Place_2,color='green')

plt.xlabel("Cases Types")
plt.ylabel("Count of cases")
plt.title(Place_1+" and "+Place_2+str("'s Details"))
plt.xticks(x_pos,x_axis)

plt.legend()
plt.show()


im = Image.open("Map.PNG")
im.show()
