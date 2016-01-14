# ucsm-ansible

##### Pre-requisites:
* Install https://github.com/vijayvikrant/ucsmsdk.git
* Install https://github.com/vijayvikrant/ucsmsdk-samples.git
* Ansible


##### Usage:
```
vagrant@vvb:~$ git clone https://github.com/vijayvikrant/ucsm-ansible.git
vagrant@vvb:~$ cd ucsm-ansible 
vagrant@vvb:~/ucsm-ansible$ ansible-playbook ucsm-common-conf.yml

PLAY ***************************************************************************

TASK [Login 10.104.223.192] ****************************************************
ok: [ucspe]

TASK [Configure Dns Server] ****************************************************
ok: [ucspe]

TASK [Logout 10.104.223.192] ***************************************************
ok: [ucspe]

PLAY RECAP *********************************************************************
ucspe                      : ok=3    changed=0    unreachable=0    failed=0

vagrant@vvb:~/ucsm-ansible$
```
