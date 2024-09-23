from django.apps import AppConfig
import logging
import sys, os
logger = logging.getLogger('oc_lettings_site')

class OCLettingsSiteConfig(AppConfig):
    name = 'oc_lettings_site'
    
    def ready(self):
        super().ready()
        if os.environ.get('RUN_MAIN') == 'true':
            logger.info("L'application a démarré.")