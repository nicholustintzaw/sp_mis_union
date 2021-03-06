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

df_raw  = pd.DataFrame()  

i = 1

for file in offices :
    
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
                        
        
            df_raw = df_raw.append(dta)
            
            i = 1 + i
    
  
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
   

df_newreg_all = df_raw


####################################################################################################
####################################################################################################

print('Woow, just finished the New Register Sheet combinnation for final dataset, please check your outputs folder for result excel files')
