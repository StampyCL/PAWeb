# TD2-s4.py

import http.server
import socketserver
import sqlite3
import json

from urllib.parse import urlparse, parse_qs, unquote


#
# Définition du nouveau handler
#

class RequestHandler(http.server.SimpleHTTPRequestHandler):

  # sous-répertoire racine des documents statiques
  static_dir = '/client'

  #
  # On surcharge la méthode qui traite les requêtes GET
  #
  def do_GET(self):
    # on récupère les paramètres
    self.init_params()
    
    if self.path_info[0] == "location":
      self.send_locations()

    # requete description - retourne la description du lieu dont on passe l'id en paramètre dans l'URL
    elif self.path_info[0] == "description" and len(self.path_info) > 1:
      #self.send_country(self.path_info[1])
      '''
      #self.send_description(int(self.path_info[1]))
      data=[{'id':1,'desc':"Il ne faut pas être <b>trop grand</b> pour marcher dans cette rue qui passe sous une maison"},
            {'id':2,'desc':"Cette rue est <b>si étroite</b> qu'on touche les 2 côtés en tendant les bras !"},
            {'id':3,'desc':"Ce jardin <b>méconnu</b> évoque le palais idéal du Facteur Cheval"}]
      for c in data:
        if c['id'] == int(self.path_info[1]):
          self.send_json(c)
          break
      '''

    # le chemin d'accès commence par /time
    elif self.path.startswith('/time'):
      self.send_time()
   
    # le chemin d'accès commence par /countries
    elif self.path.startswith('/countries'):
      self.send_countries()

    # le chemin d'accès commence par /country et se poursuit par un nom de pays
    elif self.path_info[0] == 'country' and len(self.path_info) > 1:
      self.send_country(self.path_info[1])
      
    # ou pas...
    else:
      self.send_static()

  #
  # On surcharge la méthode qui traite les requêtes HEAD
  #
  def do_HEAD(self):
    self.send_static()

  # méthode pour traiter les requêtes POST - non utilisée dans l'exemple
  def do_POST(self):
    self.init_params()

    # requête générique
    if self.path_info[0] == "service":
      self.send_html(('<p>Path info : <code>{}</code></p><p>Chaîne de requête : <code>{}</code></p>' \
          + '<p>Corps :</p><pre>{}</pre>').format('/'.join(self.path_info),self.query_string,self.body));

    else:
      self.send_error(405)


  #
  # On envoie le document statique demandé
  #
  def send_static(self):

    # on modifie le chemin d'accès en insérant un répertoire préfixe
    self.path = self.static_dir + self.path

    # on appelle la méthode parent (do_GET ou do_HEAD)
    # à partir du verbe HTTP (GET ou HEAD)
    if (self.command=='HEAD'):
        http.server.SimpleHTTPRequestHandler.do_HEAD(self)
    else:
        http.server.SimpleHTTPRequestHandler.do_GET(self)
        

  #     
  # on analyse la requête pour initialiser nos paramètres
  #
  def init_params(self):
    # analyse de l'adresse
    info = urlparse(self.path)
    self.path_info = [unquote(v) for v in info.path.split('/')[1:]]  # info.path.split('/')[1:]
    self.query_string = info.query
    self.params = parse_qs(info.query)

    # récupération du corps
    length = self.headers.get('Content-Length')
    ctype = self.headers.get('Content-Type')
    if length:
      self.body = str(self.rfile.read(int(length)),'utf-8')
      if ctype == 'application/x-www-form-urlencoded' : 
        self.params = parse_qs(self.body)
    else:
      self.body = ''
   
    # traces
    print('path_info =',self.path_info)
    print('body =',length,ctype,self.body)
    print('params =', self.params)


  #
  # On envoie un document avec l'heure
  #
  def send_time(self):
    
    # on récupère l'heure
    time = self.date_time_string()

    # on génère un document au format html
    body = '<!doctype html>' + \
           '<meta charset="utf-8">' + \
           '<title>l\'heure</title>' + \
           '<div>Voici l\'heure du serveur :</div>' + \
           '<pre>{}</pre>'.format(time) 

    # pour prévenir qu'il s'agit d'une ressource au format html
    headers = [('Content-Type','text/html;charset=utf-8')]

    # on envoie
    self.send(body,headers)
  
  def send_locations(self):
    # création d'un curseur (conn est globale)
    c = conn.cursor()
    
    # récupération de la liste des pays dans la base
    c.execute("SELECT nom, vn, Regime, Capital, Population, Aire, PIB, Monnaie, Drive, Langue, Drapeau, Call, Web, Latitude, Longitude FROM pays")
    r = c.fetchall()

    # construction de la réponse
    data = []
    n = 0
    for a in r:
       n += 1
       data.append({'id':n, 'nom':a[0], 'vn':a[1], 'Regime':a[2], 'Capital':a[3], 'Population':a[4], 'Aire':a[5], 'PIB':a[6], 'Monnaie':a[7], 'Drive':a[8], 'Langue':a[9], 'Drapeau':a[10], 'Call':a[11], 'Web':a[12], 'Latitude':a[13], 'Longitude':a[14]})
    
    self.send_json(data)

  #
  # On renvoie la liste des pays
  #
  def send_countries(self):

    # création d'un curseur (conn est globale)
    c = conn.cursor()
    
    # récupération de la liste des pays dans la base
    c.execute("SELECT name FROM Countries")
    r = c.fetchall()

    # construction de la réponse
    txt = 'List of all {} countries :\n'.format(len(r))
    n = 0
    for a in r:
       n += 1
       txt = txt + '[{}] - {}\n'.format(n,a[0])
    
    # envoi de la réponse
    headers = [('Content-Type','text/plain;charset=utf-8')]
    self.send(txt,headers)

  #
  # On renvoie les informations d'un pays
  #
  def send_country(self,country):

    # préparation de la requête SQL
    c = conn.cursor()
    sql = 'SELECT * from countries WHERE wp=?'

    # récupération de l'information (ou pas)
    c.execute(sql,(country,))
    r = c.fetchone()

    # on n'a pas trouvé le pays demandé
    if r == None:
      self.send_error(404,'Country not found')

    # on génère un document au format html
    else:
      body = '<h2>{}</h2>'.format(country)
      body += '<link rel="stylesheet" href="/TD2-s8.css">'
      body += '<main>'
      body += '<h1>{}</h1>'.format(r['name'])
      body += '<ul>'
      body += '<li>{}: {}</li>'.format('Capital',r['capital'])
      body += '</ul>'
      body += '</main>'

      # on envoie la réponse
      headers = [('Content-Type','text/html;charset=utf-8')]
      self.send(body,headers)


  # on envoie un document html dynamique
  def send_html(self,content):
     headers = [('Content-Type','text/html;charset=utf-8')]
     html = '<!DOCTYPE html><title>{}</title><meta charset="utf-8">{}' \
         .format(self.path_info[0],content)
     self.send(html,headers)

  # on envoie un contenu encodé en json
  def send_json(self,data,headers=[]):
    body = bytes(json.dumps(data),'utf-8') # encodage en json et UTF-8
    self.send_response(200)
    self.send_header('Content-Type','application/json')
    self.send_header('Content-Length',int(len(body)))
    [self.send_header(*t) for t in headers]
    self.end_headers()
    self.wfile.write(body) 
    
  #
  # On envoie les entêtes et le corps fourni
  #
  def send(self,body,headers=[]):

    # on encode la chaine de caractères à envoyer
    encoded = bytes(body, 'UTF-8')

    # on envoie la ligne de statut
    self.send_response(200)

    # on envoie les lignes d'entête et la ligne vide
    [self.send_header(*t) for t in headers]
    self.send_header('Content-Length',int(len(encoded)))
    self.end_headers()

    # on envoie le corps de la réponse
    self.wfile.write(encoded)


#
# Ouverture d'une connexion avec la base de données
#
conn = sqlite3.connect('pays.db')

# Pour accéder au résultat des requêtes sous forme d'un dictionnaire
conn.row_factory = sqlite3.Row

#
# Instanciation et lancement du serveur
#
httpd = socketserver.TCPServer(("", 8080), RequestHandler)
httpd.serve_forever()

