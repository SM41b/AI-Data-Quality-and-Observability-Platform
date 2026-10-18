import os
import psycopg
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def get_connection():
    '''Create and return connection to project database'''
    required_variables=[
        "DB_HOST",
        "DB_PORT",
        "DB_NAME",
        "DB_USER",
        "DB_PASSWORD",
    ]
    missing_variables=[name for name in required_variables if not os.getenv(name)]
    if missing_variables:
        raise RuntimeError(f'Missing database configuration : {missing_variables}')
    return psycopg.connect(
        host=os.environ['DB_HOST'],
        port = int(os.environ['DB_PORT']),
        dbname = os.environ['DB_NAME'],
        user = os.environ['DB_USER'],
        password = os.environ['DB_PASSWORD'],
        connect_timeout = 5,
    )