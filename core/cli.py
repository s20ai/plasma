#!/usr/bin/python3

import click


@click.group()
def plasma_cli():
    pass


@click.command(help="Display status information")
def status():
    return True


@click.command(help="Connect to plasma dashboard")
def connect():
    raise NotImplementedError


# Configure command group

@click.command(help="configure plasma")
def configure():
    pass

# Workflow command group


@click.group(help="Manage Plasma Workflows")
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
    pass


# Component command group

@click.group(help="Manage Plasma Components")
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
    return plasma_cli
