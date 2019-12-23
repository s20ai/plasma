import json
import os
from pathlib import Path


project_config = {}


def create_project(project_name):
    global project_config
    project_path = os.getcwd()+'/'+project_name+'/'
    if os.path.isdir(plasma_path):
        print('> directory already exists')
    else:
        project_config['project_name'] = project_name
        project_config['project_path'] = project_path
        project_config['log_path'] = project_path + 'logs/'
        project_config['components_path'] = project_path + 'components/'
        project_config['workflows_path'] = project_path + 'workflows/'
        project_config['data_path'] = project_path + 'data/'
        project_config['models_path'] = project_path + 'models/'
        setup_project_directories(project_config)
        with open(project_path+'.plasma.json', 'w') as config_file:
            json.dump(plasma_config, config_file)
    return project_config


def load_project(project_path):
    global project_config
    absolute_path = os.path.abspath('project_path')
    project_name =  os.path.basename(absolute_path)
      

def get_project_info(project_path):
    pass


def setup_project_directories(project_config):
    os.mkdir(plasma_config['project_path'])
    os.mkdir(plasma_config['log_path'])
    os.mkdir(plasma_config['components_path'])
    os.mkdir(plasma_config['workflows_path'])
    os.mkdir(plasma_config['data_path']) 
    os.mkdir(plasma_config['models_path'])


def find_config_file(path):
    try:
        current_path = os.path.abspath(path)
        plasma_file = '.plasma.json'
        if plasma_file in os.listdir(current_path):
            plasma_file_path = current_path+'/'+plasma_file
            return plasma_file_path
        else:
            parent_dir = str(Path(current_path).parent)
            if parent_dir != current_path:
                return find_config_file(parent_dir)
            else:
                return False
    except Exception as e:
        return False
    

def get_config():
    try:
        config_file_path = find_config_file('.')
        if config_file_path:
            with open(config_file_path) as config_file:
                plasma_config = json.load(config_file)
            return plasma_config
        else:
            print("\n> not a plasma project directory\n")
            exit(1)
    except Exception as e:
        print("> failed to load plasma_config.json")
        exit(1)

