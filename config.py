import os

# Render inyecta la URL de la base de datos aquí.
# Las versiones modernas de SQLAlchemy exigen que empiece con "postgresql://" en lugar de "postgres://".
DATABASE_URL = os.environ.get("DATABASE_URL")
if DATABASE_URL and DATABASE_URL.startswith("postgres://"):
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://", 1)

# Si la variable de entorno existe, usa la de Render. Si no, usa tu base de datos local.
POSTGRESQL = DATABASE_URL or "postgresql+psycopg2://postgres:@localhost:5432/blogposts_db"

class Config:
    # Cambia a False automáticamente en producción si no configuras FLASK_DEBUG como 1
    DEBUG = os.environ.get("FLASK_DEBUG") == "1" or False
    SECRET_KEY = os.environ.get("SECRET_KEY", "dev")
    SQLALCHEMY_DATABASE_URI = POSTGRESQL
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CKEDITOR_PKG_TYPE = "full"
    

