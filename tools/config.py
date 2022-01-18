import configparser

class Config:

    def __init__(self, ready: bool=True, file: str='tools/config.ini'):
        self.config = configparser.ConfigParser()
        self.file = file
        if ready: self.load()


    def save(self, token: str, channels: list):
        self.config['client'] = {}
        self.config['client']['token'] = token
        self.config['client']['channels'] = str(channels).strip('[]')
        
        with open(self.file, 'w') as f:
            self.config.write(f)


    def load(self):
        self.config.read(self.file)
        self.token = self.config['client']['token']
        self.channels = [ word.strip() for word in self.config.get('client', 'channels').split(',') ]