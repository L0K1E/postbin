import os


class Config:
    SECRET_KEY = 'dc54809d588d486a9626ef6d'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///site.db'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = 'logeshkeyboader@gmail.com'
    MAIL_PASSWORD = 'logesh18032002'
    WHOOSHEE_MIN_STRING_LEN = '3'
    WHOOSHEE_DIR = 'whoose'
