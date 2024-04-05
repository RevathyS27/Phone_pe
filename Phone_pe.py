#Importing
import os
import json
import pandas as pd
import sqlalchemy
from sqlalchemy import engine
import streamlit as st
from PIL import Image
import plotly.express as px
import plotly.graph_objects as go
import matplotlib.pyplot as plt

#Data_Extraction
#Data_Extraction_From_Github_file
agg_path="C:\Users\Revathy\Desktop\Project\Phone_pe\pulse\data\aggregated\transaction\country\india\state"
Agg_state_list=os.listdir(agg_path)
#Agg_state_list
#Extracting_first_DF(Aggregated_Tx):
Agg_tnx={'State':[], 'Year':[],'Quater':[],'Transaction_type':[], 'Transaction_count':[], 'Transaction_amount':[]}
for i in Agg_state_list:
    p=agg_path+i+"/"
    Agg_year=os.listdir(p)
    for j in Agg_year:
        Pa=p+j+"/"
        Agg_yr_Qt=os.listdir(Pa)
        for k in Agg_yr_Qt:
            P1=Pa+k
            Data=open(P1,'r')
            D=json.load(Data)
            for z in D['data']['transactionData']:
                Name=z['name']
                Transaction_Count=z['paymentInstruments'][0]['count']
                Transaction_Amount=z['paymentInstruments'][0]['amount']
                Agg_tnx['State'].append(i)
                Agg_tnx['Year'].append(j)
                Agg_tnx['Quater'].append(int(k.strip('.json')))
                Agg_tnx['Transaction_type'].append(Name)
                Agg_tnx['Transaction_count'].append(Transaction_Count)
                Agg_tnx['Transaction_amount'].append(Transaction_Amount)
#Creating Dataframe
df_Agg_Transaction=pd.DataFrame(Agg_tnx)
#df_Aggregated_Trans
#Mapping States name to geojson State name
df_Agg_Transaction['State'] = df_Agg_Transaction['State'].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar Island','andhra-pradesh':'Andhra Pradesh',
                                                                     'arunachal-pradesh':'Arunanchal Pradesh','assam':'Assam','bihar':'Bihar', 
                                                                     'chandigarh':'Chandigarh','chhattisgarh':'Chhattisgarh',
                                                                     'dadra-&-nagar-haveli-&-daman-&-diu':'Dadra and Nagar Haveli and Daman and Diu', 
                                                                     'delhi': 'Delhi', 'goa':'Goa',  'gujarat': 'Gujarat','haryana':'Haryana',
                                                                     'himachal-pradesh':'Himachal Pradesh','jammu-&-kashmir':'Jammu & Kashmir', 
                                                                     'jharkhand':'Jharkhand', 'karnataka':'Karnataka', 'kerala':'Kerala', 
                                                                     'ladakh':'Ladakh', 'lakshadweep':'Lakshadweep', 
                                                                     'madhya-pradesh':'Madhya Pradesh','maharashtra':'Maharashtra', 
                                                                     'manipur':'Manipur', 'meghalaya':'Meghalaya', 'mizoram':'Mizoram', 
                                                                     'nagaland':'Nagaland','odisha':'Odisha', 'puducherry':'Puducherry', 
                                                                     'punjab':'Punjab', 'rajasthan':'Rajasthan', 'sikkim':'Sikkim',
                                                                     'tamil-nadu': 'Tamil Nadu', 'telangana':'Telangana','tripura':'Tripura', 
                                                                     'uttar-pradesh':'Uttar Pradesh','uttarakhand':'Uttarakhand', 
                                                                     'west-bengal':'West Bengal'})

