#!/usr/bin/python3

import logging
from core.project import get_config
from core.component_manager import component_loader
from core.workflow import Workflow
import yaml
import os
import venv
import sys
import subprocess

logger = logging.getLogger("WXE")


def verify_components(workflow):
    plasma_config = get_config()
    logger.info('verifying components')
    components_path = plasma_config['paths']['components_path']
    local_components = os.listdir(components_path)
    workflow_components = list(workflow['workflow'].keys())
    for component in workflow_components:
        if component not in local_components:
            logger.error('unable to execute workflow')
            logger.error('component not found : '+component)
            verified = False
            break
        else:
            verified = True
    return verified


def generate_workflow_requirements(workflow):
    plasma_config = get_config()
    workflow_name = workflow.name
    logger.info('generating workflow requirements')
    try:
        components = list(workflow.workflow['workflow'].keys())
        requirements_list = []
        for component in components:
            requirements_path = plasma_config['paths']['components_path'] + \
                component+'/requirements.txt'
            with open(requirements_path, 'r') as requirements_file:
                requirements = requirements_file.read().split('\n')
                requirements = [x for x in requirements if x != '']
                requirements_list += requirements
        workflow_requirements_path = plasma_config['paths']['data_path'] + \
            workflow_name+'.requirements'
        with open(workflow_requirements_path, 'w') as file:
            requirements_string = '\n'.join(requirements_list)
            file.write(requirements_string)
        return workflow_requirements_path
    except Exception as e:
        logger.error('failed to generate requirementes file')
        logger.error(e)
        exit(1)


def setup_virtual_environment(requirements_path, workflow_name):
    plasma_config = get_config()
    try:
        logger.info('setting up virtual environment')
        venv_path = plasma_config['paths']['data_path']+workflow_name+'_venv'
        venv.create(venv_path)
        logger.info('activating virtual environment')
        output = os.system('bash '+venv_path+'/bin/activate')
        logger.info('installing dependencies')
        output = subprocess.check_output(
            ['pip3', 'install', '-r', requirements_path])
        return True
    except Exception as e:
        logger.error("unable to setup virtual environment")
        exit(1)


def update_output_variables(step,output_dict):
    output_keys = list(output_dict.keys())
    update_list = []
    updated_parameters = {}
    for key,value in step['parameters'].items():
        if value in output_keys:
            updated_parameters[key] = output_dict[value]
        else:
            updated_parameters[key] = value
    step['parameters'] = updated_parameters
    return step



def execute_step(step):
    plasma_config = get_config()
    try:
        logger.info('executing step :'+step['component'])
        component_name = step['component']
        component_path = plasma_config['paths']['components_path'] + \
            component_name+'/component.py'
        component = component_loader(component_name, component_path)
        logging.getLogger(component_name).setLevel(logging.WARNING)
        output = component.main(step)
        return output
    except Exception as e:
        logger.error('failed to execute step : %s > %s' %
                     (step['component'], step['operation']))
        logger.error(e)


def execute_workflow(workflow_steps):
    logger.info('executing workflow')
    try:
        output_dict = {}
        for step in workflow_steps:
            step = update_output_variables(step,output_dict)
            output = execute_step(step)
            if type(output) is dict:
                output_dict.update(output)
        return True
    except Exception as e:
        logger.error('exception : '+str(e))
        exit(1)


def run_workflow(workflow_name):
    config = get_config()
    workflow_path = config['paths']['workflows_path'] + workflow_name
    workflow = Workflow(workflow_path)
    workflow_valid = workflow.validate()
    if workflow_valid:
        requirements = generate_workflow_requirements(workflow)
        virtual_environment = setup_virtual_environment(requirements, workflow_name)
        state = execute_workflow(workflow.steps)
        if state is True:
            logger.info('Workflow Executed')
        else:
            logger.info('Failed to execute workflow')
        print('\n')
    else:
        logger.error('invalid workflow')
        exit(1)
