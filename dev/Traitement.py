# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:58:00 2019

@author: 33647
"""

from zipfile import ZipFile
import json
import re
import cv_coords

def get_info(continent,country):
    with ZipFile(continent+'.zip','r') as z:
        info = json.loads(z.read(country))
        return(info)
        



def get_name(info):
    vn=info['conventional_long_name']
    while vn[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", vn)
        vn=m.group(1)
    return(vn)
    
def print_capital(info):
    capital=info['capital']
    while capital[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", capital)
        capital=m.group(1)
    pays=info['common_name']
    if common_name(info)=='Brazil':
       coordonnees= '15|47|S|47|52|W'
       c=cv(coordonnees)
    elif info['conventional_long_name']=='Republic of Vanuatu':
       c= -17.7450363,168.315741
    else:
        coordonnees=info['coordinates']
        c=cv(coordonnees[8:])
    return(capital,c)

with ZipFile('oceania.zip','r') as z:
    l=z.namelist()  
    
def print_capitalNauru(info):
    capital='Aucune officiellement, mais officieusement District de Yaren'
    while capital[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", capital)
        capital=m.group(1)
    pays=info['common_name']
    coordonnees=info['coordinates']
    c=cv(coordonnees[8:])
    return(capital,c)


def print_capitalPalau(info):
    capital=info['capital']
    while capital[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", capital)
        capital=m.group(1)
    pays='Palau'
    coordonnees=info['coordinates']
    c=cv(coordonnees[8:])
    return(capital,c)
    
def print_capitalGuyana(info):
    capital=info['capital'][2:11]
    pays=info['common_name']
    coordonnees=info['coordinates']
    c=cv(coordonnees[8:])
    return(capital,c)


def print_capitalBolivia(info):
    capital=info['capital']
    while capital[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", capital)
        capital=m.group(1)
    pays=info['common_name']
    coordonnees='19|02|N|65|15|W'
    c=cv(coordonnees[8:])
    return(capital,c)
    
def get_nameArgentina(info):
    vn='Argentine Republic'
    return(vn)
    
def get_regime(info):
    if common_name(info)=='Papua New Guinea' or common_name(info)=='Tonga':
        return('Unitary parliamentary constitutional monarchy')
    if common_name(info)=='Samoa':
        return('Unitary dominant-party aristocracy parliamentary democracy with a trace of aristocracy')
    if common_name(info)=='Brazil':
        return('Federal presidential constitutional republic')
    if common_name(info)=='Guyana':
        return('Unitary presidential constitutional socialist republic')
    s=''
    rg=info['government_type']
    l=rg.split('] [')
    for i in range(len(l)):
        while '|' in l[i]:
            a=l[i].index('|')
            l[i]=l[i][a+1:]
        while '[' in l[i]:
            l[i]=l[i].replace('[','')
        while ']' in l[i]:
            l[i]=l[i].replace(']','')
        while '}}' in l[i]:
            l[i]=l[i].replace('}}','')
    for n in l:
        s= s +' '+ n
    if s[0]==' ':
        s=s[1:]
    return(s)
    
def get_population(pays,info):
    if pays=='Venezuela':
        return('28,067,000')
    if  pays=='Federated_States_of_Micronesia':
        return('110,986')
    if pays=='Solomon_Islands':
        return('514,040')
    if pays=='Bolivia':
        return('11,428,245')
    if pays=='Brazil':
        return('210,147,125')
    if pays=='Colombia':
        return('48,258,494')
    if pays=='Paraguay':
        return('7,152,703')
    return(info['population_census'])

    

    
def get_aire(info):
    return(info['area_km2'])
    

    
def get_langue(info):
    lg=[]
    if get_name(info)=='Republic of Fiji':
        return(['English', 'Fijian', 'Rotuman','Fiji Hindi'])
    elif get_name(info)=='Independent State of Papua New Guinea':
        return(['Engligh','Hiri Motu','PNG Sign Language','Tok Pisin'])
    elif get_name(info)=='Plurinational State of Bolivia':
        return(['Spanish','36 indigenous languages'])
    else:
        try:
            langue=info['official_languages']
        except:
            langue=info['languages']
        matches = re.findall(r'\[\[.+?\]\]',langue) #Fiji, Papua, Bolivia,
        for i in matches:
            t = re.search(r"\b\|\w+", i)
            try:
                l = t.group()
                l=l[1:]
                lg.append(l)
            except:
                x=3
        
        return(lg)
        
def common_name(info):
    if get_name(info)=='Republic of Palau':
        return('Palau')
    cn=info['common_name']
    return(cn)
    
def get_monnaie(info):
    if common_name(info)=='Venezuela':
        return(['Petro','Bolívar'])
    lg=[]
    mn=info['currency']
    matches = re.findall(r'\[\[.+?\]\]',mn)
    for i in matches:
            t = re.search(r"\b\|\w+", i)
            try:
                l = t.group()
                l=l[1:]
            except:
                l=i[2:-2]
            if not('Dollar sign' in l):
                lg.append(l)
                
                
    return(lg)
    
def get_drive(info):
    if common_name(info)=='Argentina':
        return('right')
    elif common_name(info)=='Samoa':
        return('left')
    else:
        dr=info['drives_on']
        try:
            t = re.search(r"\b\|\w+", dr)
            l = t.group()
            l=l[1:]
        except:
            l=dr
        return(l)

def get_call(info):
    cc=info["calling_code"]
    if '|' in cc:
        a=cc.index('|')
        l=cc[a+1:-2]
    else:
        l=cc[2:-2]
    return(l)
    
def get_web(info):
    dn=info['cctld']
    return(dn[2:-2])
    
def get_pib(info):
    if common_name(info)=='Australia':
        return('$1.500 trillion')
    pib=info['GDP_nominal']
    a=pib.index('$')
    pib=pib[a:]
    if '&' in pib:
        a=pib.index('&')
        pib=pib[:a]+' '+pib[a+6:]
    return(pib)
