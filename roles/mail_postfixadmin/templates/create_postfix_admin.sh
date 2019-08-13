#!/bin/bash

{
    sleep 0.5;
    echo "admin@{{ vhost }}";
    sleep 0.5;
    echo '"{{ lookup('password', '/root/062-pfxadmin_admin_password chars=ascii_letters,digits length=24') }}"';
    sleep 0.5;
    echo '"{{ lookup('password', '/root/062-pfxadmin_admin_password') }}"';
    sleep 0.5;
    echo "y";
    sleep 0.5;
    echo '"{{ vhost }}"';
    sleep 0.5;
    echo "y";
} | bash /var/www/postfixadmin/scripts/postfixadmin-cli admin add
