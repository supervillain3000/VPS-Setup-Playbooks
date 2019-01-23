#!/bin/sh
#
# metadata_begin
# recipe: PS.kz nginx + php-fpm + mysql
# tags: debian8,debian9,ubuntu1604,ubuntu1804
# revision: 2
# description_ru: Nginx + php-fpm + mysql
# description_en: Nginx + php-fpm + mysql
# metadata_end
#

LOG_PIPE=/tmp/log.pipe.$$
mkfifo ${LOG_PIPE}
LOG_FILE=/root/recipe.log
touch ${LOG_FILE}
chmod 600 ${LOG_FILE}

tee < ${LOG_PIPE} ${LOG_FILE} &

exec > ${LOG_PIPE}
exec 2> ${LOG_PIPE}

killjobs() {
	test -n "$(jobs -p)" && kill $(jobs -p) || :
}
trap killjobs INT TERM EXIT

vhostname=`hostname`
hostnamewd=$(echo "$vhostname" | sed 's/\.//')

if [ -f /etc/redhat-release ]; then
  osname="centos"
else
  osname="debian"
fi

echo $osname

# install ansible and git
if [ $osname = "debian" ]; then
	apt update
  apt-add-repository --yes --update ppa:ansible/ansible
  apt -y install software-properties-common ansible git
else
  yum -y install ansible git
fi

mkdir /root/ansible
git clone https://github.com/blaarb/recipes /root/ansible/
cd /root/ansible/

ansible-playbook current.yml
