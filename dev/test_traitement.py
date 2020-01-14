# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 09:00:07 2019

@author: 33647
"""
import Traitement

data=get_info('oceania','Vanuatu.json')
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
    D[pays[:-5]]['Phone']=get_call(data)
    D[pays[:-5]]['Langue']=get_langue(data)
    D[pays[:-5]]['web']=get_web(data)
    D[pays[:-5]]['Drive']=get_drive(data)
    D[pays[:-5]]['Monnaie']=get_monnaie(data)
    if pays=='Nauru.json':
        print(pays)
        
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capitalNauru(data)
    elif pays=='Palau.json':
        print(pays)
        
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capitalPalau(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
        D[pays[:-5]]['PIB']=get_pib(data)
        #Mo
        #D
        #P
    elif pays=='Federated_States_of_Micronesia.json':
        print(pays)
        
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
    elif pays=='Solomon_Islands.json':
        print(pays)
        
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
    else:
        print(pays)
        
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
        
O=D        
with ZipFile('south_america.zip','r') as z:
    l=z.namelist()
    
D={}
for pays in l:
    D[pays[:-5]]={}
    D[pays[:-5]]['Drapeau']=pays[:-5]+'.png'
    data=get_info('south_america',pays)
    D[pays[:-5]]['Phone']=get_call(data)
    D[pays[:-5]]['Langue']=get_langue(data)
    D[pays[:-5]]['web']=get_web(data)
    D[pays[:-5]]['Drive']=get_drive(data)
    D[pays[:-5]]['Monnaie']=get_monnaie(data)
    if  pays=='Argentina.json':
        print(pays)
        
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Aire']=get_aire(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_nameArgentina(data),print_capital(data)
    elif  pays=='Bolivia.json':
        print(pays)
        
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Aire']=get_aire(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capitalBolivia(data)
    elif  pays=='Guyana.json':
        print(pays)
        
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capitalGuyana(data)
        D[pays[:-5]]['Aire']=get_aire(data)
    elif pays=='Brazil.json':
        print(pays)
       
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
    elif pays=='Colombia.json':
        print(pays)
       
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
    elif pays=='Paraguay.json':
        print(pays)
   
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
    elif pays=='Venezuela.json':
        print(pays)
      
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
    else:
        print(pays)
     
        D[pays[:-5]]['PIB']=get_pib(data)
        D[pays[:-5]]['vn'],D[pays[:-5]]['Capital']=get_name(data),print_capital(data)
        D[pays[:-5]]['Regime']=get_regime(data)
        D[pays[:-5]]['Population']=get_population(pays[:-5],data)
        D[pays[:-5]]['Aire']=get_aire(data)
        
SA=D
