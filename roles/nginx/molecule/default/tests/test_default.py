import os
import requests
import pytest

# You can parametrize by OS type if needed
@pytest.mark.parametrize("pkg_name", ["nginx"])
def test_nginx_is_installed(host, pkg_name):
    pkg = host.package(pkg_name)
    assert pkg.is_installed


def test_nginx_service_running_and_enabled(host):
    service = host.service("nginx")
    assert service.is_running
    assert service.is_enabled

def test_nginx_conf_exists_and_owned_correctly(host):
    f = host.file("/etc/nginx/nginx.conf")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


@pytest.mark.parametrize("conf_name", [
    "00-conn.conf",
    "01-gzip.conf",
    "02-proxy.conf",
    "03-timeout.conf",
    "04-ssl.conf",
    "05-open_file.conf"
])
def test_conf_d_configs(host, conf_name):
    f = host.file(f"/etc/nginx/conf.d/{conf_name}")
    assert f.exists
    assert f.user == "root"
    assert f.group == "root"
    assert f.mode == 0o644


def test_vhosts_dir_exists(host):
    d = host.file("/etc/nginx/vhosts/")
    assert d.exists
    assert d.is_directory
    assert d.mode == 0o755

def test_nginx_http_status():
    response = requests.get("http://localhost")
    assert response.status_code == 200