#Data_Extraction_From_Github_file
User_path="C:\Users\Revathy\Desktop\Project\Phone_pe\pulse\data\aggregated\user\country\india\state"
Agg_state_list=os.listdir(User_path)
#Extracting_Second_DF(Aggregated_User):
agg_user={'State':[], 'Year':[],'Quater':[],'Brand':[], 'Counts':[], 'Percentage':[]}
for i in Agg_state_list:
    P=User_path+i+"/"
    Agg_year=os.listdir(P)
    for j in Agg_year:
        Pa=P+j+"/"
        Agg_yr_Qt=os.listdir(Pa)
        for k in Agg_yr_Qt:
            P1=Pa+k
            Data=open(P1,'r')
            D=json.load(Data)
            try:
                for z in D['data']['usersByDevice']:
                    Brand=z['brand']
                    Count=z['count']
                    Percentage=z['percentage']
                    agg_user['State'].append(i)
                    agg_user['Year'].append(j)
                    agg_user['Quater'].append(int(k.strip('.json')))
                    agg_user['Brand'].append(Brand)
                    agg_user['Counts'].append(Count)
                    agg_user['Percentage'].append(Percentage)
            except:
                pass
#Creating_DataFrame
df_Aggregated_User=pd.DataFrame(agg_user)
#df_Aggregated_Usr
#Mapping States name to geojson State name
df_Aggregated_User['State'] = df_Aggregated_User['State'].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar Island','andhra-pradesh':'Andhra Pradesh',
                                                                     'arunachal-pradesh':'Arunanchal Pradesh','assam':'Assam','bihar':'Bihar', 
                                                                     'chandigarh':'Chandigarh','chhattisgarh':'Chhattisgarh',
                                                                     'dadra-&-nagar-haveli-&-daman-&-diu':'Dadra and Nagar Haveli and Daman and Diu', 
                                                                     'delhi': 'Delhi', 'goa':'Goa',  'gujarat': 'Gujarat','haryana':'Haryana',
                                                                     'himachal-pradesh':'Himachal Pradesh','jammu-&-kashmir':'Jammu & Kashmir', 
                                                                     'jharkhand':'Jharkhand', 'karnataka':'Karnataka', 'kerala':'Kerala', 
                                                                     'ladakh':'Ladakh', 'lakshadweep':'Lakshadweep', 
                                                                     'madhya-pradesh':'Madhya Pradesh','maharashtra':'Maharashtra', 
                                                                     'manipur':'Manipur', 'meghalaya':'Meghalaya', 'mizoram':'Mizoram', 
                                                                     'nagaland':'Nagaland','odisha':'Odisha', 'puducherry':'Puducherry', 
                                                                     'punjab':'Punjab', 'rajasthan':'Rajasthan', 'sikkim':'Sikkim',
                                                                     'tamil-nadu': 'Tamil Nadu', 'telangana':'Telangana','tripura':'Tripura', 
                                                                     'uttar-pradesh':'Uttar Pradesh','uttarakhand':'Uttarakhand', 
                                                                     'west-bengal':'West Bengal'})

#Data_Extraction_From_Github_file
Map_Tnx_path="C:\Users\Revathy\Desktop\Project\Phone_pe\pulse\data\map\transaction\hover\country\india\state"
Hover_state_list=os.listdir(Map_Tnx_path)
#Extracting_Third_DF(Map_Tnx):
Map_Agg_tnx={'State':[], 'Year':[],'Quater':[],'District':[], 'Total_Count':[], 'Total_amount':[]}
for i in Hover_state_list:
    P=Map_Tnx_path+i+"/"
    Agg_year=os.listdir(P)
    for j in Agg_year:
        Pa=P+j+"/"
        Agg_yr_Qt=os.listdir(Pa)
        for k in Agg_yr_Qt:
            P1=Pa+k
            Data=open(P1,'r')
            D=json.load(Data)
            for z in D['data']['hoverDataList']:
                District=z['name']
                Total_Count=z['metric'][0]['count']
                Total_amount=z['metric'][0]['amount']
                Map_Agg_tnx['State'].append(i)
                Map_Agg_tnx['Year'].append(j)
                Map_Agg_tnx['Quater'].append(int(k.strip('.json')))
                Map_Agg_tnx['District'].append(District)
                Map_Agg_tnx['Total_Count'].append(Total_Count)
                Map_Agg_tnx['Total_amount'].append(Total_amount)
