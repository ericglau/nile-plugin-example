import click
from nile.nre import NileRuntimeEnvironment

@click.command()
@click.argument("proxy_address", type=str)
@click.argument("contract_name", type=str)
def upgrade_proxy(proxy_address, contract_name):
    # Help message
    """
    Upgrade a proxy to a different implementation contract.
    """

    nre = NileRuntimeEnvironment()

    click.echo(f"Declaring new implementation {contract_name}...")
    hash = nre.declare(contract_name)
    click.echo(f"Implementation declared with hash {hash}")

    # TODO check that new impl has upgrade function

    click.echo(f"Upgrading proxy...")
    nre.invoke(proxy_address, "upgrade", params=[hash])
    click.echo(f"Proxy upgraded to implementation with hash {hash}")

    # Update deployments with new abi
    
