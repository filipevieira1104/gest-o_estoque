from pathlib import Path
import os

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-s0t1scsb6^s&t@&g2o!l6j(sf41bw#=#@g#p+bo!q@!t7e2uho'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'plataforma',
    'notebook',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'app.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'app.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

STATIC_URL = 'static/'
STATICFILES_DIRS = (os.path.join(BASE_DIR, 'templates/static'),)
STATIC_ROOT = os.path.join('static')
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MADIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

JAZZMIN_SETTINGS = {
    # Personalizar o título da aba do navegador (o que aparece na aba do browser)
    "site_title": "Painel de Controle",

    # Personalizar o cabeçalho (o nome que aparece no topo do painel de administração)
    "site_header": "Processo ADM/DEM",

    # Personalizar a marca do site (o nome que aparece na barra lateral e topo do site)
    "site_brand": "Processo ADM/DEM",

    # Opcional: mensagem de boas-vindas no dashboard
    "welcome_sign": "Bem-vindo ao Painel de Administração",

    # Opcional: texto do botão de logout
    "logout_message": "Até logo!",

    "login_logo": "img/Logomaior.jpg",
    
    "site_logo": "img/logo.jpg"
}

JAZZMIN_UI_TWEAKS = {
    "theme": "slate",  # Mudança de tema Bootstrap (pode ser darkly, flatly, etc.)
    "navbar": "navbar-dark navbar-primary",  # Classe do Navbar
    "sidebar": "sidebar-dark-primary",  # Classe da Sidebar
    "navbar_fixed": True,  # Navbar fixo
    "footer_fixed": False,  # Footer fixo
    "body_small_text": True,  # Fonte menor
    "brand_small_text": False,  # Tamanho da fonte da marca
    "sidebar_nav_small_text": False,  # Tamanho da fonte na navegação
    "sidebar_disable_expand": False,  # Expandir o menu lateral
    "sidebar_nav_child_indent": True,  # Indentar itens filhos no menu lateral
    "sidebar_nav_compact_style": False,  # Estilo compacto no menu lateral
    "sidebar_nav_flat_style": False,  # Estilo flat no menu lateral
    "theme_switcher": True,  # Mostrar switcher de tema no topo
    "actions_sticky_top": True,  # Deixar as ações fixas no topo dos forms
}