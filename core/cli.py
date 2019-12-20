#!/usr/bin/python3

from core.command_dispatcher import execute
import click
import os
import collections


class OrderedGroup(click.Group):
    def __init__(self, name=None, commands=None, **attrs):
        super(OrderedGroup, self).__init__(name, commands, **attrs)
        #: the registered subcommands by their exported names.
        self.commands = commands or collections.OrderedDict()

    def list_commands(self, ctx):
        return self.commands


@click.group(cls=OrderedGroup)
def cli():
    pass


# Plasma init

@click.argument('project_name', required=True)
@click.command(name="init", help="initialize a plasma project", )
def initialize_project(project_name):
    execute('setup_plasma_project', project_name)


# Model command group

@click.group(cls=OrderedGroup, help="manage connected models")
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

@click.group(cls=OrderedGroup, help="manage plasma workflows")
def workflow():
    pass


@click.command(name="run", help="run workflow")
@click.argument('workflow_name', required=True)
def run_workflow(workflow_name):
    print('\n> Running workflow '+workflow_name+'\n')
    execute('run_workflow', workflow_name)


@click.command(name="schedule", help="schedule workflows")
@click.argument('workflow_name', required=True)
def schedule_workflow(workflow_name):
    execute('schedule_workflow', workflow_name)


# Component command group

@click.group(cls=OrderedGroup, help="manage plasma components")
def component():
    pass


@click.command(name="list", help="list components")
def list_component():
    execute('list_components')


@click.command(name="search", help="search for components")
@click.argument('component_name', required=True)
def search_component(component_name):
    execute('search_components', component_name)


@click.command(name="get", help="download components")
@click.argument('component_name', required=True)
def get_component(component_name):
    execute('download_component', component_name)


@click.command(name="describe", help="download components")
@click.argument('component_name', required=True)
def describe_component(component_name):
    execute('describe_component', component_name)


@click.command(name="run", help="run components")
@click.argument('component_name', required=True)
@click.option("--parameters", "-p", multiple=True)
def run_component(component_name, parameters):
    execute('run_component', [component_name, parameters])


def plasma_cli():
    model.add_command(list_model)
    model.add_command(serve_model)
    model.add_command(monitor_model)
    workflow.add_command(run_workflow)
    workflow.add_command(schedule_workflow)
    component.add_command(list_component)
    component.add_command(search_component)
    component.add_command(get_component)
    component.add_command(describe_component)
    cli.add_command(initialize_project)
    cli.add_command(component)
    cli.add_command(workflow)
    cli.add_command(model)
    return cli
