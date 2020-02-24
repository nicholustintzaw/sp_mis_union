#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec  4 20:28:44 2019

@author: nicholustintzaw
"""


####################################################################################################
####################################################################################################
'''
project tite    :           social pension database - national level
purpose         :           new quarter - report generating
developed by    :           Nicholus Tint Zaw             
modified date   :           3rd Dec 2019

follow-up action:
    
'''
####################################################################################################
####################################################################################################


### PLEASE, CHANGE YOUR DIRECTORY BELOW ###

masterdir = ('/Users/nicholustintzaw/Dropbox/06_DSW_SP_Database/_Union_SP_MIS')

#masterdir = r'C:\Users\Age.ing\Dropbox\01_Eligable\_New_QRT_COMBINE_CHECK_Window'

### PLEASE, CHANGE THE CASH TRANSFER BUDGET YEAR QUARTER BELOW ###
qrt = '2nd_qrt_2019_2020'

lastqrt = '1st_qrt_2019_2020'




####################################################################################################
####################################################################################################
################ PLEASE, DON'T TOUCH ANY PYTHON CODES BELOW ########################################
####################################################################################################
####################################################################################################





####################################################################################################
### task 1: prepare the directory setting
####################################################################################################

import os
os.chdir(masterdir)

## task 0: prepare the directory setting
exec(open("00_directory_setting.py").read());



####################################################################################################
### task 2: Combined Reports 
####################################################################################################

## FIRST REPORT GENERATION
# 12_newregister_dataset.py
exec(open("12_newregister_dataset.py", 'r', encoding="utf8").read())
#exec(open("12_newregister_dataset.py").read());

# 12_update_dataset.py
exec(open("12_update_dataset.py", 'r', encoding="utf8").read())
#exec(open("12_update_dataset.py").read());

# 13_report_generating.py
exec(open("13_report_generating.py", 'r', encoding="utf8").read())
#exec(open("13_report_generating.py").read());


## ADDITIONAL ADD + DROP
# 14_additional_check
exec(open("14_additional_check.py", 'r', encoding="utf8").read())
#exec(open("14_additional_check.py").read());

# 15_additional_update_data
exec(open("15_additional_update_data.py", 'r', encoding="utf8").read())
#exec(open("15_additional_update_data.py").read());

# 16_additional_report
exec(open("16_additional_report.py", 'r', encoding="utf8").read())
#exec(open("16_additional_report.py").read());





####################################################################################################


