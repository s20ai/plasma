#!/usr/bin/python3

import click

@click.group()
def command_dispatcher()
    pass


@click.group(help="manage plasma pipelines")
def pipelines():
    pass

@click.command(help="list existing pipelines"):
def list():
    pass

@click.command(help="run pipeline"):
def run():
    pass

@click.command(help="schedule pipelines")
def schedule():
    pass



@click.command()
def status(help="display plasma status information"):
    return True


