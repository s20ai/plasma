import json
import os
from pathlib import Path


def create_plasma_project(project_name):
    plasma_path = os.getcwd()+'/'+project_name+'/'
    if os.path.isdir(plasma_path):
        print('> directory already exists')
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
        plasma_config['project_name'] = project_name
        plasma_config['plasma_path'] = plasma_path
        plasma_config['log_path'] = log_path
        plasma_config['data_path'] = data_path
        plasma_config['components_path'] = components_path
        plasma_config['models_path'] = models_path
        plasma_config['workflows_path'] = workflows_path
        with open(plasma_path+'plasma_config.json', 'w') as config_file:
            json.dump(plasma_config, config_file)
    return plasma_config


def find_config_file(path):
    try:
        current_path = os.path.abspath(path)
        plasma_file = 'plasma_config.json'
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


def parse_workflow(workflow):
    try:
        workflow = workflow['workflow']
        components = list(workflow.keys())
        command_set = []
        for component in components:
            operations = list(workflow[component].keys())
            for operation in operations:
                command = {}
                command['component'] = component
                command['operation'] = operation
                command['parameters'] = workflow[component][operation]
                command_set.append(command)
        return command_set
    except Exception as e:
        return False
