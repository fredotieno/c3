import json
import re
from parser import ContentParser

class Notebook():
    def __init__(self, path):
        with open(path) as json_file:
            self.notebook = json.load(json_file)
            self.name = self.notebook['cells'][0]['source'][0]
            self.description = self.notebook['cells'][1]['source'][0]

            cp = ContentParser()
            self.envs = cp.parse(path)['env_vars']

            self.requirements = self._get_requirements()

    def _get_requirements(self):
        for cell in self.notebook['cells']:
            cell_content = cell['source'][0]
            pattern = r"(![ ]*pip[ ]*install[ ]*)([A-Za-z=0-9.:]*)"

            print(re.findall(pattern,cell_content)) # TODO romeo multiple matches not working
            