#Creating_DataFrame
df_Map_Transaction=pd.DataFrame(Map_Agg_tnx)
#df_Map_Tran
#Mapping States name to geojson State name
df_Map_Transaction['State'] = df_Map_Transaction['State'].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar Island','andhra-pradesh':'Andhra Pradesh',
                                                                     'arunachal-pradesh':'Arunanchal Pradesh','assam':'Assam','bihar':'Bihar', 
                                                                     'chandigarh':'Chandigarh','chhattisgarh':'Chhattisgarh',
                                                                     'dadra-&-nagar-haveli-&-daman-&-diu':'Dadra and Nagar Haveli and Daman and Diu', 
                                                                     'delhi': 'Delhi', 'goa':'Goa',  'gujarat': 'Gujarat','haryana':'Haryana',
                                                                     'himachal-pradesh':'Himachal Pradesh','jammu-&-kashmir':'Jammu & Kashmir', 
                                                                     'jharkhand':'Jharkhand', 'karnataka':'Karnataka', 'kerala':'Kerala', 
                                                                     'ladakh':'Ladakh', 'lakshadweep':'Lakshadweep', 
                                                                     'madhya-pradesh':'Madhya Pradesh','maharashtra':'Maharashtra', 
                                                                     'manipur':'Manipur', 'meghalaya':'Meghalaya', 'mizoram':'Mizoram', 
                                                                     'nagaland':'Nagaland','odisha':'Odisha', 'puducherry':'Puducherry', 
                                                                     'punjab':'Punjab', 'rajasthan':'Rajasthan', 'sikkim':'Sikkim',
                                                                     'tamil-nadu': 'Tamil Nadu', 'telangana':'Telangana','tripura':'Tripura', 
                                                                     'uttar-pradesh':'Uttar Pradesh','uttarakhand':'Uttarakhand', 
                                                                     'west-bengal':'West Bengal'})

#Data_Extraction_From_Github_file
Map_Usr_path="C:\Users\Revathy\Desktop\Project\Phone_pe\pulse\data\map\user\hover\country\india\state"
Hover_state_list=os.listdir(Map_Usr_path)
#Extracting_Fourth_DF(Map_User):
Map_Agg_Usr={'State':[], 'Year':[],'Quater':[],'District':[], 'RegisteredUsers':[], 'appOpens':[]}
for i in Hover_state_list:
    P=Map_Usr_path+i+"/"
    Agg_year=os.listdir(P)
    for j in Agg_year:
        Pa=P+j+"/"
        Agg_yr_Qt=os.listdir(Pa)
        for k in Agg_yr_Qt:
            P1=Pa+k
            Data=open(P1,'r')
            D=json.load(Data)
            for z in D['data']['hoverData'].items():
                District=z[0]
                RegisteredUsers=z[1]['registeredUsers']
                appOpens=z[1]['appOpens']
                Map_Agg_Usr['State'].append(i)
                Map_Agg_Usr['Year'].append(j)
                Map_Agg_Usr['Quater'].append(int(k.strip('.json')))
                Map_Agg_Usr['District'].append(District)
                Map_Agg_Usr['RegisteredUsers'].append(RegisteredUsers)
                Map_Agg_Usr['appOpens'].append(RegisteredUsers)
                
