#!/usr/bin/env python
# coding: utf-8

# In[113]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plot


# In[114]:


# Primero cargo mis datos con pandas para poder ver el dataframe y así, a la hora de cargarlo con numpy, solo cargar las columnas que me interesan ya que 24 son muchas y no las usaremos todas.
ny_pd = pd.read_csv("C:/Users/mpf_2/Downloads/Speculation_Watch_List.csv")


# In[115]:


ny_pd.shape
#534 filas x 24 columnas


# In[116]:


ny_pd


# In[117]:


# Una vez visualizado ya cargo mis datos con Numpy
ny = np.genfromtxt("C:/Users/mpf_2/Downloads/Speculation_Watch_List.csv", dtype=str, usecols = (3,4,18,19,20), delimiter=",")
ny[:10]


# In[118]:


#Vemos que tenemos 5 columnas y 535 filas
print(np.size(ny[0]))
print(np.size(ny[:,0]))


# In[119]:


##### Minimo y máximo Tax Lot
# Primero cargaremos los datos en la variable lot
lot = ny[1:,0]

# Convertimos a float para poder hacer cálculos
lot2 = lot.astype(float)

# Y finalmente encontramos el minimo y el máximo
min_lot = np.amin(lot2)
max_lot = np.amax(lot2)
print("Valor mínimo: ",min_lot)
print("Valor máximo: ",max_lot)


# In[120]:


##### Minimo y máximo Tax Block
# Primero cargaremos los datos en la variable block
block = ny[1:,1]

# Convertimos a float para poder hacer cálculos
block2 = block.astype(float)

# Y finalmente encontramos el minimo y el máximo
min_block = np.amin(block2)
max_block = np.amax(block2)
print("Valor mínimo: ",min_block)
print("Valor máximo: ",max_block)


# In[121]:


##### Media Tax Lot y Tax Block
lot2_media = np.mean(lot2)
print("Media de Tax Lot:",lot2_media)
block2_media = np.mean(block2)
print("Media de Tax Block:",block2_media)


# In[122]:


##### Desviación Tax Lot y Tax Block
lot2_std = np.std(lot2)
print("Desviación de Tax Lot:",lot2_std)
block2_std = np.std(block2)
print("Desviación de Tax Block:",block2_std)


# In[123]:


##### Varianza Tax Lot y Tax Block
lot2_var = np.var(lot2)
print("Varianza de Tax Lot:",lot2_var)
block2_var = np.var(block2)
print("Varianza de Tax Block:",block2_var)


# In[124]:


##### Suma de todos los Tax Lot
lot_sum = np.sum(lot2)
print("Suma de Tax Lot: ", lot_sum)


# In[125]:


plot.bar(np.arange(0,len(lot2)),lot2)


# In[126]:


plot.bar(np.arange(0,len(block2)),block2)

