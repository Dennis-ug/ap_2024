from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "django-insecure-)!v8dnm^=dg%2jzjbccq=4oz4qfxeqk08+n!cu3&uo+#p$um&1"

# SECURITY WARNING: define the correct hosts in production!
ALLOWED_HOSTS = ["*"]

CORS_ALLOWED_ORIGINS = [
    "https://alvinandpartners.com",
]

CSRF_ALLOWED_ORIGINS = ["https://mysite.com"]
CORS_ORIGINS_WHITELIST = ["https://mysite.com"]



EMAIL_BACKEND = "django.core.mail.backends.console.EmailBackend"


try:
    from .local import *
except ImportError:
    pass
