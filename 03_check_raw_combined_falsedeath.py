#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:55:42 2019

@author: nicholustintzaw
"""


####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           quaterly data combine and check - false death
developed by    :           Nicholus Tint Zaw             
modified date   :           7th Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################

print('Now, the spyder is working on False Death in Sheet, please wait for a few minutes')

## STEP 2: APPLICATION PACKAGE SETTING ##
## package setting ##

import pandas as pd
import numpy as np


####################################################################################################

# columns name assignment

col_na = ['benef_id']


col_names = ['No.', 'benef_id', 'Benef: Name']


col_person = ['Benef: Name']

col_match = ['benef_id', 'Benef: Name']

col_comb = ['No.', 'benef_id', 'Benef: Name', 'source']


#sheet = ['01_new_register', '02_moved_in', '03_false_death_in', '04_death', '05_moved_out', '06_false_register']




####################################################################################################
####################################################################################################

## STEP 3: COMBINED ALL COMPLETED DATA MIGRATION FIELS ##
## Combined data from each office

sum_merge      = pd.DataFrame()


i = 1
j = 1

for file in offices :
    
    df_raw_j        = pd.DataFrame()  
    
    print("working in the state and region " + file)
        
    xlsxs = os.listdir(raw + file +'/_raw/')
            
    for xlsx in xlsxs :
        
        if xlsx.endswith(".xlsx"):
            print(i)
            print("now working in " + xlsx)
            
            dta = pd.read_excel(raw + file + '/_raw/' + xlsx, sheet_name = '03_false_death_in', \
                            skiprows = 3, header = None, index_col = False, usecols="A:C", names = col_names)


            # drop na from selected main variables
            dta = dta.dropna(how = 'all', subset = col_na)
            
            #dta['geo_township'] = geo_township
            dta.sort_values('benef_id')
            
            source = xlsx
            dta['source'] = source
                        
        
            df_raw_j = df_raw_j.append(dta)
            
            i = 1 + i
    
    df_raw = df_raw_j
    if len(df_raw) == 0 :
        
        col_raw = df_raw.columns
        
        for col in col_raw :
            
            df_raw[col] = df_raw[col].astype(str)
    
     
    
    # duplicate by beneficiares info - booleen var + ID
    dup_resp_raw   = df_raw.duplicated(subset = col_person, keep = False)
    dup_id_raw     = df_raw.duplicated(subset = 'benef_id', keep = False)
    
    # duplciate by id and beneficiares info dataset + ID duplicate
    dup_resp_raw   = df_raw.loc[dup_resp_raw == True]
    dup_id_raw     = df_raw.loc[dup_id_raw == True]
  
    # stata for raw
    tot_raw     = len(df_raw.index)
    dupid_raw   = len(dup_id_raw.index)
    dupresp_raw = len(dup_resp_raw.index)
    

    xlsxs = os.listdir(raw + file + '/_combined/')
            
    for xlsx in xlsxs :
        
        if xlsx.endswith(".xlsx"):
            print("now working in " + xlsx)
                 
            df_comb = pd.read_excel(raw + file + '/_combined/' + xlsx, sheet_name = '03_false_death_in', 
                                     skiprows = 1, header = None, index_col = False, usecols="B:E", names = col_comb)
              

    if len(df_comb) == 0 :
        
        col_comb_j = df_comb.columns
    
        for col in col_comb_j :
            
            df_comb[col] = df_comb[col].astype(str)
        

    # duplicate by beneficiares info - booleen var + ID
    dup_resp_comb   = df_comb.duplicated(subset = col_person, keep = False)
    dup_id_comb     = df_comb.duplicated(subset = 'benef_id', keep = False)
    
    # duplciate by id and beneficiares info dataset + ID duplicate
    dup_resp_comb   = df_comb.loc[dup_resp_comb == True]
    dup_id_comb     = df_comb.loc[dup_id_comb == True]
    
    
    # stata for combined
    tot_comb     = len(df_comb.index)  
    dupid_comb   = len(dup_id_comb.index)
    dupresp_comb = len(dup_resp_comb.index)   
    
    
        
    merge_j = pd.merge(df_raw, df_comb, on = col_match , suffixes = ('_raw', '_comb'), 
                     indicator = 'merge', how = 'outer')
    x_j = merge_j.loc[merge_j['merge'] == 'both']
    y_j = merge_j.loc[merge_j['merge'] == 'right_only']
    z_j = merge_j.loc[merge_j['merge'] == 'left_only']
    
    x_j.count()
    y_j.count()
    z_j.count()
    
    # stata for merge
    both_j    = len(x_j.index)
    right_j   = len(y_j.index)
    left_j    = len(z_j.index)
    
    
    merge_j = {'State and Region': [file], 'Raw False Death In': [tot_raw], 'Raw ID Duplicate': [dupid_raw], 'Raw Person Duplicate': [dupresp_raw],
               'Combined Flase Death In': [tot_comb], 'Combined ID Duplicate': [dupid_comb], 'Combined Person Duplicate': [dupresp_comb],
               'Total Match': [both_j], 'Unmatched Raw': [left_j], 'Unmatched Combined': [right_j]}
    merge_j = pd.DataFrame(merge_j)
    sum_merge   = sum_merge.append(merge_j)
    
    
    # export as summary statistic figures for all combined data migration files 
    sum_merge.to_excel(output + '03_flase_deathin_raw_combined_check_result.xlsx', index = False)
    
   
    writer = pd.ExcelWriter(output + file + '/' + file + '_duplicated_falsedeath_results.xlsx', engine = 'xlsxwriter')    
    obs = len(dup_id_raw)
    if obs > 0 : 
        dup_id_raw.to_excel(writer, sheet_name = 'dup_id_raw')
  
    obs = len(dup_resp_raw)
    if obs > 0 : 
        dup_resp_raw.to_excel(writer, sheet_name = 'dup_resp_raw')
        
    obs = len(dup_id_comb)
    if obs > 0 : 
        dup_id_comb.to_excel(writer, sheet_name = 'dup_id_comb')
  
    obs = len(dup_resp_comb)
    if obs > 0 : 
        dup_resp_comb.to_excel(writer, sheet_name = 'dup_resp_comb')
      
    writer.save()
    writer.close()
    
    obs_z = len(z_j)
    obs_y = len(y_j)
    
    if obs_z > 0 | obs_y >0 :  
        writer = pd.ExcelWriter(output + file + '/' + file + '_unmatched_falsedeath_results.xlsx', engine = 'xlsxwriter')    
        obs = len(z_j)
        if obs > 0 : 
            z_j.to_excel(writer, sheet_name = 'raw_unmatched')
      
        obs = len(y_j)
        if obs > 0 : 
            y_j.to_excel(writer, sheet_name = 'combined_unmatched')
          
        writer.save()
        writer.close()
    
    
    j = 1 + j


####################################################################################################
####################################################################################################

print('Woow, just finished the False Death in checking, please check your outputs folder for result excel files')

