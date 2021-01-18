# OPC_Project02
Utilisez les bases de Python pour l'analyse de marché


## Description du produit
Un simple outils de scrapping du site Book.toscrape.com. \
Permet l'extraction des données et images de chaque produit.


## Table des matières :
* [Prérequis](#Prérequis)
* [Mise en place](#Mise-en-place)
* [Utilisation](#Utilisation)

## Prérequis
*  Python3 : https://www.python.org/downloads
*  Pip : https://pip.pypa.io/en/stable/installing/
*  venv : https://pypi.org/project/virtualenv/

## Mise en place 
### Acquisition du code
Acquisition du code grace à l'outil git ou directement sur la page.
### Methode Git
```
mkdir mon_dossier
cd mon_dossier
git clone https://github.com/Dhyakia/OPC_Project02.git
```
### Methode manuel
1. Rendez-vous sur [ce lien](https://github.com/Dhyakia/OPC_Project02)
2. Sélectionnez "Code" (bouton vert) puis "Download Zip"
3. Décompresser le fichier dans le dossier de votre choix

### Mise en place et activation de l'environnement virtuel

1. Naviguer à l'aide de l'invité de commande jusqu'à la destination d'installation.
2. Entrer la commande : ```virtualenv venv```
3. Votre environment virtuel maintenant créé, il vous faut l'activer : 

   Sous windows : ```cd venv/Scripts``` puis ```activate```
   
   Sous linux : ```cd venv/bin``` puis ```activate```
   
4. (venv) s'affiche maintenant à gauche de la ligne de l'invité de commande, signalant le succès de l'opération

### Récupération des modules
   1. Toujours dans l'invité de commande, entrez la commande ```pip install -U -r requirements.txt```
   2. Attendez que les modules s'installent/se mettent à jours
      
Félicitation, il ne reste plus qu'à lancer le programme !

## Utilisation
<b>ATTENTION</b> : Avant de lancer le programme, soyez sûr d'avoir activé l'environnement virtuel !

Une fois activé, entrez la commande ```python scrapper.py``` \
Attendez que le programme ais terminé avant d'interagir avec les éléments

## Future viewing
This is my first out of a dozen of project in Python, realised with OpenClassRoom, that will be released in the year 2021.