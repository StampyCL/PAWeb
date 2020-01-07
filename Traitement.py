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
    
def get_nameArgentina(info):
    vn='Argentine Republic'
    return(vn)
    
def get_regime(info):
    regime=info['government_type']
    regime=regime.split('] [')
    regime[0]=regime[1:]
    regime[-1]=regime[-1][:-1]
    return(regime)