import os
import sys
from django.core.wsgi import get_wsgi_application

# Ensure the backend directory is in the Python path
sys.path.append(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')

application = get_wsgi_application()
