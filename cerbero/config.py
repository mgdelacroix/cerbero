import yaml
import os

class Config():
    data = {}
    keydir = None
    keys = []

    def add_keys(self):
        if not os.path.isdir(self.keydir):
            raise Exception("Directory \"{}\" doesn't exist.".format(self.keydir))

        for f in os.listdir(self.keydir):
            if f.endswith('.pub'):
                self.keys.append(f[:-4])


    def load(self, path, keydir):
        with open(path) as f:
            self.data = yaml.load(f)

        self.keydir = keydir
        self.add_keys()


config = Config()
