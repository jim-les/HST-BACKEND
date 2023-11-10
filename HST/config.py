import os
from dotenv import load_dotenv
import dj_database_url

load_dotenv()

def get_db_details():
    if os.environ.get('DATABASE_URL', None):
        return {
            'default': dj_database_url.parse(os.environ.get('DATABASE_URL'))
        }
    else:
        return {
            'default': {
                'ENGINE': 'django.db.backends.postgresql_psycopg2',
                'NAME': os.environ.get('DB_NAME', None),
                'USER': os.environ.get('DB_USER', None),
                'PASSWORD': os.environ.get('DB_PASSWORD', None),
                'HOST': os.environ.get('DB_HOST', None),
                'PORT': os.environ.get('DB_PORT', None),
            }
        }