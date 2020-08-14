Things to improve
- Separate let's encrypt verification dir, instead of web-site root. Reason: site root folder may be changed which breaks LE verification.
- Make use of TLS SNI in postfix, switch to postfix 3 on centos 7.
- Add nginx reload to ubuntu certbot cron task, check the same on other oses.
- Add nginx SSL lines to config by default. Enable them if cert issus is successful.