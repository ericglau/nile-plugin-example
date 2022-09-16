import click
from nile.nre import NileRuntimeEnvironment

@click.command()
@click.argument("contract_name", type=str)
def deploy_proxy(contract_name):
    # Help message
    """
    Deploy an upgradeable proxy for an implementation contract.
    """

    nre = NileRuntimeEnvironment()

    click.echo(f"Declaring implementation {contract_name}...")
    hash = nre.declare(contract_name)
    click.echo(f"Implementation declared with hash {hash}")

    click.echo(f"Deploying upgradeable proxy...")
    addr, abi = nre.deploy("Proxy", arguments=[hash])
    click.echo(f"Proxy deployed to address {addr}")

    return addr