import pytest

# Helper to get lowercase distro name
def get_distro(host):
    return host.system_info.distribution.lower()

# Common package list with distro mapping
@pytest.mark.parametrize("name,distros", [
    ("lsb-release", ["ubuntu", "debian"]),
    ("apt-transport-https", ["ubuntu", "debian"]),
    ("ca-certificates", ["ubuntu", "debian"]),
    ("ufw", ["ubuntu", "debian"]),
    ("epel-release", ["centos", "redhat", "rocky", "almalinux"]),
    ("yum-utils", ["centos", "redhat", "rocky", "almalinux"]),
    ("firewalld", ["centos", "redhat", "rocky", "almalinux"]),
    ("wget", ["ubuntu", "debian", "centos", "redhat", "rocky", "almalinux"]),
    ("git", ["ubuntu", "debian", "centos", "redhat", "rocky", "almalinux"]),
    ("python3-pip", ["ubuntu", "debian", "centos", "redhat", "rocky", "almalinux"]),
    ("chrony", ["ubuntu", "debian", "centos", "redhat", "rocky", "almalinux"]),
    ("rsyslog", ["ubuntu", "debian", "centos", "redhat", "rocky", "almalinux"]),
    ("fail2ban", ["ubuntu", "debian", "centos", "redhat", "rocky", "almalinux"])
])
def test_packages(host, name, distros):
    distro = get_distro(host)
    if distro in distros:
        pkg = host.package(name)
        assert pkg.is_installed, f"{name} should be installed on {distro}"

# Only run firewalld-related tests on RHEL-family distros
@pytest.mark.skipif(
    get_distro.__code__ is None,
    reason="firewalld only runs on RHEL-based systems"
)
def test_firewalld_running_and_enabled(host):
    if get_distro(host) in ["centos", "redhat", "rocky", "almalinux"]:
        firewalld = host.service("firewalld")
        assert firewalld.is_running, "firewalld should be running"
        assert firewalld.is_enabled, "firewalld should be enabled"

def test_ssh_port_open_in_firewalld(host):
    if get_distro(host) in ["centos", "redhat", "rocky", "almalinux"]:
        cmd = host.run("firewall-cmd --list-all")
        assert "ssh" in cmd.stdout, "SSH should be allowed in firewalld"

def test_chronyd_running_and_enabled(host):
    chronyd = host.service("chronyd")
    assert chronyd.is_running, "chronyd should be running"
    assert chronyd.is_enabled, "chronyd should be enabled"

def test_rsyslog_running_and_enabled(host):
    rsyslog = host.service("rsyslog")
    assert rsyslog.is_running, "rsyslog should be running"
    assert rsyslog.is_enabled, "rsyslog should be enabled"

def test_logrotate_compression_enabled(host):
    f = host.file("/etc/logrotate.conf")
    assert f.contains("compress"), "Logrotate should have 'compress' directive"

def test_hosts_file_exists(host):
    f = host.file("/etc/fail2ban/jail.local")
    assert f.exists, "/etc/fail2ban/jail.local should exist"

def test_fail2ban_running_and_enabled(host):
    fail2ban = host.service("fail2ban")
    assert fail2ban.is_running, "fail2ban should be running"
    assert fail2ban.is_enabled, "fail2ban should be enabled"

def test_repos_enabled(host):
    distro = get_distro(host)
    if distro in ["centos", "redhat", "rocky", "almalinux"]:
        enabled_repos = host.check_output("dnf repolist enabled")
        distro_version = host.system_info.release
        distro_major = int(distro_version.split('.')[0])
        if distro_major >= 9:
            assert "crb" in enabled_repos.lower(), "'crb' repo should be enabled"
        else:
            assert "powertools" in enabled_repos.lower(), "'powertools' repo should be enabled"
