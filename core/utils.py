import json
import os
from pathlib import Path
import importlib.util


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
        data_path = plasma_path + 'data/'
        models_path = plasma_path + 'models/'
        os.mkdir(plasma_path)
        os.mkdir(data_path)
        os.mkdir(log_path)
        os.mkdir(components_path)
        os.mkdir(workflows_path)
        os.mkdir(models_path)
        plasma_config['plasma_path'] = plasma_path
        plasma_config['log_path'] = log_path
        plasma_config['data_path'] = data_path
        plasma_config['components_path'] = components_path
        plasma_config['models_path'] = models_path
        plasma_config['workflows_path'] = workflows_path
        with open(plasma_path+'plasma_config.json', 'w') as config_file:
            json.dump(plasma_config, config_file)
    return plasma_config


def get_config():
    home = str(Path.home())
    config_file_path = home+'/.plasma/plasma_config.json'
    with open(config_file_path) as config_file:
        plasma_config = json.load(config_file)
    return plasma_config


def get_status():
    print('Plasma')
    print('Version : 0.1')


def configure_plasma():
    home = str(Path.home())
    config_file_path = home+'/.plasma/plasma_config.json'
    print('Edit the config file at '+config_file_path+' to change defaults.')

