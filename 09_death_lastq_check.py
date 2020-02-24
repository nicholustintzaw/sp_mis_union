#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:55:42 2019

@author: nicholustintzaw
"""


####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           quaterly data combine and check - moved in
developed by    :           Nicholus Tint Zaw             
modified date   :           7th Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################

print('Now, the spyder is working on Death Sheet, please wait for a few minutes')


## STEP 2: APPLICATION PACKAGE SETTING ##
## package setting ##

import pandas as pd
import numpy as np


####################################################################################################

# columns name assignment

col_na = ['benef_id']


col_names = ['No.', 'benef_id', 'Benef: Name', 'Status: Date', 'Status Month', 'Status: Year', 'Status Date']


col_person = ['Benef: Name']


####################################################################################################
####################################################################################################

## STEP 3: COMBINED ALL COMPLETED DATA MIGRATION FIELS ##
## Combined data from each office
df_raw         = pd.DataFrame()  

i = 1

for file in offices :
    
    print("working in the state and region " + file)
        
    xlsxs = os.listdir(raw + file +'/_raw/')
            
    for xlsx in xlsxs :
        
        if xlsx.endswith(".xlsx"):
            print(i)
            print("now working in " + xlsx)
            
            dta_raw = pd.read_excel(raw + file + '/_raw/' + xlsx, sheet_name = '04_death', \
                            skiprows = 3, header = None, index_col = False, usecols="A:G", names = col_names)


            # drop na from selected main variables
            dta_raw = dta_raw.dropna(how = 'all', subset = col_na)
            
            #dta['geo_township'] = geo_township
            dta_raw.sort_values('benef_id')
            
            source = xlsx
            dta_raw['source'] = source
                        
        
            df_raw = df_raw.append(dta_raw)
            
            i = 1 + i

df_test = df_raw

####################################################################################################
####################################################################################################

## STEP 4: SUMMARY STATISTIC FOR DATA MIGRATION FILES ##

# use as different dataset name for summary stat figures

obs = len(df_test.index)
if obs > 0 :

    
    # myanmar fount zero and wa lone replacement
    df_test['benef_id'] = df_test['benef_id'].astype(str)
    
    df_test['benef_id'] = df_test['benef_id'].str.replace('ဝ', '၀')
      
    # english numeric to Myanmar numeric convertion
    df_test['benef_id'] = df_test['benef_id'].str.replace('0', '၀')
    df_test['benef_id'] = df_test['benef_id'].str.replace('1', '၁')
    df_test['benef_id'] = df_test['benef_id'].str.replace('2', '၂')
    df_test['benef_id'] = df_test['benef_id'].str.replace('3', '၃')
    df_test['benef_id'] = df_test['benef_id'].str.replace('4', '၄')
    df_test['benef_id'] = df_test['benef_id'].str.replace('5', '၅')
    df_test['benef_id'] = df_test['benef_id'].str.replace('6', '၆')
    df_test['benef_id'] = df_test['benef_id'].str.replace('7', '၇')
    df_test['benef_id'] = df_test['benef_id'].str.replace('8', '၈')
    df_test['benef_id'] = df_test['benef_id'].str.replace('9', '၉')

    df_death = df_test
    
    df_death_x = df_death[['benef_id', 'Benef: Name', 'source']]

    df_death_x.rename(columns={'benef_id':'death_id', 'Benef: Name': 'death_name'}, inplace=True)
    
    
    merge_j = pd.merge(df_last_x, df_death_x, left_on = ['benef_id_new'], 
                       right_on = ['death_id'],
                       indicator = 'merge', how = 'outer')
    
    
    x_j = merge_j.loc[merge_j['merge'] == 'both']
    y_j = merge_j.loc[merge_j['merge'] == 'right_only']
    z_j = merge_j.loc[merge_j['merge'] == 'left_only']
    
    x_j.count()
    y_j.count()
    z_j.count()
    
    #, 'Benef: Name' , 'death_name'
    #df_death_remain = y_j
   # df_death_remain = df_death_remain.drop(['death_id', 'death_name', 'merge'], axis = 1)
    #df_death_remain = df_death_remain.drop(['merge'], axis = 1)
        
        
    #merge_j = pd.merge(df_last_x, df_death, on = ['benef_id', 'Benef: Name'] , suffixes = ('_last', '_new'), 
    #                 indicator = 'merge', how = 'outer')

    #merge_j = pd.merge(df_last_x, df_death_x,  left_on = ['benef_id', 'Benef: Name'], 
                       #right_on = ['death_id', 'death_name'],
                       #indicator = 'merge', how = 'outer')
                       
                       
                    #   on = ['benef_id'] , suffixes = ('_last', '_new'), 
                    # indicator = 'merge', how = 'outer')

    
    #x_j = merge_j.loc[merge_j['merge'] == 'both']
    #y_j = merge_j.loc[merge_j['merge'] == 'right_only']
    #z_j = merge_j.loc[merge_j['merge'] == 'left_only']
    
    #x_j.count()
    #y_j.count()
    #z_j.count()
    
    
    # export as summary statistic figures for all combined data migration files 
    #dup_resp.to_excel(output + qrt + '_dup_person.xlsx', index = False)
    obs_x = len(x_j)
    obs_y = len(y_j)
    
    if obs_x > 0 | obs_y > 0 : 
        writer = pd.ExcelWriter(output + '04_death_notfound_olddata.xlsx', engine = 'xlsxwriter')
       
        obs = len(x_j)
        if obs > 0 : 
            x_j.to_excel(writer, sheet_name = 'matched')
       
        obs = len(y_j)
        if obs > 0 : 
            y_j.to_excel(writer, sheet_name = 'not_matched')
    
        writer.save()
        writer.close()
        

            
####################################################################################################
####################################################################################################

print('Woow, just finished the death Sheet checking, please check your outputs folder for result excel files')



