from dotenv import load_dotenv
import os

BASEDIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

load_dotenv(os.path.join(BASEDIR, '.env'))

class DatabaseConfig:
    DB_HOST : str = os.environ.get("DB_HOST")
    DB_PORT : int = os.environ.get("DB_PORT")
    DB_NAME : str = os.environ.get("DB_NAME")
    DB_USER : str = os.environ.get("DB_USER")
    DB_PASS : str = os.environ.get('DB_PASS')
    DB_URL : str = f"postgresql+asyncpg://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

class Config(DatabaseConfig):
    pass

settings = Config()

# print(settings.DB_NAME)
