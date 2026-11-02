import os

BASE_DIR = os.path.abspath(os.path.dirname(__file__))

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY', "chave-temporaria-desenvolvimento")  #chave utilizada para proteger sessões e formulários
    #
    SQLALCHEMY_DATABASE_URI = (
        "sqlite:///" + os.path.join(BASE_DIR, "instance", "stockflow.db") #informa onde ficará nosso banco SQLite.
        )

    SQLALCHEMY_TRACK_MODIFICATIONS = False #desativa um recurso de rastreamento que não precisamos.