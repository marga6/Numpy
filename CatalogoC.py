#!/usr/bin/env python
# coding: utf-8

# In[122]:


import numpy as np
import pandas as pd
import matplotlib.pyplot as plot


# In[123]:


# Primero cargo mis datos con pandas para una más fácil y rápida visualización del dataframe
gov_pd = pd.read_csv("C:/Users/mpf_2/Downloads/gov_10a_exp_page_linear.csv.gz")
gov_pd


# In[124]:


# Ahora ya los cargo con Numpy. Solo me interesa cargar 3 de las columnas ("geo", "time_period" y "obs_value") puesto que las demás no las usaremos para nada.
gov = np.loadtxt("C:/Users/mpf_2/Downloads/gov_10a_exp_page_linear.csv", dtype=str, usecols = (7,8,9),delimiter=",")
gov[:10,]


# In[125]:


#Vemos cuantas columnas y filas tiene nuestro nuevo dataset
print(np.size(gov[0]))
print(np.size(gov[:,0]))


# In[126]:


# Quiero obtener el valor mínimo y máximo de la columna Obs_Value
# Para ello, primero selecciono la columna OBS_VALUE a partir de la fila 1, puesto que la 0 son los nombres de las variables.
obs_val = gov[1:,2]
# Lo convierto a float puesto que sino, más tarde, no podré realizar los cálculos que quiero.
obs_val2 = obs_val.astype(float)
obs_val2


# In[127]:


# Valor mínimo y máximo de la columna Obs_Value
minimo = np.amin(obs_val2)
maximo = np.amax(obs_val2)
print("Valor mínimo: ",minimo)
print("Valor máximo: ",maximo)


# In[128]:


# Obtenemos la varianza
varianza = obs_val2.var()
print("La varianza es: ", varianza)


# In[129]:


# Obtenemos la media y la desviación
media = obs_val2.mean()
print("La media es: ", media)
desviacion = obs_val2.std()
print("La desviación es: ", desviacion)


# In[130]:


# Generamos un gráfico de puntos con las localidades geopóliticas (sus abreviaciones) en le eje x y los valores observados en el eje y.
x = gov[1:,0]
y = obs_val2
plot.title("Localidades geopolíticas x Valores observados") 
plot.xlabel("Localidades geopolíticas") 
plot.ylabel("Valores Observados") 
plot.plot(x,y,"ob") 
plot.show()


# In[131]:


# Realizmos otra gráfica pero esta vez de barras, en la que cada barra es un año (por ejemplo el año 2012) en el eje x y en el eje y siguen estando los valores observados.
x = gov[1:,1]
y = obs_val2  
 
plot.bar(x, y, align = 'center') 
plot.title('Bar graph') 
plot.ylabel('Valores Observados') 
plot.xlabel('Años')  

plot.show()
# Con esta gráfica podemos ver como, más o menos, los resultados para todos los años son similares, a excepción de en el 2013 y 2020 que son un tanto mayores.

