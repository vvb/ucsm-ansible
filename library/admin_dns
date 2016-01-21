#!/usr/bin/python
# -*- mode: python -*-

# Copyright 2015 Cisco Systems, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


DOCUMENTATION = '''
---
module: admin_dns 
short_description: configure/remove dns settings 
description:
  - Lets the user add/remove and configure dns server IP address/hostname and description 
version_added: "0.1.0"
options:
  name:
    aliases: [ 'name', 'hostname' ]
    description:
    - The hostname/ip of the dns server to add to the inventory
    required: true
  state:
    aliases: [ 'state' ]
    description:
    - defines if the dns entry should be added or removed 
    required: true 
  handle:
    description:
    - serialized UcsHandle string 
    required: true 

author: 
    - "Cisco UCS Team"
    - "Vikrant Balyan"
'''

EXAMPLES = '''
# add a dns entry to the Ucs server
- admin_dns: name={{ dns_server }}
             state=present

# remove a dns entry from the Ucs server
- admin_dns: name={{ dns_server }}
             state=absent
'''

from ucsmsdk_samples.admin.dns import dns_server_add, dns_server_remove, dns_server_exists
from ucsmsdk.ucshandle import UcsHandle

def admin_dns(module):
    name = module.params.get('name')
    state = module.params.get('state')
    handle = module.params.get('handle')

    results = {}
    ucs_handle = UcsHandle.from_json(handle)

    exists = dns_server_exists(ucs_handle, name)

    if state == "present":
        if not exists:
            mo = dns_server_add(ucs_handle, name)
            results['created'] = True
            results['changed'] = True
        else:
            results['created'] = False 
            results['changed'] = False 
            
    else:
        if exists:
            dns_server_remove(ucs_handle, name)
            results['created'] = False 
            results['changed'] = True
        else:
            results['created'] = False 
            results['changed'] = False 


    results['state'] = state
    return results

def main():
    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            name      = dict(required=True),
            handle    = dict(required=True)
        )
    )

    results = admin_dns(module)
    module.exit_json(**results)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

