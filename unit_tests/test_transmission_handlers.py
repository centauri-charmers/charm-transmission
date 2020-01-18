# Copyright 2020 Centauri Solutions
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#  http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from __future__ import absolute_import
from __future__ import print_function

# import json
# import mock

# import charm.openstack.manila_ganesha as manila_ganesha
import reactive.transmission as handlers

import charms_openstack.test_utils as test_utils


class TestRegisteredHooks(test_utils.TestRegisteredHooks):

    def test_hooks(self):
        defaults = [
            'charm.installed',
            'config.changed',
            'update-status',
            'upgrade-charm',
        ]
        hook_set = {
            'when': {
                'configure_transmission': ('apt.installed.transmission',
                                           'user.transmission.created',)
            },
            'when_not': {
                'configure_transmission': ('transmission.configured',),
                'create_user': ('user.transmission.created',)
            },
            'when_all': {}
        }
        # test that the hooks were registered via the
        # reactive.transmission handlers
        self.registered_hooks_test_helper(handlers, hook_set, defaults)
