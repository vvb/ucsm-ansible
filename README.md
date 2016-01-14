# ucsm-ansible

##### Pre-requisites:
* Install https://github.com/vijayvikrant/ucsmsdk.git
* Install https://github.com/vijayvikrant/ucsmsdk_samples.git
* Ansible


##### Usage:
```
vagrant@vvb:~$ git clone https://github.com/vijayvikrant/ucsm-ansible.git
vagrant@vvb:~$ cd ucsm-ansible 
vagrant@vvb:~/work/ucsm-ansible$ ansible-playbook ucsm-common-conf.yml

PLAY ***************************************************************************

TASK [Login 10.104.223.192] ****************************************************
ok: [ucspe]

TASK [Configure Dns Server 10.104.223.192] *************************************
changed: [ucspe]

TASK [Configure Qos Policy 10.104.223.192] *************************************
changed: [ucspe]

TASK [Logout 10.104.223.192] ***************************************************
ok: [ucspe]

PLAY RECAP *********************************************************************
ucspe                      : ok=4    changed=2    unreachable=0    failed=0


vagrant@vvb:~/work/ucsm-ansible$
vagrant@vvb:~/work/ucsm-ansible$ ansible-playbook ucsm-common-conf.yml

PLAY ***************************************************************************

TASK [Login 10.104.223.192] ****************************************************
ok: [ucspe]

TASK [Configure Dns Server 10.104.223.192] *************************************
ok: [ucspe]

TASK [Configure Qos Policy 10.104.223.192] *************************************
ok: [ucspe]

TASK [Logout 10.104.223.192] ***************************************************
ok: [ucspe]

PLAY RECAP *********************************************************************
ucspe                      : ok=4    changed=0    unreachable=0    failed=0

vagrant@vvb:~/work/ucsm-ansible$
vagrant@vvb:~/work/ucsm-ansible$ ansible-playbook ucsm-common-conf-cleanup.yml

PLAY ***************************************************************************

TASK [Login 10.104.223.192] ****************************************************
ok: [ucspe]

TASK [Remove Dns Server 10.104.223.192] ****************************************
changed: [ucspe]

TASK [Remove Qos Policy 10.104.223.192] ****************************************
changed: [ucspe]

TASK [Logout 10.104.223.192] ***************************************************
ok: [ucspe]

PLAY RECAP *********************************************************************
ucspe                      : ok=4    changed=2    unreachable=0    failed=0

vagrant@vvb:~/work/ucsm-ansible$
vagrant@vvb:~/work/ucsm-ansible$ ansible-playbook ucsm-common-conf-cleanup.yml

PLAY ***************************************************************************

TASK [Login 10.104.223.192] ****************************************************
ok: [ucspe]

TASK [Remove Dns Server 10.104.223.192] ****************************************
ok: [ucspe]

TASK [Remove Qos Policy 10.104.223.192] ****************************************
ok: [ucspe]

TASK [Logout 10.104.223.192] ***************************************************
ok: [ucspe]

PLAY RECAP *********************************************************************
ucspe                      : ok=4    changed=0    unreachable=0    failed=0

vagrant@vvb:~/work/ucsm-ansible$
```
