import pytest

def test_php_binary_exists(host):
    assert host.exists("php")

def test_php_version(host):
    cmd = host.run("php -v")
    assert cmd.rc == 0
    assert "PHP" in cmd.stdout
