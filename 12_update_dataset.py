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

print('Now, the spyder is working on updating dataset, please wait for a few minutes')


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



col_movein = ['benef_id', 'Benef: Name', 'Benef: Gender', 'Benef: Father Name',
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

df_last_new = df_last 


##  remove the out cases ##
#   remove the death cases  
# dcases = list(df_death.benef_id) # list the value from column

df_death_x = df_death[['benef_id', 'Benef: Name']]

df_death_x.rename(columns={'benef_id':'death_id', 'Benef: Name': 'death_name'}, inplace=True)


merge_j = pd.merge(df_last_new, df_death_x, left_on = ['benef_id_new'], 
                   right_on = ['death_id'],
                   indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


df_last_new = z_j
df_last_new = df_last_new.drop(['death_id', 'death_name', 'merge'], axis = 1)

y_j.to_excel(report + '04_death_exclude_data.xlsx', index = False)

####################################################################################################
#   remove move-out cases

df_moveout_x = df_moveout[['benef_id', 'Benef: Name']]

df_moveout_x.rename(columns={'benef_id':'death_id', 'Benef: Name': 'death_name'}, inplace=True)


merge_j = pd.merge(df_last_new, df_moveout_x, left_on = ['benef_id_new'], 
                   right_on = ['death_id'],
                   indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


df_last_new = z_j
df_last_new = df_last_new.drop(['death_id', 'death_name', 'merge'], axis = 1)

y_j.to_excel(report + '05_movedout_exclude_data.xlsx', index = False)

####################################################################################################
#   remove false register cases

df_falsereg_x = df_falsereg[['benef_id', 'Benef: Name']]

df_falsereg_x.rename(columns={'benef_id':'death_id', 'Benef: Name': 'death_name'}, inplace=True)


merge_j = pd.merge(df_last_new, df_falsereg_x, left_on = ['benef_id_new'], 
                   right_on = ['death_id'],
                   indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


df_last_new = z_j
df_last_new = df_last_new.drop(['death_id', 'death_name', 'merge'], axis = 1)

y_j.to_excel(report + '06_flase_register_exclude_data.xlsx', index = False)

####################################################################################################
## add the in cases ##
df_last_newin = df_last_new


#  add moved-in cases 
merge_j = pd.merge(df_last_x, df_movein, right_on = ['benef_id', 'Benef: Name'] , 
                   left_on = ['benef_id_new', 'Benef: Name'], suffixes = ('_last', '_new'), 
                   indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()

x_j.to_excel(report + '02_movedin_not_movedout_obs.xlsx', index = False)

df_movein.rename(columns={'benef_id':'benef_id_new'}, inplace=True)

df_last_newin = df_last_newin.append(df_movein)    


#  add false death in cases 
merge_j = pd.merge(df_last_x, df_falsed, right_on = ['benef_id', 'Benef: Name'] , 
                   left_on = ['benef_id_new', 'Benef: Name'], suffixes = ('_last', '_new'), 
                   indicator = 'merge', how = 'outer')

x_j = merge_j.loc[merge_j['merge'] == 'both']
y_j = merge_j.loc[merge_j['merge'] == 'right_only']
z_j = merge_j.loc[merge_j['merge'] == 'left_only']

x_j.count()
y_j.count()
z_j.count()


x_j.to_excel(report + '03_false_deathin_but_inprogram_obs.xlsx', index = False)

df_falsed.rename(columns={'benef_id':'benef_id_new'}, inplace=True)

df_last_newin = df_last_newin.append(df_falsed)    


# y_j.to_excel(report + '03_false_death_notfound_exclude.xlsx', index = False)
# because of missing township info in one matched case, exclude all false death in case
# df_falsed.to_excel(report + '03_false_death_notfound_exclude.xlsx', index = False)

#df_last_newin = df_last_newin.append(x_j)    


#  add new register cases 
df_newreg_all.rename(columns={'benef_id':'benef_id_new'}, inplace=True)

df_last_newin = df_last_newin.append(df_newreg_all)    





## STEP 3: RE - NUMBERING ALL THE BENEFICIARES PER TOWNSHIP ##
df_last_newin.isnull().sum()


## prepare new beneficaires id ##
#'State/Region Name', 'District Name','Township Name'
'''       
# 1 - create old id var
df_last_newin['benef_id_old'] = df_last_newin['benef_id']

# 2 - gave new seial number of id based on each township 
df_last_newin['benef_sirnum_new'] = df_last_newin.groupby(['State/Region Name', 'Township Name']).cumcount() + 1; df_last_newin

# 3 - treat as string and to create 6 digits srial number
df_last_newin['benef_sirnum_new_str'] = df_last_newin['benef_sirnum_new'].astype(str)
df_last_newin['benef_sirnum_len'] = df_last_newin['benef_sirnum_new_str'].str.len()


# 4 - apply 6 digits ruls to get all serial number become 6 serial number
df_last_newin['benef_sirnum_final'] = df_last_newin['benef_sirnum_new_str'].astype(str).str.rjust(6,'0')


# 5 - split benefi_id into different sub data item
df_last_newin[['program_code','region_code', 'town_code','benef_sirnum']] = df_last_newin.benef_id.str.split('/', expand=True) 


# 6 - generate new benef_id 
'''

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

'''
df_last_newin['program_code'] = '02'

df_last_newin['benef_id_new'] = df_last_newin.program_code.str.cat(df_last_newin[['master_region_code','master_towncode','benef_sirnum_final']].astype(str), sep = "/")
'''

df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].astype(str)
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('ဝ', '၀')
  
# english numeric to Myanmar numeric convertion
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('0', '၀')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('1', '၁')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('2', '၂')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('3', '၃')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('4', '၄')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('5', '၅')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('6', '၆')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('7', '၇')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('8', '၈')
df_last_newin['benef_id_new'] = df_last_newin['benef_id_new'].str.replace('9', '၉')


## STEP 4: RE-ORDER THE COLUMNS AND PREPARE FOR EXPORT ##

# Male Burmese fount Standartization
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('ကျား ', 'ကျား')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('ကျား\xa0', 'ကျား')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('ကျား', 'ကျား')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('ကျးာ', 'ကျား')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('က', 'ကျား')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('ကျားျား', 'ကျား')

df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace(' ကျား', 'ကျား')


# Female Burmese fount Standartization  
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('မ ', 'မ')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('မ\xa0', 'မ')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('မ', 'မ')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('\u200bမ', 'မ')
df_last_newin['Benef: Gender'] = df_last_newin['Benef: Gender'].str.replace('မ ', 'မ')
   
df_last_newin['District Name'] = df_last_newin['District Name'].str.replace(' ', '')
   

# DUPLICATE OBSERVATION CHECK
# duplicate by beneficiares info - booleen var + ID
dup_resp_upd   = df_last_newin.duplicated(subset = col_person, keep = False)
dup_id_upd     = df_last_newin.duplicated(subset = 'benef_id_new', keep = False)

# duplciate by id and beneficiares info dataset + ID duplicate
dup_resp_upd   = df_last_newin.loc[dup_resp_upd == True]
dup_id_upd     = df_last_newin.loc[dup_id_upd == True]
  

# stata for raw
tot_upd     = len(df_last_newin.index)
dupid_upd   = len(dup_id_upd.index)
dupresp_upd = len(dup_resp_upd.index)


update_sum = {'Updated beneficiaries': [tot_upd], 'ID Duplicate': [dupid_upd], 'Person Duplicate': [dupresp_upd]}
update_sum = pd.DataFrame(update_sum)


    
# export as summary statistic figures for all updated database  
writer = pd.ExcelWriter(output + '00_updated_data_duplicates.xlsx', engine = 'xlsxwriter')
update_sum.to_excel(writer, sheet_name = 'duplicate_summary')

obs = len(dup_id_upd)
if obs > 0 : 
    dup_id_upd.to_excel(writer, sheet_name = 'id_duplicate')
  
obs = len(dup_resp_upd)
if obs > 0 : 
    dup_resp_upd.to_excel(writer, sheet_name = 'person_info_duplicate')
  
writer.save()
writer.close()



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




df_last_newin.to_excel(db + qrt + '.xlsx', index = False)
df_report.to_excel(report + qrt + '_formatted.xlsx', index = False)
df_visual.to_csv(report + qrt+ '_formatted.csv')



####################################################################################################
