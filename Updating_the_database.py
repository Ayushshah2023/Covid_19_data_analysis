import os
import csv
import requests
import matplotlib.pyplot as plt
import numpy as np

url = 'https://api.covid19india.org/state_district_wise.json'
headers = ['state/ut', 'cnfrmd', 'actv', 'rcvd', 'dcsd']
def get_covid_data(url):
    raw = requests.get(url)
    raw_dict = raw.json()
    working_path = "E:\PYTHON\Covid-19-India\Attempt 01\covid19india-master"

    print(raw_dict.keys())
    for state in raw_dict.keys():
        total_cases = 0
        total_active_case = 0
        total_recovery = 0
        total_death = 0
        state_data = raw_dict[state]["districtData"]
        name = state.replace(' ', '_')+".csv"
        file_name = name + ".csv"
        file_path = os.path.join(working_path, file_name)
        with open(file_path, "w",newline='') as fp:
            csv_writer = csv.writer(fp)
            csv_writer.writerow(headers)
            for key, value in state_data.items():
                total_cases+=int(value["confirmed"])
                total_active_case+=int(value["active"])
                total_recovery+=int(value["recovered"])
                total_death+=int(value["deceased"])
                
                temp_row = [key, value["confirmed"], value["active"], value["recovered"], value["deceased"]]
                csv_writer.writerow(temp_row)
            final_row = ["Total",total_cases,total_active_case,total_recovery,total_death]
            csv_writer.writerow(final_row)


print(get_covid_data(url))

State_name = input("Enter the state whose charts you want to plot")
