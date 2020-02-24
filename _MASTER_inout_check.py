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
purpose         :           new quarter - moved-in, false death, death, moved-out and flase register
                            check - are the present in the previous updated dataset?
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
### task 2: Obs Check with Old Data
####################################################################################################

## IN

# 07_movedin_info_pulling - moved in obs data check
exec(open("07_movedin_info_pulling.py", 'r', encoding="utf8").read())
#exec(open("07_movedin_info_pulling.py").read());

# 08_flasedeath_info_pulling - false death in obs data check
exec(open("08_flasedeath_info_pulling.py", 'r', encoding="utf8").read())
#exec(open("08_flasedeath_info_pulling.py").read());


# OUT
# 09_death_lastq_check - death obs info check
exec(open("09_death_lastq_check.py", 'r', encoding="utf8").read())
#exec(open("09_death_lastq_check.py").read());

# 10_movedout_lastq_check - move out obs data check
exec(open("10_movedout_lastq_check.py", 'r', encoding="utf8").read())
#exec(open("10_movedout_lastq_check.py").read());

# 11_flasereg_lastq_check - false register obs data check
exec(open("11_flasereg_lastq_check.py", 'r', encoding="utf8").read())
#exec(open("11_flasereg_lastq_check.py").read());



####################################################################################################


