import pytest

import testinfra.utils.ansible_runner

def test_node_installed(host):
    node = host.exists("node")
    npm = host.exists("npm")

    assert node, "Node.js binary should be present"
    assert npm, "NPM binary should be present"

def test_node_version(host):
    cmd = host.run("node --version")
    assert cmd.rc == 0, "Node.js should run successfully"
    version = cmd.stdout.strip()

    expected_prefix = "v20."
    assert version.startswith(expected_prefix), f"Expected Node.js version to start with {expected_prefix}, got {version}"
