#!/usr/bin/python3

import requests
from core.utils import get_config
import os
import zipfile
import io
import logging
from core.execution_engine import execute_workflow

plasma_config = get_config()
logger = logging.getLogger('Workflow Manager')


def describe_workflow(name):
    logger.debug('Executing describe workflow')
    if os.path.exists(plasma_config['workflows_path']+name):
        readme_file = plasma_config['workflows_path']+name+'/README'
        with open(readme_file, 'r') as readme:
            print(readme.read())
    else:
        print('\n> workflow description not found.\n')


def list_workflows():
    logger.debug('Executing list workflows')
    workflows_path = plasma_config['workflows_path']
    workflows = os.listdir(workflows_path)
    if workflows:
        print('\n> listing workflows ')
        for item in workflows:
            if os.path.isdir(workflows_path+item):
                print('\t- '+item)
        print()
    else:
        print('\n> no workflows have been created\n')


def run_workflow(name):
    logger.debug('Executing run workflow')
    execution_status = execute_workflow(name)
    logger.debug('Execution status : '+str(execution_status))
    return execution_status


def schedule_workflow(name):
    logger.debug('Executing schedule workflow')
    raise NotImplementedError
