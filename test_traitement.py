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
    if pays=='Nauru.json':
        print(pays)
        data=get_info('oceania',pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['capital']=get_name(data),print_capitalNauru(data)
    elif pays=='Palau.json':
        print(pays)
        data=get_info('oceania',pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['capital']=get_name(data),print_capitalPalau(data)
    else:
        print(pays)
        data=get_info('oceania',pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['capital']=get_name(data),print_capital(data)

with ZipFile('south_america.zip','r') as z:
    l=z.namelist()
    
for pays in l:
    D[pays[:-5]]={}
    if  pays=='Argentina.json':
        print(pays)
        data=get_info('south_america',pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['capital']=get_nameArgentina(data),print_capital(data)
    if  pays=='Bolivia.json':
        print(pays)
        data=get_info('south_america',pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['capital']=get_name(data),print_capitalBolivia(data)
    elif  pays=='Guyana.json':
        print(pays)
        data=get_info('south_america',pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['capital']=get_name(data),print_capitalGuyana(data)
    else:
        print(pays)
        data=get_info('south_america',pays)
        D[pays[:-5]]['vn'],D[pays[:-5]]['capital']=get_name(data),print_capital(data)
        