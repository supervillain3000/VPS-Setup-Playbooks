import pytest

@pytest.fixture
def apache_service_name(host):
    if host.system_info.distribution in ("debian", "ubuntu"):
        return "apache2"
    else:
        return "httpd"

@pytest.fixture
def apache_conf_path(host):
    if host.system_info.distribution in ("debian", "ubuntu"):
        return "/etc/apache2"
    else:
        return "/etc/httpd"

def test_apache_package_installed(host, apache_service_name):
    pkg = host.package(apache_service_name)
    assert pkg.is_installed

def test_apache_service_running_and_enabled(host, apache_service_name):
    svc = host.service(apache_service_name)
    assert svc.is_running
    assert svc.is_enabled

def test_apache_is_listening_on_expected_port(host):
    socket = host.socket(f"tcp://0.0.0.0:80")
    assert socket.is_listening or host.socket(f"tcp://127.0.0.1:80").is_listening

def test_apache_vhost_symlink_exists(host, apache_conf_path):
    sites_enabled = f"{apache_conf_path}/sites-enabled"
    cmd = host.run(f"ls -l {sites_enabled}")
    assert "->" in cmd.stdout

def test_apache_document_root_exists(host, apache_conf_path):
    www_root = "/var/www"
    dirs = host.file(www_root)
    assert dirs.exists
    assert dirs.is_directory

def test_apache_returns_200(host):
    cmd = host.run(f"curl -s -o /dev/null -w '%{{http_code}}' http://127.0.0.1:80")
    assert cmd.stdout == "200"

def test_ports_conf_disabled(host, apache_conf_path):
    ports_conf = host.file(f"{apache_conf_path}/ports.conf")
    assert ports_conf.exists
    assert "# disabled" in ports_conf.content_string
