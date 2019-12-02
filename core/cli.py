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


# Pipeline command group

@click.group(help="Manage Plasma Pipelines")
def pipeline():
    pass


@click.command(name="list", help="list existing pipelines")
def list_pipeline():
    pass


@click.command(name="run", help="run pipeline")
@click.argument('pipeline_name', required=True)
def run_pipeline(pipeline_name):
    pass


@click.command(name="schedule", help="schedule pipelines")
@click.argument('pipeline_name', required=True)
def schedule_pipeline(pipeline_name):
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
    pipeline.add_command(list_pipeline)
    pipeline.add_command(run_pipeline)
    pipeline.add_command(schedule_pipeline)
    component.add_command(list_component)
    component.add_command(search_component)
    component.add_command(get_component)
    component.add_command(run_component)
    plasma_cli.add_command(status)
    plasma_cli.add_command(component)
    plasma_cli.add_command(pipeline)
    return plasma_cli
