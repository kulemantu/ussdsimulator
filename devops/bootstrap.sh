#!/bin/bash
 
#set up ansible on the dev box
 
echo "setting up ansible...."
 
if [[ ! $(ansible --version 2> /dev/null) =~ 1\.6 ]]; then
    sudo apt-get update && \
    sudo apt-get -y install python-software-properties && \
    sudo add-apt-repository -y ppa:rquillo/ansible && \
    sudo apt-get update && \
    sudo apt-get -y install ansible
fi
 
echo "provisioning with ansible...."
PYTHONUNBUFFERED=1 ansible-playbook /vagrant/devops/main.yml \
    --inventory-file=/vagrant/devops/development \
    --connection=local