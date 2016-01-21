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

def ucs_logout(module):
    handle = module.params.get('handle')

    results = {}
    ucs_handle = UcsHandle.from_json(handle)

    try:
        ucs_handle.logout()
        results['logged_out'] = True
    except:
        module.fail_json(msg="logout failed")

    return results

def main():
    module = AnsibleModule(
        argument_spec = dict(
            handle    = dict(required=True)
        )
    )

    results = ucs_logout(module)
    module.exit_json(**results)

from ansible.module_utils.basic import *
if __name__ == '__main__':
    main()

