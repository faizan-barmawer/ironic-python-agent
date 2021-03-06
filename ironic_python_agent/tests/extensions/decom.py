# Copyright 2013 Rackspace, Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import mock
from oslotest import base as test_base

from ironic_python_agent.extensions import decom


class TestDecomExtension(test_base.BaseTestCase):
    def setUp(self):
        super(TestDecomExtension, self).setUp()
        self.agent_extension = decom.DecomExtension()

    @mock.patch('ironic_python_agent.hardware.dispatch_to_managers',
                autospec=True)
    def test_erase_devices(self, mocked_dispatch):
        result = self.agent_extension.erase_hardware()
        result.join()
        mocked_dispatch.assert_called_once_with('erase_devices')
        self.assertTrue('result' in result.command_result.keys())
        cmd_result_text = 'erase_hardware: finished'
        self.assertEqual(cmd_result_text, result.command_result['result'])
