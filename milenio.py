#!/usr/bin/env python
# coding: utf-8

# In[26]:


import requests
from bs4 import BeautifulSoup

request=requests.get("https://www.milenio.com/")
soup=BeautifulSoup(request.text,"html.parser")

imagen=soup.select(".image")#si hay espacio en las clases signfica que hay más de una clase . si es clase y # para id
for i in range(len(imagen)):
    imagen=soup.select(".image")[i]
    if imagen.find('img')["alt"]=="":
        continue
    else:
        print("Título de la imagen: " ,imagen.find('img')["alt"])
        print("Imagen: ","https://www.milenio.com/"+imagen.find('img')["data-src"],"\n")
    

