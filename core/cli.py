#!/usr/bin/python3

from core.utils import get_status
import click
import os

@click.group()
def plasma_cli():
    pass


@click.command(help="display status information")
def status():
    get_status()


@click.command(help="Connect to plasma dashboard")
def connect():
    raise NotImplementedError


# Model command group

@click.group(help="manage connected models")
def model():
    pass


@click.command(name="list",help="list connected models")
def list_model():
    raise NotImplementedError


@click.command(name="deploy",help="serve a model")
@click.argument('model_name', required=True)
def serve_model():
    raise NotImplementedError


@click.command(name="monitor",help="monitor a deployed model")
@click.argument('model_name',required = True)
def monitor_model():
    raise NotImplementedError


# Configure command group
@click.command(help="configure plasma")
def configure():
    pass

# Workflow command group

@click.group(help="manage plasma workflows")
def workflow():
    pass


@click.command(name="list", help="list existing workflows")
def list_workflow():
    pass


@click.command(name="run", help="run workflow")
@click.argument('workflow_name', required=True)
def run_workflow(workflow_name):
    pass


@click.command(name="describe", help="describe workflow")
@click.argument('workflow_name', required=True)
def describe_workflow(workflow_name):
    pass


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
    pass


@click.command(name="search", help="search for components")
@click.argument('component_name', required=True)
def search_component(component_name):
    pass


@click.command(name="get", help="download components")
@click.argument('component_name', required=True)
def get_component(component_name):
    pass


@click.command(name="run", help="run components")
@click.argument('component_name', required=True)
@click.option("--parameters", "-p", multiple=True)
def run_component(component_name, parameters):
    print(parameters)
    pass


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
    component.add_command(run_component)
    plasma_cli.add_command(configure)
    plasma_cli.add_command(status)
    plasma_cli.add_command(component)
    plasma_cli.add_command(workflow)
    plasma_cli.add_command(model)
    return plasma_cli
