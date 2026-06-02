import os

# Render inyecta la URL de la base de datos en esta variable.
# Las versiones modernas de SQLAlchemy exigen que empiece con "postgresql://" en lugar de "postgres://".
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Si la variable 'DATABASE_URL' existe (en Render), la usa. Si no (en tu PC), usa localhost.
POSTGRESQL = DATABASE_URL or "postgresql+psycopg2://postgres:@localhost:5432/blogposts_db"

class Config:
    # Se apaga el modo debug automáticamente en producción por seguridad
    DEBUG = os.environ.get("FLASK_DEBUG") == "1" or False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_PKG_TYPE = "full"
    

