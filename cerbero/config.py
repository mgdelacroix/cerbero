import yaml
import os
from utils import merge_dicts


default_host = {
    "port": 22
}

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


    def get_hosts(self):
        def validate_host(name, data):
            return merge_dicts(default_host, data, {"name": name})

        return [validate_host(k, v) for k, v in self.data.items()]


config = Config()
