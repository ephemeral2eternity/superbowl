#!/bin/sh
echo "Install Curl!"
yum -y install curl
echo "Install iperf!"
yum -y install iperf
echo "Install bind-utils!"
yum -y install bind-utils
echo "Installing python-pip!"
cd ~
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python ~/get-pip.py
echo "Display the pip version!"
pip -V
echo "Install python requests packages!"
pip install requests
echo "Upgrading the requests package to the latest version!"
pip install --upgrade requests
