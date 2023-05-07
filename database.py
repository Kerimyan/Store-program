import json


class Database:

    def loader(self, filename):
        with open(filename) as f:
            dict_l = json.load(f)
        return dict_l

    def save(self,dict_s, filename):
        with open(filename, 'w') as f:
            json.dump(dict_s, f)
