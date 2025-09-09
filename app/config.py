import os
from dotenv import load_dotenv

# loading envronmental variables
load_dotenv()
class Config :
    SQLALCHEMY_DATABASE_URI= os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SECRET_KEY= os.getenv('SECRET_KEY')
