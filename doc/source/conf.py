import os
import sys
import django
# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

sys.path.insert(0, os.path.abspath('../..'))
os.environ['DJANGO_SETTINGS_MODULE'] = 'oc_lettings_site.settings'
django.setup()

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'oc lettings site'
copyright = '2024, BARILLER Eric / OC'
author = 'BARILLER Eric / OC'
release = '1.00'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = ['sphinx.ext.autodoc', 'sphinx.ext.napoleon', 'sphinx.ext.autosummary', 'sphinx_autodoc_typehints']

templates_path = ['_templates']
exclude_patterns = []

language = 'fr'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

html_theme = 'sphinx_rtd_theme'
html_static_path = ['_static']


autoclass_content = 'both'  
autodoc_member_order = 'bysource'  
autodoc_inherit_docstrings = True 