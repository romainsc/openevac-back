import configparser


config = configparser.ConfigParser()

config.read('backend.conf')

db_user = config['openevac']['db_user']
db_name = config['openevac']['db_name']