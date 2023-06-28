#==========[IMPORT LIBRARIES]==========#

# Cloning Libraries
import requests
import subprocess

# File Handling libraries
import pandas as pd
import os
import json

# SQL Libraries
import mysql.connector
import sqlalchemy
from sqlalchemy import create_engine

#==========[CLONING OF GITHUB REPOSITORY URL]==========#

# Cloning of the required GitHub repository url
response = requests.get('https://api.github.com/repos/PhonePe/pulse')
repo = response.json()
clone_url = repo['clone_url']

# Specify the local directory path and clone the repository
clone_dir = "C:/phonepe_pulse"
subprocess.run(["git", "clone", clone_url, clone_dir], check=True)

# ==========[DATA PROCESSING]==========#

# Processing the Aggregated data, Map data and Top data

# AGGREGATE DATA --> TRANSACTION

path_1 = "C:/phonepe_pulse/data/aggregated/transaction/country/india/state/"
Agg_trans_state_list = os.listdir(path_1)
Agg_trans = {'State': [], 'Year': [], 'Quarter': [], 'Transaction_type': [], 'Transaction_count': [],
             'Transaction_amount': []}

for i in Agg_trans_state_list:
    p_i = path_1 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            A = json.load(Data)

            for l in A['data']['transactionData']:
                Name = l['name']
                count = l['paymentInstruments'][0]['count']
                amount = l['paymentInstruments'][0]['amount']
                Agg_trans['State'].append(i)
                Agg_trans['Year'].append(j)
                Agg_trans['Quarter'].append(int(k.strip('.json')))
                Agg_trans['Transaction_type'].append(Name)
                Agg_trans['Transaction_count'].append(count)
                Agg_trans['Transaction_amount'].append(amount)

df_aggregated_transaction = pd.DataFrame(Agg_trans)

# AGGREGATED DATA -> USER

path_2 = "C:/phonepe_pulse/data/aggregated/user/country/india/state/"
Agg_user_state_list = os.listdir(path_2)

Agg_user = {'State': [], 'Year': [], 'Quarter': [], 'Brands': [], 'User_Count': [], 'User_Percentage': []}

for i in Agg_user_state_list:
    p_i = path_2 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            B = json.load(Data)

            try:
                for l in B["data"]["usersByDevice"]:
                    brand_name = l["brand"]
                    count_ = l["count"]
                    ALL_percentage = l["percentage"]
                    Agg_user["State"].append(i)
                    Agg_user["Year"].append(j)
                    Agg_user["Quarter"].append(int(k.strip('.json')))
                    Agg_user["Brands"].append(brand_name)
                    Agg_user["User_Count"].append(count_)
                    Agg_user["User_Percentage"].append(ALL_percentage * 100)
            except:
                pass

df_aggregated_user = pd.DataFrame(Agg_user)

# MAP DATA --> TRANSACTION

path_3 = "C:/phonepe_pulse/data/map/transaction/hover/country/india/state/"
map_trans_state_list = os.listdir(path_3)

map_trans = {'State': [], 'Year': [], 'Quarter': [], 'District': [], 'Transaction_Count': [], 'Transaction_Amount': []}

for i in map_trans_state_list:
    p_i = path_3 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            C = json.load(Data)

            for l in C["data"]["hoverDataList"]:
                District = l["name"]
                count = l["metric"][0]["count"]
                amount = l["metric"][0]["amount"]
                map_trans['State'].append(i)
                map_trans['Year'].append(j)
                map_trans['Quarter'].append(int(k.strip('.json')))
                map_trans["District"].append(District)
                map_trans["Transaction_Count"].append(count)
                map_trans["Transaction_Amount"].append(amount)

df_map_transaction = pd.DataFrame(map_trans)

# MAP DATA --> USER

path_4 = "C:/phonepe_pulse/data/map/user/hover/country/india/state/"
map_user_state_list = os.listdir(path_4)

map_user = {"State": [], "Year": [], "Quarter": [], "District": [], "Registered_User": []}

for i in map_user_state_list:
    p_i = path_4 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            D = json.load(Data)

            for l in D["data"]["hoverData"].items():
                district = l[0]
                registereduser = l[1]["registeredUsers"]
                map_user['State'].append(i)
                map_user['Year'].append(j)
                map_user['Quarter'].append(int(k.strip('.json')))
                map_user["District"].append(district)
                map_user["Registered_User"].append(registereduser)

df_map_user = pd.DataFrame(map_user)

# TOP DATA --> TRANSACTION

path_5 = "C:/phonepe_pulse/data/top/transaction/country/india/state/"
top_trans_state_list = os.listdir(path_5)

top_trans = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Transaction_count': [],
             'Transaction_amount': []}

for i in top_trans_state_list:
    p_i = path_5 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            E = json.load(Data)

            for l in E['data']['pincodes']:
                Name = l['entityName']
                count = l['metric']['count']
                amount = l['metric']['amount']
                top_trans['State'].append(i)
                top_trans['Year'].append(j)
                top_trans['Quarter'].append(int(k.strip('.json')))
                top_trans['District_Pincode'].append(Name)
                top_trans['Transaction_count'].append(count)
                top_trans['Transaction_amount'].append(amount)

