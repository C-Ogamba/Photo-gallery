"""
ASGI config for photoshare project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/asgi/
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/..' )
sys.path.append(os.path.dirname(os.path.abspath(__file__)) + '/../photoshare')


from django.core.asgi import get_asgi_application

os.environ['DJANGO_SETTINGS_MODULE'] = 'photoshare.settings'
# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'photo-gallery.settings')

application = get_asgi_application()
