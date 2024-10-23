from setuptools import setup, find_packages

setup(
    name='Oc_lettings_site_BARILLER',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'alabaster==0.7.16',
        'asgiref==3.8.1',
        'babel==2.16.0',
        'certifi==2024.8.30',
        'charset-normalizer==3.3.2',
        'colorama==0.4.6',
        'coverage==7.6.1',
        'Django==3.2',
        'django-extensions==3.2.3',
        'docutils==0.18.1',
        'entrypoints==0.3',
        'flake8==3.7.0',
        'gunicorn==23.0.0',
        'idna==3.10',
        'imagesize==1.4.1',
        'iniconfig==2.0.0',
        'Jinja2==3.1.4',
        'MarkupSafe==2.1.5',
        'mccabe==0.6.1',
        'packaging==24.1',
        'pillow==10.4.0',
        'pluggy==1.5.0',
        'pycodestyle==2.5.0',
        'pydotplus==2.0.2',
        'pyflakes==2.1.1',
        'Pygments==2.18.0',
        'pyparsing==3.2.0',
        'pytest==8.3.3',
        'pytest-cov==5.0.0',
        'pytest-django==3.9.0',
        'pytz==2024.2',
        'requests==2.32.3',
        'sentry-sdk==2.14.0',
        'setuptools==74.1.2',
        'six==1.16.0',
        'snowballstemmer==2.2.0',
        'Sphinx==6.2.1',
        'sphinx-autodoc-typehints==1.21.8',
        'sphinx-rtd-theme==1.2.2',
        'sphinxcontrib-applehelp==2.0.0',
        'sphinxcontrib-devhelp==2.0.0',
        'sphinxcontrib-htmlhelp==2.1.0',
        'sphinxcontrib-jquery==4.1',
        'sphinxcontrib-jsmath==1.0.1',
        'sphinxcontrib-qthelp==2.0.0',
        'sphinxcontrib-serializinghtml==2.0.0',
        'sqlparse==0.5.1',
        'tzdata==2024.2',
        'urllib3==2.2.3',
        'whitenoise==6.7.0'
    ],
)
