from Shop.settings import *
from .skey import key

SECRET_KEY = key

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["www.benybeny.com","benybeny.com"]

CSRF_TRUSTED_ORIGINS = ['http://benybney.com']

DATABASES = {
	'default': {
		'ENGINE': 'django.db.backends.mysql',
		'NAME': 'benybeny_online_shop',
		'USER': 'benybeny_Benfoxy',
		'PASSWORD': 'nZ&v3KyRR~^_',
		'HOST':'localhost',
		'PORT':'3306',
	}
}


STATIC_URL = '/statics/'
MEDIA_URL = '/media/'
STATIC_ROOT = '/home/benybeny/public_html/statics'
MEDIA_ROOT = '/home/benybeny/public_html/media/product_pic'
STATICFILES_DIRS = [
    BASE_DIR / "statics",
]

SESSION_COOKIE_SECURE = True