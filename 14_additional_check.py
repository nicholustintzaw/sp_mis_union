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

print('Now, the spyder is working on Moved in Sheet, please wait for a few minutes')


## STEP 2: APPLICATION PACKAGE SETTING ##
## package setting ##

import pandas as pd
import numpy as np


####################################################################################################

# columns name assignment
offices = ['01_kachin', '02_kayah', '03_kayin','04_chin', '05_sagaing', '06_tanintharyi', '07_bago', '08_magwe', 
           '09_mandalay', '10_mon', '11_rakhine', '12_yangon', '13_shan', '14_ayeyarwady', '15_nay pyi taw']


col_drop = ['sirnum', 'benef_id', 'Benef: Name']

col_na = ['benef_id', 'Benef: Name']

   
col_update = ['benef_sirnum_new', 'State/Region Name', 'District Name',
       'Township Name', 'Rural or Urban', 'Ward', 'Village', 'Village Tract',
       'benef_id_new', 'Benef: Name', 'Benef: Gender', 'Benef: Father Name',
       'Age Verification Doc', 'NRC New', 'NRC Old', 'Address Detail',
       'eao_yesno', 'eao_name', 'source', 'benef_id_old', 'benef_id',
       'program_code', 'region_code', 'town_code', 'Beneficiaries Reg. No.',
       'benef_sirnum', 'benef_sirnum_new_str', 'benef_sirnum_len',
       'benef_sirnum_final', 'master_region_code', 'master_towncode',
       'dist_town', 'DOB Type', 'Benef: DOB Myanmar', 'Benef: DOB Day',
       'Benef: DOB Month', 'Benef: DOB Year', 'Benef: DOB', 'Cal_DOB_MM_ENG',
       'benef_dob_mm', 'Correct Calculation', 'Correct DOB MM to ENG',
       'Enrollment End Date', 'Enrollment End: Day', 'Enrollment End: Month',
       'Enrollment End: Year', 'Age in Years', 'NRC Format', 'NRC old - Text',
       'NRC old - Digits', 'NRC - Region Code', 'NRC - Township Code',
       'NRC Status', 'NRC - Digits', 'State/Region Code', 'Township Code',
       'cal_dist_town', 'cal_district', 'cal_nrc_region', 'cal_region',
       'cal_town', 'state_region_code', 'township_code', 'No.', 'sr_no']


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



####################################################################################################
####################################################################################################

## previous existing quarter update dataset ##
dta = pd.read_excel(db + qrt + '.xlsx', 
                        skiprows = 1, header = None, index_col = False, names = col_update)

'''
# myanmar fount zero and wa lone replacement
dta['benef_id'] = dta['benef_id'].astype(str)
dta['benef_id'] = dta['benef_id'].str.replace('ဝ', '၀')

# english numeric to Myanmar numeric convertion
dta['benef_id'] = dta['benef_id'].str.replace('0', '၀')
dta['benef_id'] = dta['benef_id'].str.replace('1', '၁')
dta['benef_id'] = dta['benef_id'].str.replace('2', '၂')
dta['benef_id'] = dta['benef_id'].str.replace('3', '၃')
dta['benef_id'] = dta['benef_id'].str.replace('4', '၄')
dta['benef_id'] = dta['benef_id'].str.replace('5', '၅')
dta['benef_id'] = dta['benef_id'].str.replace('6', '၆')
dta['benef_id'] = dta['benef_id'].str.replace('7', '၇')
dta['benef_id'] = dta['benef_id'].str.replace('8', '၈')
dta['benef_id'] = dta['benef_id'].str.replace('9', '၉')
'''

## to drop from previous update data ##
## Combined data from each office

df_to_drop  = pd.DataFrame()  


i = 1
       
xlsxs = os.listdir(raw +'_additional_action/')
        
for xlsx in xlsxs :
    
    if xlsx.endswith(".xlsx"):
        print(i)
        print("now working in " + xlsx)
        
        dta_raw = pd.read_excel(raw + '_additional_action/' + xlsx, sheet_name = '02_exit_correction', 
                                skiprows = 3, header = None, index_col = False, usecols="A:C", names = col_drop)


        # drop na from selected main variables
        dta_raw = dta_raw.dropna(how = 'all', subset = col_na)
        
        #dta['geo_township'] = geo_township
        dta_raw.sort_values('benef_id')
        
        source = xlsx
        dta_raw['source'] = source
                    
    
        df_to_drop = df_to_drop.append(dta_raw)
        
        i = 1 + i

   
# myanmar fount zero and wa lone replacement
df_to_drop['benef_id'] = df_to_drop['benef_id'].astype(str)
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('ဝ', '၀')
  
# english numeric to Myanmar numeric convertion
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('0', '၀')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('1', '၁')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('2', '၂')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('3', '၃')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('4', '၄')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('5', '၅')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('6', '၆')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('7', '၇')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('8', '၈')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('9', '၉')


df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('.', '/')
df_to_drop['benef_id'] = df_to_drop['benef_id'].str.replace('//', '/')


