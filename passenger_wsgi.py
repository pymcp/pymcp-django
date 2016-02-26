import sys, os
# Force local install of postgresql
os.environ['LD_LIBRARY_PATH'] = '/home/pymcp/pgsql/9.5/lib'

INTERP = os.path.join(os.environ['HOME'], 'django_env', 'bin', 'python')
if sys.executable != INTERP:
    os.execl(INTERP, INTERP, *sys.argv)

cwd = os.getcwd()
sys.path.append(cwd)
sys.path.append(cwd + '/pymcp')  #You must add your project here

os.environ['DJANGO_SETTINGS_MODULE'] = "pymcp.settings"
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
