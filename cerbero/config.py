import yaml

class Config():
    data = {}

    def load_config(self, path):
        with open(path) as f:
            self.data = yaml.load(f)


config = Config()
