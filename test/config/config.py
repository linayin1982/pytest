import os.path
from configparser import ConfigParser


class Config:
    def __init__(self):
        self.config_ini = os.getcwd() + '\..\config\config.ini'
        self.parser = ConfigParser()

    def config(self,section,name):
        print(self.config_ini)
        self.parser.read(self.config_ini, encoding='utf-8')
        return self.parser.get(section,name)

def test_config():
    config_ = Config()
    print(config_.config('default', 'token_api'))





