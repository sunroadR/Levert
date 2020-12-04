#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""


@author: solveigraddum
"""

from datetime import datetime
from datetime import timedelta
import locale
locale.setlocale(locale.LC_ALL,'no_NO')




def oppgave1a():
    """
    printer dato og tid følgende formatet
    I dag er det dd.mm.yy, klokken er HH:MM
    >>> I dag er det 14.10.20, klokken er 16:10
    """
    dag = datetime.now()
    
    print (dag.strftime('I dag er det %d.%m.%Y, Klokken er %H:%m.'))
    
def  oppgave1b():
    """
    printer dato og tid følgende formatet
    I dag er det dd.mm.yyyy, klokken er HH:MM:SS
    >>> I dag er det 14.10.2020, klokken er 16:10:17
    """
    
    dag = datetime.now()
    
    print (dag.strftime('I dag er det %A %d.%m.%Y, Klokken er %H:%m:%S.'))
                       

def oppgave1c():
    """
    printer dato og tid følgende formatet
    I dag er det ukedag dd. månede. 
    >>> I dag er det onsdag 14. oktober.
    """
    
    dag = datetime.now()
    
    print ('I dag er det '+dag.strftime('%A %d.%B.')+'')

def oppgave2a():
    """
    leser inn dato og tid, som input fra bruker
    på følgende format : dd.mm.yy
    >>> Vennligst oppgi en dato 'dd.mm.yy': 14.10.20
        2020-10-14 00:00:00
    """
    dato=datetime.strptime(input("Vennligst oppgi en dato 'dd.mm.yy': ")
                                , "%d.%m.%y")
    print(dato)
    

def oppgave2b():
    """
    leser inn dato og tid, som input fra bruker
    på følgende format : dd-mm-yyyy
    >>> Vennligst oppgi en dato 'dd-mm-yyyy': 14.10.2020
        2020-10-14 00:00:00
    """
    
    dato=datetime.strptime(input("Vennligst oppgi en dato 'dd-mm-yyyy': "),
                          "%d-%m-%Y")
    print(dato)
        
    
def oppgave2c():
    """
    leser inn dato og tid, som input fra bruker
    på følgende format : dd, mm, yy
    >>> Vennligst oppgi en dato 'dd, mm, yy': 14, 10, 20
        2020-10-14 00:00:00
    """
    
    dato=datetime.strptime(input("Vennligst oppgi en dato 'dd, mm, yy': "),
                          "%d, %m, %y")
    print(dato)
             
def oppgave2d():
    """
    leser inn dato og tid, som input fra bruker
    på følgende format : dd/mm-yyyy
    >>> Vennligst oppgi en dato 'dd/mm-yyyy': 14/10-2020
        2020-10-14 00:00:00
    """
    
    
    dato=datetime.strptime(input("Vennligst oppgi en dato 'dd/mm-yyyy': "),
                          "%d/%m-%Y")
    print(dato)    
    
def oppgave3a():
     """
    Printer datoen som er 10 dager frem i tid fra i dag
    På formatet:
    'om 10 dager er det ukedag dd. måned'    
    >>> 
    Om 10 dager er det onsdag 4. november

    """
     i_dag=datetime.now()
     om_ti_dager= i_dag + timedelta(10)
     print(om_ti_dager.strftime('Om 10 dager er det %A %d. %B.') )
 
def oppgave3b():
    """
    Regn ut hvor mange (hele) dager det er igjen av nåværende år
    >>>
    Det er 66 igjen av 2020
    """
    år_2020 = datetime(2020, 12, 31)
    i_dag = datetime.now()
    dager_igjen =år_2020-i_dag
    print(år_2020.strftime('Det er '+str(dager_igjen.days)+' igjen av %Y'))
  
def oppgave3c():
    

    dag1= datetime(2019, 12, 31)
    dag2 =datetime(2020, 12, 31)
    antalldager_20 =dag2-dag1 

    print(dag2.strftime('%Y består av '+str(antalldager_20.days)+' dager'))
    
    
def main():
    print()
    oppgave1a()
    print()
    oppgave1b()
    print()
    oppgave1c()
    print ()
    oppgave2a()
    print()
    oppgave2b()
    print()
    oppgave2c()
    print()
    oppgave2d()
    print()
    oppgave3a()
    print()
    oppgave3b()
    print()
    oppgave3c()
   
    

main()    