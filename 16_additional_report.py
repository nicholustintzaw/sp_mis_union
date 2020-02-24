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
####################################################################################################
#### EXPORTING TO EACH STATE AND REGION, DISTRICT AND TOWNSHIP UPDATE BENEFICIARES SHEETS
####################################################################################################
####################################################################################################

states = df_report['State/Region Name'].unique() 

for state in states :
    
    # get the state level dataset
    df_state = df_report.loc[df_report['State/Region Name'] == state]
    districts = df_state['District Name'].unique() 
    
    for district in districts :
        directory = os.path.join(report, '_township_list', state, district)
        
        # make directories
        if not os.path.exists(directory):
            
            os.makedirs(directory)
         
            
        # make district dataset
        df_dir2 = df_state.loc[df_state['District Name'] == district]
        dta_dists = df_state['District Name'].unique() 
        
        for dta in dta_dists :
            df_dir2['Township Name'] = df_dir2['Township Name'] .str.replace('/', '')
            towns = df_dir2['Township Name'].unique() 
        
            for town in towns :
                df_town = df_dir2.loc[df_dir2['Township Name'] == town]

                df_town.to_excel(directory + '/' + town + qrt + '.xlsx', index = False)
    
                
                     
####################################################################################################
####################################################################################################
### EXPORT FOR SUMMARY SHEET                            
                
# UNION 
                
tot = len(df_report.index)
xx = df_report['Benef: Gender'] == 'ကျား'
xy = df_report['Benef: Gender'] == 'မ'

xx = df_report.loc[xx == True]
xy = df_report.loc[xy == True]

male = len(xx.index)
female = len(xy.index)
       
sum_union = {'Total Benef:': [tot], 'Male': [male], 'Female': [female]}
df_union = pd.DataFrame(sum_union)


# STATE & REGION 
sum_region      = pd.DataFrame()  
sum_district    = pd.DataFrame()
sum_town        = pd.DataFrame()

                             
i = 1
j = 1
x = i 

regions = df_report['State/Region Name'].unique() 


for region in regions : 
            
        # keep one state/region
        df_region = df_report.loc[df_report['State/Region Name'] == region]
        
        dta_ind = pd.DataFrame()
        
        # count the number of obs
        tot = len(df_region.index)
        xx = df_region['Benef: Gender'] == 'ကျား'
        xy = df_region['Benef: Gender'] == 'မ'
      
        xx = df_region.loc[xx == True]
        xy = df_region.loc[xy == True]
        
        male = len(xx.index)
        female = len(xy.index)
        
        d_i = {'State & Region Name': [region], 'Total New Register': [tot], 'Male': [male], 'Female': [female]}
        
        dta_i = pd.DataFrame(d_i)
        sum_region = sum_region.append(dta_i)
        
        
        # prepare for the district level figure
        districts = df_region['District Name'].unique() 
                    
        for district in districts :
            
            # keep one state/region
            df_district = df_region.loc[df_region['District Name'] == district]
            
            # count the number of obs
            tot = len(df_district.index)
            xx = df_district['Benef: Gender'] == 'ကျား'
            xy = df_district['Benef: Gender'] == 'မ'
    
            
            xx = df_district.loc[xx == True]
            xy = df_district.loc[xy == True]
            
            male = len(xx.index)
            female = len(xy.index)
            
            d_j = {'State & Region Name': [region], 'District Name': [district], 'Total New Register': [tot], 'Male': [male], 'Female': [female]}
            
            dta_j = pd.DataFrame(d_j)
            sum_district = sum_district.append(dta_j)
            
            
            
            # prepare for the township level figure
            towns = df_district['Township Name'].unique() 
            
            for town in towns :
                
                # keep one township
                df_town = df_district.loc[df_district['Township Name'] == town]
                
                # count the number of obs
                tot = len(df_town.index)
                
                xx = df_town['Benef: Gender'] == 'ကျား'
                xy = df_town['Benef: Gender'] == 'မ'
    
                xx = df_town.loc[xx == True]
                xy = df_town.loc[xy == True]
                
                tmale = len(xx.index)
                tfemale = len(xy.index)
                
                            
                d_x = {'State & Region Name': [region], 'District Name': [district], 'Township Name': [town],'Total New Register': [tot],  'Male': [tmale], 'Female': [tfemale]}
                
                dta_x = pd.DataFrame(d_x)  
                
                dta_ind = pd.DataFrame(d_x)  
                
                dta_ind.to_excel(report + '_summary_figure/' + region + '_summstat.xlsx', index = False)
                
                sum_town = sum_town.append(dta_x)



writer = pd.ExcelWriter(report + qrt + '_summary_sheet.xlsx', engine = 'xlsxwriter')
df_union.to_excel(writer, sheet_name = 'Union')
sum_region.to_excel(writer, sheet_name = 'State_Region')
sum_district.to_excel(writer, sheet_name = 'District')
sum_town.to_excel(writer, sheet_name = 'Townships')
writer.save()
writer.close()

      
        