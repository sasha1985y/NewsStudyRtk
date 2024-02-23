import os
import sys

try:
  sys.path.remove('/usr/lib/python3/dist-packages')
except:
  pass

sys.path.append('/home/c/cd80175/deploy53/public_html/NewsStudyRtk/')
sys.path.append('/home/c/cd80175/deploy53/public_html/venv/lib/python3.10/site-packages/')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsStudyRtk.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
