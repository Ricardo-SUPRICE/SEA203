# SAE 203



## Présentation

Dans le cadre d'un project scolaire, j'ai crée ce programme qui a partir d'un fichier de configuration:

-Lis un flux rss grace a son url 

-Prend les information importante de ce flux

-Affiche les informations importante dans un fichier html avec son css 

## Installation

Récuperé les programme via gitlab:

```
apt insall git
git clone https://etulab.univ-amu.fr/s23001073/sae-203.git
ls sae-203
```

## Paramétrage

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


sources:
  - #url
  - #url
rss-name: #file_name
destination: #path html
tri-chrono: #True or False

```

Une fois un fichier de config compléter lancer la commande:
```
./aggreg.py 

ou si il n'y a pas de de fichier dans /etc/aggreg/aggreg.conf

./aggreg.py <file_config>
```

## FAQ

reponse question a faire resolation de probleme

