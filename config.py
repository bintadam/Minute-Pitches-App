import os


class Config:
    ''' General configuration class '''
  
    SECRET_KEY = 'zakiya'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    UPLOADED_PHOTOS_DEST ='app/static/photos'

#  email configurations
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")


class Config:
    # simple mde  configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_USE_CDN = True


class ProdConfig(Config):
    '''
    Production configuration child class 
    Args: 
        Config : The parent configuration class with General configuration settings 
    '''

    SQLALCHEMY_DATABASE_URL = os.environ.get("DATABASE_URL")
    if SQLALCHEMY_DATABASE_URL and SQLALCHEMY_DATABASE_URL.startswith("postgres://"):
        SQLALCHEMY_DATABASE_URL = SQLALCHEMY_DATABASE_URL.replace ("postgres://", "postgresql://", 1)


class TestConfig(Config):
    '''
    Testing configuration child class 
    Args:
        Config : The parent configuration class with General configuration settings
    '''         


class DevConfig(Config):
    '''
    Delepment configuration child class 
    Args:
        Config : The parent configuration class with General configuration settings 
    '''    

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True


config_options = {
    'development': DevConfig,
    'production' : ProdConfig,
    'test' : TestConfig
}    