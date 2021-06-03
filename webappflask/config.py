from decouple import config


class Config:
    SECRET_KEY = config('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config('EMAIL_USER')
    MAIL_PASSWORD = config('EMAIL_PASS')


class Test_Config:
    SECRET_KEY = config('SECRET_KEY_TEST')
    SQLALCHEMY_DATABASE_URI = config('SQLALCHEMY_DATABASE_URI_TEST')
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = config('EMAIL_USER')
    MAIL_PASSWORD = config('EMAIL_PASS')
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BCRYPT_LOG_ROUNDS = 4
    TESTING = True
    WTF_CSRF_ENABLED = False
