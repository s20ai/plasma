#!/usr/bin/python3

import logging
import yaml

class Workflow:
    def __init__(self,workflow_path):
        self.logger = logging.getLogger('Workflow')
        self.name = None
        self.version = None
        self.description = None
        self.path = workflow_path
        self.steps = None
        self.workflow = self.load()


    def load(self):
        with open(self.path) as workflow_file:
            workflow = yaml.load(workflow_file, Loader=yaml.FullLoader)
        return workflow


    def validate(self):
        try:
            self.name = self.workflow['name']
            self.version = self.workflow['version']
            self.description = self.workflow['description']
            steps = self.parse_workflow(self.workflow)
            self.steps = steps
            return True
        except Exception as e:
            self.logger.error(e)
            return False


    def parse_workflow(self,workflow):
        workflow = workflow['workflow']
        components = list(workflow.keys())
        steps = []
        for component in components:
            operations = list(workflow[component].keys())
            for operation in operations:
                step = {}
                step['component'] = component
                step['operation'] = operation
                step['parameters'] = workflow[component][operation]
                steps.append(step)
        return steps
