# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2021.
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
Integration Tests for IbmAnalyticsEngineApiV2
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from iaesdk.ibm_analytics_engine_api_v2 import *

# Config file name
config_file = "ibm_analytics_engine_api_v2.env"


class TestIbmAnalyticsEngineApiV2:
    """
    Integration Test Class for IbmAnalyticsEngineApiV2
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ["IBM_CREDENTIALS_FILE"] = config_file

            cls.ibm_analytics_engine_api_service = (
                IbmAnalyticsEngineApiV2.new_instance()
            )
            cls.instance_guid = os.getenv("IBM_ANALYTICS_ENGINE_INSTANCE_GUID")

            assert cls.ibm_analytics_engine_api_service is not None

            cls.config = read_external_sources(
                IbmAnalyticsEngineApiV2.DEFAULT_SERVICE_NAME
            )
            assert cls.config is not None

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_get_all_analytics_engines(self):
        get_all_analytics_engines_response = (
            self.ibm_analytics_engine_api_service.get_all_analytics_engines()
        )

        assert get_all_analytics_engines_response.get_status_code() == 200

    @needscredentials
    def test_get_analytics_engine_by_id(self):
        get_analytics_engine_by_id_response = (
            self.ibm_analytics_engine_api_service.get_analytics_engine_by_id(
                self.instance_guid
            )
        )

        assert get_analytics_engine_by_id_response.get_status_code() == 200
        analytics_engine = get_analytics_engine_by_id_response.get_result()
        assert analytics_engine is not None

    @needscredentials
    def test_get_analytics_engine_state_by_id(self):
        get_analytics_engine_state_by_id_response = (
            self.ibm_analytics_engine_api_service.get_analytics_engine_state_by_id(
                self.instance_guid
            )
        )

        assert get_analytics_engine_state_by_id_response.get_status_code() == 200
        analytics_engine_state = get_analytics_engine_state_by_id_response.get_result()
        assert analytics_engine_state is not None

    @needscredentials
    def test_create_customization_request(self):
        # Construct a dict representation of a AnalyticsEngineCustomActionScript model
        analytics_engine_custom_action_script_model = {
            "source_type": "http",
            "script_path": "testString",
            "source_props": {"unknown type: object"},
        }

        # Construct a dict representation of a AnalyticsEngineCustomAction model
        analytics_engine_custom_action_model = {
            "name": "testString",
            "type": "bootstrap",
            "script": analytics_engine_custom_action_script_model,
            "script_params": ["testString"],
        }

        create_customization_request_response = (
            self.ibm_analytics_engine_api_service.create_customization_request(
                self.instance_guid,
                target="all",
                custom_actions=[analytics_engine_custom_action_model],
            )
        )

        assert create_customization_request_response.get_status_code() == 200
        analytics_engine_create_customization_response = (
            create_customization_request_response.get_result()
        )
        assert analytics_engine_create_customization_response is not None

    @needscredentials
    def test_get_all_customization_requests(self):
        get_all_customization_requests_response = (
            self.ibm_analytics_engine_api_service.get_all_customization_requests(
                self.instance_guid
            )
        )

        assert get_all_customization_requests_response.get_status_code() == 200
        list_analytics_engine_customization_request_collection_item = (
            get_all_customization_requests_response.get_result()
        )
        assert list_analytics_engine_customization_request_collection_item is not None

    @needscredentials
    def test_get_customization_request_by_id(self):
        get_customization_request_by_id_response = (
            self.ibm_analytics_engine_api_service.get_customization_request_by_id(
                self.instance_guid, request_id="testString"
            )
        )

        assert get_customization_request_by_id_response.get_status_code() == 200
        analytics_engine_customization_run_details = (
            get_customization_request_by_id_response.get_result()
        )
        assert analytics_engine_customization_run_details is not None

    @needscredentials
    def test_resize_cluster(self):
        # Construct a dict representation of a ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest model
        resize_cluster_request_model = {
            "compute_nodes_count": 38,
        }

        resize_cluster_response = self.ibm_analytics_engine_api_service.resize_cluster(
            self.instance_guid, body=resize_cluster_request_model
        )

        assert resize_cluster_response.get_status_code() == 200
        analytics_engine_resize_cluster_response = resize_cluster_response.get_result()
        assert analytics_engine_resize_cluster_response is not None

    @needscredentials
    def test_reset_cluster_password(self):
        reset_cluster_password_response = (
            self.ibm_analytics_engine_api_service.reset_cluster_password(
                self.instance_guid
            )
        )

        assert reset_cluster_password_response.get_status_code() == 200
        analytics_engine_reset_cluster_password_response = (
            reset_cluster_password_response.get_result()
        )
        assert analytics_engine_reset_cluster_password_response is not None

    @needscredentials
    def test_configure_logging(self):
        # Construct a dict representation of a AnalyticsEngineLoggingNodeSpec model
        analytics_engine_logging_node_spec_model = {
            "node_type": "management",
            "components": ["ambari-server"],
        }

        # Construct a dict representation of a AnalyticsEngineLoggingServer model
        analytics_engine_logging_server_model = {
            "type": "logdna",
            "credential": "testString",
            "api_host": "testString",
            "log_host": "testString",
            "owner": "testString",
        }

        configure_logging_response = (
            self.ibm_analytics_engine_api_service.configure_logging(
                self.instance_guid,
                log_specs=[analytics_engine_logging_node_spec_model],
                log_server=analytics_engine_logging_server_model,
            )
        )

        assert configure_logging_response.get_status_code() == 202

    @needscredentials
    def test_get_logging_config(self):
        get_logging_config_response = (
            self.ibm_analytics_engine_api_service.get_logging_config(self.instance_guid)
        )

        assert get_logging_config_response.get_status_code() == 200
        analytics_engine_logging_config_details = (
            get_logging_config_response.get_result()
        )
        assert analytics_engine_logging_config_details is not None

    @needscredentials
    def test_update_private_endpoint_whitelist(self):
        update_private_endpoint_whitelist_response = (
            self.ibm_analytics_engine_api_service.update_private_endpoint_whitelist(
                self.instance_guid, ip_ranges=["testString"], action="add"
            )
        )

        assert update_private_endpoint_whitelist_response.get_status_code() == 200
        analytics_engine_whitelist_response = (
            update_private_endpoint_whitelist_response.get_result()
        )
        assert analytics_engine_whitelist_response is not None

    @needscredentials
    def test_delete_logging_config(self):
        delete_logging_config_response = (
            self.ibm_analytics_engine_api_service.delete_logging_config(
                self.instance_guid
            )
        )

        assert delete_logging_config_response.get_status_code() == 202
