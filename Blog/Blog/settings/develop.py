#!/user/bin/env python
# 每天都要有好心情
from .base import *  # NOQA

DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, '../db.sqlite3'),
    }
}

INSTALLED_APPS += [
    # 'debug_toolbar',
    # 'template_flamegraph',
    # 'pympler',
    # 'debug_toolbar_line_profiler',
    'silk',
]

MIDDLEWARE += [
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
    'silk.middleware.SilkyMiddleware',
]

# DEBUG_TOOLBAR_PANELS = [
#     'template_flamegraph.TemplateFlamegraphPanel',
#     'pympler.panels.MemoryPanel',
#     'debug_toolbar_line_profiler.panel.ProfilingPanel',
# ]

DEBUG_TOOLBAR_CONFIG = {
    'JQUERY_URL': 'https://cdn.bootcss.com/jquery/3.5.0/jquery.min.js',
}

INTERNAL_IPS = ['127.0.0.1', ]
