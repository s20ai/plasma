#!/usr/bin/python3

from core.utils import configure_plasma
import core.component_manager as component_manager
import core.workflow_manager as workflow_manager
import core.execution_engine as execution_engine
import click
import os


@click.group()
def plasma_cli():
    pass


# Model command group

@click.group(help="manage connected models")
def model():
    pass


@click.command(name="list", help="list connected models")
def list_model():
    raise NotImplementedError


@click.command(name="deploy", help="serve a model")
@click.argument('model_name', required=True)
def serve_model():
    raise NotImplementedError


@click.command(name="monitor", help="monitor a deployed model")
@click.argument('model_name', required=True)
def monitor_model():
    raise NotImplementedError

# Workflow command group


@click.group(help="manage plasma workflows")
def workflow():
    pass


@click.command(name="list", help="list existing workflows")
def list_workflow():
    workflow_manager.list_workflows()


@click.command(name="run", help="run workflow")
@click.argument('workflow_name', required=True)
def run_workflow(workflow_name):
    print('\n> Running workflow '+workflow_name+'\n')
    workflow_manager.run_workflow(workflow_name)


@click.command(name="describe", help="describe workflow")
@click.argument('workflow_name', required=True)
def describe_workflow(workflow_name):
    workflow_manager.describe_workflow(workflow_name)


@click.command(name="schedule", help="schedule workflows")
@click.argument('workflow_name', required=True)
def schedule_workflow(workflow_name):
    os.system('crontab -e')


# Component command group

@click.group(help="manage plasma components")
def component():
    pass


@click.command(name="list", help="list components")
def list_component():
    component_manager.list_components()


@click.command(name="search", help="search for components")
@click.argument('component_name', required=True)
def search_component(component_name):
    component_manager.search_components(component_name)


@click.command(name="get", help="download components")
@click.argument('component_name', required=True)
def get_component(component_name):
    component_manager.download_component(component_name)


@click.command(name="describe", help="download components")
@click.argument('component_name', required=True)
def describe_component(component_name):
    component_manager.describe_component(component_name)


@click.command(name="run", help="run components")
@click.argument('component_name', required=True)
@click.option("--parameters", "-p", multiple=True)
def run_component(component_name, parameters):
    # output = execution_engine.run_component(component_name,
           # parameters)
    # print(output)
    raise NotImplementedError


def command_dispatcher():
    model.add_command(list_model)
    model.add_command(serve_model)
    model.add_command(monitor_model)
    workflow.add_command(list_workflow)
    workflow.add_command(run_workflow)
    workflow.add_command(describe_workflow)
    workflow.add_command(schedule_workflow)
    component.add_command(list_component)
    component.add_command(search_component)
    component.add_command(get_component)
    component.add_command(describe_component)
    component.add_command(run_component)
    plasma_cli.add_command(component)
    plasma_cli.add_command(workflow)
    plasma_cli.add_command(model)
    return plasma_cli
