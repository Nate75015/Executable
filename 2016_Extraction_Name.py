
# coding: utf-8

# In[1]:

import pandas as pd
import os


# In[3]:

print('Quelles marques voulez-vous extraire ? (Utilisez le séparateur "," svp) !')


# In[4]:

answer = input()


# In[ ]:

print('Comment voulez vous appeller votre fichier de sortie ?')


# In[ ]:

ANSWER2 = input()


# In[5]:

List = answer.split(",")
ListFinal = []
for ele in List:
    ListFinal.append(ele.strip())


# In[6]:

ListFinal


# In[ ]:

print("Chargement du fichier 1")


# In[7]:

Doc1 = pd.read_excel('week1_2\\ORD-227368-D1N4_DATA_wk01-02.xlsx',sheet_name=1)
Doc1['Année'] = 2016
Doc1['Semaine'] = '01-02'
DOC1 = Doc1[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq51','q5_1_1','q5bis_1',
             'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1','q23_1',
             'xchosenq52','q5_1_2','q5bis_2','q6_1_2','q7_2','q11x1_2','q11x2_2','q11x3_2','q14_2','q18x1_1_2',
             'q18x2_1_2','q18x3_1_2','q23_2','xchosenq53','q5_1_3','q5bis_3','q6_1_3','q7_3','q11x1_3','q11x2_3',
             'q11x3_3','q14_3','q18x1_1_3','q18x2_1_3','q18x3_1_3','q23_3','xchosenq54','q5_1_4','q5bis_4',
             'q6_1_4','q7_4','q11x1_4','q11x2_4','q11x3_4','q14_4','q18x1_1_4','q18x2_1_4','q18x3_1_4','q23_4',
             'Année','Semaine'
            ]]


# In[ ]:

print("Fin de chargement du fichier 1")


# In[ ]:

print("Chargement du fichier 2")


# In[8]:

Doc2 = pd.read_excel('week3_6\\Final\\ORD-227368-D1N4_data_wks_03-06.xlsx',sheet_name=1)
Doc2['Année'] = 2016
Doc2['Semaine'] = '03-06'
DOC2 = Doc2[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq51','q5_1_1','q5bis_1',
             'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1','q23_1',
             'xchosenq52','q5_1_2','q5bis_2','q6_1_2','q7_2','q11x1_2','q11x2_2','q11x3_2','q14_2','q18x1_1_2',
             'q18x2_1_2','q18x3_1_2','q23_2','xchosenq53','q5_1_3','q5bis_3','q6_1_3','q7_3','q11x1_3','q11x2_3',
             'q11x3_3','q14_3','q18x1_1_3','q18x2_1_3','q18x3_1_3','q23_3','xchosenq54','q5_1_4','q5bis_4',
             'q6_1_4','q7_4','q11x1_4','q11x2_4','q11x3_4','q14_4','q18x1_1_4','q18x2_1_4','q18x3_1_4','q23_4',
             'Année','Semaine'
            ]]


# In[ ]:

print("Fin de chargement du fichier 2")


# In[ ]:

print("Chargement du fichier 3")


# In[9]:

Doc3 = pd.read_excel('week7_10\\ORD-227368-D1N4_data_wks07-10.xlsx',sheet_name=1)
Doc3['Année'] = 2016
Doc3['Semaine'] = '07-10'
DOC3 = Doc3[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq51','q5_1_1','q5bis_1',
             'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1','q23_1',
             'xchosenq52','q5_1_2','q5bis_2','q6_1_2','q7_2','q11x1_2','q11x2_2','q11x3_2','q14_2','q18x1_1_2',
             'q18x2_1_2','q18x3_1_2','q23_2','xchosenq53','q5_1_3','q5bis_3','q6_1_3','q7_3','q11x1_3','q11x2_3',
             'q11x3_3','q14_3','q18x1_1_3','q18x2_1_3','q18x3_1_3','q23_3','xchosenq54','q5_1_4','q5bis_4',
             'q6_1_4','q7_4','q11x1_4','q11x2_4','q11x3_4','q14_4','q18x1_1_4','q18x2_1_4','q18x3_1_4','q23_4',
             'Année','Semaine'
            ]]


