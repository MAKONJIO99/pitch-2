import os

class Config:
    """
    """

    SECRET_KEY = '1999'
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1999@localhost/pitch'
    UPLOADED_PHOTOS_DEST = 'app/static/photos'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587 
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'francismakonjio2@gmail.com'
    MAIL_PASSWORD = 'makonjio1999'
    # SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")

class ProdConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL","")
    if SQLALCHEMY_DATABASE_URI.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URI =SQLALCHEMY_DATABASE_URI.replace("postgres://","postgresql://",1)
class DevConfig(Config):
    """
    """

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://moringa:1999@localhost/pitchup'
    DEBUG = True    

config_options = {
'development':DevConfig,
'production':ProdConfig
}    