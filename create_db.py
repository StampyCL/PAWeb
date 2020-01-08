import sqlite3
from zipfile import ZipFile

# cursor.execute("""INSERT INTO pays ("France", "République Française", "Europe", "République", "Paris", 30, "Francais", "Euro", "Droite", "0033", "fr", 15, 25)""")
# conn.commit()
# conn.close()

#?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)

# data = {'Australia':{'vn':'Republic of Australia','Regime':'Republique parlementaire', 'capital':'Canberra', 'Population':14, 'Aire':20, 'PIB':180}}

'''
Initialisation de la liste de spays
'''

liste_pays = []
with ZipFile('oceania.zip','r') as z:
    for t in z.namelist():
        liste_pays.append(t.split('.')[0])

with ZipFile('south_america.zip','r') as z:
    for t in z.namelist():
        liste_pays.append(t.split('.')[0])

# print(liste_pays)

'''
Script pour la DB
'''
conn = sqlite3.connect('pays.db')
cursor = conn.cursor()
sql = 'INSERT INTO pays VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)'
for t in liste_pays:
    data_pays = data.get(t)
    print(data_pays)
    cursor.execute(sql, (t, data_pays['vn'], data_pays['Regime'], data_pays['capital'],
    data_pays['Population'],  data_pays['Aire'], data_pays['PIB'], data_pays['Monnaie'], data_pays['drive']))
    conn.commit()
