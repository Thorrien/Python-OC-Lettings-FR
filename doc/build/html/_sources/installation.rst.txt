Installation du projet
======================

Pour installer le projet localement, suivez les instructions ci-dessous :

Prérequis
---------

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Installation sur macOS / Linux
------------------------------

1. Clonez le repository :
   ::
      git clone https://gitlab.com/eric.bariller.49/oc_lettings_site.git
      cd /path/to/Python-OC-Lettings-FR

2. Créez un environnement virtuel :
   ::
      python -m venv venv

3. Activez l'environnement virtuel :
   ::
      source venv/bin/activate

4. Vérifiez que l'interpréteur Python utilisé est la bonne version :
   ::
      python --version

5. Installez les dépendances :
   ::
      pip install --requirement requirements.txt

6. Exécutez le serveur :
   ::
      python manage.py runserver

7. Ouvrez votre navigateur et accédez à l'URL :
   ::
      http://localhost:8000

Installation sur Windows
------------------------

Les étapes sont similaires à macOS/Linux, avec quelques différences :

1. Clonez le repository et créez l'environnement virtuel, comme sur macOS/Linux.
   
2. Activez l'environnement virtuel en utilisant PowerShell :
   ::
      venv/Scripts/activate

3. Vérifiez la version de Python et installez les dépendances comme décrit ci-dessus.
