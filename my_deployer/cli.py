"""My_deployer's CLI commands.
"""
import click

from cli_commands import config


@click.group()
def my_deployer():
    """Handy lightweight container deployment CLI program."""
    pass


def cli():
    """Execute the command using the CLI flags."""
    my_deployer.add_command(config)
    my_deployer()


if __name__ == '__main__':
    cli()
