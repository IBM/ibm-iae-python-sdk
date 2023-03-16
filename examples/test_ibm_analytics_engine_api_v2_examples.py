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
Examples for IbmAnalyticsEngineApiV2
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from iaesdk.ibm_analytics_engine_api_v2 import *

#
# This file provides an example of how to use the IBM Analytics Engine API service.
#
# The following configuration properties are assumed to be defined:
# IBM_ANALYTICS_ENGINE_API_URL=<service base url>
# IBM_ANALYTICS_ENGINE_API_AUTH_TYPE=iam
# IBM_ANALYTICS_ENGINE_API_APIKEY=<IAM apikey>
# IBM_ANALYTICS_ENGINE_API_AUTH_URL=<IAM token service base URL - omit this if using the production environment>
#
# These configuration properties can be exported as environment variables, or stored
# in a configuration file and then:
# export IBM_CREDENTIALS_FILE=<name of configuration file>
#
config_file = "ibm_analytics_engine_api_v2.env"

ibm_analytics_engine_api_service = None

config = None


##############################################################################
# Start of Examples for Service: IbmAnalyticsEngineApiV2
##############################################################################
# region
class TestIbmAnalyticsEngineApiV2Examples:
    """
    Example Test Class for IbmAnalyticsEngineApiV2
    """

    @classmethod
    def setup_class(cls):
        global ibm_analytics_engine_api_service
        if os.path.exists(config_file):
            os.environ["IBM_CREDENTIALS_FILE"] = config_file

            # begin-common

            ibm_analytics_engine_api_service = IbmAnalyticsEngineApiV2.new_instance()

            # end-common
            assert ibm_analytics_engine_api_service is not None

            # Load the configuration
            global config
            config = read_external_sources(IbmAnalyticsEngineApiV2.DEFAULT_SERVICE_NAME)

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_get_all_analytics_engines_example(self):
        """
        get_all_analytics_engines request example
        """
        try:
            # begin-getAllAnalyticsEngines

            response = ibm_analytics_engine_api_service.get_all_analytics_engines()

            # end-getAllAnalyticsEngines
            print(
                "\nget_all_analytics_engines() response status code: ",
                response.get_status_code(),
            )

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_analytics_engine_by_id_example(self):
        """
        get_analytics_engine_by_id request example
        """
        try:
            print("\nget_analytics_engine_by_id() result:")
            # begin-getAnalyticsEngineById

            analytics_engine = (
                ibm_analytics_engine_api_service.get_analytics_engine_by_id(
                    instance_guid="testString"
                ).get_result()
            )

            print(json.dumps(analytics_engine, indent=2))

            # end-getAnalyticsEngineById

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_analytics_engine_state_by_id_example(self):
        """
        get_analytics_engine_state_by_id request example
        """
        try:
            print("\nget_analytics_engine_state_by_id() result:")
            # begin-getAnalyticsEngineStateById

            analytics_engine_state = (
                ibm_analytics_engine_api_service.get_analytics_engine_state_by_id(
                    instance_guid="testString"
                ).get_result()
            )

            print(json.dumps(analytics_engine_state, indent=2))

            # end-getAnalyticsEngineStateById

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_customization_request_example(self):
        """
        create_customization_request request example
        """
        try:
            print("\ncreate_customization_request() result:")
            # begin-createCustomizationRequest

            analytics_engine_custom_action_model = {
                "name": "testString",
            }

            analytics_engine_create_customization_response = (
                ibm_analytics_engine_api_service.create_customization_request(
                    instance_guid="testString",
                    target="all",
                    custom_actions=[analytics_engine_custom_action_model],
                ).get_result()
            )

            print(json.dumps(analytics_engine_create_customization_response, indent=2))

            # end-createCustomizationRequest

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_all_customization_requests_example(self):
        """
        get_all_customization_requests request example
        """
        try:
            print("\nget_all_customization_requests() result:")
            # begin-getAllCustomizationRequests

            list_analytics_engine_customization_request_collection_item = (
                ibm_analytics_engine_api_service.get_all_customization_requests(
                    instance_guid="testString"
                ).get_result()
            )

            print(
                json.dumps(
                    list_analytics_engine_customization_request_collection_item,
                    indent=2,
                )
            )

            # end-getAllCustomizationRequests

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_customization_request_by_id_example(self):
        """
        get_customization_request_by_id request example
        """
        try:
            print("\nget_customization_request_by_id() result:")
            # begin-getCustomizationRequestById

            analytics_engine_customization_run_details = (
                ibm_analytics_engine_api_service.get_customization_request_by_id(
                    instance_guid="testString", request_id="testString"
                ).get_result()
            )

            print(json.dumps(analytics_engine_customization_run_details, indent=2))

            # end-getCustomizationRequestById

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_resize_cluster_example(self):
        """
        resize_cluster request example
        """
        try:
            print("\nresize_cluster() result:")
            # begin-resizeCluster

            resize_cluster_request_model = {}

            analytics_engine_resize_cluster_response = (
                ibm_analytics_engine_api_service.resize_cluster(
                    instance_guid="testString", body=resize_cluster_request_model
                ).get_result()
            )

            print(json.dumps(analytics_engine_resize_cluster_response, indent=2))

            # end-resizeCluster

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_reset_cluster_password_example(self):
        """
        reset_cluster_password request example
        """
        try:
            print("\nreset_cluster_password() result:")
            # begin-resetClusterPassword

            analytics_engine_reset_cluster_password_response = (
                ibm_analytics_engine_api_service.reset_cluster_password(
                    instance_guid="testString"
                ).get_result()
            )

            print(
                json.dumps(analytics_engine_reset_cluster_password_response, indent=2)
            )

            # end-resetClusterPassword

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_configure_logging_example(self):
        """
        configure_logging request example
        """
        try:
            # begin-configureLogging

            analytics_engine_logging_node_spec_model = {
                "node_type": "management",
                "components": ["ambari-server"],
            }

            analytics_engine_logging_server_model = {
                "type": "logdna",
                "credential": "testString",
                "api_host": "testString",
                "log_host": "testString",
            }

            response = ibm_analytics_engine_api_service.configure_logging(
                instance_guid="testString",
                log_specs=[analytics_engine_logging_node_spec_model],
                log_server=analytics_engine_logging_server_model,
            )

            # end-configureLogging
            print(
                "\nconfigure_logging() response status code: ",
                response.get_status_code(),
            )

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_logging_config_example(self):
        """
        get_logging_config request example
        """
        try:
            print("\nget_logging_config() result:")
            # begin-getLoggingConfig

            analytics_engine_logging_config_details = (
                ibm_analytics_engine_api_service.get_logging_config(
                    instance_guid="testString"
                ).get_result()
            )

            print(json.dumps(analytics_engine_logging_config_details, indent=2))

            # end-getLoggingConfig

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_private_endpoint_whitelist_example(self):
        """
        update_private_endpoint_whitelist request example
        """
        try:
            print("\nupdate_private_endpoint_whitelist() result:")
            # begin-updatePrivateEndpointWhitelist

            analytics_engine_whitelist_response = (
                ibm_analytics_engine_api_service.update_private_endpoint_whitelist(
                    instance_guid="testString", ip_ranges=["testString"], action="add"
                ).get_result()
            )

            print(json.dumps(analytics_engine_whitelist_response, indent=2))

            # end-updatePrivateEndpointWhitelist

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_logging_config_example(self):
        """
        delete_logging_config request example
        """
        try:
            # begin-deleteLoggingConfig

            response = ibm_analytics_engine_api_service.delete_logging_config(
                instance_guid="testString"
            )

            # end-deleteLoggingConfig
            print(
                "\ndelete_logging_config() response status code: ",
                response.get_status_code(),
            )

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: IbmAnalyticsEngineApiV2
##############################################################################
