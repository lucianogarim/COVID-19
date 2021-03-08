# -*- coding: utf-8 -*-
"""
Created on Sun Mar  7 16:35:56 2021

@author: luciano
"""

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

url='https://ti.saude.rs.gov.br/covid19/download'
ds=pd.read_csv(url, sep=";")


ds = ds.replace(np.nan, '', regex=True)
ds['DATA_CONFIRMACAO']= pd.to_datetime(ds['DATA_CONFIRMACAO'])
ds['DATA_SINTOMAS']= pd.to_datetime(ds['DATA_SINTOMAS'])
ds['DATA_EVOLUCAO']= pd.to_datetime(ds['DATA_EVOLUCAO'])
ds['DATA_INCLUSAO_OBITO']= pd.to_datetime(ds['DATA_INCLUSAO_OBITO'])
ds['DATA_EVOLUCAO_ESTIMADA']= pd.to_datetime(ds['DATA_EVOLUCAO_ESTIMADA'])

# Número total de casos confirmados
num_total_casos = len(ds)
# Hospitalizações
tot_hosp=ds.loc[ds.HOSPITALIZADO=='SIM','HOSPITALIZADO'].count()
# Obtidos
tot_obt=ds.loc[ds.EVOLUCAO=='OBITO','EVOLUCAO'].count()
# Em acompanhamento
tot_acom=ds.loc[ds.EVOLUCAO=='EM ACOMPANHAMENTO','EVOLUCAO'].count()
# Recuperados
tot_rec=ds.loc[ds.EVOLUCAO=='RECUPERADO','EVOLUCAO'].count()

num_casos=ds[['MUNICIPIO','COD_IBGE']].groupby('MUNICIPIO').count().reset_index()
num_casos_10=num_casos.nlargest(10,'COD_IBGE')


fig1, ax1 = plt.subplots()
ax1=plt.bar(num_casos_10['MUNICIPIO'],num_casos_10['COD_IBGE'])
plt.xticks(rotation=30, ha='right')


hom_mul=[ds.loc[ds.SEXO=='Masculino','SEXO'].count(),ds.loc[ds.SEXO=='Feminino','SEXO'].count()]
fig2, ax2 = plt.subplots()
ax2.pie(hom_mul,labels=['Homens','Mulheres'],autopct='%1.1f%%')

raca=[ds.loc[ds.RACA_COR=='BRANCA','RACA_COR'].count(),
      ds.loc[ds.RACA_COR=='INDIGENA','RACA_COR'].count(),
      ds.loc[ds.RACA_COR=='PARDA','RACA_COR'].count(),
      ds.loc[ds.RACA_COR=='AMARELA','RACA_COR'].count(),
      ds.loc[ds.RACA_COR=='PRETA','RACA_COR'].count(),
      ds.loc[ds.RACA_COR=='NAO INFORMADO','RACA_COR'].count()]


fig3, ax3 = plt.subplots()
ax3.pie(raca,labels=['Branca','Indígena','Parda','Amarela','Preta','Não Informada'])
plt.legend()


