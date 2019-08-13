#!/bin/bash

{
    sleep 0.3;
    echo "admin@{{ vhost }}";
    sleep 0.3;
    echo '--password "{{ lookup('password', '/root/062-pfxadmin_admin_password chars=ascii_letters,digits,hexdigits length=15') }}"';
    sleep 0.3;
    echo '--password2 "{{ lookup('password', '/root/062-pfxadmin_admin_password') }}"';
    sleep 0.3;
    echo "--superadmin 1"
    sleep 0.3;
    echo '"{{ vhost }}"'
    sleep 0.3;
    echo "--active 1"
} | bash /var/www/postfixadmin/scripts/postfixadmin-cli admin add