# In[ ]:

print("Fin de chargement du fichier 3")


# In[ ]:

print("Chargement du fichier 4")


# In[10]:

Doc4 = pd.read_excel('week15_19\\ORD-227368-D1N4_weeks_15-19_final_data.xlsx',sheet_name=1)
Doc4['Année'] = 2016
Doc4['Semaine'] = '15-19'
DOC4 = Doc4[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq51','q5_1_1','q5bis_1',
             'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1','q23_1',
             'xchosenq52','q5_1_2','q5bis_2','q6_1_2','q7_2','q11x1_2','q11x2_2','q11x3_2','q14_2','q18x1_1_2',
             'q18x2_1_2','q18x3_1_2','q23_2','xchosenq53','q5_1_3','q5bis_3','q6_1_3','q7_3','q11x1_3','q11x2_3',
             'q11x3_3','q14_3','q18x1_1_3','q18x2_1_3','q18x3_1_3','q23_3','xchosenq54','q5_1_4','q5bis_4',
             'q6_1_4','q7_4','q11x1_4','q11x2_4','q11x3_4','q14_4','q18x1_1_4','q18x2_1_4','q18x3_1_4','q23_4',
             'Année','Semaine'
            ]]


# In[ ]:

print("Fin de chargement du fichier 4")


# In[ ]:

print("Chargement du fichier 5")


# In[11]:

Doc5 = pd.read_excel('week24_27\\ORD-227368-D1N4_Final_data_wks24-27.xlsx',sheet_name=1)
Doc5['Année'] = 2016
Doc5['Semaine'] = '24-27'
DOC5 = Doc5[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq51','q5_1_1','q5bis_1',
             'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1','q23_1',
             'xchosenq52','q5_1_2','q5bis_2','q6_1_2','q7_2','q11x1_2','q11x2_2','q11x3_2','q14_2','q18x1_1_2',
             'q18x2_1_2','q18x3_1_2','q23_2','xchosenq53','q5_1_3','q5bis_3','q6_1_3','q7_3','q11x1_3','q11x2_3',
             'q11x3_3','q14_3','q18x1_1_3','q18x2_1_3','q18x3_1_3','q23_3','xchosenq54','q5_1_4','q5bis_4',
             'q6_1_4','q7_4','q11x1_4','q11x2_4','q11x3_4','q14_4','q18x1_1_4','q18x2_1_4','q18x3_1_4','q23_4',
             'Année','Semaine'
            ]]


# In[ ]:

print("Fin de chargement du fichier 5")


# In[ ]:

TOT = pd.concat([DOC1,DOC2,DOC3,DOC4,DOC5])
TOT


# In[ ]:

