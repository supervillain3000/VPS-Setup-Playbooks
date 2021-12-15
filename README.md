

Things to improve:
- Separate let's encrypt verification dir, instead of web-site root. Reason: site root folder may be changed, which breaks LE verification.
- Make use of TLS SNI in postfix, switch to postfix 3 on centos 7.
- Add nginx reload to ubuntu certbot cron task, check the same on other OS.
- Add nginx SSL lines to webhost config by default. Enable them if cert issue is successful.