#Creating_DataFrame
df_Map_Userr=pd.DataFrame(Map_Agg_Usr)
#df_Map_Usr
#Mapping States name to geojson State name
df_Map_Userr['State'] = df_Map_Userr['State'].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar Island','andhra-pradesh':'Andhra Pradesh',
                                                                     'arunachal-pradesh':'Arunanchal Pradesh','assam':'Assam','bihar':'Bihar', 
                                                                     'chandigarh':'Chandigarh','chhattisgarh':'Chhattisgarh',
                                                                     'dadra-&-nagar-haveli-&-daman-&-diu':'Dadra and Nagar Haveli and Daman and Diu', 
                                                                     'delhi': 'Delhi', 'goa':'Goa',  'gujarat': 'Gujarat','haryana':'Haryana',
                                                                     'himachal-pradesh':'Himachal Pradesh','jammu-&-kashmir':'Jammu & Kashmir', 
                                                                     'jharkhand':'Jharkhand', 'karnataka':'Karnataka', 'kerala':'Kerala', 
                                                                     'ladakh':'Ladakh', 'lakshadweep':'Lakshadweep', 
                                                                     'madhya-pradesh':'Madhya Pradesh','maharashtra':'Maharashtra', 
                                                                     'manipur':'Manipur', 'meghalaya':'Meghalaya', 'mizoram':'Mizoram', 
                                                                     'nagaland':'Nagaland','odisha':'Odisha', 'puducherry':'Puducherry', 
                                                                     'punjab':'Punjab', 'rajasthan':'Rajasthan', 'sikkim':'Sikkim',
                                                                     'tamil-nadu': 'Tamil Nadu', 'telangana':'Telangana','tripura':'Tripura', 
                                                                     'uttar-pradesh':'Uttar Pradesh','uttarakhand':'Uttarakhand', 
                                                                     'west-bengal':'West Bengal'})


#Data_Extraction_From_Github_file
Top_Tnx_path="C:\Users\Revathy\Desktop\Project\Phone_pe\pulse\data\top\transaction\country\india\state"
Hover_state_list=os.listdir(Top_Tnx_path)
#Extracting_Fifth_DF(Top_Tnx):
Top_Dist_Trnx={'State':[], 'Year':[],'Quater':[],'District':[], 'Transaction_Count_Pin':[], 'Transaction_amount_Pin':[]}
#Top_Pin_Trnx={'State':[], 'Year':[],'Quater':[],'Pincode':[], 'Transaction_Count_Pin':[], 'Transaction_amount_Pin':[]}
for i in Hover_state_list:
    P=Top_Tnx_path+i+"/"
    Agg_year=os.listdir(P)
    for j in Agg_year:
        Pa=P+j+"/"
        Agg_yr_Qt=os.listdir(Pa)
        #print(Agg_yr_Qt)
        for k in Agg_yr_Qt:
            P1=Pa+k
            Data=open(P1,'r')
            D=json.load(Data)
            #print(D)
            for z in D['data']['districts']:
                District=z['entityName']
                Transaction_Count_Dis=z['metric']['count']
                Transaction_Amount_Dis=z['metric']['amount']
                Top_Dist_Trnx['State'].append(i)
                Top_Dist_Trnx['Year'].append(j)
                Top_Dist_Trnx['Quater'].append(int(k.strip('.json')))
                Top_Dist_Trnx['District'].append(District)
                Top_Dist_Trnx['Transaction_Count_Pin'].append(Transaction_Count_Dis)
                Top_Dist_Trnx['Transaction_amount_Pin'].append(Transaction_Amount_Dis)
df_Top_Dis_Transaction=pd.DataFrame(Top_Dist_Tnx)
#df_Top_Dis_Tran
#Mapping States name to geojson State name
df_Top_Dis_Transaction['State'] = df_Top_Dis_Transaction['State'].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar Island','andhra-pradesh':'Andhra Pradesh',
                                                                     'arunachal-pradesh':'Arunanchal Pradesh','assam':'Assam','bihar':'Bihar', 
                                                                     'chandigarh':'Chandigarh','chhattisgarh':'Chhattisgarh',
                                                                     'dadra-&-nagar-haveli-&-daman-&-diu':'Dadra and Nagar Haveli and Daman and Diu', 
                                                                     'delhi': 'Delhi', 'goa':'Goa',  'gujarat': 'Gujarat','haryana':'Haryana',
                                                                     'himachal-pradesh':'Himachal Pradesh','jammu-&-kashmir':'Jammu & Kashmir', 
                                                                     'jharkhand':'Jharkhand', 'karnataka':'Karnataka', 'kerala':'Kerala', 
                                                                     'ladakh':'Ladakh', 'lakshadweep':'Lakshadweep', 
                                                                     'madhya-pradesh':'Madhya Pradesh','maharashtra':'Maharashtra', 
                                                                     'manipur':'Manipur', 'meghalaya':'Meghalaya', 'mizoram':'Mizoram', 
                                                                     'nagaland':'Nagaland','odisha':'Odisha', 'puducherry':'Puducherry', 
                                                                     'punjab':'Punjab', 'rajasthan':'Rajasthan', 'sikkim':'Sikkim',
                                                                     'tamil-nadu': 'Tamil Nadu', 'telangana':'Telangana','tripura':'Tripura', 
                                                                     'uttar-pradesh':'Uttar Pradesh','uttarakhand':'Uttarakhand', 
                                                                     'west-bengal':'West Bengal'})

