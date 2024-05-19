# SAE 203



## Présentation

Dans le cadre d'un project scolaire, j'ai crée :

- 5 machine vituel dans le même reseau 

    - 3 serveur qui génère des flux_rss 
    - 1 aggregateur 
        - Qui lis les flux_rss grace a leurs URL (http://serveur1/rss.xml)
        - Prend les information importante de ce flux
        - Affiche les informations dans un fichier html avec son css
    - 1 client
        - Pour pouvoir voir la page html générée
## Installation


Premièrement crée l'infrastructure :

 Récuperation des machines virtuelles(celles du prof) et installation de certain paquets :
    - SSH
    - APACHE
    - PIP (python3-pip)
 Changement des adresse IP et masque
 ```
 sudo nano /etc/netwok/interfaces
 ```
 Pour les 3 serveurs, suivre les étapes dans le site du prof (https://eric-wurbel.pedaweb.univ-amu.fr/extranet/Enseignement/SAE203/environnement-de-test.html) pour pouvoir générée les fluc_rss et les affichier (Apache).
 









ou récupérer le fichier comprésser 


## Paramétrage

Tout d'abord téléchargé les packet yaml et feedparser: 
```
apt-get install python3
apt install python3-pip
pip3 install PyYAML
pip3 install feedparser
```

Crée un fichier de config dans /etc :

```
sudo mkdir /etc/aggreg
sudo touch /etc/aggreg/aggreg.conf
```
Sinon mettre un fichier de config en argument:
```
./aggreg.py <file_config>
```

Dans le fichier config ecrire:
```
#sources: --> source des page rss  
#  - http://serveur1/rss.xml
#  - http://server2/rss.xml
#  - url
#  - ...

#rss-name: rss.xml --> nom du fichier 

#destination: /var/www/superviseur/index.html --> destinantion pour la création de la page web

#tri-chrono: true --> pour trier:True = evenement les plus récent et False = evenement les plus critique

#Exemple:
#sources:
#  - #url
#  - #url
#rss-name: #file_name
#destination: #path html
#tri-chrono: #True or False

```

Une fois un fichier de config compléter lancer la commande:
```
./aggreg.py 

ou si il n'y a pas de de fichier dans /etc/aggreg/aggreg.conf

./aggreg.py <file_config>
```

## Problèmes survenus ? 
    
Si un problème survient quand la commande est lancée, lire l’erreur et faire ce qu’il y a marqué dans l’erreur. 

Si ce n’est pas réglée, vérifier 1 par 1 les informations ci-dessous : 

- Fichier de config 

- Url des flux rss 

- Bonne installation des paquets 

- Bon droit sur les fichiers 

Si erreur persistante contacter moi --> ricardo.suprice@etu.univ-amu.fr je me ferais un plaisir de vous aider ! 

