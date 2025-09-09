import os
from dotenv import load_dotenv

load_dotenv()

class Configurations:
    SQLALCHEMY_MODIFICATION= False
    SQLALCHEMY_DATABASE_URI= os.getenv("DATABASE")
    SECRET_KEY= os.getenv('SECRET_KEY')