#Data_Extraction_From_Github_file
Top_User_path="C:\Users\Revathy\Desktop\Project\Phone_pe\pulse\data\top\user\country\india\state"
Hover_state_list=os.listdir(Top_User_path)

#Extracting_Seventh_DF(Top_User):
Top_agg_Usr={'State':[], 'Year':[],'Quater':[],'Name':[], 'RegisteredUsers':[]}
for i in Hover_state_list:
    P=Top_User_path+i+"/"
    Agg_year=os.listdir(P)
    for j in Agg_year:
        Pa=P+j+"/"
        Agg_yr_Qt=os.listdir(Pa)
        for k in Agg_yr_Qt:
            P1=Pa+k
            Data=open(P1,'r')
            D=json.load(Data)
            for z in D['data']['pincodes']:
                Name=z['name']
                RegisteredUsers=z['registeredUsers']
                Top_agg_Usr['State'].append(i)
                Top_agg_Usr['Year'].append(j)
                Top_agg_Usr['Quater'].append(int(k.strip('.json')))
                Top_agg_Usr['Name'].append(Name)
                Top_agg_Usr['RegisteredUsers'].append(RegisteredUsers)

#Creating Dataframe
df_Top_User=pd.DataFrame(Top_agg_Usr)
#df_Top_User
#Mapping States name to geojson State name
df_Top_User['State'] = df_Top_User['State'].replace({'andaman-&-nicobar-islands': 'Andaman & Nicobar Island','andhra-pradesh':'Andhra Pradesh',
                                                                     'arunachal-pradesh':'Arunanchal Pradesh','assam':'Assam','bihar':'Bihar', 
                                                                     'chandigarh':'Chandigarh','chhattisgarh':'Chhattisgarh',
                                                                     'dadra-&-nagar-haveli-&-daman-&-diu':'Dadra and Nagar Haveli and Daman and Diu', 
                                                                     'delhi': 'Delhi', 'goa':'Goa',  'gujarat': 'Gujarat','haryana':'Haryana',
                                                                     'himachal-pradesh':'Himachal Pradesh','jammu-&-kashmir':'Jammu & Kashmir', 
                                                                     'jharkhand':'Jharkhand', 'karnataka':'Karnataka', 'kerala':'Kerala', 
                                                                     'ladakh':'Ladakh', 'lakshadweep':'Lakshadweep', 
                                                                     'madhya-pradesh':'Madhya Pradesh','maharashtra':'Maharashtra', 
                                                                     'manipur':'Manipur', 'meghalaya':'Meghalaya', 'mizoram':'Mizoram', 
                                                                     'nagaland':'Nagaland','odisha':'Odisha', 'puducherry':'Puducherry', 
                                                                     'punjab':'Punjab', 'rajasthan':'Rajasthan', 'sikkim':'Sikkim',
                                                                     'tamil-nadu': 'Tamil Nadu', 'telangana':'Telangana','tripura':'Tripura', 
                                                                     'uttar-pradesh':'Uttar Pradesh','uttarakhand':'Uttarakhand', 
                                                                     'west-bengal':'West Bengal'})

#Data_Cleaning and Pre Processing
#df_Aggregated_Trans
print(df_Agg_Transaction.isnull().sum())

