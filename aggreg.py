#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import yaml
import sys #voir tp7 r107
import os
from pathlib import Path, PosixPath # pathlib permet de manipuler des chemins du système de fichiers de façon très pratique.
import xml.etree.ElementTree as ET
import feedparser
import requests
from requests.exceptions import HTTPError
from requests.exceptions import ConnectionError
from requests.exceptions import MissingSchema
import datetime  #https://docs.python.org/fr/3.6/library/datetime.html 
#https://rtavenar.github.io/poly_python/content/dates.html
#https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior


def charge_urls(liste_url):
    """
    A ecrire
    """
    news_feed = []
    for url in liste_url:
        try: # essaye une action 
            r = requests.get(url)
            r.raise_for_status()
        except HTTPError: #si cette action envoie une erreur (nom de l'erreur qui est dnas la doc, ici dans notre cas c'est  "HTTPError" )
            news_feed.append("None") #alors on fais sa 
        except ConnectionError:
            news_feed.append("None")
        except MissingSchema: #si l'URL ne commence pas par https://
            print("Error : URL pas bon -->",url)
            print("Doit commencer par https://")
        else:#sinon
            bozo = feedparser.parse(url)["bozo"] #voir si c'est un rss ou non
            if bozo == False: #donc c'est un rss
                news_feed.append(feedparser.parse(url))
           
    return news_feed
    

def fusion_flux(liste_url, liste_flux, tri_chrono):
    """
    Crée une liste finale de flux rss, avec des information spécifique de ce flux
    et si le dernier argument est:
        True trie les flux des evenement les plus récent
        False trie les flux par catégorie CRITICAL > MAJOR > MINOR (donc dans l'odre décroissant ici)
    """
    liste_temp = []
    for i in liste_flux:
        if i != "None" : #si dans la liste de fulx_rss y'a pas none, on traite la valeur                       
            #print(len(i['entries'])) #nombre de flux rss par liens donnée

            #Description générale du flux
            #diction_temp["titre_flux _general"] = i['feed']['title'] 

            #Description des éléments du flux
            #diction_temp["title"] = j["title"]
            
            for j in i["entries"]:
                diction_temp = {}
                #Ajoute dans un dictionaire des chose qu'on veut
                diction_temp["title"] = j["title"]
                diction_temp["categorie"] = j['category']  
                mot_lien = []
                mot_lien.append(i['feed']['link'])
                for k in range(len(mot_lien)):# pour avoir que le nom du serveur et pas http://serveur1.net/rss.xml
                    nom = mot_lien[k].split("/")
                    diction_temp["serveur"] = nom[2]
                diction_temp["date_publi"] = j['published'] 
                diction_temp["lien"] = j['link']
                diction_temp["description"] = j['summary']
                liste_temp.append(diction_temp)
            #    print(diction_temp)
            #    print()  
            liste_fin_fin = []         
            if tri_chrono == True:
                liste_fin_fin = sorted(liste_temp,key=lambda x: datetime.datetime.strptime(x["date_publi"], "%a, %d %b %Y %H:%M"))#trie la liste qu'on a crée des evenement grace a la date
                #ici la date et de la forme "Fri, 26 Apr 2024 01:22" donc --> "%a, %d %b %Y %H:%M"
                #datetime.datetime.strptime(x["date_publi"]--> lis une date de n'importe qu'elle forme ici la forme est -->Fri, 26 Apr 2024 11:52:14 GMT / donc ce lis "%a, %d %b %Y %H:%M:%S %Z" pour l'avoir dans un type date classique
                #https://rtavenar.github.io/poly_python/content/dates.html
                #https://docs.python.org/3.5/library/datetime.html#strftime-and-strptime-behavior
                #key=lammbda x:datetime.datetime.strptime(x["date_publi"], "%a, %d %b %Y %H:%M:%S %Z"), cela signifi que pour chaque element x de liste_fin il compare avec la valeur transformer de la date
            else:
                for t in range(3):
                    for j in liste_temp:
                        evenement = j["categorie"]#MAJOR,MINOR ou CRITICAL
                        if evenement == "MINOR" and t == 0: # ajoute a la liste final tout les evenement minor, quand le tour(t) vaut 0(premier tour)
                            liste_fin_fin.append(j)
                        if evenement == "MAJOR" and t == 1:# ajoute a la liste final tout les evenement major, quand le tour(t) vaut 1
                            liste_fin_fin.append(j)
                        if evenement == "CRITICAL" and t == 2:# ajoute a la liste final tout les evenement critical, quand le tour(t) vaut 2
                            liste_fin_fin.append(j)
                
            return liste_fin_fin  #place ici comme si si c'est y'a none sa prend pas en compte donc return none          


