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

Pour les 3 machines virtuelles qui serviront de serveurs, suivre les étapes dans le site du prof (https://eric-wurbel.pedaweb.univ-amu.fr/extranet/Enseignement/SAE203/environnement-de-test.html) pour pouvoir générée les fluc_rss et les affichier(Apache).

De même, pour la machine virtuelle qui servira d'aggregateur suivre les étapes du prof sur son site et ensuite ajouter notre programme aggreg.py dans le répertoire courant du bon utilisateur(voir site prof) et **suivre guide du programme aggreg.py IMPORTANT**.


## Utilisation

- Lancer toutes les machines.
- Puis avec le client accéder à la page web de l'aggregateur via un navigateur web et l'adresse ip de la machine aggregateur.


## Problèmes survenus ? 
    
Si un problème survient vérifier :

- Ip des machines

- Service Apache actif sur les serveur et l'aggregateur 

- Voir guide du programme aggreg.py 

- Bonne config des serveurs(revoir site du prof)

Si erreur persistante contacter moi --> ricardo.suprice@etu.univ-amu.fr je me ferais un plaisir de vous aider ! 

