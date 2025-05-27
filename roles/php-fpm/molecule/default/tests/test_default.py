import pytest
import re

## Hardcoded versions
@pytest.fixture
def php_service_name(host):
    if host.system_info.distribution in ("debian", "ubuntu"):
        return "php8.3-fpm.service"
    else:
        return "php83-php-fpm.service"

def test_nginx_is_installed(host):
    pkg = host.service("nginx")
    assert pkg.is_enabled
    assert pkg.is_running

def test_php_service_running_and_enabled(host, php_service_name):
    svc = host.service(php_service_name)
    assert svc.is_running
    assert svc.is_enabled
