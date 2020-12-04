#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: solveigraddum
"""
import numpy as np
import matplotlib.pyplot as plt

data_liste =[]
data_valg = []

import os.path
def les_csv_sample(filnavn):
    
    
    if not os.path.isfile(filnavn):
        print('Filen %s eksisterer ikke' %filnavn)
        
    else :
        
        with open (filnavn) as fil_leser:
            rad=0
            for linje in fil_leser:
                if rad == 0:
                    rad += 1
                    continue
                rad +=1
                felt = linje.rstrip().split(',')
                data_fra_fil = dict()
                
                data_fra_fil['x'] = int(felt[0])
                data_fra_fil['sample1'] = float(felt[1])
                data_fra_fil['sample2'] = float(felt[2])
                
                data_liste.append(data_fra_fil)
                
            
                
def hent_y_akse_verdier(sample):       

      y_aksen =[] 

      for y in data_liste:
          y_aksen.append(y[sample])
      
        
      return y_aksen  
      
      
def hent_x_akse_verdier():       

      x_aksen =[] 

      for x in data_liste:
          x_aksen.append(str(x['x']))
      
      return x_aksen  
  
def les_csv_valgfil(filnavn):
    
    
    if not os.path.isfile(filnavn):
        print('Filen %s eksisterer ikke' %filnavn)
        
    else :
        
        with open (filnavn, 'r', encoding = "utf-8") as fil_leser:
            rad=0
            for linje in fil_leser:
                if rad <3:
                    rad += 1
                    continue
                rad +=1
                felt = linje.rstrip().split(';')
                data_fra_fil = dict()
                
                data_fra_fil['parti'] = str(felt[0])
                data_fra_fil['2017'] = int(felt[3])
                
                data_valg.append(data_fra_fil)
    

                

def hent_x_akse_partier():       

      x_aksen =[] 

      for parti in data_valg:
          x_aksen.append(parti['parti'])
      
      print(x_aksen)    
      
      return x_aksen      

def hent_y_akse_stemmer():       

      y_aksen =[] 

      for parti in data_valg:
          y_aksen.append(parti['2017'])
      
      print(y_aksen)    
      
      return y_aksen      
            

def main():
    
    
    les_csv_valgfil('tabell.csv')
    x = hent_x_akse_partier()
    
    y = hent_y_akse_stemmer()
    print(y)
    
    
    plt.xticks(rotation=90)
    plt.bar(x,y)
    plt.show()
    les_csv_sample('uke46sample.csv')
    
    
    
    plt.plot(hent_x_akse_verdier(),hent_y_akse_verdier('sample1'))
    plt.plot(hent_x_akse_verdier(),hent_y_akse_verdier('sample2'))

    plt.show()
    
    
    
    
main()    