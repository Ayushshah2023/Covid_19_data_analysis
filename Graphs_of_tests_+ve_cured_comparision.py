import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#PART 1
State_name = input("Enter the state whose charts you want to plot")
name = State_name.replace(' ', '_')+".csv"
file_name = name + ".csv"
data=pd.read_csv(file_name)
data_1 = pd.read_csv("StatewiseTestingDetails.csv")
data_2 = pd.read_csv("covid_19_india.csv")
final_row = data[data["state/ut"] == "Total"]
print("The percentage of active cases in the state are")
#print(final_row[1])
print(str((float(final_row["actv"]/final_row["cnfrmd"])*100))+" %")

print("The percentage of recovered cases in the state are")
#print(final_row[1])
print(str((float(final_row["rcvd"]/final_row["cnfrmd"])*100))+" %")

print("The percentage of death cases in the state are")
#print(final_row[1])
print(str((float(final_row["dcsd"]/final_row["cnfrmd"])*100))+" %")




#PART 2
#fig = plt.figure()
N = 5
#ax = fig.add_axes([0,0,1,1])
#ax.set_ylabel('Count')
#ax.set_ylabel('Cases ka masti')

labels = ['G1', 'G2', 'G3', 'G4', 'G5']


Place_1 = input("Enter the first district you want to compare")
Place_2 = input("Enter the first district you want to compare")
place_1_row = data[data["state/ut"] == Place_1]
print(place_1_row["cnfrmd"])
row_1 = [int(place_1_row["cnfrmd"]),int(place_1_row["actv"]),int(place_1_row["rcvd"]),int(place_1_row["dcsd"])]
place_2_row = data[data["state/ut"] == Place_2]
row_2 = [int(place_2_row["cnfrmd"]),int(place_2_row["actv"]),int(place_2_row["rcvd"]),int(place_2_row["dcsd"])]
print(row_1)
print(row_2)

ind = np.arange(len(labels)) 
width = 0.35

fig,ax = plt.subplots()
x_axis = ["Total","Active","Recov","Death"]
x_pos = [i for i, _ in enumerate(x_axis)]
#plt.subplot(1, 2, 1)
ax.legend()
plt.bar(x_pos,row_1,label=Place_1,color='red')

#plt.xlabel("Cases Types")
#plt.ylabel("Count of cases")
#plt.title(Place_1+str("'s Details"))
#plt.xticks(x_pos,x_axis)
#plt.subplot(1, 2, 2)
plt.bar(x_pos,row_2,label=Place_2,color='green')

plt.xlabel("Cases Types")
plt.ylabel("Count of cases")
plt.title(Place_1+" and "+Place_2+str("'s Details"))
plt.xticks(x_pos,x_axis)
#ax.set_xticklabels(labels)
ax.legend()


#fig.tight_layout()
plt.show()

#Part 3 graphs aur sab idhar aayegaa


State_forinfo = input("Enter the state whose charts you want to plot")
data_plotting = data_1[data_1["State"]==State_forinfo]
#print(data_plotting.iloc[-1,])
Column_total_tests = data_plotting.iloc[:, 3]
Column_positive_tests = data_plotting.iloc[:,5]
print(Column_total_tests)
dates = data_plotting.iloc[:,1]
plt.subplot(2,1,1)
plt.xlabel("Day Count")
plt.ylabel("Count of cases")
plt.title("No of tests vs days passed by")
#plt.xticks(np.arange(10))
plt.plot(dates,Column_total_tests)

plt.subplot(2,1,2)
plt.xlabel("Day Count")
plt.ylabel("Count of cases")
plt.title("No of +ve tests vs days passed by")
#plt.xticks(np.arange(10))
plt.plot(dates,Column_positive_tests)
#plt.tight_layout()
plt.tight_layout()
plt.show()


#graphs for active cases and recovered cases over time          
data_plotting_2 = data_2[data_2["State/UnionTerritory"]==State_forinfo]
count_row = data_plotting_2.shape[0]
count_column = data_plotting_2.shape[1]
x_axis_list = []
for i in range(count_row):
    x_axis_list.append(i+1)
print(x_axis_list)    
print(count_row)
Column_confirmed = data_plotting_2.iloc[:,8]
print(Column_confirmed)
Column_Cured = data_plotting_2.iloc[:,6]
Column_Death = data_plotting_2.iloc[:,7]
print(Column_Cured)

plt.plot(x_axis_list,Column_confirmed,label="Confirmed")
plt.plot(x_axis_list,Column_Cured,label="Cured")
plt.plot(x_axis_list,Column_Death,label="Dead")
plt.xlabel("No.of days passing")
plt.ylabel("No.of cases")
plt.title("Trends of the all 3 day by day")
plt.legend()

plt.show()

