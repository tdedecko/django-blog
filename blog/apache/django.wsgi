import os
import sys
path = '/home/thom/workspace/blog'
if path not in sys.path:
    sys.path.append(path)

os.environ['DJANGO_SETTINGS_MODULE'] = 'blog.settings'

import django.core.handlers.wsgi
application = django.core.handlers.wsgi.WSGIHandler()