# First, import click dependency
import click
from nile.nre import NileRuntimeEnvironment

# Decorate the method that will be the command name with `click.command`
@click.command()
@click.argument("contract_name", type=str)
# You can define custom parameters as defined in `click`: https://click.palletsprojects.com/en/7.x/options/
def greet(contract_name):
    # Help message to show with the command
    """
    Subcommand plugin that does something.
    """
    # Done! Now implement your custom functionality in the command
    click.echo(f"contract_name ${contract_name}")
    nre = NileRuntimeEnvironment()

    address, abi = nre.deploy(contract_name)
    print(abi, address)