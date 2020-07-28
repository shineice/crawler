#!/usr/bin/env python
# coding: utf-8

# In[1]:


import datetime
import dropbox
import pandas as pd


# In[2]:


dbx = dropbox.Dropbox('jSOgekM9_boAAAAAAAtzlgmQHOXIJhE86JM4YkHS9saAnlnXZjF7jdH2UgYolUdg')


# In[3]:


def createlink(x):
   
    jpg=dbx.sharing_create_shared_link(path=x[i], short_url=False, pending_upload=None)
    jpg_url=jpg.url
    jpg_path_name=jpg.path.split('/')[-1]
    
    return jpg_url,jpg_path_name


# In[5]:


def fil(l):
    l=list(filter(lambda x: 'gif' not in x, l))
    l=list(filter(lambda x: 'Final TIFFS' not in x, l))
    l=list(filter(lambda x: 'TIF' not in x, l))
    l=list(filter(lambda x: 'TGA' not in x, l))
    lid=list(filter(lambda x: '.' not in x, l))
    jpg=list(filter(lambda x: '.jpg' in x, l))
    jpg=list(filter(lambda x: 'LS1' not in x, jpg))
    jpg=list(filter(lambda x: 'LS2' not in x, jpg))
    return lid,jpg


# In[7]:


folder=[]
for entry in dbx.files_list_folder(path='/+ Images/YOUTH').entries:
    en="/+ Images/YOUTH/"+entry.name
    folder.append(en)


# In[17]:


jpg=[]
li=[]
folder1=[]
try:
    for i in range(len(folder)):
    
        for entry in dbx.files_list_folder(path=folder[i]).entries:
            en=folder[i]+"/"+entry.name
            li.append(en)
            folder1=fil(li)[0]
            jpg+=list(set(fil(li)[1]))
except:
    extra.append(folder[i])


# In[79]:


li=[]
folder2=[]
for i in range(len(folder1)):
    for entry in dbx.files_list_folder(path=folder1[i]).entries:
        en=folder1[i]+"/"+entry.name
        li.append(en)
        folder2=fil(li)[0]
        jpg+=list(set(fil(li)[1]))


# In[80]:


li=[]
folder3=[]
extra=[]
try:
    for i in range(len(folder2)):

        for entry in dbx.files_list_folder(path=folder2[i]).entries:
            en=folder2[i]+"/"+entry.name
            li.append(en)
        folder3=fil(li)[0]
        jpg+=set(fil(li)[1])
except:
     extra.append(folder2[i])


# In[74]:


li=[]
folder4=[]
try:
    for i in range(len(folder3)):

        for entry in dbx.files_list_folder(path=folder3[i]).entries:
            en=folder3[i]+"/"+entry.name
            li.append(en)
            folder4=fil(li)[0]
            jpg1+=list(set(fil(li)[1]))
except:
    extra.append(folder3[i])


# In[75]:


li=[]
folder5=[]
for i in range(len(folder4)):
    for entry in dbx.files_list_folder(path=folder4[i]).entries:
        en=folder4[i]+"/"+entry.name
        li.append(en)
        folder5=fil(li)[0]
        jpg1+=fil(li)[1]


# In[59]:


li=[]
folder6=[]
for i in range(len(folder5)):

    for entry in dbx.files_list_folder(path=folder5[i]).entries:
        en=folder5[i]+"/"+entry.name
        li.append(en)
        folder6=fil(li)[0]
        jpg3+=fil(li)[1]


# In[83]:


jpg_all=[]
jpg_all+=jpg#YOUTH
jpg_all+=jpg1#HOME
jpg_all+=jpg2#SEATING
jpg_all+=jpg3#OCCASIONAL
jpg_all+=jpg4#DINING
jpg_all+=jpg5#BEDROOM
jpg_all+=jpg6#OUTDOOR
jpg_all=list(set(jpg_all))


# In[ ]:


folder_next=[]
url_folder_list=[]
jpg_path_name_list=[]

for i in range(len(jpg_all)):
    url_folder=[createlink(jpg_all)[0]]
    jpg_path_name=[createlink(jpg_all)[1]]
    url_folder_list+=url_folder
    jpg_path_name_list+=jpg_path_name


# In[ ]:


data = pd.DataFrame(
{'name': jpg_path_name_list,
'url': url_folder_list,
})

data=data.drop_duplicates(subset='jpg_path_name',keep='first', inplace=False)
data.to_csv('dropbox.csv')

