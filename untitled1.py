# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 13:52:11 2020

@author: ERP80
"""
import glassdoor_scraper_Spyder as gs
import pandas as pd
path = "C:/Users/ERP80/Documents/ds_salary_proj/chromedriver"

df = gs.get_jobs('data scientist',20,False,path,15)

# df = df[df['Salary Estimate']!='-1']

