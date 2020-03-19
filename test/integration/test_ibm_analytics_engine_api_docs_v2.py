# coding: utf-8

# Copyright 2019 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""
Test the mysdk service API operations
"""

import pytest
import unittest
import os
import json
import iaesdk
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator


@pytest.mark.skipif(
    os.getenv('VCAP_SERVICES') is None, reason='requires VCAP_SERVICES')
class TestExampleServiceV1(unittest.TestCase):
    def setUp(self):
        vcap_services = json.loads(os.getenv('VCAP_SERVICES'))
        authenticator = IAMAuthenticator(vcap_services["ibm_analytics_engine_api_docs_v2"][0]["credentials"]["apikey"])
        self.iaesdk_service = iaesdk.IbmAnalyticsEngineApiDocsV2(authenticator=authenticator)
        self.iaesdk_service.set_service_url("https://api.us-south.ae.cloud.ibm.com")
        self.instance_guid=vcap_services["ibm_analytics_engine_api_docs_v2"][0]["credentials"]["instance_guid"]

    def tearDown(self):
        # Delete the resources
        print("Clean up complete.")

    def test_get_analytics_engine_by_id(self):
        status_code = self.iaesdk_service.get_analytics_engine_by_id(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_get_analytics_engine_state_by_id(self):
        status_code = self.iaesdk_service.get_analytics_engine_state_by_id(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_create_customization_request(self):
        # Construct a dict representation of a AnalyticsEngineCustomActionScript model
        analytics_engine_custom_action_script_model =  {
            'source_type': 'http',
            'script_path': 'testString',
            'source_props': 'unknown type: object'
        }
        # Construct a dict representation of a AnalyticsEngineCustomAction model
        analytics_engine_custom_action_model =  {
            'name': 'testString',
            'type': 'bootstrap',
            'script': analytics_engine_custom_action_script_model,
            'script_params': ['testString']
        }

        # Set up parameter values
        instance_guid = 'testString'
        target = 'all'
        custom_actions = [analytics_engine_custom_action_model]

        # Invoke method
        status_code = self.iaesdk_service.create_customization_request(
            self.instance_guid,
            target,
            custom_actions,
        ).get_status_code()

        assert status_code == 200

    def test_get_all_customization_requests(self):
        status_code = self.iaesdk_service.get_all_customization_requests(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_get_customization_request_by_id(self):
        result = self.iaesdk_service.get_all_customization_requests(self.instance_guid).get_result()
        request_id = result[0]["id"]
        status_code = self.iaesdk_service.get_customization_request_by_id(self.instance_guid, request_id).get_status_code()
        assert status_code == 200

    def test_resize_cluster(self):
        compute_nodes_count = 1
        status_code = self.iaesdk_service.resize_cluster(self.instance_guid, compute_nodes_count).get_status_code()
        assert status_code == 200

    def test_reset_cluster_password(self):
        status_code = self.iaesdk_service.reset_cluster_password(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_configure_logging(self):

        # Construct a dict representation of a AnalyticsEngineLoggingNodeSpec model
        analytics_engine_logging_node_spec_model =  {
            'node_type': 'management',
            'components': ['ambari-server']
        }
        # Construct a dict representation of a AnalyticsEngineLoggingServer model
        analytics_engine_logging_server_model =  {
            'type': 'logdna',
            'credential': 'testString',
            'api_host': 'testString',
            'log_host': 'testString',
            'owner': 'testString'
        }

        # Set up parameter values
        instance_guid = 'testString'
        log_specs = [analytics_engine_logging_node_spec_model]
        log_server = analytics_engine_logging_server_model

        status_code = self.iaesdk_service.configure_logging(
            self.instance_guid,
            log_specs,
            log_server,
        ).get_status_code()

        assert status_code == 202

    def test_get_logging_config(self):
        status_code = self.iaesdk_service.get_logging_config(self.instance_guid).get_status_code()
        assert status_code == 200

    def test_delete_logging_config(self):
        status_code = self.iaesdk_service.delete_logging_config(self.instance_guid).get_status_code()
        assert status_code == 202
