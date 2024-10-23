Guide de démarrage rapide
=========================

Ce guide explique comment démarrer rapidement le projet en local.

1. Clonez le projet :
   ::
      git clone https://gitlab.com/eric.bariller.49/oc_lettings_site.git
      cd /path/to/Python-OC-Lettings-FR

2. Créez un environnement virtuel Python :
   ::
      python -m venv venv

3. Activez l'environnement virtuel :
   - Sur macOS/Linux :
     ::
        source venv/bin/activate
   - Sur Windows :
     ::
        venv/Scripts/activate

4. Installez les dépendances nécessaires :
   ::
      pip install --requirement requirements.txt

5. Exécutez la commande pour lancer le serveur Django :
   ::
      python manage.py runserver

6. Accédez à l'application sur votre navigateur à l'adresse :
   ::
      http://localhost:8000

Vous devriez voir la page d'accueil avec les listings de profils et de locations.