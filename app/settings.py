import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
DB_PATH = Path(os.getenv("APP_DB_PATH", str(BASE_DIR / "data" / "service.sqlite3")))
DB_PATH.parent.mkdir(parents=True, exist_ok=True)
SECRET_KEY = os.getenv("APP_SECRET_KEY", "local-development-key")
DEBUG = False
ROOT_URLCONF = "app.urls"
ALLOWED_HOSTS = ["*"]
INSTALLED_APPS = ["django.contrib.contenttypes", "rest_framework"]
MIDDLEWARE = []
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": DB_PATH,
    }
}
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
REST_FRAMEWORK = {"UNAUTHENTICATED_USER": None}