#df_Aggregated_Usr
print(df_Aggregated_User.isnull().sum())

#df_Map_Tran
print(df_Map_Transaction.isnull().sum())

#df_Map_Usr
print(df_Map_Userr.isnull().sum())

#df_Top_Dis_Tran
print(df_Top_Dis_Transaction.isnull().sum())

#df_Top_User
print(df_Top_User.isnull().sum())

#Transfering Data to Database
import mysql.connector
# Establish a connection to your MySQL database
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    auth_plugin="mysql_native_password"
)
mycursor = mydb.cursor()
#Creating database
query1='CREATE DATABASE IF NOT EXISTS Phone_Pe_Project'
mycursor.execute(query1)
mydb.commit()

#Inserting using sqlalchemy
#Aggreagted_Transaction
import sqlalchemy
from sqlalchemy import create_engine
engine =sqlalchemy. create_engine('mysql+mysqlconnector://root:root@localhost/phone_pe_project')

df_Aggregated_Trans.to_sql('aggregated_transaction', engine, if_exists = 'replace', index=False,dtype={
                                                                    "State":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Year":sqlalchemy.types.Integer,
                                                                    "Quater":sqlalchemy.types.Integer,
                                                                    "Transaction_type":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Transaction_count":sqlalchemy.types.BIGINT,
                                                                    "Transaction_amount":sqlalchemy.types.FLOAT(precision=5, asdecimal=True)})
                                                                    
#Inserting using sqlalchemy
#Aggreagted_User
import sqlalchemy
from sqlalchemy import create_engine
engine =sqlalchemy. create_engine('mysql+mysqlconnector://root:root@localhost/phone_pe_project')

df_Aggregated_User.to_sql('aggregated_user', engine, if_exists = 'replace', index=False,dtype={
                                                                    "State":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Year":sqlalchemy.types.Integer,
                                                                    "Quater":sqlalchemy.types.Integer,
                                                                    "Brand":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Counts":sqlalchemy.types.BIGINT,
                                                                    "Percentage":sqlalchemy.types.FLOAT(precision=5, asdecimal=True)})
                                                                    
#Inserting using sqlalchemy
#Map_Transaction
import sqlalchemy
from sqlalchemy import create_engine
engine =sqlalchemy. create_engine('mysql+mysqlconnector://root:root@localhost/phone_pe_project')

df_Map_Transaction.to_sql('map_transaction', engine, if_exists = 'replace', index=False,dtype={
                                                                    "State":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Year":sqlalchemy.types.Integer,
                                                                    "Quater":sqlalchemy.types.Integer,
                                                                    "District":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Total_Count":sqlalchemy.types.BIGINT,
                                                                    "Total_amount":sqlalchemy.types.FLOAT(precision=5, asdecimal=True)})
                                                                    
#Inserting using sqlalchemy
#Map_User
import sqlalchemy
from sqlalchemy import create_engine
engine =sqlalchemy. create_engine('mysql+mysqlconnector://root:root@localhost/phone_pe_project')

df_Map_Userr.to_sql('map_user', engine, if_exists = 'replace', index=False,dtype={
                                                                    "State":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Year":sqlalchemy.types.Integer,
                                                                    "Quater":sqlalchemy.types.Integer,
                                                                    "District":sqlalchemy.types.VARCHAR(length=50),
                                                                    "RegisteredUsers":sqlalchemy.types.BIGINT,
                                                                    "appOpens":sqlalchemy.types.BIGINT})
                                                                    
#Inserting using sqlalchemy
#Top_Districtwise_Transaction
import sqlalchemy
from sqlalchemy import create_engine
engine =sqlalchemy. create_engine('mysql+mysqlconnector://root:root@localhost/phone_pe_project')

df_Top_Dis_Transaction.to_sql('top_district_transaction', engine, if_exists = 'replace', index=False,dtype={
                                                                    "State":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Year":sqlalchemy.types.Integer,
                                                                    "Quater":sqlalchemy.types.Integer,
                                                                    "districts":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Transaction_Count_Pin":sqlalchemy.types.BIGINT,
                                                                    "Transaction_amount_Pin":sqlalchemy.types.FLOAT(precision=5, asdecimal=True)})

                                                                    
