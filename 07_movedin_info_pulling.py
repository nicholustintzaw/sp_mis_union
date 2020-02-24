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

col_na = ['State/Region Name', 'District Name', 'Township Name', 'Benef: Name',
       'Benef: Gender']



col_names = ['No.', 'State/Region Name', 'cal_region', 'State/Region Code',
       'District Name', 'cal_district', 'Township Name', 'cal_dist_town',
       'cal_town', 'Township Code', 'Rural or Urban', 'Ward', 'Village Tract',
       'Village', 'Address Detail', 'benef_id',
       'Benef: Name', 'Benef: Gender', 'Benef: Father Name']


col_person = ['Benef: Name', 'Benef: Gender', 'Benef: Father Name']



offices = ['01_kachin', '02_kayah', '03_kayin','04_chin', '05_sagaing', '06_tanintharyi', '07_bago', '08_magwe', 
           '09_mandalay', '10_mon', '11_rakhine', '12_yangon', '13_shan', '14_ayeyarwady', '15_nay pyi taw']


col_last = ['sr_no', 'State/Region Name', 'cal_region', 'state_region_code',
       'District Name', 'cal_district', 'Township Name', 'cal_dist_town',
       'cal_town', 'township_code', 'Rural or Urban', 'Ward', 'Village Tract',
       'Village', 'Address Detail', 'Beneficiaries Reg. No.', 'benef_id',
       'eao_yesno', 'eao_name', 'Benef: Name', 'Benef: Gender', 'benef_dob_mm',
       'Cal_DOB_MM_ENG', 'Age in Years', 'Age Verification Doc', 'NRC Format',
       'NRC old - Text', 'NRC old - Digits', 'NRC Old', 'NRC - Region Code',
       'cal_nrc_region', 'NRC - Township Code', 'NRC Status', 'NRC - Digits',
       'NRC New', 'Benef: Father Name', 'source']



col_movein = ['State/Region Name', 'cal_region', 'state_region_code',
               'District Name', 'cal_district', 'Township Name', 'cal_dist_town',
               'cal_town', 'township_code', 'Rural or Urban', 'Ward', 'Village Tract',
               'Village', 'Address Detail',
               'benef_id_new', 'Benef: Name', 'Benef: Gender', 'Benef: Father Name',
              'Cal_DOB_MM_ENG', 'Age Verification Doc', 'NRC Format',
               'NRC old - Text', 'NRC old - Digits', 'NRC Old', 'NRC - Region Code',
               'cal_nrc_region', 'NRC - Township Code', 'NRC Status', 'NRC - Digits',
               'NRC New']
            
col_moveinnoeli = ['benef_id', 'Benef: Name', 'benef_gender', 'Benef: Father Name',
              'Cal_DOB_MM_ENG', 'Age Verification Doc', 'NRC Format',
               'NRC old - Text', 'NRC old - Digits', 'NRC Old', 'NRC - Region Code',
               'cal_nrc_region', 'NRC - Township Code', 'NRC Status', 'NRC - Digits',
               'NRC New']
            

col_noeli = ['No.', 'State/Region Name', 'cal_region', 'State/Region Code',
           'District Name', 'cal_district', 'Township Name', 'cal_dist_town',
           'cal_town', 'Township Code', 'Rural or Urban', 'Ward', 'Village Tract',
           'Village', 'Address Detail',
           'Beneficiaries Reg. No.', 'benef_id', 'eao_yesno', 'eao_name',
           'Benef: Name', 'benef_gender', 'Day', 'Month', 'Year', 'DR', 'DR29S',
           'MR', 'MRS', 'YS', 'DOB1TAGU', 'Benef: DOB Myanmar', 'Cal_DOB_MM_ENG',
           'Age in Years', 'Age Verification Doc', 'NRC Format', 'NRC old - Text',
           'NRC old - Digits', 'NRC Old', 'NRC - Region Code', 'cal_nrc_region',
           'NRC - Township Code', 'NRC Status', 'NRC - Digits', 'NRC New',
           'Benef: Father Name', 'Benef: status', 'Status: Date', 'Status Month',
           'Status: Year', 'Status Date', 'Moved: State/Region Name',
           'Moved: cal_region', 'Moved: State/Region Code', 'Moved: District Name',
           'cal_district.1', 'Moved: Township Name', 'cal_move_dist_ts',
           'cal_town.1', 'Moved: Township Code', 'Rural or Urban.1', 'Moved: Ward',
           'Moved: Village Tract', 'Moved: Village',
           'Moved: Address', 'source']


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
'''
####################################################################################################
####################################################################################################

## previous dataset ##

df_last = pd.read_excel(olddb + lastqrt + '_additional.xlsx', sheet_name = 'Sheet1', 
                        index_col = False)


#df_last = pd.read_excel(olddb + lastqrt + '_additional.xlsx', sheet_name = 'Sheet1', 
#                        skiprows = 1, header = None, index_col = False, usecols="A:AK", names = col_last)

 
df_last_x = df_last[col_movein] 

# need to create the moved out dataset + last quarter data and check in here, 
# for now only check with last quarter dataset
# df_lastlei = pd.read_excel(olddb + 'dsw_sp_4qrd_20182019_noteligable.xlsx', sheet_name = 'Sheet1', 
#                        skiprows = 1, header = None, index_col = False, usecols="A:BM", names = col_noeli)

# df_lastlei_x = df_lastlei[col_moveinnoeli] 
# df_lastlei_x['Benef: status'] = df_lastlei['Benef: status'] 

# df_last_x = df_last_x.append(df_lastlei_x)


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
            
            dta_raw = pd.read_excel(raw + file + '/_raw/' + xlsx, sheet_name = '02_moved_in', 
                                    skiprows = 3, header = None, index_col = False, usecols="A:S", names = col_names)


            # drop na from selected main variables
            dta_raw = dta_raw.dropna(how = 'all', subset = col_na)
            
            #dta['geo_township'] = geo_township
            dta_raw.sort_values('Township Name')
            
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

    # Male Burmese fount Standartization
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျား ', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျား\xa0', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျား', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျးာ', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('က', 'ကျား')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('ကျားျား', 'ကျား')
    
    
    # Female Burmese fount Standartization  
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('မ ', 'မ')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('မ\xa0', 'မ')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('မ', 'မ')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('\u200bမ', 'မ')
    df_test['Benef: Gender'] = df_test['Benef: Gender'].str.replace('မ ', 'မ')
    
    
    df_movein = df_test
    
    merge_j = pd.merge(df_last_x, df_movein, right_on = ['benef_id'] , 
                       left_on = ['benef_id_new'], suffixes = ('_last', '_new'), 
                       indicator = 'merge', how = 'outer')
    
    x_j = merge_j.loc[merge_j['merge'] == 'both']
    y_j = merge_j.loc[merge_j['merge'] == 'right_only']
    z_j = merge_j.loc[merge_j['merge'] == 'left_only']
    
    x_j.count()
    y_j.count()
    z_j.count()
    
                  
    # export as summary statistic figures for all combined data migration files 
    #dup_resp.to_excel(output + qrt + '_dup_person.xlsx', index = False)
    
    
    obs_x = len(x_j)
    obs_y = len(y_j)
    
    if obs_x > 0 | obs_y > 0 :    
        writer = pd.ExcelWriter(output + '02_movedin_notfound_olddata.xlsx', engine = 'xlsxwriter')
       
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

print('Woow, just finished the Moved-in Sheet checking, please check your outputs folder for result excel files')


