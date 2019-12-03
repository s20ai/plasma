import json, os
from pathlib import Path


def setup_plasma():
    home = str(Path.home())
    plasma_path = home+'/.plasma/'
    if os.path.isdir(plasma_path):
        with open(plasma_path+'plasma_config.json') as config_file:
            plasma_config = json.load(config_file)
    else:
        plasma_config = {}
        log_path = plasma_path + 'logs/'
        components_path = plasma_path + 'components/'
        workflows_path = plasma_path + 'workflows/'
        os.mkdir(plasma_path)
        os.mkdir(log_path)
        os.mkdir(components_path)
        os.mkdir(workflows_path)
        plasma_config['plasma_path'] = plasma_path
        plasma_config['log_path'] = log_path
        plasma_config['components_path'] = components_path
        plasma_config['workflows_path'] = workflows_path
        with open(plasma_path+'plasma_config.json','w') as config_file:
            json.dump(plasma_config,config_file)
    return plasma_config

