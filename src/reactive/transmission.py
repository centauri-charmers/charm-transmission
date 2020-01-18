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

# import subprocess

import charms
import charms.reactive as reactive
# import charms.reactive.relations as relations

import charmhelpers.core as ch_core
import charmhelpers.core.hookenv as hookenv


hooks = hookenv.Hooks()


@hooks.hook('install')
def install():
    charms.apt.queue_install(['transmission'])


@reactive.when_not('user.transmission.created')
def create_user():
    ch_core.host.add_user(
        username='transmission',
        system_user=True,
        uid=1001
    )
    reactive.set_state('user.transmission.created')


@reactive.when(
    'apt.installed.transmission',
    'user.transmission.created'
)
@reactive.when_not('transmission.configured')
def configure_transmission():
    reactive.set_state('transmission.configured')
