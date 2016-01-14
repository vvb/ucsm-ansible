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
module: network_qos_class
short_description: configure/remove qos classes 
description:
  - Lets the user add/remove and configure qos classes 
version_added: "0.1.0"
author: 
    - "Cisco UCS Team"
    - "Vikrant Balyan"
'''

EXAMPLES = '''
# add a qos class the Ucs server
- network_qos_class: 
    priority={{ priority }}
    cos={{ cos }}
    drop={{ drop }}
    weight={{ weight }}
    mtu={{ mtu }}
    multicast_optimize={{ multicast_optimize }}
    handle={{ handle }}
    state=present

# remove a qos class from the Ucs server
- network_qos_class: 
    priority={{ priority }}
    handle={{ handle }}
    state=absent
'''

from ucsmsdk_samples.network.qos import qos_class_enable, qos_class_disable, qos_class_exists 
from ucsmsdk.ucshandle import UcsHandle

def network_qos_class(module):
    state = module.params.get('state')
    handle = module.params.get('handle')
    priority = module.params.get('priority')

    results = {}
    ucs_handle = UcsHandle.from_json(handle)

    if state == "present":
        cos = module.params.get('cos')
        drop = module.params.get('drop')
        weight = module.params.get('weight')
        mtu = module.params.get('mtu')
        multicast_optimize = module.params.get('multicast_optimize')

        exists = qos_class_exists(ucs_handle, priority=priority, cos=cos,
                                  drop=drop, weight=weight, mtu=mtu,
                                  multicast_optimize=multicast_optimize,
                                  admin_state="enabled", match_props=True)
        if not exists:
            mo = qos_class_enable(ucs_handle, priority=priority, cos=cos,
                                     drop=drop, weight=weight, mtu=mtu,
                                     multicast_optimize=multicast_optimize)
            results["created"] = True
            results["changed"] = True
        else:
            results["created"] = False
            results["changed"] = False
    else:
        exists = qos_class_exists(ucs_handle, priority=priority, 
                                  admin_state="disabled", match_props=False)
        if exists:
            mo = qos_class_disable(ucs_handle, priority=priority)
            results["created"] = False 
            results["changed"] = True
        else:
            results["created"] = False 
            results["changed"] = False 

    results['state'] = state
    return results

def main():
    module = AnsibleModule(
        argument_spec = dict(
            state     = dict(default='present', choices=['present', 'absent']),
            handle    = dict(required=True),
            priority  = dict(required=True),
            cos       = dict(required=True),
            drop      = dict(required=True),
            weight    = dict(required=True),
            mtu       = dict(required=True),
            multicast_optimize = dict(required=True)
        )
    )

    results = network_qos_class(module)
    module.exit_json(**results)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

