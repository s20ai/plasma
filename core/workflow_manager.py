#!/usr/bin/python3

import requests
from core.project import get_config
import os
import zipfile
import io
import logging
import core.execution_engine as execution_engine

logger = logging.getLogger('Workflow Manager')


def describe_workflow(name):
    plasma_config = get_config()
    logger.debug('Executing describe workflow')
    if os.path.exists(plasma_config['paths']['workflows_path']+name):
        readme_file = plasma_config['paths']['workflows_path']+name+'/README'
        with open(readme_file, 'r') as readme:
            print(readme.read())
    else:
        print('\n> workflow description not found.\n')


def list_workflows():
    plasma_config = get_config()
    logger.debug('Executing list workflows')
    workflows_path = plasma_config['paths']['workflows_path']
    workflows = os.listdir(workflows_path)
    if workflows:
        print('\n> listing workflows ')
        for item in workflows:
            if item.endswith('.yml'):
                print('\t- '+item)
        print()
    else:
        print('\n> no workflows have been created\n')


def run_workflow(name):
    logger.debug('Executing run workflow')
    execution_status = execution_engine.run_workflow(name)
    logger.debug('Execution status : '+str(execution_status))
    return execution_status


def schedule_workflow(name):
    logger.debug('Executing schedule workflow')
    raise NotImplementedError
