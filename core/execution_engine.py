#!/usr/bin/python3

import logging
from core.utils import get_config
import yaml
import os

logger = logging.getLogger("WXE")
plasma_config = get_config()


def load_workflow_file(workflow_name):
    try:
        logger.info('loading workflow file')
        config = get_config()
        workflow_path = config['workflows_path'] + workflow_name
        with open(workflow_path) as workflow_file:
            workflow = yaml.load(workflow_file, Loader=yaml.FullLoader)
        return workflow
    except FileNotFoundError:
        logger.error('unable to execute workflow : File Not Found')
        exit(1)
    except yaml.scanner.ScannerError as e:
        logger.error('unable to execute workflow : YAML Invalid')
        logger.error(e)
        exit(1)
    except Exception as e:
        logger.error('unable to execute workflow :'+str(e))
        exit(1)


def validate_workflow(workflow):
    logger.info('validating workflow file')
    workflow_keys = list(workflow.keys())
    required_keys = ["name", "description", "version", "workflow"]
    for key in required_keys:
        if key not in workflow_keys:
            logger.error('unable to execute workflow')
            logger.error('missing key : '+str(key))
            exit(1)
    verified = verify_components(workflow)
    return verified


def verify_components(workflow):
    logger.info('verifying components')
    components_path = plasma_config['components_path']
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
        logger.error('invalid Workflow')
        exit(1)
