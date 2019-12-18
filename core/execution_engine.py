#!/usr/bin/python3

import logging

logger = logging.getLogger("WXE")

def load_workflow_file(file_path):
    logger.info('parsing workflow file')
    raise NotImplementedError

def validate_workflow(workflow):
    logger.info('validating workflow file')
    raise NotImplementedError

def verify_components():
    logger.info('verifying components')
    raise NotImplementedError

def generate_workflow_requirements():
    logger.info('generating workflow requirements')
    raise NotImplementedError

def setup_virtual_environment():
    logger.info('setting up virtual environment')
    raise NotImplementedError

def execute_workflow():
    logger.info('executing workflow')
    raise NotImplementedError

def run_workflow(file_path):
    workflow = load_workflow_file(file_path)
    workflow_valid = validate_workflow(workflow)
    if workflow_valid:
        requirements = generate_workflow_requirements(workflow)
        virtual_environment = setup_virtual_environment(requirements)
        execute_workflow(workflow,virtual_environment)
    else:
        logger.error('Invalid Workflow')
        exit(1)
