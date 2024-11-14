## base

Base configuration of OS. Installs chrony, rsyslog. Configure firewall, logrotate.

### variables:
- base_debian_package_list: List of packages that will be installed on Debian-based OS.
- base_redhat_package_list: List of packages that will be installed on RedHat-based OS.