df_top_transaction = pd.DataFrame(top_trans)

# TOP DATA --> USER

path_6 = "C:/phonepe_pulse/data/top/user/country/india/state/"
top_user_state_list = os.listdir(path_6)

top_user = {'State': [], 'Year': [], 'Quarter': [], 'District_Pincode': [], 'Registered_User': []}

for i in top_user_state_list:
    p_i = path_6 + i + "/"
    Agg_yr = os.listdir(p_i)

    for j in Agg_yr:
        p_j = p_i + j + "/"
        Agg_yr_list = os.listdir(p_j)

        for k in Agg_yr_list:
            p_k = p_j + k
            Data = open(p_k, 'r')
            F = json.load(Data)

            for l in F['data']['pincodes']:
                Name = l['name']
                registeredUser = l['registeredUsers']
                top_user['State'].append(i)
                top_user['Year'].append(j)
                top_user['Quarter'].append(int(k.strip('.json')))
                top_user['District_Pincode'].append(Name)
                top_user['Registered_User'].append(registeredUser)

df_top_user = pd.DataFrame(top_user)

#  =============     CONNECT SQL SERVER  /   CREAT DATA BASE    /  CREAT TABLE    /    STORE DATA    ========  #

# Connect to the MySQL server
mydb = mysql.connector.connect(
  host = "localhost",
  user = "root",
  password = "root",
  auth_plugin = "mysql_native_password"
)

# Create a new database and use
mycursor = mydb.cursor()
mycursor.execute("CREATE DATABASE IF NOT EXISTS phonepe_pulse")

# Close the cursor and database connection
mycursor.close()
mydb.close()

# Connect to the new created database
engine = create_engine('mysql+mysqlconnector://root:root@localhost/phonepe_pulse', echo=False)

# Use pandas to insert the DataFrames datas to the SQL Database -> table1

# 1
df_aggregated_transaction.to_sql('aggregated_transaction', engine, if_exists = 'replace', index=False,
                                 dtype={'State': sqlalchemy.types.VARCHAR(length=50),
                                       'Year': sqlalchemy.types.Integer,
                                       'Quarter': sqlalchemy.types.Integer,
                                       'Transaction_type': sqlalchemy.types.VARCHAR(length=50),
                                       'Transaction_count': sqlalchemy.types.Integer,
                                       'Transaction_amount': sqlalchemy.types.FLOAT(precision=5, asdecimal=True)})
# 2
df_aggregated_user.to_sql('aggregated_user', engine, if_exists = 'replace', index=False,
                          dtype={'State': sqlalchemy.types.VARCHAR(length=50),
                                 'Year': sqlalchemy.types.Integer,
                                 'Quarter': sqlalchemy.types.Integer,
                                 'Brands': sqlalchemy.types.VARCHAR(length=50),
                                 'User_Count': sqlalchemy.types.Integer,
                                 'User_Percentage': sqlalchemy.types.FLOAT(precision=5, asdecimal=True)})
# 3
df_map_transaction.to_sql('map_transaction', engine, if_exists = 'replace', index=False,
                          dtype={'State': sqlalchemy.types.VARCHAR(length=50),
                                 'Year': sqlalchemy.types.Integer,
                                 'Quarter': sqlalchemy.types.Integer,
                                 'District': sqlalchemy.types.VARCHAR(length=50),
                                 'Transaction_Count': sqlalchemy.types.Integer,
                                 'Transaction_Amount': sqlalchemy.types.FLOAT(precision=5, asdecimal=True)})
# 4
df_map_user.to_sql('map_user', engine, if_exists = 'replace', index=False,
                   dtype={'State': sqlalchemy.types.VARCHAR(length=50),
                          'Year': sqlalchemy.types.Integer,
                          'Quarter': sqlalchemy.types.Integer,
                          'District': sqlalchemy.types.VARCHAR(length=50),
                          'Registered_User': sqlalchemy.types.Integer, })
# 5
df_top_transaction.to_sql('top_transaction', engine, if_exists = 'replace', index=False,
                         dtype={'State': sqlalchemy.types.VARCHAR(length=50),
                                'Year': sqlalchemy.types.Integer,
                                'Quarter': sqlalchemy.types.Integer,
                                'District_Pincode': sqlalchemy.types.Integer,
                                'Transaction_count': sqlalchemy.types.Integer,
                                'Transaction_amount': sqlalchemy.types.FLOAT(precision=5, asdecimal=True)})
# 6
df_top_user.to_sql('top_user', engine, if_exists = 'replace', index=False,
                   dtype={'State': sqlalchemy.types.VARCHAR(length=50),
                          'Year': sqlalchemy.types.Integer,
                          'Quarter': sqlalchemy.types.Integer,
                          'District_Pincode': sqlalchemy.types.Integer,
                          'Registered_User': sqlalchemy.types.Integer,})

