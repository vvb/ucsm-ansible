# ucsm-ansible

##### Pre-requisites:
* Install https://github.com/vijayvikrant/ucsmsdk.git
* Install https://github.com/vijayvikrant/ucsmsdk_samples.git
* Ansible: For sake of https://github.com/ansible/ansible/issues/3103 fix get the RC build
    * wget http://releases.ansible.com/ansible/ansible-2.0.0-0.9.rc4.tar.gz
    * tar -xvzf ansible-2.0.0-0.9.rc4.tar.gz
    * cd ansible-2.0.0
    * sudo python setup.py install


##### Usage:
```
vagrant@vvb:~$ git clone https://github.com/vijayvikrant/ucsm-ansible.git
vagrant@vvb:~$ cd ucsm-ansible 

vagrant@vvb:~/work/ucsm-ansible$ ansible-playbook fi-setup.yml

PLAY ***************************************************************************

TASK [Login 10.104.223.192] ****************************************************
ok: [ucspe]

TASK [Configure Dns Server 10.104.223.192] *************************************
changed: [ucspe]

TASK [Configure Qos Class Platinum  10.104.223.192] ****************************
changed: [ucspe]

TASK [Configure Qos Class Gold 10.104.223.192] *********************************
changed: [ucspe]

TASK [Configure Qos Class Silver 10.104.223.192] *******************************
changed: [ucspe]

TASK [Configure Qos Class Bronze 10.104.223.192] *******************************
changed: [ucspe]

TASK [Logout 10.104.223.192] ***************************************************
ok: [ucspe]

PLAY RECAP *********************************************************************
ucspe                      : ok=7    changed=5    unreachable=0    failed=0

vagrant@vvb:~/work/ucsm-ansible$

vagrant@vvb:~/work/ucsm-ansible$ ansible-playbook fi-setup.yml

PLAY ***************************************************************************

TASK [Login 10.104.223.192] ****************************************************
ok: [ucspe]

TASK [Configure Dns Server 10.104.223.192] *************************************
ok: [ucspe]

TASK [Configure Qos Class Platinum  10.104.223.192] ****************************
ok: [ucspe]

TASK [Configure Qos Class Gold 10.104.223.192] *********************************
ok: [ucspe]

TASK [Configure Qos Class Silver 10.104.223.192] *******************************
ok: [ucspe]

TASK [Configure Qos Class Bronze 10.104.223.192] *******************************
ok: [ucspe]

TASK [Logout 10.104.223.192] ***************************************************
ok: [ucspe]

PLAY RECAP *********************************************************************
ucspe                      : ok=7    changed=0    unreachable=0    failed=0

vagrant@vvb:~/work/ucsm-ansible$
```
