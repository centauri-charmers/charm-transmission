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

import mock

import charms_openstack.test_utils as test_utils

import charm.transmission as transmission


class Helper(test_utils.PatchHelper):

    def setUp(self):
        super().setUp()


class TestTransmissionCharm(Helper):

    def test_load_config(self):
        with mock.patch(
                "builtins.open",
                mock.mock_open(read_data='{"thing": 2}')) as _open:
            config = transmission.load_config("transmission")
            _open.assert_called_once_with(
                "/home/transmission/.config/transmission/settings.json", "r")
        self.assertEqual(config, {'thing': 2})
