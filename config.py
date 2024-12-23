import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    DATABASE_URL = os.getenv('DATABASE_URL', 'postgresql://avnadmin:AVNS_qSY-E_GGG1SESLMzcOv@pg-39cec8a9-istu-7a4b.k.aivencloud.com:25134/defaultdb?sslmode=require')
    SQLALCHEMY_DATABASE_URI = DATABASE_URL
    SQLALCHEMY_TRACK_MODIFICATIONS = False

