"""
WSGI config for djangoone project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/howto/deployment/wsgi/
"""

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "djangorest.settings")

from django.core.wsgi import get_wsgi_application
##heroku import
from dj_static import Cling

##local conf
#application = get_wsgi_application()
##heroku conf
application = Cling(get_wsgi_application())