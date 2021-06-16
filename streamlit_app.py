import streamlit as st
st.write('Hello, world!')

x = st.slider('x')
st.write(x, 'squared is', x * x)

import pandas as pd


# In[3]:


death_db = pd.read_csv('Downloads/dsdeath.csv')


# In[7]:


print('observations {0} and attributes {1}'.format(death_db.shape[0], (death_db.shape[1])))


# In[14]:


print('*************Attributes***************')
death_db.columns


# In[11]:


death2=pd.read_csv('Downloads/decateml1.csv')


# In[12]:


print('*************Attributes***************')
death_db.columns


# In[16]:


print('**** Data ****')
death_db.head(10)


# In[19]:


data3=pd.read_csv('Downloads/def17_ian.csv')


# In[20]:


print('*************Attributes***************')
data3.columns


# In[26]:


print('**** Data ****')
data3.head()


# In[30]:


# Delete the rows with labels 0,1,5
data3.drop([0,1], axis=0).head(5)


# In[31]:


data3.head(5)


# In[41]:


df_csv = pd.read_csv('Downloads/def17_ian.csv', header=2)
df_csv.head(5)


# In[48]:


df_csv['CAUSA_DEF'].count()


# In[51]:


print (df_csv.CAUSA_DEF)


# In[80]:


table = pd.pivot_table(data=df_csv,index=['CAUSA_DEF'],aggfunc={'CAUSA_DEF':np.sum})
table


# In[104]:


table=pd.pivot_table(data=df_csv,
               index=['CAUSA_DEF'],
               values=['NACIONALID'],
               fill_value='1',
               aggfunc=np.sum,
               margins=True,
               margins_name='Total'
              )
table


# In[166]:


causa_muerte =  df_csv.groupby('CAUSA_DEF')['CAUSA_DEF'].count()
causa_muerte


# In[155]:


death_group = df_csv.groupby('CAUSA_DEF')['CAUSA_DEF'].count()
for x in death_group:
    print(x)
    


# In[151]:


largest=death_group.nlargest()
largest


# In[163]:


primera=death_db[death_db['CLAVE\tNOMBRE'].str.contains("I219")]
segunda=death_db[death_db['CLAVE\tNOMBRE'].str.contains("E119")]
tercera=death_db[death_db['CLAVE\tNOMBRE'].str.contains("E112")]

print(primera, segunda, tercera)


# In[182]:


estado =  df_csv.groupby('ENT_OCURR')['ENT_OCURR'].count()
estado


# In[179]:


#Group by two keys and then summarize each group
per_entity =  df_csv.groupby(['CAUSA_DEF','ENT_OCURR'],as_index=False).CAUSA_DEF.count()
print(per_entity)




conteo =  df_csv.groupby(['ENT_OCURR', 'CAUSA_DEF'],as_index=False).CAUSA_DEF.count()
conteo




state1_1=df_csv[df_csv['CAUSA_DEF'].str.contains("I219")]
df_csv.groupby(['ENT_OCURR', 'CAUSA_DEF'],as_index=False).CAUSA_DEF.count()
state1_1




def estadoenfermedad():
    state1_1=df_csv[df_csv['CAUSA_DEF'].str.contains("I219")]
    df_csv.groupby(['ENT_OCURR', 'CAUSA_DEF'],as_index=False).CAUSA_DEF.count()
state1_1







