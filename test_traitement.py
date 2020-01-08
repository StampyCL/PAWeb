# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:00:07 2019

@author: 33647
"""
import Traitement

data=get_info('south_america','Argentina.json')
data['capital'][2:11]

get_name(data)
print_capital(data)

D={}

with ZipFile('oceania.zip','r') as z:
    l=z.namelist()

for pays in l:
    D[pays[:-5]]={}
    data=get_info('oceania',pays)
    D[pays[:-5]]['Drapeau']=pays[:-5]+'.png'
    D[pays[:-5]]['Population']=get_population(pays[:-5],data)
    D[pays[:-5]]['Langue']=get_langue(data)
    D[pays[:-5]]['Monnaie']=get_monnaie(data)
    D[pays[:-5]]['Drive']=get_drive(data)
    D[pays[:-5]]['Regime']=get_regime(data)
    D[pays[:-5]]['Aire']=get_aire(data)+'km²'
    D[pays[:-5]]['Phone']=get_call(data)
    D[pays[:-5]]['Domaine_internet']=get_web(data)
    D[pays[:-5]]['PIB']=get_pib(data)
    if pays=='Nauru.json':
        print(pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capitalNauru(data)
    elif pays=='Palau.json':
        print(pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capitalPalau(data)
    else:
        print(pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)

with ZipFile('south_america.zip','r') as z:
    l=z.namelist()

Q={}
  
for pays in l:
    Q[pays[:-5]]={}
    data=get_info('south_america',pays)
    Q[pays[:-5]]['Drapeau']=pays[:-5]+'.png'
    Q[pays[:-5]]['Population']=get_population(pays[:-5],data)
    Q[pays[:-5]]['Langue']=get_langue(data)
    Q[pays[:-5]]['Monnaie']=get_monnaie(data)
    Q[pays[:-5]]['Drive']=get_drive(data)
    Q[pays[:-5]]['Regime']=get_regime(data)
    Q[pays[:-5]]['Aire']=get_aire(data)+'km²'
    Q[pays[:-5]]['Phone']=get_call(data)
    Q[pays[:-5]]['Domaine_internet']=get_web(data)
    Q[pays[:-5]]['PIB']=get_pib(data)
    if  pays=='Argentina.json':
        print(pays)
        Q[pays[:-5]]['vn'],Q[pays[:-5]]['Capital']=get_nameArgentina(data),print_capital(data)
    if  pays=='Bolivia.json':
        print(pays)
        Q[pays[:-5]]['vn'],Q[pays[:-5]]['Capital']=get_name(data),print_capitalBolivia(data)
    elif  pays=='Guyana.json':
        print(pays)
        Q[pays[:-5]]['vn'],Q[pays[:-5]]['Capital']=get_name(data),print_capitalGuyana(data)
    else:
        print(pays)
        Q[pays[:-5]]['vn'],Q[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        
        
South_America=Q
Oceania=D
        
