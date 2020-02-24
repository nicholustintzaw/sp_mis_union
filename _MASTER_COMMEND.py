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
purpose         :           new quarter - raw and combined data check and check report results
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
### task 2: New and Combined Check 
####################################################################################################

## IN

# 02_new_register
exec(open("01_check_raw_combined_newregister.py", 'r', encoding="utf8").read())
#exec(open("01_check_raw_combined_newregister.py").read());

# 03_moved_in
exec(open("02_check_raw_combined_movedin.py", 'r', encoding="utf8").read())
#exec(open("02_check_raw_combined_movedin.py").read());

# 04_false_death
exec(open("03_check_raw_combined_falsedeath.py", 'r', encoding="utf8").read())
#exec(open("03_check_raw_combined_falsedeath.py").read());


# OUT

# 05_death
exec(open("04_check_raw_combined_death.py", 'r', encoding="utf8").read())
#exec(open("04_check_raw_combined_death.py").read());

# 06_moved_out
exec(open("05_check_raw_combined_movedout.py", 'r', encoding="utf8").read())
#exec(open("05_check_raw_combined_movedout.py").read());

# 07_false_reg
exec(open("06_check_raw_combined_flasereg.py", 'r', encoding="utf8").read())
#exec(open("06_check_raw_combined_flasereg.py").read());



####################################################################################################


