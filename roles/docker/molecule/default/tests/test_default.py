import pytest

@pytest.mark.parametrize("pkg_name", ["docker-ce", "docker-ce-cli", "containerd.io", "docker-buildx-plugin", "docker-compose-plugin"])
def test_packages_is_installed(host, pkg_name):
    pkg = host.package(pkg_name)
    assert pkg.is_installed

def test_docker_service_running_and_enabled(host):
    docker_service = host.service("docker")
    assert docker_service.is_enabled
    assert docker_service.is_running


def test_docker_socket_exists(host):
    docker_sock = host.file("/var/run/docker.sock")
    assert docker_sock.exists
    assert docker_sock.is_socket

@pytest.mark.parametrize("cmd", [
    "docker --version",
    "docker info"
])
def test_docker_cli_commands(host, cmd):
    result = host.run(cmd)
    assert result.rc == 0
