## Initial setup solutions for VPS hosting

#### Supported and tested on: 
- Ubuntu 20, 22, 24 
- RockyLinux 8, 9
- Debian 11, 12
- AlmaLinux 8, 9

#### Playbooks:
[base](./roles/base/README.md), [fail2ban](./roles/fail2ban/README.md) and [sftp](./roles/sftp/README.md) roles are included in every playbook.

- certbot: Installs SSL certificate from Let's Encrypt.
- django: Installs Django with Postgresql and Nginx web-server.
- docker: Installs docker.
- lamp_nginx: Installs LAMP stack with NGINX as a reverse proxy.
- lamp: Installs LAMP stack: Apache, MySQL, PHP.
- mean: Installs MEAN stack: MongoDB, Express.js, Angular, NodeJS
- wordpress: Installs LAMP stack with NGINX as a reverse proxy and deploys latest WordPress engine.

#### Roles: 

- [base](./roles/base/README.md)
- [certbot](./roles/certbot/README.md)
- [django](./roles/django/README.md)
- [docker](./roles/docker/README.md)
- [fail2ban](./roles/fail2ban/README.md)
- [httpd](./roles/httpd/README.md)
- [mariadb](./roles/mariadb/README.md)
- [mongodb](./roles/mongodb/README.md)
- [nginx](./roles/nginx/README.md)
- [nodejs](./roles/nodejs/README.md)
- [php](./roles/php/README.md)
- [phpmyadmin](./roles/phpmyadmin/README.md)
- [postgresql](./roles/postgresql/README.md)
- [sftp](./roles/sftp/README.md)
- [wordpress](./roles/wordpress/README.md)
