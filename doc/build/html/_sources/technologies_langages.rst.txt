Technologies et langages de programmation utilisés
==================================================


Langages et Frameworks
----------------------

- `Python 3.6 ou supérieur <https://www.python.org/>`_ : Langage principal utilisé pour le développement de l'application. Il est choisi pour sa simplicité et sa large gamme de bibliothèques.
- `Django 3.0 <https://www.djangoproject.com/>`_ : Framework web Python utilisé pour gérer le backend de l'application, y compris la gestion des utilisateurs, des profils et des locations immobilières.
- `SQLite <https://www.sqlite.org/index.html>`_ : Base de données relationnelle utilisée pour stocker les informations localement lors du développement. Elle est simple à configurer et bien adaptée aux petites applications.

Bibliothèques et outils supplémentaires
---------------------------------------

- `asgiref 3.8.1 <https://pypi.org/project/asgiref/>`_ : Outil pour gérer les serveurs d'applications web asynchrones, indispensable pour les applications Django modernes.
- `certifi 2024.8.30 <https://pypi.org/project/certifi/>`_ : Fournit des certificats racine pour la validation SSL.
- `charset-normalizer 3.3.2 <https://pypi.org/project/charset-normalizer/>`_ : Utilisé pour gérer l'encodage des fichiers.
- `colorama 0.4.6 <https://pypi.org/project/colorama/>`_ : Ajoute un support de coloration dans les terminaux Windows.
- `coverage 7.6.1 <https://pypi.org/project/coverage/>`_ : Utilisé pour mesurer la couverture des tests Python.
- `docutils 0.21.2 <https://pypi.org/project/docutils/>`_ : Utilisé pour transformer des documents reStructuredText en divers formats.
- `entrypoints 0.3 <https://pypi.org/project/entrypoints/>`_ : Permet de découvrir les points d’entrée pour les plugins dans les bibliothèques Python.
- `Flake8 3.7.0 <https://pypi.org/project/flake8/>`_ : Outil de linting Python, utilisé pour s’assurer que le code respecte les normes de style.
- `Gunicorn 23.0.0 <https://pypi.org/project/gunicorn/>`_ : Serveur WSGI pour exécuter les applications Django en production.
- `idna 3.10 <https://pypi.org/project/idna/>`_ : Implémentation de l'Internationalized Domain Names (IDNA).
- `Jinja2 3.1.4 <https://pypi.org/project/Jinja2/>`_ : Moteur de templates utilisé par Django pour générer des fichiers HTML dynamiques.
- `MarkupSafe 2.1.5 <https://pypi.org/project/MarkupSafe/>`_ : Aide à éviter les failles XSS en rendant le texte "sûr" pour l'inclusion dans les documents HTML.
- `mccabe 0.6.1 <https://pypi.org/project/mccabe/>`_ : Mesure la complexité du code Python.
- `Packaging 24.1 <https://pypi.org/project/packaging/>`_ : Gère les dépendances de package dans Python.
- `Pillow 10.4.0 <https://pypi.org/project/Pillow/>`_ : Bibliothèque pour le traitement d’images dans Python.
- `Pluggy 1.5.0 <https://pypi.org/project/pluggy/>`_ : Plugin utilisé par Pytest pour ajouter des fonctionnalités supplémentaires.
- `Pygments 2.18.0 <https://pypi.org/project/Pygments/>`_ : Bibliothèque de coloration syntaxique, utilisée pour la génération de documentation.
- `Pytest 8.3.3 <https://pypi.org/project/pytest/>`_ : Framework de test pour Python.
- `Pytest-Cov 5.0.0 <https://pypi.org/project/pytest-cov/>`_ : Extension pour Pytest permettant de mesurer la couverture de tests.
- `Pytest-Django 3.9.0 <https://pypi.org/project/pytest-django/>`_ : Plugin Pytest pour faciliter les tests dans Django.
- `pytz 2024.2 <https://pypi.org/project/pytz/>`_ : Gestion des fuseaux horaires dans les applications Python.
- `requests 2.32.3 <https://pypi.org/project/requests/>`_ : Bibliothèque HTTP pour Python, utilisée pour faire des requêtes HTTP simples.
- `sentry-sdk 2.14.0 <https://pypi.org/project/sentry-sdk/>`_ : Bibliothèque utilisée pour intégrer Sentry pour la gestion des erreurs dans l'application.
- `six 1.16.0 <https://pypi.org/project/six/>`_ : Bibliothèque d'utilitaires pour gérer la compatibilité entre Python 2 et Python 3.
- `SQLparse 0.5.1 <https://pypi.org/project/sqlparse/>`_ : Utilisé pour analyser et formater les requêtes SQL.
- `urllib3 2.2.3 <https://pypi.org/project/urllib3/>`_ : Gestionnaire de connexions HTTP, utilisé par `requests`.
- `whitenoise 6.7.0 <https://pypi.org/project/whitenoise/>`_ : Sert les fichiers statiques dans les environnements de production pour Django.

Outils de documentation
-----------------------

- `Sphinx 8.0.2 <https://www.sphinx-doc.org/>`_ : Utilisé pour générer la documentation du projet.
- `Alabaster 1.0.0 <https://pypi.org/project/alabaster/>`_ : Thème par défaut pour la documentation générée par Sphinx.
- `Babel 2.16.0 <https://pypi.org/project/Babel/>`_ : Utilisé pour la gestion des localisations dans le projet.
- `snowballstemmer 2.2.0 <https://pypi.org/project/snowballstemmer/>`_ : Algorithme de stemming utilisé par Sphinx pour analyser la documentation.
- `sphinxcontrib-applehelp 2.0.0 <https://pypi.org/project/sphinxcontrib-applehelp/>`_ : Extension pour Sphinx permettant de générer des fichiers d'aide pour les systèmes Apple.
- `sphinxcontrib-devhelp 2.0.0 <https://pypi.org/project/sphinxcontrib-devhelp/>`_ : Génère des fichiers d'aide pour le système GNOME.
- `sphinxcontrib-htmlhelp 2.1.0 <https://pypi.org/project/sphinxcontrib-htmlhelp/>`_ : Génère des fichiers d'aide HTML.
- `sphinxcontrib-jsmath 1.0.1 <https://pypi.org/project/sphinxcontrib-jsmath/>`_ : Permet l'intégration des mathématiques dans la documentation Sphinx.
- `sphinxcontrib-qthelp 2.0.0 <https://pypi.org/project/sphinxcontrib-qthelp/>`_ : Génère des fichiers d'aide pour Qt.
- `sphinxcontrib-serializinghtml 2.0.0 <https://pypi.org/project/sphinxcontrib-serializinghtml/>`_ : Génère des fichiers HTML statiques pour la documentation.

Serveur Web
-----------

- `Gunicorn <https://pypi.org/project/gunicorn/>`_ : Utilisé pour exécuter l'application en production, il est compatible avec Django pour le déploiement sur des serveurs comme Render.
