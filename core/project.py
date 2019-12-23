import json
import os
from pathlib import Path

project_config = {}


def generate_project_config(base_path):
    project_config = {}
    project_paths = {}
    project_config['paths'] = project_paths
    base_path = os.path.abspath(base_path)
    project_config['project_name'] = os.path.basename(base_path)
    project_paths['project_path'] = base_path
    project_paths['log_path'] = os.path.join(base_path,'logs/')
    project_paths['components_path'] = os.path.join(base_path,'components/')
    project_paths['workflows_path'] = os.path.join(base_path,'workflows/')
    project_paths['data_path'] = os.path.join(base_path,'data/')
    project_paths['models_path'] = os.path.join(base_path,'models/') 
    return project_config


def create_project(project_name):
    global project_config
    project_path = os.getcwd()+'/'+project_name+'/'
    if os.path.isdir(project_path):
        print('> directory already exists')
    else:
        project_config = generate_project_config(project_path)
        setup_project_directories(project_config)
        with open(project_path+'.plasma.json', 'w') as config_file:
            json.dump(project_config, config_file)
    return project_config


def load_project(project_path):
    global project_config
    absolute_path = os.path.abspath(project_path)
    project_name =  os.path.basename(absolute_path)
    project_config = generate_project_config(absolute_path)
    for directory_name, directory_path in project_config['paths'].items():
        try:
            if not os.path.exists(directory_path):
                print('> '+directory_name+' path does not exists')
                print('> creating '+directory_name+' directory at '+directory_path)
                os.mkdir(directory_path)
        except Exception as e:
            print('> Failed to validate project_paths '+str(e))
    config_path = os.path.join(project_config['paths']['project_path'],'.plasma.json')
    with open(config_path,'w') as config_file:
        json.dump(project_config,config_file)
    print('> loaded project '+str(project_name))


def get_project_info(project_path):
    pass


def setup_project_directories(project_config):
    for directory_name, directory_path in project_config['paths'].items():
        try:
            os.mkdir(directory_path)
        except FileExistsError:
            print('> '+directory_name+' path already exists')



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
    

def get_config(path='.'):
    try:
        config_file_path = find_config_file(path)
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