#Inserting using sqlalchemy
#Top_User
import sqlalchemy
from sqlalchemy import create_engine
engine =sqlalchemy. create_engine('mysql+mysqlconnector://root:root@localhost/phone_pe_project')

df_Top_User.to_sql('top_user', engine, if_exists = 'replace', index=False,dtype={
                                                                    "State":sqlalchemy.types.VARCHAR(length=50),
                                                                    "Year":sqlalchemy.types.Integer,
                                                                    "Quater":sqlalchemy.types.Integer,
                                                                    "Name":sqlalchemy.types.VARCHAR(length=50),
                                                                    "RegisteredUsers":sqlalchemy.types.BIGINT,})
tab1, tab2 = st.tabs(["***EXPLORE_DATA***","***ANALYSIS***"])
with tab1:
    col1,col2,col3=st.columns(3)
    with col1:
        selected_Year = st.selectbox("Select Year", ["2018", "2019", "2020", "2021", "2022","2023"])
    with col2:
        selected_Quater = st.selectbox("Select Quater", ["1", "2", "3", "4"])
    with col3:
        selected_Type = st.selectbox("Select Type", [ "map_transaction", "map_user"])
    # Specify the correct column name for coloring based on the selected type
    color_column = "Total_amount" if selected_Type == "map_transaction" else "RegisteredUsers"

    sql = f"SELECT * FROM {selected_Type} WHERE year = {selected_Year} AND quater = {selected_Quater}"
    engine =sqlalchemy. create_engine('mysql+mysqlconnector://root:root@localhost/phone_pe_project')
    mysql_df = pd.read_sql_query(sql, engine.connect(), index_col=None, chunksize=None)
    print(mysql_df)
    fig = px.choropleth(
        mysql_df,
        geojson="https://gist.githubusercontent.com/jbrobst/56c13bbbf9d97d187fea01ca62ea5112/raw/e388c4cae20aa53cb5090210a42ebb9b765c0a36/india_states.geojson",
        featureidkey='properties.ST_NM',
        locations='State',
        color=color_column,
        range_color= (0,1000000000),
        color_continuous_scale='viridis'
    )

    fig.update_geos(fitbounds="locations",visible=False)  # To show up the Indian boundaries
    st.plotly_chart(fig,use_container_width=True)
with tab2:
    import streamlit as st
    # Define function to generate list of particular states
    def Particular_state():
        # Your logic to fetch particular states goes here
        particular_states = [ 'Andaman & Nicobar Island','Andhra Pradesh','Arunanchal Pradesh','Assam','Bihar','Chandigarh','Chhattisgarh',
                                'Dadra and Nagar Haveli and Daman and Diu','Delhi', 'Goa',   'Gujarat','Haryana','Himachal Pradesh','Jammu & Kashmir', 
                                'Jharkhand','Karnataka','Kerala','Ladakh', 'Lakshadweep','Madhya Pradesh','Maharashtra', 
                                'Manipur', 'Meghalaya', 'Mizoram','Nagaland','Odisha', 'Puducherry','Punjab', 'Rajasthan', 'Sikkim',
                                'Tamil Nadu', 'Telangana','Tripura','Uttar Pradesh','Uttarakhand','West Bengal']  # Example list of states
        return particular_states
    # Add options for select box
    options = ['All India'] + Particular_state()
    # Create select box
    select_state = st.selectbox("State", options)
    select_Year = st.selectbox("Year", ["2018", "2019", "2020", "2021", "2022", "2023"])
    select_Quater = st.selectbox("Quater", ["1", "2", "3", "4"])
    select_Type = st.selectbox("Type", ["aggregated_transaction", "aggregated_user", "map_transaction", "map_user", "top_district_transaction", "top_pincode_transaction", "top_user"])
    select_graph = st.selectbox("Graph", ['Bar', "Pie"])

