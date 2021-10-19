"""My deployer."""
import click as click


@click.command()
@click.argument('remote_ip')
def config(remote_ip):
    click.echo(f"configuring {remote_ip}!")
