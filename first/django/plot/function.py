#!/usr/bin/env python
# coding: utf-8

# In[7]:


import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib as mpl
import os
from matplotlib import font_manager, rc
font_path = "C:/Windows/Fonts/NGULIM.TTF"
font = font_manager.FontProperties(fname=font_path).get_name()
rc('font', family=font)

from config.settings import BASE_DIR
# In[6]:


def make_df(area):
    df = pd.read_csv(os.path.join(BASE_DIR, 'static', 'today_number0912.csv'))
    df2 = pd.read_csv(os.path.join(BASE_DIR, 'static', 'local_number.csv'))
    df3 = pd.read_csv(os.path.join(BASE_DIR, 'static', 'area.csv'),encoding='CP949')
    df4 = pd.read_csv(os.path.join(BASE_DIR, 'static', 'local_per0912.csv'))
                 
    region1 = area[0]
    region2 = area[1]
    region3 = area[2]

    df_region1 = df[df['지역명']==region1]
    df_region2 = df[df['지역명']==region2]
    df_region3 = df[df['지역명']==region3]

    total = df_region1.append(df_region2, ignore_index = True)
    total = total.append(df_region3,ignore_index=True)
                
    df_region1_2 = df2[df2['지역명']==region1]
    df_region2_2 = df2[df2['지역명']==region2]
    df_region3_2 = df2[df2['지역명']==region3]

    total_2 = df_region1_2.append(df_region2_2, ignore_index = True)
    total2 = total_2.append(df_region3_2,ignore_index=True)

    df_region1_3 = df3[df3['sido']==region1]
    df_region2_3 = df3[df3['sido']==region2]
    df_region3_3 = df3[df3['sido']==region3]

    total_3 = df_region1_3.append(df_region2_3, ignore_index = True)
    total3 = total_3.append(df_region3_3,ignore_index=True)

    df_region1_4 = df4[df4['지역명']==region1]
    df_region2_4 = df4[df4['지역명']==region2]
    df_region3_4 = df4[df4['지역명']==region3]

    total_4 = df_region1_4.append(df_region2_4, ignore_index = True)
    total4 = total_4.append(df_region3_4,ignore_index=True)

    df_total = [total, total2,total3, total4]  
                
    return df_total



# In[9]:


def make_bar_plot(df_name):
    sns.factorplot(x = '지역명', y= '확진자수', data= df_name, kind='bar', height = 2.5)
    plt.title('■지역별 확진자수■')
    plt.savefig(os.path.join(BASE_DIR, 'static', 'number.png'),transparent=True,bbox_inches='tight')
def make_bar_plot2(df_name):
    sns.factorplot(x ='지역명', y = '거리두기 단계', data = df_name, kind = 'bar', height = 2.5)
    plt.title('■지역별 거리두기단계■')
    plt.savefig(os.path.join(BASE_DIR, 'static', 'local_num.png'),transparent=True,bbox_inches='tight')
def make_bar_plot3(df_name):
    sns.factorplot(x ='sido', y = 'restnum', data = df_name, kind = 'bar', height = 2.5)
    plt.title('■지역별 안심식당수■')
    plt.ylabel('안심식당수')
    plt.xlabel('지역명')
    plt.savefig(os.path.join(BASE_DIR, 'static', 'restnum.png'),transparent=True,bbox_inches='tight')
def make_bar_plot4(df_name):
    sns.factorplot(x ='지역명', y = '백신접종률', data = df_name, kind = 'bar', height = 2.5)
    plt.title('■지역별 백신접종률■')
    plt.savefig(os.path.join(BASE_DIR, 'static', 'per.png'),transparent=True,bbox_inches='tight')
def make_bar_plot5(df_name):
    sns.factorplot(x ='sido', y = 'clinicnum', data = df_name, kind = 'bar', height = 2.5)
    plt.title('■지역별 선발진료소수■')
    plt.ylabel('선발진료소수')
    plt.xlabel('지역명')
    plt.savefig(os.path.join(BASE_DIR, 'static', 'clinicnum.png'),transparent=True,bbox_inches='tight')


# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:





# In[ ]:




