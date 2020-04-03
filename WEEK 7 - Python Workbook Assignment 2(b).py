#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd
from sqlalchemy import create_engine
engine = create_engine(r"sqlite:///~/Downloads/learn-data-analysis-w-python-master/datasets/gradedata.db")                   
sql = "select name from sqlite_master"
"where type = 'table';"

sales_data_df = pd.read_sql(sql, engine)

sales_data_df

