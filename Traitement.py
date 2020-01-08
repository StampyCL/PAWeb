# -*- coding: utf-8 -*-
"""
Created on Tue Dec 17 08:58:00 2019

@author: 33647
"""

from zipfile import ZipFile
import json
import re

def get_info(continent,country):
    with ZipFile(continent+'.zip','r') as z:
        info = json.loads(z.read(country))
        return(info)
        



def get_name(info):
    vn=info['conventional_long_name']
    while vn[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", vn)
        vn=m.group(1)
    if vn=='Argentine Republic {{efn-ua|name|=|altnames|Article 35 of the [[Argentine Constitution]] gives equal recognition to the names "[[United Provinces of the Rio de la Plata]]", "Argentine Republic" and "Argentine Confederation" and using "Argentine Nation" in the making and enactment of laws.|sfn|Constitution of Argentina|loc|=|art. 35}} {{sfn|Constitution of Argentina|loc|=|art. 35}}':
        vn='Argentine Republic'
    return(vn)
    
def print_capital(info):
    capital=info['capital']
    while capital[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", capital)
        capital=m.group(1)
    pays=info['common_name']
    coordonnees=info['coordinates']
    return(capital,coordonnees)

with ZipFile('oceania.zip','r') as z:
    l=z.namelist()  
    
def print_capitalNauru(info):
    capital='Aucune officiellement, mais officieusement District de Yaren'
    while capital[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", capital)
        capital=m.group(1)
    pays=info['common_name']
    coordonnees=info['coordinates']
    return(capital,coordonnees)


def print_capitalPalau(info):
    capital=info['capital']
    while capital[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", capital)
        capital=m.group(1)
    pays='Palau'
    coordonnees=info['coordinates']
    return(capital,coordonnees)
    
def print_capitalGuyana(info):
    capital=info['capital'][2:11]
    pays=info['common_name']
    coordonnees=info['coordinates']
    return(capital,coordonnees)


def print_capitalBolivia(info):
    capital=info['capital']
    while capital[0]=="[":
        m = re.match("\[\[([\w ]+)\]\]", capital)
        capital=m.group(1)
    pays=info['common_name']
    coordonnees='unknown'
    return(capital,coordonnees)


def get_regime(info):
    regime=info['government_type']
    regime=regime.split('] [')
    regime[0]=regime[1:]
    regime[-1]=regime[-1][:-1]
    return(regime)
    
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