#!/usr/bin/env python
# coding: utf-8

# In[41]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plot


# In[42]:


# Cargamos los datos con Numpy.
balears = np.loadtxt("C:/Users/mpf_2/Downloads/50376.csv", dtype=str, delimiter=";")
balears


# In[43]:


print(np.size(balears[:,0]))


# In[44]:


##### Series por nacidos vivos por residencia materna (nacidos)
# Primero de todo, realizamos un reshape() para que se vea más claro las diferentes columnas y variables. 
myb = balears[1:336,].reshape(67,15)
print(myb[0:3,])


# In[45]:


# Seleccionamos todas las filas de tan solo la columna 2 [:,2], puesto que esta es la de "nacidos vivos por residencia materna"
nacidos = myb[:,2]
# Lo convierto a float puesto que sino, más tarde, no podré realizar los cálculos como la media, el minimo, etc. Haremos este paso con los 5 indicadores.
nacidos2 = nacidos.astype(float)
nacidos2


# In[46]:


##### Serie ordenada por fallecidos por el luegar de residencia (fallecidos)
# Seleccionamos todas las filas de tan solo la columna 5 [:,5], puesto que esta es la de "fallecidos por el luegar de residencia"
fallecidos = myb[:,11]
fallecidos2 =fallecidos.astype(float)
fallecidos2


# In[47]:


# Serie ordenada por muertes fetales tardíaspor residencia materna (muertes_fetales)
muertes_fetales = myb[:,5]
muertes_fetales2 = muertes_fetales.astype(float)
muertes_fetales2


# In[48]:


# Serie ordenada por matrimonios por el lugar en que han fijado residencia (matrimonio)
matrimonio = myb[:,8]
matrimonio2 = matrimonio.astype(float)
matrimonio2


# In[49]:


# Serie ordenada por crecimiento vegetativo (cv)
cv = myb[:,14]
cv2 = cv.astype(float)
cv2


# In[50]:


# desviación de los cinco indicadores disponibles (desviacion)
nacidos2_std = np.std(nacidos2)
print("Desviación de nacidos vivos por residencia materna:",nacidos2_std)
fallecidos2_std = np.std(fallecidos2)
print("Desviación de fallecidos por el luegar de residencia:",fallecidos2_std)
muertes_fetales2_std = np.std(muertes_fetales2)
print("Desviación de muertes fetales tardíaspor residencia materna:",muertes_fetales2_std)
matrimonio2_std = np.std(matrimonio2)
print("Desviación de matrimonios por el lugar en que han fijado residencia:",matrimonio2_std)
cv2_std = np.std(cv2)
print("Desviación de crecimiento vegetativo: ", cv2_std)


# In[51]:


# media de los cinco indicadores disponibles (media)
nacidos2_media = np.mean(nacidos2)
print("Media de nacidos vivos por residencia materna:",nacidos2_media)
fallecidos2_media = np.mean(fallecidos2)
print("Media de fallecidos por el luegar de residencia:",fallecidos2_media)
muertes_fetales2_media = np.mean(muertes_fetales2)
print("Media de muertes fetales tardíaspor residencia materna:",muertes_fetales2_media)
matrimonio2_media = np.mean(matrimonio2)
print("Media de matrimonios por el lugar en que han fijado residencia:",matrimonio2_media)
cv2_media = np.mean(cv2)
print("Media de crecimiento vegetativo: ", cv2_media)


# In[52]:


plot.bar(np.arange(0,len(nacidos2)),nacidos2)


# In[53]:


plot.bar(np.arange(0,len(fallecidos2)),fallecidos2)


# In[54]:


plot.bar(np.arange(0,len(muertes_fetales2)),muertes_fetales2)


# In[55]:


plot.bar(np.arange(0,len(matrimonio2)),matrimonio2)


# In[56]:


plot.bar(np.arange(0,len(cv2)),cv2)

