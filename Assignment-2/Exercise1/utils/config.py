from json import load
from os.path import abspath, join, dirname

class Config:

    def __init__(self):
        self.config_file = load(open(join(abspath(dirname(__file__)), '../testing_config.json')))

    def get_batch_size(self):
        return self.config_file['batch_size']
    
    def get_datetime_format(self):
        return self.config_file['datetime_format']
    
    def get_random_seed(self):
        return self.config_file['random_seed']