import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

app = Celery('project')
app.config_from_object('django.conf:settings', namespace = 'CELERY')

app.autodiscover_tasks()

from django.template.loader import render_to_string
from django.utils.html import strip_tags
html_message = strip_tags(render_to_string('mail_template.html', {'context': 'values'}))
