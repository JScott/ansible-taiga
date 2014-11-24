# OLD BITS, DEPRECATE:

# from .common import *

# MEDIA_URL = "{{ taiga_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/media/"
# STATIC_URL = "{{ taiga_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/static/"
# ADMIN_MEDIA_PREFIX = "{{ taiga_url_scheme }}://{{ taiga_hostname }}:{{ taiga_port }}/static/admin/"
# SITES["front"]["domain"] = "{{ taiga_hostname }}:{{ taiga_port }}"

# DEBUG = True
# TEMPLATE_DEBUG = True
# PUBLIC_REGISTER_ENABLED = True

# REST_FRAMEWORK["DEFAULT_RENDERER_CLASSES"] = (
#     "rest_framework.renderers.JSONRenderer",
# )


# Copyright (C) 2014 Andrey Antukh <niwi@niwi.be>
# Copyright (C) 2014 Jesús Espino <jespinog@gmail.com>
# Copyright (C) 2014 David Barragán <bameda@dbarragan.com>
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as
# published by the Free Software Foundation, either version 3 of the
# License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.

from .development import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '{{ taiga_database_username }}',
        'USER': '{{ taiga_database_username }}',
        'PASSWORD': '{{ taiga_database_password }}',
        'HOST': '{{ taiga_database_host }}',
        'PORT': '{{ taiga_database_port }}',
    }
}

HOST="http://{{ taiga_hostname }}:{{ taiga_port }}"

#MEDIA_ROOT = '/home/taiga/media'
#STATIC_ROOT = '/home/taiga/static'

EMAIL_BACKEND = "django.core.mail.backends.smtp.EmailBackend"
EMAIL_USE_TLS = True
EMAIL_HOST = "{{ taiga_email_host }}"
EMAIL_HOST_USER = "{{ taiga_aws_access_key_id }}"
EMAIL_HOST_PASSWORD = "{{ taiga_aws_secret_access_key }}"
EMAIL_PORT = "{{ taiga_email_port }}"
DEFAULT_FROM_EMAIL = "{{ taiga_from_email_address }}"

# GITHUB SETTINGS
#GITHUB_URL = "https://github.com/"
#GITHUB_API_URL = "https://api.github.com/"
#GITHUB_API_CLIENT_ID = "yourgithubclientid"
#GITHUB_API_CLIENT_SECRET = "yourgithubclientsecret"
