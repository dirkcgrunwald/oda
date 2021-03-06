from .base import *

DEBUG = True
COMPRESS_ENABLED = False

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':   'odatest'
    }
}

ALLOWED_HOSTS = [
    'localhost'
]

# Hard-code secret key for development (DO NOT make the same key as production)
SECRET_KEY = "%@z)i7!o9k7g(k2is&4dbayp6+!@4iwt+8!=(#3q5w@wwcypm&"

# Use the local file system instead of GoogleStorage
DEFAULT_FILE_STORAGE = 'django.core.files.storage.FileSystemStorage'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'