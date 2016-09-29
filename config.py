# Abilitazione/Disattivazione del development environment
DEBUG = True

# Definizione della directory dell'applicazione
import os
BASE_DIR = os.path.abspath(os.path.dirname(__file__))

# Definizione del db

# Application threads. Uso due thread per processore disponibile
# uno per gestire le request in ingresso e uno per i processi
# in background.
THREADS_PER_PAGE = 2

# Abilito protezione contro i *Cross-site Request Forgery (CSRF)*
CSRF_ENABLED = True

# Secret key for signing the data.
CSRF_SESSION_KEY = "secret"

# Secret key for signing cookies
SECRET_KEY = "secret"
