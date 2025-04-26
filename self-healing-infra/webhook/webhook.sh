#!/bin/bash
echo "Webhook triggered, running Ansible playbook..." >> /tmp/webhook.log
ansible-playbook -i ansible/inventory ansible/playbook.yml >> /tmp/ansible.log 2>&1