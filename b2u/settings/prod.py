
import os
from .common import *
from dotenv import load_dotenv
load_dotenv()
# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-&e)tsj51voech(@=jh-@_p@&9r$@v+q63#n7ct9!9s3p7zc(cg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.getenv('DB_NAME', 'b2u'),
        'HOST': os.getenv('DB_HOST', 'localhost'),
        'PORT': os.getenv('DB_PORT', '5432'),
        'USER': os.getenv('DB_USER', 'postgres'),
        'PASSWORD': os.getenv('DB_PASSWORD')
    }
}
CORS_ALLOWED_ORIGINS = [
   'https://*',
    'http://*'
]