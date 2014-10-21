from .common import *

MEDIA_URL = "{{ taiga_back_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/media/"
STATIC_URL = "{{ taiga_back_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/static/"
ADMIN_MEDIA_PREFIX = "{{ taiga_back_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/static/admin/"
SITES["front"]["domain"] = "{{ taiga_hostname }}:{{ taiga_port }}"

DEBUG = True
TEMPLATE_DEBUG = True
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "{{ taiga_from_email_address }}"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

#EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_USE_TLS = False
#EMAIL_HOST = "localhost"
#EMAIL_HOST_USER = ""
#EMAIL_HOST_PASSWORD = ""
#EMAIL_PORT = 25

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
    "rest_framework.renderers.JSONRenderer",
)
