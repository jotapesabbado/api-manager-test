import os

user = os.environ.get('DB_USER', 'root')
password = os.environ.get('DB_PASS', '12345678(Jp')
database = os.environ.get('DB_DATABASE', 'ventura')
host = os.environ.get('DB_HOST', 'localhost')
port = os.environ.get('DB_PORT', 3306)

DATABASE_CONNECTION_URI = f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}?charset=UTF8MB4'