#df_to_drop.to_excel(report + 'test_drop.xlsx', index = False)



# duplicate by beneficiares info - booleen var + ID
dup_drop   = df_to_drop.duplicated(subset = 'benef_id', keep = False)

# duplciate by id and beneficiares info dataset + ID duplicate
dup_drop   = df_to_drop.loc[dup_drop == True]

if len(dup_drop) > 0 :
    dup_drop.to_excel(report + '00_additional_to_drop_duplicate.xlsx', index = False)

    


## to correct at previous update data ##
## Combined data from each office

df_to_correct  = pd.DataFrame()  


i = 1
       
xlsxs = os.listdir(raw +'_additional_action/')
        
for xlsx in xlsxs :
    
    if xlsx.endswith(".xlsx"):
        print(i)
        print("now working in " + xlsx)
        
        dta_raw = pd.read_excel(raw + '_additional_action/' + xlsx, sheet_name = '03_info_correction', 
                                skiprows = 3, header = None, index_col = False, usecols="A:AO", names = col_names)


        # drop na from selected main variables
        dta_raw = dta_raw.dropna(how = 'all', subset = col_na)
        
        #dta['geo_township'] = geo_township
        dta_raw.sort_values('benef_id')
        
        source = xlsx
        dta_raw['source'] = source
                    
    
        df_to_correct = df_to_correct.append(dta_raw)
        
        i = 1 + i



       
# myanmar fount zero and wa lone replacement
df_to_correct['benef_id'] = df_to_correct['benef_id'].astype(str)
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('ဝ', '၀')
  
# english numeric to Myanmar numeric convertion
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('0', '၀')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('1', '၁')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('2', '၂')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('3', '၃')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('4', '၄')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('5', '၅')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('6', '၆')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('7', '၇')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('8', '၈')
df_to_correct['benef_id'] = df_to_correct['benef_id'].str.replace('9', '၉')


df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].astype(str)
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('ဝ', '၀')
  
# english numeric to Myanmar numeric convertion
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('0', '၀')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('1', '၁')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('2', '၂')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('3', '၃')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('4', '၄')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('5', '၅')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('6', '၆')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('7', '၇')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('8', '၈')
df_to_correct['Beneficiaries Reg. No.'] = df_to_correct['Beneficiaries Reg. No.'].str.replace('9', '၉')

 # myanmar fount zero and wa lone replacement
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].astype(str)

df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('ဝ', '၀')

df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].astype(str)

df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('ဝ', '၀')


# english numeric to Myanmar numeric convertion
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('0', '၀')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('1', '၁')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('2', '၂')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('3', '၃')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('4', '၄')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('5', '၅')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('6', '၆')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('7', '၇')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('8', '၈')
df_to_correct['NRC - Digits'] = df_to_correct['NRC - Digits'].str.replace('9', '၉')


df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('0', '၀')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('1', '၁')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('2', '၂')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('3', '၃')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('4', '၄')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('5', '၅')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('6', '၆')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('7', '၇')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('8', '၈')
df_to_correct['NRC old - Digits'] = df_to_correct['NRC old - Digits'].str.replace('9', '၉')
   
# Male Burmese fount Standartization
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('ကျား ', 'ကျား')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('ကျား\xa0', 'ကျား')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('ကျား', 'ကျား')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('ကျးာ', 'ကျား')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('က', 'ကျား')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('ကျားျား', 'ကျား')


# Female Burmese fount Standartization  
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('မ ', 'မ')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('မ\xa0', 'မ')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('မ', 'မ')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('\u200bမ', 'မ')
df_to_correct['Benef: Gender'] = df_to_correct['Benef: Gender'].str.replace('မ ', 'မ')
   


# duplicate by beneficiares info - booleen var + ID
dup_correct   = df_to_correct.duplicated(subset = 'benef_id', keep = False)

# duplciate by id and beneficiares info dataset + ID duplicate
dup_correct   = df_to_correct.loc[dup_correct == True]

if len(dup_correct) > 0 :
    dup_correct.to_excel(report + '00_additional_to_correct_duplicate.xlsx', index = False)

    


## additional register ##
## Combined data from each office

df_to_add  = pd.DataFrame()  


i = 1
       
xlsxs = os.listdir(raw +'_additional_action/')
        
for xlsx in xlsxs :
    
    if xlsx.endswith(".xlsx"):
        print(i)
        print("now working in " + xlsx)
        
        dta_raw = pd.read_excel(raw + '_additional_action/' + xlsx, sheet_name = '01_additional_add', 
                                skiprows = 3, header = None, index_col = False, usecols="A:AO", names = col_names)


        # drop na from selected main variables
        dta_raw = dta_raw.dropna(how = 'all', subset = col_na)
        
        #dta['geo_township'] = geo_township
        dta_raw.sort_values('benef_id')
        
        source = xlsx
        dta_raw['source'] = source
                    
    
        df_to_add = df_to_add.append(dta_raw)
        
        i = 1 + i



   
