import click
from nile.nre import NileRuntimeEnvironment
from nile.common import ABIS_DIRECTORY
import os

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

    pt = os.path.dirname(os.path.realpath(__file__)).replace("/nile_upgrades", "")
    click.echo(f"pt: {pt}")
    overriding_path = (f"{pt}/artifacts", f"{pt}/artifacts/abis")
    click.echo(f"overriding_path: {overriding_path}")


    click.echo(f"Deploying upgradeable proxy...")
    overriding_abi = f"{ABIS_DIRECTORY}/{contract_name}.json";
    addr, abi = nre.deploy("Proxy", arguments=[hash], overriding_path=overriding_path, overriding_abi=overriding_abi)
    click.echo(f"Proxy deployed to address {addr}, abi {abi}")

    return addr