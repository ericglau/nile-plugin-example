# First, import click dependency
import click
from nile.nre import NileRuntimeEnvironment


# Decorate the method that will be the command name with `click.command`
@click.command()
@click.argument("a", type=int)
@click.argument("b", type=int)
# You can define custom parameters as defined in `click`: https://click.palletsprojects.com/en/7.x/options/
def greet(a, b):
    # Help message to show with the command
    """
    Subcommand plugin that does something.
    """
    # Done! Now implement your custom functionality in the command
    click.echo(f"Hello! I'm a Nile plugin with ${a} and ${b}")
    nre = NileRuntimeEnvironment()

    address, abi = nre.deploy("contract", alias="my_contract")
    print(abi, address)
    return a + b