def genere_html(liste_evenements, chemin_html):
    """
    genere un fichier html avec son css, cette page a les infos des flux_rss
    """
    dossier_css = chemin_html + '/css/'
    chemin_css = chemin_html + '/css/feed.css'
    chemin_html = chemin_html + '/index.html'
    try: 
        os.makedirs(dossier_css)
    except FileExistsError:
        pass #si il y a une erreur sa le pass et rentre dans le else
    
    with open(chemin_css, "w")as css:#création fichier css
        css.write("""
*{
    margin: 0;
    padding: 0;
    box-sizing: border-box;
}
body>article>header>h1{
    color: white;
    background-color: #202020;
    padding: 50px;
    margin-bottom: 10px;
}
.flux_rss{
    width:90%;
    margin:auto;
    border-left:1px;
} 
.date_gene{
    margin-left:10px;
} 
p{
    padding:10px;
}                                
""")
    with open(chemin_html, "w")as html:#création fichier html
        date = datetime.datetime.now() #la date actuelle
        date = str(date.day) +'/'+ str(date.month) +'/'+ str(date.year) +' '+ str(date.hour)+':'+str(date.minute) #pour avoir l'écriture que je veux
        html.write("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Events log</title>
    <link rel="stylesheet" href="css/feed.css" type="text/css"/>
  </head>
  <body>
    <article>
      <header>
        <h1>Events log</h1>
      </header>
                   
      <i><p class="date_gene">""")
        html.write(str(date))
        for i in liste_evenements:#pour chaque dictio contenant information sur son flux rss
            html.write("""</p></i>
        <!-- liste des événements (items du flux RSS). Un bloc <article> par item dans le flux -->
        <article class="flux_rss">
            <header>
            <u><h2> """)
            html.write(str(i["title"]))
            html.write("""</h2></u>
            </header>
            <p>from: """) 
            html.write(i["serveur"])
            html.write("""</p>
            <p>date: """)
            html.write(i["date_publi"])
            html.write("""</p>
            <p>catégorie: """)
            html.write(i["categorie"])
            html.write("""</p>
            <p>giud: """)
            lien_split = i["lien"].split("/")#pour avoir le guid car il est dans le lien
            lien_split = lien_split[3].split(".") #pour enlever le .html a la fin
            html.write(lien_split[0])
            html.write('''</p>

            <p><a href="''')
            html.write(i["lien"])
            html.write('''">''')
            html.write(i["lien"])
            html.write("""</a></p>

            <p>""")
            html.write(i["description"])
            html.write("""</p>
        </article>
        </article>
    </body>
    </html>""")
    return   #return 2 fichier (avec 1rep si non existe) 1 fichier html et 1fichier css
        

def aggreg(chemin_fichier_conf):
    
    try:
        with open(chemin_fichier_conf,'r')as file_conf:#essaye le chemin classique du fichier config 
            conf = yaml.safe_load(file_conf)
            #print(conf)
            liste_lien = conf["sources"]
            print(liste_lien)

    except FileNotFoundError:#si il existe pas, regarde si il n'y a pas unu fichier mis en agrument
        try:
            with open(sys.argv[1])as file_conf: #ouvre le fichier de conf
                conf = yaml.safe_load(file_conf) #charge le fichier yaml
                #print(conf)
                liste_url = [] #lien avec les bon url pour aller a la page des flux rss
                liste_lien = conf["sources"]#liste du fichier yaml
                for i in liste_lien:
                    i = i +'/'+str(conf["rss-name"])#ajoute au lien pour ciblé la page rss
                    liste_url.append(i)
                file_RSS = charge_urls(liste_url) #voir fonction charge_url
                liste_evenements = fusion_flux(liste_url,file_RSS, conf["tri-chrono"])#voir fonction fusion_flux
                genere_html(liste_evenements,conf["destination"])
        except IndexError: #si y'en a pas
            print("Error: fichier config inexistant --> '/etc/aggreg/aggreg.conf' ")
            print("Error : Aucun fichier mis en argument pour remplacé fichier config")

    
    return


def main():

    aggreg('/etc/aggreg/aggreg.conf')#fichier de configuration de base
    

        
    
if __name__ == '__main__':
    main() 