# myanmar fount zero and wa lone replacement
df_to_add['benef_id'] = df_to_add['benef_id'].astype(str)
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('ဝ', '၀')
  
# english numeric to Myanmar numeric convertion
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('0', '၀')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('1', '၁')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('2', '၂')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('3', '၃')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('4', '၄')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('5', '၅')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('6', '၆')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('7', '၇')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('8', '၈')
df_to_add['benef_id'] = df_to_add['benef_id'].str.replace('9', '၉')


df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].astype(str)
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('ဝ', '၀')
  
# english numeric to Myanmar numeric convertion
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('0', '၀')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('1', '၁')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('2', '၂')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('3', '၃')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('4', '၄')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('5', '၅')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('6', '၆')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('7', '၇')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('8', '၈')
df_to_add['Beneficiaries Reg. No.'] = df_to_add['Beneficiaries Reg. No.'].str.replace('9', '၉')

 # myanmar fount zero and wa lone replacement
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].astype(str)

df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('ဝ', '၀')

df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].astype(str)

df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('ဝ', '၀')


# english numeric to Myanmar numeric convertion
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('0', '၀')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('1', '၁')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('2', '၂')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('3', '၃')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('4', '၄')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('5', '၅')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('6', '၆')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('7', '၇')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('8', '၈')
df_to_add['NRC - Digits'] = df_to_add['NRC - Digits'].str.replace('9', '၉')


df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('0', '၀')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('1', '၁')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('2', '၂')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('3', '၃')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('4', '၄')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('5', '၅')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('6', '၆')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('7', '၇')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('8', '၈')
df_to_add['NRC old - Digits'] = df_to_add['NRC old - Digits'].str.replace('9', '၉')
   
# Male Burmese fount Standartization
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('ကျား ', 'ကျား')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('ကျား\xa0', 'ကျား')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('ကျား', 'ကျား')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('ကျးာ', 'ကျား')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('က', 'ကျား')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('ကျားျား', 'ကျား')


# Female Burmese fount Standartization  
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('မ ', 'မ')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('မ\xa0', 'မ')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('မ', 'မ')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('\u200bမ', 'မ')
df_to_add['Benef: Gender'] = df_to_add['Benef: Gender'].str.replace('မ ', 'မ')
   
    

# duplicate by beneficiares info - booleen var + ID
dup_add   = df_to_add.duplicated(subset = 'benef_id', keep = False)

# duplciate by id and beneficiares info dataset + ID duplicate
dup_add   = df_to_add.loc[dup_add == True]

if len(dup_add) > 0 :
    dup_add.to_excel(report + '00_additional_to_add_duplicate.xlsx', index = False)




####################################################################################################  
##      CHECK THE ID WITH MASTER DATASET - INCLUDED IN DATASET OR NOT
####################################################################################################
# 02 - to drop cases  

df_drop_x = df_to_drop[['benef_id']]

merge_j = pd.merge(dta, df_drop_x, left_on = ['benef_id_new'], right_on = ['benef_id'],
                   suffixes = ('_dta', '_drop'), indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


y_j.rename(columns={'benef_id_drop':'benef_id'}, inplace=True)


if len(y_j) > 0 :
    
    y_j = y_j['benef_id']
    merge_j = pd.merge(df_to_drop, y_j, on = ['benef_id'], 
                   indicator = 'merge', how = 'outer')

    x_j = merge_j.loc[merge_j['merge'] == 'both']
    y_j = merge_j.loc[merge_j['merge'] == 'right_only']
    z_j = merge_j.loc[merge_j['merge'] == 'left_only']
    
    x_j.count()
    y_j.count()
    z_j.count()
    
    x_j.to_excel(report + '00_additional_to_drop_not_found.xlsx', index = False)
    
    
    

####################################################################################################
# 03 - the correct cases 
df_correct_x = df_to_correct[['benef_id']]

merge_j = pd.merge(dta, df_correct_x, left_on = ['benef_id_new'], right_on = ['benef_id'],
                   suffixes = ('_dta', '_drop'), indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


y_j.rename(columns={'benef_id_drop':'benef_id'}, inplace=True)



if len(y_j) > 0 :
    
    y_j = y_j['benef_id']
    merge_j = pd.merge(df_to_correct, y_j, on = ['benef_id'], 
                   indicator = 'merge', how = 'outer')

    x_j = merge_j.loc[merge_j['merge'] == 'both']
    y_j = merge_j.loc[merge_j['merge'] == 'right_only']
    z_j = merge_j.loc[merge_j['merge'] == 'left_only']
    
    x_j.count()
    y_j.count()
    z_j.count()
    
    x_j.to_excel(report + '00_additional_to_correct_not_found.xlsx', index = False)
    
    
####################################################################################################
# 04 - to add used existing id or not check

merge_j = pd.merge(dta, df_to_add, left_on = ['benef_id_new'], right_on = ['benef_id'],
                   suffixes = ('_dta', '_add'), indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


if len(x_j) > 0 :
    
    x_j.to_excel(report + '00_additional_to_add_id_existing.xlsx', index = False)
    
####################################################################################################