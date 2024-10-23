## Résumé

Site web d'Orange County Lettings

Lien GITLAB : https://gitlab.com/eric.bariller.49/oc_lettings_site

## Développement local

### Prérequis

- Compte GitHub avec accès en lecture à ce repository
- Git CLI
- SQLite3 CLI
- Interpréteur Python, version 3.6 ou supérieure

Dans le reste de la documentation sur le développement local, il est supposé que la commande `python` de votre OS shell exécute l'interpréteur Python ci-dessus (à moins qu'un environnement virtuel ne soit activé).

### macOS / Linux

#### Créer l'environnement virtuel

- `cd /path/to/Python-OC-Lettings-FR`
- `python -m venv venv`
- `apt-get install python3-venv` (Si l'étape précédente comporte des erreurs avec un paquet non trouvé sur Ubuntu)
- Activer l'environnement `source venv/bin/activate`
- Confirmer que la commande `python` exécute l'interpréteur Python dans l'environnement virtuel
`which python`
- Confirmer que la version de l'interpréteur Python est la version 3.6 ou supérieure `python --version`
- Confirmer que la commande `pip` exécute l'exécutable pip dans l'environnement virtuel, `which pip`
- Pour désactiver l'environnement, `deactivate`

#### Exécuter le site

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pip install --requirement requirements.txt`
- `python manage.py runserver`
- Aller sur `http://localhost:8000` dans un navigateur.
- Confirmer que le site fonctionne et qu'il est possible de naviguer (vous devriez voir plusieurs profils et locations).

#### Linting

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `flake8`

#### Tests unitaires

- `cd /path/to/Python-OC-Lettings-FR`
- `source venv/bin/activate`
- `pytest`

#### Base de données

- `cd /path/to/Python-OC-Lettings-FR`
- Ouvrir une session shell `sqlite3`
- Se connecter à la base de données `.open oc-lettings-site.sqlite3`
- Afficher les tables dans la base de données `.tables`
- Afficher les colonnes dans le tableau des profils, `pragma table_info(Python-OC-Lettings-FR_profile);`
- Lancer une requête sur la table des profils, `select user_id, favorite_city from
  Python-OC-Lettings-FR_profile where favorite_city like 'B%';`
- `.quit` pour quitter

#### Panel d'administration

- Aller sur `http://localhost:8000/admin`
- Connectez-vous avec l'utilisateur `admin`, mot de passe `Abc1234!`

### Windows

Utilisation de PowerShell, comme ci-dessus sauf :

- Pour activer l'environnement virtuel, `.\venv\Scripts\Activate.ps1` 
- Remplacer `which <my-command>` par `(Get-Command <my-command>).Path`


###  Sentry

Installer / mettre à jour Sentry :
`pip install --upgrade sentry-sdk`

**Obtenir votre DSN Sentry** : Après avoir créé un projet sur Sentry, vous pouvez trouver votre DSN dans les paramètres du projet sous la section **Client Keys (DSN)**.
  
  ![Obtenir le DSN](https://docs.sentry.io/assets/sentry-dsn.png)

Creer à la racine du programme un fichier sentry_key.py
Dans ce fichier y mettre `SENTRY_LINK ="votreliensentry"`

Remplacez "votreliensentry" par votre DSN réel fourni par Sentry lors de la création de votre projet.

Dans le fichier settings.py remplacer `SENTRY_LINK = ""` par `from sentry_key import SENTRY_LINK`


### Déploiment

#### Récapitulatif du fonctionnement du déploiement

Le pipeline GitLab CI/CD est conçu pour gérer l'intégration continue, la qualité du code, les tests et enfin le déploiement de l'application. Chaque étape est orchestrée via le fichier `.gitlab-ci.yml`. Une fois le build Docker de l'application terminé, celle-ci est déployée automatiquement sur un service de déploiement continu, ici [Render](https://render.com/).

Le pipeline suit ces étapes :

1. **Install** : Installation des dépendances Python et création de l'environnement virtuel.
2. **Lint** : Vérification de la qualité du code avec Flake8.
3. **Test** : Exécution des tests unitaires et de la migration de la base de données.
4. **Quality** : Analyse de la qualité du code avec CodeClimate (Facultatif).
5. **Build** : Construction et push de l'image Docker de l'application.
6. **Deploy** : Déploiement automatique de l'image Docker sur l'environnement de production via Render.

#### Configuration requise

1. **Environnement** : 
    - **PostgreSQL 13** : La base de données utilisée par l'application. Une configuration minimale est définie dans le fichier `.gitlab-ci.yml`. (Pour de la prod)
    - **Python 3.12** : Utilisé pour exécuter l'application et les tests.
    - **Django** : Cadre web Python utilisé, avec les paramètres de configuration définis dans `DJANGO_SETTINGS_MODULE`.
    - **Docker** : Utilisé pour la construction et le déploiement de l'application sous forme d'image Docker.
    - **Service de déploiement** : L'application est déployée sur **Render**, en utilisant une API REST pour déclencher le déploiement.

2. **Variables d'environnement** :
    - `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` : Informations pour configurer PostgreSQL. (Pour de la prod)
    - `DATABASE_URL` : URL de connexion à la base de données PostgreSQL.
    - `CI_REGISTRY`, `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD` : Utilisées pour l'authentification sur le registre Docker.

#### Étapes nécessaires pour effectuer le déploiement

Voici les étapes détaillées que votre successeur devra suivre pour effectuer le déploiement sans difficulté :

1. **Configurer GitLab CI/CD** :
    - Assurez-vous que GitLab CI/CD est correctement configuré et activé dans le projet.
    - Ajoutez les **variables CI** nécessaires dans la configuration GitLab :
        - `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD` : Credentials pour accéder au registre Docker.
        - `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD`, `DATABASE_URL` : Variables pour la base de données PostgreSQL.

2. **Pipeline CI/CD** :
    - Le pipeline est automatiquement déclenché lors des pushs sur la branche `main`. Assurez-vous de bien travailler sur cette branche pour que le déploiement fonctionne correctement.

3. **Installation des dépendances** :
    - Le job `install_dependencies` installe les dépendances Python dans un environnement virtuel. Cela inclut les bibliothèques nécessaires pour faire tourner Django ainsi que les tests.

4. **Linting et tests** :
    - Les jobs `lint` et `test` vérifient respectivement la qualité du code et l'intégrité de l'application via les tests unitaires. Ces étapes doivent réussir avant d'aller plus loin dans le pipeline.

5. **Analyse de la qualité** :
    - Un rapport de qualité est généré avec CodeClimate. Ce rapport est accessible sous forme d'artifact dans GitLab, mais cette étape n'empêche pas le pipeline de continuer même si elle échoue.

6. **Construction Docker** :
    - Le job `build` construit une image Docker de l'application et la pousse dans le registre Docker. Vous devez vous assurer que `docker` est bien installé et que les variables CI pour le registre sont correctement configurées.

7. **Déploiement** :
    - Le job `deploy` déclenche le déploiement via une requête `POST` à l'API de Render. L'application sera ainsi déployée dans l'environnement de production. L'URL pour déclencher ce déploiement est déjà incluse dans le fichier `.gitlab-ci.yml`.

