import click
from nile.nre import NileRuntimeEnvironment
from nile import deployments
from nile.deployments import HashExistsException
import fileinput
import sys

@click.command()
@click.argument("proxy_address", type=str)
@click.argument("contract_name", type=str)
def upgrade_proxy(proxy_address, contract_name):
    # Help message
    """
    Upgrade a proxy to a different implementation contract.
    """

    nre = NileRuntimeEnvironment()

    click.echo(f"Declaring implementation {contract_name}...")
    hash = None
    try:
        hash = nre.declare(contract_name)
        click.echo(f"Implementation declared with hash {hash}")
    except HashExistsException as e:
        hash = e.hash
        click.echo(f"Implementation with hash {hash} already exists")

    # TODO check that new impl has upgrade function

    click.echo(f"Upgrading proxy...")
    nre.invoke(proxy_address, "upgrade", params=[hash])
    click.echo(f"Proxy upgraded to implementation with hash {hash}")

    deployments.update(proxy_address, f"artifacts/abis/{contract_name}.json", "localhost", alias=None)

def updateDeployment(file, proxy_address, contract_name):
    for line in fileinput.input(file, inplace=1):
        if proxy_address in line:
            line = f"{proxy_address}:artifacts/abis/{contract_name}.json"
        sys.stdout.write(line)
