Procédures de déploiement et gestion de l'application
=====================================================

Cette page détaille le processus de déploiement de l'application ainsi que la gestion du pipeline GitLab CI/CD. Vous trouverez un récapitulatif du fonctionnement du pipeline, les configurations nécessaires et les étapes à suivre pour effectuer le déploiement.



Récapitulatif du fonctionnement du déploiement
-----------

Le pipeline GitLab CI/CD est conçu pour gérer l'intégration continue, la qualité du code, les tests et enfin le déploiement de l'application. Chaque étape est orchestrée via le fichier `.gitlab-ci.yml`. Une fois le build Docker de l'application terminé, celle-ci est déployée automatiquement sur un service de déploiement continu, ici **Render**.

Le pipeline suit ces étapes :

1. **Install** : Installation des dépendances Python et création de l'environnement virtuel.
2. **Lint** : Vérification de la qualité du code avec Flake8.
3. **Test** : Exécution des tests unitaires et de la migration de la base de données.
4. **Quality** : Analyse de la qualité du code avec CodeClimate (Facultatif).
5. **Build** : Construction et push de l'image Docker de l'application.
6. **Deploy** : Déploiement automatique de l'image Docker sur l'environnement de production via Render.

Configuration requise
-----------


1. **Environnement** : 

    - **PostgreSQL 13** : La base de données utilisée par l'application. Une configuration minimale est définie dans le fichier `.gitlab-ci.yml`.
    - **Python 3.12** : Utilisé pour exécuter l'application et les tests.
    - **Django** : Cadre web Python utilisé, avec les paramètres de configuration définis dans `DJANGO_SETTINGS_MODULE`.
    - **Docker** : Utilisé pour la construction et le déploiement de l'application sous forme d'image Docker.
    - **Service de déploiement** : L'application est déployée sur **Render**, en utilisant une API REST pour déclencher le déploiement.

2. **Variables d'environnement** :

    - `POSTGRES_DB`, `POSTGRES_USER`, `POSTGRES_PASSWORD` : Informations pour configurer PostgreSQL.
    - `DATABASE_URL` : URL de connexion à la base de données PostgreSQL.
    - `CI_REGISTRY`, `CI_REGISTRY_USER`, `CI_REGISTRY_PASSWORD` : Utilisées pour l'authentification sur le registre Docker.

Étapes nécessaires pour effectuer le déploiement
-----------


Voici les étapes détaillées à suivre pour effectuer le déploiement sans difficulté :

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

    - Un rapport de qualité est généré avec **CodeClimate**. Ce rapport est accessible sous forme d'artifact dans GitLab, mais cette étape n'empêche pas le pipeline de continuer même si elle échoue.

6. **Construction Docker** :

    - Le job `build` construit une image Docker de l'application et la pousse dans le registre Docker. Vous devez vous assurer que **Docker** est bien installé et que les variables CI pour le registre sont correctement configurées.

7. **Déploiement** :

    - Le job `deploy` déclenche le déploiement via une requête `POST` à l'API de **Render**. L'application sera ainsi déployée dans l'environnement de production. L'URL pour déclencher ce déploiement est déjà incluse dans le fichier `.gitlab-ci.yml`.
