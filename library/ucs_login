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


from ucsmsdk.ucshandle import UcsHandle

def ucs_login(module):
    ip = module.params.get('ip')
    username = module.params.get('username')
    password = module.params.get('password')

    results = {}

    handle = UcsHandle(ip, username, password)
    try:
        handle.login()
        results['logged_in'] = True
    except:
        module.fail_json(msg="login failed")

    results['handle'] = handle.to_json() 
    results['cookie'] = handle.cookie
    return results

def main():
    module = AnsibleModule(
        argument_spec = dict(
            ip        = dict(required=True),
            username  = dict(required=True),
            password  = dict(required=True)
        )
    )

    results = ucs_login(module)
    module.exit_json(**results)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

