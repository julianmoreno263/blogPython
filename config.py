import os

# Render te dará una URL de base de datos que empieza con "postgres://", 
# pero SQLAlchemy moderno requiere que empiece con "postgresql://". Esto lo soluciona:
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Si no está en Render, usa tu BD local
POSTGRESQL = DATABASE_URL or "postgresql+psycopg2://postgres:@localhost:5432/blogposts_db"

class Config:
    # En Render DEBE ser False por seguridad y rendimiento
    DEBUG = os.environ.get("FLASK_DEBUG") == "1" or False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev") # Usa una clave segura en producción
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_PKG_TYPE = "full"
    

