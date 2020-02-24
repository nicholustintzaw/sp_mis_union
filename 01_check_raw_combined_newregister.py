#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov  4 07:55:42 2019

@author: nicholustintzaw
"""


####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           new quarter - raw and combined data check - new register
developed by    :           Nicholus Tint Zaw             
modified date   :           3rd Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################

print('Now, the spyder is working on New Register Sheet, please wait for a few minutes')

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

col_nrc = ['NRC New', 'NRC Old']

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


offices = ['01_kachin', '02_kayah', '03_kayin','04_chin', '05_sagaing', '06_tanintharyi', '07_bago', '08_magwe', 
           '09_mandalay', '10_mon', '11_rakhine', '12_yangon', '13_shan', '14_ayeyarwady', '15_nay pyi taw']

 
col_match = ['benef_id', 'Benef: Name', 'Benef: Gender', 'Age in Years', 'Benef: Father Name']


col_person = ['Benef: Name', 'Benef: Gender', 'Age in Years', 'Benef: Father Name']


#['01. Kachin', '02. Kayah', '03. Kayin', '04. Chin', '05. Sagaing', '06. Thanintharyi', '07. Bago', '09. Mandalay', '10. Mon', '11. Rakhine', '12. Yangon', '13. Shan', '14. Ayeyawaddy', '15. Nay Pyi Taw']

####################################################################################################
####################################################################################################

## STEP 3: COMBINED ALL COMPLETED DATA MIGRATION FIELS ##
## Combined data from each office

sum_merge      = pd.DataFrame()


i = 1
j = 1

for file in offices :
    df_raw_j  = pd.DataFrame()  

    
    print("working in the state and region " + file)
        
    xlsxs = os.listdir(raw + file +'/_raw/')
            
    for xlsx in xlsxs :
        
        if xlsx.endswith(".xlsx"):
            print(i)
            print("now working in " + xlsx)
            
            dta = pd.read_excel(raw + file + '/_raw/' + xlsx, sheet_name = '01_new_register', 
                                    skiprows = 3, header = None, index_col = False, usecols="A:AO", names = col_names)


            # drop na from selected main variables
            dta = dta.dropna(how = 'all', subset = col_na)
            
            #dta['geo_township'] = geo_township
            dta.sort_values('Township Name')
            
            source = xlsx
            dta['source'] = source
                        
        
            df_raw_j = df_raw_j.append(dta)
            
            i = 1 + i
    
    df_raw = df_raw_j
    if len(df_raw) == 0 :
        
        col_raw = df_raw.columns
        
        for col in col_raw :
            
            df_raw[col] = df_raw[col].astype(str)
            
            
        
    # myanmar fount zero and wa lone replacement
  
    df_raw['benef_id'] = df_raw['benef_id'].astype(str)
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('ဝ', '၀')
      
    # english numeric to Myanmar numeric convertion
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('0', '၀')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('1', '၁')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('2', '၂')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('3', '၃')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('4', '၄')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('5', '၅')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('6', '၆')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('7', '၇')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('8', '၈')
    df_raw['benef_id'] = df_raw['benef_id'].str.replace('9', '၉')
    
    
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].astype(str)
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('ဝ', '၀')
      
    # english numeric to Myanmar numeric convertion
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('0', '၀')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('1', '၁')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('2', '၂')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('3', '၃')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('4', '၄')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('5', '၅')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('6', '၆')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('7', '၇')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('8', '၈')
    df_raw['Beneficiaries Reg. No.'] = df_raw['Beneficiaries Reg. No.'].str.replace('9', '၉')

     # myanmar fount zero and wa lone replacement
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].astype(str)
    
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('ဝ', '၀')
    
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].astype(str)
    
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('ဝ', '၀')
    
    
    # english numeric to Myanmar numeric convertion
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('0', '၀')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('1', '၁')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('2', '၂')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('3', '၃')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('4', '၄')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('5', '၅')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('6', '၆')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('7', '၇')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('8', '၈')
    df_raw['NRC - Digits'] = df_raw['NRC - Digits'].str.replace('9', '၉')
    
    
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('0', '၀')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('1', '၁')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('2', '၂')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('3', '၃')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('4', '၄')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('5', '၅')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('6', '၆')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('7', '၇')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('8', '၈')
    df_raw['NRC old - Digits'] = df_raw['NRC old - Digits'].str.replace('9', '၉')
   
    # Male Burmese fount Standartization
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('ကျား ', 'ကျား')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('ကျား\xa0', 'ကျား')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('ကျား', 'ကျား')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('ကျးာ', 'ကျား')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('က', 'ကျား')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('ကျားျား', 'ကျား')
    
    
    # Female Burmese fount Standartization  
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('မ ', 'မ')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('မ\xa0', 'မ')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('မ', 'မ')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('\u200bမ', 'မ')
    df_raw['Benef: Gender'] = df_raw['Benef: Gender'].str.replace('မ ', 'မ')
       

    df_newreg = df_raw
    
    # duplicate by beneficiares info - booleen var + ID
    dup_resp_raw   = df_raw.duplicated(subset = col_person, keep = False)
    dup_id_raw     = df_raw.duplicated(subset = 'benef_id', keep = False)
    
    # duplciate by id and beneficiares info dataset + ID duplicate
    dup_resp_raw   = df_raw.loc[dup_resp_raw == True]
    dup_id_raw     = df_raw.loc[dup_id_raw == True]
    
    # NRC Duplicate
    df_nrc_raw = df_raw.dropna(how = 'all', subset = col_nrc)

    dup_nrc_raw   = df_nrc_raw.duplicated(subset = col_nrc, keep = False)
    dup_nrc_raw   = df_nrc_raw.loc[dup_nrc_raw == True]

    
    ## Age Criteria Check
    age_raw = df_raw['Age in Years'] < 85
    age_raw = df_raw.loc[age_raw == True]
    
  
    # stata for raw
    tot_raw     = len(df_raw.index)
    nrc_tot_raw = len(dup_nrc_raw.index)
    age_tot_raw = len(age_raw.index)
    dupid_raw   = len(dup_id_raw.index)
    dupresp_raw = len(dup_resp_raw.index)
    

    xlsxs = os.listdir(raw + file + '/_combined/')
            
    for xlsx in xlsxs :
        
        if xlsx.endswith(".xlsx"):
            print("now working in " + xlsx)
            
            df_comb = pd.read_excel(raw + file + '/_combined/' + xlsx, sheet_name = '01_new_register', 
                                     skiprows = 1, header = None, index_col = False, usecols="B:AQ", names = col_comb)
              
    if len(df_comb) == 0 :
        
        col_comb_j = df_comb.columns
    
        for col in col_comb_j :
            
            df_comb[col] = df_comb[col].astype(str)
            
            
        
    # myanmar fount zero and wa lone replacement
  
    df_comb['benef_id'] = df_comb['benef_id'].astype(str)
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('ဝ', '၀')
      
    # english numeric to Myanmar numeric convertion
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('0', '၀')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('1', '၁')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('2', '၂')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('3', '၃')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('4', '၄')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('5', '၅')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('6', '၆')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('7', '၇')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('8', '၈')
    df_comb['benef_id'] = df_comb['benef_id'].str.replace('9', '၉')
    
    
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].astype(str)
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('ဝ', '၀')
      
    # english numeric to Myanmar numeric convertion
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('0', '၀')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('1', '၁')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('2', '၂')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('3', '၃')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('4', '၄')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('5', '၅')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('6', '၆')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('7', '၇')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('8', '၈')
    df_comb['Beneficiaries Reg. No.'] = df_comb['Beneficiaries Reg. No.'].str.replace('9', '၉')

     # myanmar fount zero and wa lone replacement
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].astype(str)
    
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('ဝ', '၀')
    
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].astype(str)
    
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('ဝ', '၀')
    
    
    # english numeric to Myanmar numeric convertion
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('0', '၀')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('1', '၁')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('2', '၂')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('3', '၃')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('4', '၄')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('5', '၅')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('6', '၆')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('7', '၇')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('8', '၈')
    df_comb['NRC - Digits'] = df_comb['NRC - Digits'].str.replace('9', '၉')
    
    
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('0', '၀')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('1', '၁')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('2', '၂')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('3', '၃')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('4', '၄')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('5', '၅')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('6', '၆')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('7', '၇')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('8', '၈')
    df_comb['NRC old - Digits'] = df_comb['NRC old - Digits'].str.replace('9', '၉')
   
    # Male Burmese fount Standartization
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('ကျား ', 'ကျား')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('ကျား\xa0', 'ကျား')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('ကျား', 'ကျား')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('ကျးာ', 'ကျား')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('က', 'ကျား')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('ကျားျား', 'ကျား')
    
    
    # Female Burmese fount Standartization  
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('မ ', 'မ')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('မ\xa0', 'မ')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('မ', 'မ')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('\u200bမ', 'မ')
    df_comb['Benef: Gender'] = df_comb['Benef: Gender'].str.replace('မ ', 'မ')
       
 

    # duplicate by beneficiares info - booleen var + ID
    dup_resp_comb   = df_comb.duplicated(subset = col_person, keep = False)
    dup_id_comb     = df_comb.duplicated(subset = 'benef_id', keep = False)
    
    # duplciate by id and beneficiares info dataset + ID duplicate
    dup_resp_comb   = df_comb.loc[dup_resp_comb == True]
    dup_id_comb     = df_comb.loc[dup_id_comb == True]
 
    # NRC Duplicate
    df_nrc_comb    = df_comb.dropna(how = 'all', subset = col_nrc)

    dup_nrc_comb   = df_nrc_comb.duplicated(subset = col_nrc, keep = False)
    dup_nrc_comb   = df_nrc_comb.loc[dup_nrc_comb == True]

    
    ## Age Criteria Check
    age_comb = df_comb['Age in Years'] < 85
    age_comb = df_comb.loc[age_comb == True]
    
  
    # stata for combined
    tot_comb     = len(df_comb.index) 
    nrc_tot_comb = len(dup_nrc_comb.index)
    age_tot_comb = len(age_comb.index)
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
    
    
    merge_j = {'State and Region': [file], 'Raw New Register': [tot_raw], 'Raw Age < 85': [age_tot_raw], 
               'Raw ID Duplicate': [dupid_raw], 'Raw Person Duplicate': [dupresp_raw],
               'Raw NRC Duplicate': [nrc_tot_raw], 
               'Combined New Register': [tot_comb], 'Combined Age < 85': [age_tot_comb], 
               'Combined ID Duplicate': [dupid_comb], 'Combined Person Duplicate': [dupresp_comb],
               'Combined NRC Duplicate': [nrc_tot_comb],
               'Total Match': [both_j], 'Unmatched Raw': [left_j], 'Unmatched Combined': [right_j]}
    merge_j = pd.DataFrame(merge_j)
    sum_merge   = sum_merge.append(merge_j)
    
    
    # export as summary statistic figures for all combined data migration files 
    sum_merge.to_excel(output + '01_newregister_raw_combined_check_result.xlsx', index = False)
    
    writer = pd.ExcelWriter(output + file + '/' + file + '_duplicated_newregister_results.xlsx', engine = 'xlsxwriter')    
    obs = len(age_raw)
    if obs > 0 : 
        age_raw.to_excel(writer, sheet_name = 'age_raw')
    
    obs = len(age_comb)
    if obs > 0 : 
        age_comb.to_excel(writer, sheet_name = 'age_comb')
    
    obs = len(dup_nrc_raw)
    if obs > 0 : 
        dup_nrc_raw.to_excel(writer, sheet_name = 'dup_nrc_raw')
    
    obs = len(dup_nrc_comb)
    if obs > 0 : 
        dup_nrc_comb.to_excel(writer, sheet_name = 'dup_nrc_comb')
     
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
        writer = pd.ExcelWriter(output + file + '/' + file + '_unmatched_newregister_results.xlsx', engine = 'xlsxwriter')    
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

print('Woow, just finished the New Register Sheet checking, please check your outputs folder for result excel files')
