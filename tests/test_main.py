from nile_upgrades.main import deploy_proxy


def test_main():
    assert callable(deploy_proxy)
