Gestion du pipeline CI/CD
=====================================================

Le fichier `.gitlab-ci.yml` définit les étapes et les jobs à exécuter dans le pipeline CI/CD. Voici un récapitulatif des principales étapes et leur fonctionnement :

Stages
-----------

Les différents stages du pipeline sont :

- **install** : Installation des dépendances.
- **lint** : Vérification de la qualité du code.
- **test** : Exécution des tests unitaires.
- **quality** : Analyse de la qualité du code.
- **build** : Construction de l'image Docker.
- **deploy** : Déploiement de l'image Docker en production.


Utilisation de Docker
-----------

La configuration utilise **Docker** pour créer des environnements isolés pour le build et le déploiement. Assurez-vous que Docker est installé et que les variables CI pour le registre Docker sont correctement configurées.
