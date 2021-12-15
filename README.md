## Initial setup solutions for VPS hosting
https://www.ps.kz/hosting/vps#free-setup

Supported OS: Ubuntu 18, 20, CentOS 7, 8, Debian 10, 11

Supported php-version: 5.6 through 8.1

#### Option 1
Nginx, Apache, MySQL, and mysqladmin bundled together and ready for website deployment.

#### Option 1
Same as option 1 but with php-fpm instead of Apache.

#### Option 3
Email server + Postfixadmin. Maiboxes management availabe via http://server_ip_address/postadmin/ All server access data and db passwords are stored in /root/passwords.txt. To access maiboxes use email clients.

#### Option 4
Control panel installation: Plesk Panel Latest Stable or ISP Manager 6 Lite Stable Latest

#### Option 5
Django On Python3 without database.

#### Option 6
Bitrix Environment https://dev.1c-bitrix.ru/learning/course/index.php?COURSE_ID=37&LESSON_ID=8811

### Things to improve:
- Separate Let's Encrypt verification dir, instead of web-site root. Reason: site root folder may be changed, which breaks LE verification.
- Make use of TLS SNI in postfix, switch to postfix 3 on centos 7.
- Add nginx reload to ubuntu certbot cron task, check the same on other OS.
- Add nginx SSL lines to webhost config by default. Enable them if cert issue is successful.
