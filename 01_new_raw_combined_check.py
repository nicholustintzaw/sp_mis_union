#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:55:42 2019

@author: nicholustintzaw
"""


####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           data migration national social pension data check and summary statistics
developed by    :           Nicholus Tint Zaw             
modified date   :           3rd Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################


## STEP 2: APPLICATION PACKAGE SETTING ##
## package setting ##

import pandas as pd
import numpy as np

col_na = ['State/Region Name', 'District Name', 'Township Name', 'Benef: Name',
       'Benef: Gender', 'Beneficiaries Reg. No.']

'''
['geo_state_region', 'cal_region', 'state_region_code',
       'geo_district', 'cal_district', 'Township Name', 'cal_dist_town',
       'cal_town', 'township_code', 'Rural or Urban',
       'Beneficiaries Reg. No.', 'benef_id']
'''


col_names = ['No.', 'State/Region Name', 'District Name', 'Township Name',
       'Rural or Urban', 'Ward', 'Village Tract', 'Village',
       'Address Detail', 'Beneficiaries Reg. No.',
       'benef_id', 'eao_yesno', 'eao_name', 'Benef: Name',
       'Benef: Gender', 'DOB Type', 'Benef: DOB Myanmar', 'Cal_DOB_MM_ENG',
       'Correct Calculation', 'Correct DOB MM to ENG', 'Benef: DOB Day',
       'Benef: DOB Month', 'Benef: DOB Year', 'Benef: DOB',
       'Enrollment End: Day', 'Enrollment End: Month', 'Enrollment End: Year',
       'Enrollment End Date', 'Age in Years', 'Age Verification Doc',
       'NRC Format', 'NRC old - Text', 'NRC old - Digits', 'NRC Old',
       'NRC - Region Code', 'cal_nrc_region', 'NRC - Township Code',
       'NRC Status', 'NRC - Digits', 'NRC New', 'Benef: Father Name']


col_person = ['Benef: Name', 'Benef: Gender', 'Age in Years', 'Benef: Father Name']


col_comb = ['No.', 'State/Region Name', 'District Name', 'Township Name',
       'Rural or Urban', 'Ward', 'Village Tract', 'Village', 'Address Detail',
       'Beneficiaries Reg. No.', 'benef_id', 'eao_yesno', 'eao_name',
       'Benef: Name', 'Benef: Gender', 'DOB Type', 'Benef: DOB Myanmar',
       'Cal_DOB_MM_ENG', 'Correct Calculation', 'Correct DOB MM to ENG',
       'Benef: DOB Day', 'Benef: DOB Month', 'Benef: DOB Year', 'Benef: DOB',
       'Enrollment End: Day', 'Enrollment End: Month', 'Enrollment End: Year',
       'Enrollment End Date', 'Age in Years', 'Age Verification Doc',
       'NRC Format', 'NRC old - Text', 'NRC old - Digits', 'NRC Old',
       'NRC - Region Code', 'cal_nrc_region', 'NRC - Township Code',
       'NRC Status', 'NRC - Digits', 'NRC New', 'Benef: Father Name',
       'source']

offices = ['12. Yangon', '09. Mandalay']

 
col_match = ['benef_id', 'Benef: Name', 'Benef: Gender', 'Age in Years', 'Benef: Father Name']


col_person = ['Benef: Name', 'Benef: Gender', 'Age in Years', 'Benef: Father Name']

'''
offices = ['01_kachin', '02_kayah', '03_kayin', '04_chin', '05_sagaing',
           '06_tanitaryi','07_bago','08_magway','09_mandalay','10_mon','11_rakhine',
           '12_yangon',"13_shan",'14_ayeyarwady','15_naypyitaw']
'''
#['01. Kachin', '02. Kayah', '03. Kayin', '04. Chin', '05. Sagaing', '06. Thanintharyi', '07. Bago', '09. Mandalay', '10. Mon', '11. Rakhine', '12. Yangon', '13. Shan', '14. Ayeyawaddy', '15. Nay Pyi Taw']

####################################################################################################
####################################################################################################

## STEP 3: COMBINED ALL COMPLETED DATA MIGRATION FIELS ##
## Combined data from each office

df_raw  = pd.DataFrame()  

sum_merge      = pd.DataFrame()


i = 1
j = 1

for file in offices :
        
    xlsxs = os.listdir(raw + file +'/_raw/')
            
    for xlsx in xlsxs :
        
        if xlsx.endswith(".xlsx"):
            print(i)
            print("now working in " + xlsx)
            
            dta_raw = pd.read_excel(raw + file + '/_raw/' + xlsx, sheet_name = '01_new_register', 
                                    skiprows = 3, header = None, index_col = False, usecols="A:AO", names = col_names)


            # drop na from selected main variables
            dta_raw = dta_raw.dropna(how = 'all', subset = col_na)
            
            #dta['geo_township'] = geo_township
            dta_raw.sort_values('Township Name')
            
            source = xlsx
            dta_raw['source'] = source
                        
        
            df_raw = df_raw.append(dta_raw)
            
            i = 1 + i
  
    
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
            
            df_comb = pd.read_excel(raw + file + '/_combined/' + xlsx, sheet_name = '01_new_register', 
                                     skiprows = 1, header = None, index_col = False, usecols="B:AQ", names = col_comb)
              

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
    
    
        
    merge = pd.merge(df_raw, df_comb, on = col_match , suffixes = ('_raw', '_comb'), 
                     indicator = 'merge', how = 'outer')
    x = merge.loc[merge['merge'] == 'both']
    y = merge.loc[merge['merge'] == 'right_only']
    z = merge.loc[merge['merge'] == 'left_only']
    
    x.count()
    y.count()
    z.count()
    
    # stata for merge
    both    = len(x.index)
    right   = len(y.index)
    left    = len(z.index)
    
    
    merge_j = {'State and Region': [file], 'Raw New Register': [tot_raw], 'Raw ID Duplicate': [dupid_raw], 'Raw Person Duplicate': [dupresp_raw],
               'Combined New Register': [tot_comb], 'Combined ID Duplicate': [dupid_comb], 'Combined Person Duplicate': [dupresp_comb],
               'Total Match': [both], 'Unmatched Raw': [left], 'Unmatched Combined': [right]}
    merge_j = pd.DataFrame(merge_j)
    sum_merge   = sum_merge.append(merge_j)
    
    
    # export as summary statistic figures for all combined data migration files 
    writer = pd.ExcelWriter(output +  file + 'raw_combined_check_result.xlsx', engine = 'xlsxwriter')
    sum_merge.to_excel(writer, sheet_name = 'summary')
    
    obs = len(z)
    if obs > 0 : 
        z.to_excel(writer, sheet_name = 'raw_unmatched')
  
    obs = len(y)
    if obs > 0 : 
        y.to_excel(writer, sheet_name = 'combined_unmatched')
      
    writer.save()
    writer.close()
    
    
    j = 1 + j



                    
           
            

## Duplicated Observation 
# duplicate by id - booleen var

# duplicate by beneficiares info - booleen var
dup_resp = df_comb.duplicated(subset = col_match, keep = False)


# duplciate by id and beneficiares info dataset
dup_resp = df_comb.loc[dup_resp == True]
            


####################################################################################################
####################################################################################################

## STEP 4: SUMMARY STATISTIC FOR DATA MIGRATION FILES ##

# use as different dataset name for summary stat figures
df_test = df

# to apply loop function to generate stat figure at district level
states = df_test['geo_state_region'].unique() 

i = 1
sum_state = pd.DataFrame()

j = 1
sum_town = pd.DataFrame()

for state in states :
    
    # keep one state/region
    df_state = df_test.loc[df_test['geo_state_region'] == state]
    
    # count the number of obs
    tot = len(df_state.index)
    
    d_i = {'state/region name': [state], 'total_benef': [tot]}
    
    dta_i = pd.DataFrame(d_i)
    sum_state = sum_state.append(dta_i)
    
    # prepare for the township level figure
    towns = df_state['Township Name'].unique() 
    

    
    for town in towns :
        
        # keep one township
        df_town = df_state.loc[df_state['Township Name'] == town]
        
        # count the number of obs
        tot = len(df_town.index)
        
        d_j = {'state/region name': [state], 'township name': [town],'total_benef': [tot]}
        
        dta_j = pd.DataFrame(d_j)
        sum_town = sum_town.append(dta_j)
        

# export as summary statistic figures for all combined data migration files 
writer = pd.ExcelWriter(output +  '01_data_migration_report_figure.xlsx', engine = 'xlsxwriter')
sum_state.to_excel(writer, sheet_name = 'by_state')
sum_town.to_excel(writer, sheet_name = 'by_township')
writer.save()
writer.close()


####################################################################################################
####################################################################################################