def Extraction(DataFrame,EleListFinal):
    Matrice = DataFrame
    try :
        DOC2 = Matrice[(Matrice['xchosenq51'] == EleListFinal)]
        DOC2 = DOC2[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq51','q5_1_1','q5bis_1',
                     'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1',
                     'q23_1','Année','Semaine']]
        DOC2.columns = ['Sex','Age','Profession','ClasseAge','Adresse','CodePostale','Marque','CSAT','Verbatim','NPS',
                        'Fidelite','TOD1_1_1','TOD1_1_2','TOD1_1_3','TOD2','CES_1','CES_2','CES_3','Image','Année',
                        'Semaine']
    except:
        DOC2 = pd.DataFrame(columns=['Sex','Age','Profession','ClasseAge','Adresse','CodePostale','Marque','CSAT','Verbatim','NPS',
                        'Fidelite','TOD1_1_1','TOD1_1_2','TOD1_1_3','TOD2','CES_1','CES_2','CES_3','Image','Année',
                        'Semaine'])
        DOC2 = DOC2.fillna(0)
    try :
        DOC3 = Matrice[(Matrice['xchosenq52'] == EleListFinal)]
        DOC3 = DOC3[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq52','q5_1_1','q5bis_1',
                     'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1',
                     'q23_1','Année','Semaine']]
        DOC3.columns = ['Sex','Age','Profession','ClasseAge','Adresse','CodePostale','Marque','CSAT','Verbatim','NPS',
                        'Fidelite','TOD1_1_1','TOD1_1_2','TOD1_1_3','TOD2','CES_1','CES_2','CES_3','Image','Année',
                        'Semaine']
    except:
        DOC3 = pd.DataFrame(columns=['Sex','Age','Profession','ClasseAge','Adresse','CodePostale','Marque','CSAT','Verbatim','NPS',
                        'Fidelite','TOD1_1_1','TOD1_1_2','TOD1_1_3','TOD2','CES_1','CES_2','CES_3','Image','Année',
                        'Semaine'])
        DOC3 = DOC2.fillna(0)
    try :
        DOC4 = Matrice[(Matrice['xchosenq53'] == EleListFinal)]
        DOC4 = DOC4[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq53','q5_1_1','q5bis_1',
                     'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1',
                     'q23_1','Année','Semaine']]
        DOC4.columns = ['Sex','Age','Profession','ClasseAge','Adresse','CodePostale','Marque','CSAT','Verbatim','NPS',
                    'Fidelite','TOD1_1_1','TOD1_1_2','TOD1_1_3','TOD2','CES_1','CES_2','CES_3','Image','Année',
                    'Semaine']
    except:
        DOC4 = pd.DataFrame(columns=['Sex','Age','Profession','ClasseAge','Adresse','CodePostale','Marque','CSAT','Verbatim','NPS',
                        'Fidelite','TOD1_1_1','TOD1_1_2','TOD1_1_3','TOD2','CES_1','CES_2','CES_3','Image','Année',
                        'Semaine'])
        DOC4 = DOC2.fillna(0)
    try :
        DOC5 = Matrice[(Matrice['xchosenq54'] == EleListFinal)]
        DOC5 = DOC5[['s1','s2_1','xrecodes3','xage','agglo','recodepostcode','xchosenq54','q5_1_1','q5bis_1',
                     'q6_1_1','q7_1','q11x1_1','q11x2_1','q11x3_1','q14_1','q18x1_1_1','q18x2_1_1','q18x3_1_1',
                     'q23_1','Année','Semaine']]
        DOC5.columns = ['Sex','Age','Profession','ClasseAge','Adresse','CodePostale','Marque','CSAT','Verbatim','NPS',
                        'Fidelite','TOD1_1_1','TOD1_1_2','TOD1_1_3','TOD2','CES_1','CES_2','CES_3','Image','Année',
                        'Semaine']
    except:
        DOC5 = pd.DataFrame(columns=['Sex','Age','Profession','ClasseAge','Adresse','CodePostale','Marque','CSAT','Verbatim','NPS',
                        'Fidelite','TOD1_1_1','TOD1_1_2','TOD1_1_3','TOD2','CES_1','CES_2','CES_3','Image','Année',
                        'Semaine'])
        DOC5 = DOC2.fillna(0)
    TOT = pd.concat([DOC2,DOC3,DOC4,DOC5])
    return TOT


# In[13]:

Answer = []
for ele in ListFinal:
    Answer.append(Extraction(TOT,ele))


# In[ ]:

Final = pd.concat(Answer)
Final


# In[ ]:

Answer3 = 'verbatim_2016_' + ANSWER2 + '.csv'


# In[16]:

Final.to_csv(Answer3, sep = ';', encoding = 'utf-8')


# In[17]:

print(ListFinal)
DateListFinal = ['01-02','03-06','07-10','15-19','24-27']
df = pd.DataFrame(0, index = ListFinal, columns = DateListFinal)


# In[18]:

for (ele,numele) in zip(ListFinal,range(len(ListFinal))) :
    for (mois,nummois) in zip(DateListFinal,range(len(DateListFinal))):
        Filtre = (Final.Marque == ele) & (Final.Semaine == mois)
        df.iloc[numele,nummois] = Final[Filtre].shape[0]


# In[ ]:

Answer4 = 'Resume_Extraction_2016' + ANSWER2 + '.csv'


# In[19]:

df.to_csv(Answer4, sep=';', encoding='utf-8')


# In[ ]:




# In[ ]:




# In[ ]:




# In[ ]:



