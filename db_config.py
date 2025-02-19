from dotenv import load_dotenv
import os

load_dotenv()

def get_db_config():
    return {
        'host': os.getenv('DB_HOST'),
        'database': os.getenv('DB_NAME'),
        'user': os.getenv('DB_USER'),
        'password': os.getenv('DB_PASSWORD')
    }