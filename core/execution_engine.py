#!/usr/bin/python3

import logging
from core.utils import get_config
import yaml

logger = logging.getLogger("WXE")


def load_workflow_file(workflow_name):
    try:
        logger.info('loading workflow file')
        config = get_config()
        workflow_path = config['workflows_path'] + workflow_name
        with open(workflow_path) as workflow:
            yaml.load(workflow, Loader=yaml.FullLoader)
        return workflow
    except FileNotFoundError:
        logger.error('Unable to execute workflow : File Not Found')
        exit(1)
    except Error as e:
        logger.error('Unable to execute workflow :'+str(e))
        exit(1)


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


def run_workflow(workflow_name):
    workflow = load_workflow_file(workflow_name)
    workflow_valid = validate_workflow(workflow)
    if workflow_valid:
        requirements = generate_workflow_requirements(workflow)
        virtual_environment = setup_virtual_environment(requirements)
        execute_workflow(workflow, virtual_environment)
    else:
        logger.error('Invalid Workflow')
        exit(1)
