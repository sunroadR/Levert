#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: solveigraddum
"""


from datetime import datetime
import requests
import os.path
import statistics
import calendar
import locale
locale.setlocale(locale.LC_ALL,'no_NO')


def skrive_csv_fil(dato,oppgave,tids_bruk,effekt):
    """
    

    Parameters
    ----------
    dato : streng 
    oppgave : streng.
    tids_bruk : integer
    effekt :   integer

    skriver en CSV-fil, logg.csv , som lagrer arbeidslogg på format
    dato;oppgave;tids_bruk;effekt
   


    """
    
    if not os.path.isfile('logg'):
        with open ('logg', 'a') as skriver:
            
            skriver.write('{0:s};{1:s};{2:s};{3:s}\n'.format(
                           'dato','oppgave','tids_bruk','effekt'))
            skriver.write('{0:s};{1:s};{2:d};{3:d}\n'.format(
                           dato,oppgave,tids_bruk,effekt))
    else :
         with open ('logg', 'a') as skriver:
            skriver.write('{0:s};{1:s};{2:d};{3:d}\n'.format(
                           dato,oppgave,tids_bruk,effekt))

    
        
    



def abeids_logg():
    """
    loggfører tidsbruken til brukeren fra en arbeidsdag
    Henter dato
    Ber bruker skrive inn
    oppgave - arbeidsoppgave som skal log føres
    tids_bruk- tiden i minutter det tok å gjøre oppgaven
    effekt - brukerens vurdering av effektivitet på en skala fra én til ti

    kaller skrive_csv_fil(dato,oppgave,tids_bruk,effekt)

    """
    
    
    print('Velkommen til Arbeidsloggen!')
    
    d = datetime.now()
    dato = d.strftime('%d.%m.%Y')
    
    oppgave = input('Hva slags type oppgave har du gjennomført ? ')
    tids_bruk = int(input('Hvor mange minutter tok det ? '))
    effekt = int(input('Hvor effektiv følte du at du var (1-10) ? '))
    
    skrive_csv_fil(dato,oppgave, tids_bruk, effekt)
    
    print('Oppgaven er lagret i loggen.')

    
"Liste til lagre vær data i som blir lest i funksjonen lese_vær_data"
vær_data=[]    
    
    
def lese_vær_data():
    """

    Sjekker om filen,Florida.csv, eksister, hvis ikke printes feilmedling
    ellers leses filen med følgende data :
    Dato, Tid, Globalstraling, Solskinstid, Lufttemperatur
    Relativ, luftfuktighe, Vindretning, Vindstyrke, ufttrykk, Vindkast
   
    Dataen i filen  leses og lagresr i dictionary object vær_observsjoner,
    som blir lagt inn i vær_data listen
    


    """
   
  
      
    if not os.path.isfile('Florida.csv'):
        print('Filen FLorida eksistert ikke')
 
    else:   
        
        with open('Florida.csv') as vær_fil:
            rad = 0
            for linje in vær_fil:
                if rad == 0:
                    rad +=1
                    continue
                rad +=1
                felt = linje.rstrip().split(',')
                
                vær_observasjoner = dict()
                
                vær_observasjoner['Dato'] = felt[0]
                vær_observasjoner['Tid']  = felt[1]
                vær_observasjoner['Globalstraling'] = float(felt[2])
                vær_observasjoner['Solskinstid']    =float(felt[3])
                vær_observasjoner['Lufttemperatur'] = float(felt[4])
                vær_observasjoner['Relativ luftfuktighet'] =float(felt[5])
                vær_observasjoner['Vindretning'] = float(felt[6])
                vær_observasjoner['Vindstyrke']  = float(felt[7])
                vær_observasjoner['Lufttrykk']   = float(felt[8])
                vær_observasjoner['Vindkast']    = float(felt[9])    
                
                vær_data.append(vær_observasjoner)

                
        
    
    
 
                
def gjennomsnitt_temp_i_måned(måned):
    """
    
    måned : streng, som representer månden vi skal finne gjennomsnittstemp i
    kaller funksjonen finn_måned, som returner måneden som et hel tall
    
    legger alle luftempraturene for månend i listen temp_list,
    finner så gjennomsnitts tempraturen for måneden i temp list
    og skriver den ut

    """ 
      
    m= finn_måned(måned)
    
    temp_liste =[]
   
    for data in vær_data :
     
       if  måned == str(data['Dato'].split('-')[1]) :
           temp_liste.append((data['Lufttemperatur']))
           
    gjennsnitt= statistics.mean(temp_liste)
    print('Gjennomsnittstemperaturen i %s 2020 var %.3f'
          %(calendar.month_name[int(m)],gjennsnitt))
       
def max_vindstyrke():
    """
    Finner max vindstyrke 
    skriver ut dato og klokke slett

    """
    
    vindstyrk=0
    dato = ''
    tids_pkt =0.0
    for data in vær_data:
        if  vindstyrk < data['Vindstyrke'] :
            dato = data['Dato']
            tids_pkt =data['Tid']
    
    print('Tidspunktet med høyest vindstyrke %s kl %s' %(dato,tids_pkt))        
        
def total_soltimer(måned):
    """
    måned : streng, som representer månden vi skal finne soltimer i
    kaller funksjonen finn_måned, som returner måneden som et hel tall
    legger alle soltimene for månend i listen  soltimer
    summer så antall soltimer i lesten soltimer og skriver ut
    """
        
    m= finn_måned(måned)
   
    soltimer=[]
   
    for data in vær_data :
       if  måned == str(data['Dato'].split('-')[1]) :
           soltimer.append((data['Solskinstid']))
       
    antall_timer = sum(soltimer)       

    print('Den totale solskinnstiden i %s 2020 var %.0f'
          %(calendar.month_name[int(m)],antall_timer))
    
def finn_måned(måned):
    """
    Hjelpe-funksjon som fjerneer 0 for tallstrengene 01-09
    Parameters
    ----------
    måned : streng, som representer månden

    Returns
    -------
    m : int, som representerer månend som et tall

    """
    m=''
    if måned[0] == '0' :
        m=måned[1]
    else :
        m=måned
        
    return m    

def finn_regissøren():
    """
    Spør brukeren etter en filmtittel
    Skriver ut filemens årstall og regissør
    hvis ikke fimen finnes skrives en feilmeling 
   
    >>> Hvilken film ønsker du å vite regissøren til? The Terminal
      Django Unchained fra 2004 ble regissert av Steven Spielberg
    >>> Hvilken film ønsker du å vite regissøren til? The Termmminal  
       Finner ikke film med den tittelen 
    """
    
    film_titel = input('Hvilken film ønsker du å vite regissøren til ? ')
  
    
    res=requests.get('http://www.omdbapi.com/?t='+film_titel+'&apikey=251351e8')

    film_info = res.json()
   
    
  
    
    if film_info['Response'] == 'False' :
        
        print('Finner ikke film med den tittelen ')
        
      
    
    else :
         utgivelse = film_info['Year']
         resissør = film_info['Director']
    
         print('%s fra %s ble regissert av %s' %(film_titel,utgivelse,resissør))
        
    

def main():
    print()
    "oppgave 1"
    abeids_logg()
    print()
    "oppgave 2"
    lese_vær_data()
    gjennomsnitt_temp_i_måned('03') 
    gjennomsnitt_temp_i_måned('06')     
    max_vindstyrke()    
    total_soltimer('01')
    total_soltimer('06')
    "oppgave 3"
    finn_regissøren()
    
    
main()