# OPC_Project02
Utilisez les bases de Python pour l'analyse de march�


## Description du produit
Un simple outils de scrapping du site Book.toscrape.com. \
Permet l'extraction des donn�es et images de chaque produit.


## Table des mati�res :
* [Pr�requis](#Pr�requis)
* [Mise en place](#Mise-en-place)
* [Utilisation](#Utilisation)

## Pr�requis
*  Python3 : https://www.python.org/downloads
*  Pip : https://pip.pypa.io/en/stable/installing/
*  venv : https://pypi.org/project/virtualenv/

## Mise en place 
### Acquisition du code
Acquisition du code grace � l'outil git ou directement sur la page.
### Methode Git
```
mkdir mon_dossier
cd mon_dossier
git clone https://github.com/Dhyakia/OPC_Project02.git
```
### Methode manuel
1. Rendez-vous sur [ce lien](https://github.com/Dhyakia/OPC_Project02)
2. S�lectionnez "Code" (bouton vert) puis "Download Zip"
3. D�compresser le fichier dans le dossier de votre choix

### Mise en place et activation de l'environnement virtuel

1. Naviguer � l'aide de l'invit� de commande jusqu'� la destination d'installation.
2. Entrer la commande : ```virtualenv venv```
3. Votre environment virtuel maintenant cr��, il vous faut l'activer : 

   Sous windows : ```cd venv/Scripts``` puis ```activate```
   
   Sous linux : ```cd venv/bin``` puis ```activate```
   
4. (venv) s'affiche maintenant � gauche de la ligne de l'invit� de commande, signalant le succ�s de l'op�ration

### R�cup�ration des modules
   1. Toujours dans l'invit� de commande, entrez la commande ```pip install -U -r requirements.txt```
   2. Attendez que les modules s'installent/se mettent � jours
      
F�licitation, il ne reste plus qu'� lancer le programme !

## Utilisation
<b>ATTENTION</b> : Avant de lancer le programme, soyez s�r d'avoir activ� l'environnement virtuel !

Une fois activ�, entrez la commande ```python scrapper.py``` \
Attendez que le programme ais termin� avant d'interagir avec les �l�ments

## Future viewing
This is my first out of a dozen of project in Python, realised with OpenClassRoom, that will be released in the year 2021.