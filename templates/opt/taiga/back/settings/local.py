from .common import *

MEDIA_URL = "{{ taiga_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/media/"
STATIC_URL = "{{ taiga_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/static/"
ADMIN_MEDIA_PREFIX = "{{ taiga_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/static/admin/"
SITES["front"]["domain"] = "{{ taiga_hostname }}:{{ taiga_port }}"

DEBUG = True
TEMPLATE_DEBUG = True
PUBLIC_REGISTER_ENABLED = True

DEFAULT_FROM_EMAIL = "{{ taiga_from_email_address }}"
SERVER_EMAIL = DEFAULT_FROM_EMAIL

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "{{ taiga_email_host }}"
EMAIL_HOST_USER = "{{ taiga_aws_access_key_id }}"
EMAIL_HOST_PASSWORD = "{{ taiga_aws_secret_access_key }}"
EMAIL_PORT = "{{ taiga_email_port }}"

REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
    "rest_framework.renderers.JSONRenderer",
)
