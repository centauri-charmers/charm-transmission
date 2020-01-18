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

import json


"""A collection of helpers for working with Transmission"""


def load_config(user='transmission'):
    # read file
    with open(
            "/home/{}/.config/transmission/settings.json".format(user),
            'r') as myfile:
        data = myfile.read()
    return json.loads(data)


def save_config(config, user='transmission'):
    with open(
            "/home/{}/.config/transmission/settings.json".format(user),
            'w') as myfile:
        myfile.write(json.dumps(config))
