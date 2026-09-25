"""
WSGI config for the config project.

It exposes the WSGI callable as a module-level variable named ``application``.
This is also the file you point PythonAnywhere's "WSGI configuration file" to
when deploying.
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings')

application = get_wsgi_application()
