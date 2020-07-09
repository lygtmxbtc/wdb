from configparser import ConfigParser

class BaseConfig:
    conf = ConfigParser()
    conf_name = './main.conf.example'
    conf.read(conf_name)
    conf_sections = conf.sections()

    db_addr = conf.get('database', 'db_addr')
    db_port = conf.get('database', 'db_port')
    db_name = conf.get('database', 'db_database')
    db_username = conf.get('database', 'db_username')
    db_password = conf.get('database', 'db_password')

    server_addr = conf.get('server', 'server_addr')
    server_port = conf.get('server', 'server_port')
    remote_addr = conf.get('server', 'remote_addr')