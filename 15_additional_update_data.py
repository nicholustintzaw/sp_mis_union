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
   
    
  
####################################################################################################
##          PREPARE TO UPDATE THE DATASET
####################################################################################################

# left all the issue cases - duplciate id from to add, to drop or to correct
# and not fund id in the old dataset or used existing id
    

# To Drop additional drop and correct obs

df_last_new = dta
   
 
#   remove to correct cases 

df_to_correct_x = df_to_correct[['benef_id']]

df_to_correct_x.rename(columns={'benef_id':'tocorrect_id'}, inplace=True)


merge_j = pd.merge(df_last_new, df_to_correct_x, left_on = ['benef_id_new'], 
                   right_on = ['tocorrect_id'],
                   indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


df_last_new = z_j
df_last_new = df_last_new.drop(['tocorrect_id', 'merge'], axis = 1)

if len(y_j) > 0 :
    y_j.to_excel(report + '11_additional_correct_exclude_data.xlsx', index = False)



#   remove to drop cases 

df_to_drop_x = df_to_drop[['benef_id']]

df_to_drop_x.rename(columns={'benef_id':'todrop_id'}, inplace=True)


merge_j = pd.merge(df_last_new, df_to_drop_x, left_on = ['benef_id_new'], 
                   right_on = ['todrop_id'],
                   indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


df_last_new = z_j
df_last_new = df_last_new.drop(['todrop_id', 'merge'], axis = 1)

if len(y_j) > 0 :
    
    y_j = y_j[['todrop_id']]
    y_j.rename(columns={'todrop_id':'benef_id'}, inplace=True)

    merge_j = pd.merge(df_to_drop, y_j, on = ['benef_id'], 
                   indicator = 'merge', how = 'outer')

    x_j = merge_j.loc[merge_j['merge'] == 'both']
    y_j = merge_j.loc[merge_j['merge'] == 'right_only']
    z_j = merge_j.loc[merge_j['merge'] == 'left_only']
    
    x_j.count()
    y_j.count()
    z_j.count()
        
    x_j.to_excel(report + '12_additional_drop_exclude_data.xlsx', index = False)




# To Add additional add and correct obs

df_last_newin = df_last_new

#  add additional add cases 
df_to_add.rename(columns={'benef_id':'benef_id_new'}, inplace=True)

df_last_newin = df_last_newin.append(df_to_add)    


#  add additional correct cases 
df_to_correct.rename(columns={'benef_id':'benef_id_new'}, inplace=True)

df_last_newin = df_last_newin.append(df_to_correct)    



# merge with MIMU dataset 
col_code = ['sr_name_dsw', 'pcode_sr', 'region_code',
       'district_name_master', 'pcode_dt', 'Township Name',
       'dist_town', 'pcode_ts', 'master_towncode']


# step 1: prepare the sp mis dataset to match with mimu data

code = pd.read_excel(raw + '00_coding_mapping.xlsx', sheet_name = 'vlookup', skiprows = 1, \
                     header = None, index_col=False, names = col_code)

code['dist_town'] = code['sr_name_dsw'].str.cat(code[['Township Name']].astype(str), sep = "_")
code.dist_town = code.dist_town.str.replace(' ', '')

    
df_last_newin['dist_town'] = df_last_newin['State/Region Name'].str.cat(df_last_newin[['Township Name']].astype(str), sep = "_")
df_last_newin.dist_town = df_last_newin.dist_town.str.replace(' ', '')

code_use = code[['dist_town', 'region_code', 'master_towncode', 'pcode_sr', 'pcode_dt', 'pcode_ts']]
code_use.rename(columns={'region_code':'master_region_code'}, inplace=True)


#pcode_sr = code.drop_duplicates(subset = 'region_code', keep = 'first')

df_last_newin = df_last_newin.drop(['master_region_code','master_towncode'], axis = 1)


merge_j = pd.merge(df_last_newin, code_use, on = ['dist_town'], 
                   indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()

df_last_newin = x_j



new_col = ['benef_sirnum_new', 'State/Region Name', 'District Name', 'Township Name', 'Rural or Urban', 'Ward', 'Village', 'Village Tract', 
            'benef_id_new', 'Benef: Name', 'Benef: Gender', 'Benef: Father Name', 'Age Verification Doc', 'NRC New', 'NRC Old', 
            'Address Detail', 'eao_yesno', 'eao_name', 'source', 'benef_id_old', 'benef_id', 'program_code', 'region_code', 'town_code', 'Beneficiaries Reg. No.', 
            'benef_sirnum', 'benef_sirnum_new_str', 'benef_sirnum_len', 'benef_sirnum_final', 'master_region_code','master_towncode', 'dist_town',
            'DOB Type', 'Benef: DOB Myanmar', 'Benef: DOB Day', 'Benef: DOB Month', 'Benef: DOB Year', 'Benef: DOB', 'Cal_DOB_MM_ENG', 
            'benef_dob_mm', 'Correct Calculation', 'Correct DOB MM to ENG', 'Enrollment End Date', 'Enrollment End: Day', 'Enrollment End: Month',
            'Enrollment End: Year', 'Age in Years', 
            'NRC Format', 'NRC old - Text', 'NRC old - Digits', 'NRC - Region Code', 'NRC - Township Code', 'NRC Status', 'NRC - Digits',      
            'State/Region Code', 'Township Code', 'cal_dist_town', 'cal_district', 'cal_nrc_region', 'cal_region', 'cal_town', 'state_region_code', 
            'township_code', 'No.', 'sr_no']


report_col = ['benef_sirnum_new', 'State/Region Name', 'District Name', 'Township Name', 'Rural or Urban', 'Ward', 'Village', 'Village Tract', 
            'benef_id_new', 'Benef: Name', 'Benef: Gender', 'Benef: Father Name', 'Age Verification Doc', 'NRC New', 'NRC Old', 
            'Address Detail', 'eao_yesno', 'eao_name', 'source']


visual_col = ['benef_sirnum_new', 'State/Region Name', 'District Name', 'Township Name', 'Rural or Urban', 'Ward', 'Village', 'Village Tract', 
            'benef_id_new', 'Benef: Name', 'Benef: Gender', 'Benef: Father Name', 'Age Verification Doc', 'NRC New', 'NRC Old', 
            'Address Detail', 'eao_yesno', 'eao_name', 'source', 'pcode_sr', 'pcode_dt', 'pcode_ts']
             
df_visual = df_last_newin[visual_col]


df_last_newin = df_last_newin[new_col]


df_report = df_last_newin[report_col]





df_last_newin.to_excel(db + qrt + '_additional.xlsx', index = False)
df_report.to_excel(report + qrt + '_formatted_additional.xlsx', index = False)
df_visual.to_csv(report + qrt + '_formatted_additional.csv')



####################################################################################################
