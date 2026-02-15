## Initial setup solutions for VPS hosting

#### Supported and tested on: 
- Ubuntu 20, 22, 24 
- RockyLinux 8, 9
- Debian 11, 12
- AlmaLinux 8, 9

#### Playbooks:
`base`, `fail2ban`, and `sftp` roles are expected to be part of baseline VM setup.

- certbot: Installs SSL certificate from Let's Encrypt.
- django: Installs Django with Postgresql and Nginx web-server.
- docker: Installs docker.
- lamp_nginx: Installs LAMP stack with NGINX as a reverse proxy.
- lamp: Installs LAMP stack: Apache, MySQL, PHP.
- mean: Installs MEAN stack: MongoDB, Express.js, Angular, NodeJS
- wordpress: Installs LAMP stack with NGINX as a reverse proxy and deploys latest WordPress engine.

#### Roles:

- base
- certbot
- django
- docker
- fail2ban
- httpd
- mariadb
- mongodb
- nginx
- nodejs
- php
- php-fpm
- phpmyadmin
- postgresql
- sftp
- wordpress

## Development and testing
- Contribution workflow, Molecule usage, and role/playbook guidelines are in [`CONTRIBUTING.md`](./CONTRIBUTING.md).
- Run Molecule for all roles with scenarios:
  - `./extentions/molecule/test-all-roles.sh`
