import os
## Debug Mode (Default: False)
debug = False

## Secret Key (Replace with your own secret key0
secret_key = 'secret'
database_path = os.environ.get('DATABASE_URL', 'postgres://tim@localhost:5432/cs280-parkinglot')
