#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""


@author: solveigraddum
"""

def skriv_til_fil():
    """
    For hver x fra 1 til 10 og
    For hver y fra 1 til 10
    
    Regner ut x*y
    
    Utregning skrives til tekstfilen reultat.txt
    på følgende format
    " x * y = svar "
    
    """
    
    with open('resultat' ,'a') as writer:
        print('Starter utregningen...')
        for x in range(1,11):
            for y in range (1,11):
                writer.write('{0:<2d} * {1:<2d} = {2:<3d}\n'.format(x,y, x*y))
          
    print('Utregningen er ferdig')

def lese_fra_fil():
    """
    Leser hver linje fra resultat.txt
    Henter ut svaret
    Print til konsollen
      antall svar < 50
      antall svar >= 50
      gjennomsnittet av alle svarene
    
    >>>
    158 av svarene er mindre enn 50.
    42 av svarene er større eller lik 50. 
    Gjennomsnittet av svarene er 30.
    

    """
    
    større_el_lik=0
    mindre=0
    gjennomsnitt=0
    sum_svar =0;
    
    with open('resultat','r') as reader:
         for linje in reader:
             
             deler= linje.split('=')
             svar = int(deler[1])
             sum_svar = sum_svar + svar
             
             if svar <50:
                 mindre +=1
             else :
                 print(svar)
                 større_el_lik +=1
                 
    gjennomsnitt =sum_svar/(mindre +større_el_lik)

    print('%-3d av svarene er mindre enn 50.' %mindre)          
    print('%-3d av svarene er større eller lik 50.'%større_el_lik) 
    print('Gjennomsnittet av svarene er %3d.' %gjennomsnitt)
    
def main():
    skriv_til_fil()
    print()
    lese_fra_fil()

main()    