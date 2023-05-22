# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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
Examples for IbmAnalyticsEngineApiV3
"""

from ibm_cloud_sdk_core import ApiException, read_external_sources
import os
import pytest
from iaesdk.ibm_analytics_engine_api_v3 import *

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
config_file = 'ibm_analytics_engine_api_v3.env'

ibm_analytics_engine_api_service = None

config = None


##############################################################################
# Start of Examples for Service: IbmAnalyticsEngineApiV3
##############################################################################
# region
class TestIbmAnalyticsEngineApiV3Examples:
    """
    Example Test Class for IbmAnalyticsEngineApiV3
    """

    @classmethod
    def setup_class(cls):
        global ibm_analytics_engine_api_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            ibm_analytics_engine_api_service = IbmAnalyticsEngineApiV3.new_instance()

            # end-common
            assert ibm_analytics_engine_api_service is not None

            # Load the configuration
            global config
            config = read_external_sources(IbmAnalyticsEngineApiV3.DEFAULT_SERVICE_NAME)

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_instance_example(self):
        """
        get_instance request example
        """
        try:
            print('\nget_instance() result:')
            # begin-get_instance

            response = ibm_analytics_engine_api_service.get_instance(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            instance = response.get_result()

            print(json.dumps(instance, indent=2))

            # end-get_instance

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_state_example(self):
        """
        get_instance_state request example
        """
        try:
            print('\nget_instance_state() result:')
            # begin-get_instance_state

            response = ibm_analytics_engine_api_service.get_instance_state(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            instance_get_state_response = response.get_result()

            print(json.dumps(instance_get_state_response, indent=2))

            # end-get_instance_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_set_instance_home_example(self):
        """
        set_instance_home request example
        """
        try:
            print('\nset_instance_home() result:')
            # begin-set_instance_home

            response = ibm_analytics_engine_api_service.set_instance_home(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                new_hmac_access_key='b9****************************4b',
                new_hmac_secret_key='fa********************************************8a',
            )
            instance_home_response = response.get_result()

            print(json.dumps(instance_home_response, indent=2))

            # end-set_instance_home

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_home_credentials_example(self):
        """
        update_instance_home_credentials request example
        """
        try:
            print('\nupdate_instance_home_credentials() result:')
            # begin-update_instance_home_credentials

            response = ibm_analytics_engine_api_service.update_instance_home_credentials(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                hmac_access_key='b9****************************4b',
                hmac_secret_key='fa********************************************8a',
            )
            instance_home_response = response.get_result()

            print(json.dumps(instance_home_response, indent=2))

            # end-update_instance_home_credentials

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_default_configs_example(self):
        """
        get_instance_default_configs request example
        """
        try:
            print('\nget_instance_default_configs() result:')
            # begin-get_instance_default_configs

            response = ibm_analytics_engine_api_service.get_instance_default_configs(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            instance_default_configs = response.get_result()

            print(json.dumps(instance_default_configs, indent=2))

            # end-get_instance_default_configs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_instance_default_configs_example(self):
        """
        replace_instance_default_configs request example
        """
        try:
            print('\nreplace_instance_default_configs() result:')
            # begin-replace_instance_default_configs

            response = ibm_analytics_engine_api_service.replace_instance_default_configs(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                body={
                    'spark.driver.memory': '8G',
                    'spark.driver.cores': '2',
                },
            )
            instance_default_configs = response.get_result()

            print(json.dumps(instance_default_configs, indent=2))

            # end-replace_instance_default_configs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_update_instance_default_configs_example(self):
        """
        update_instance_default_configs request example
        """
        try:
            print('\nupdate_instance_default_configs() result:')
            # begin-update_instance_default_configs

            response = ibm_analytics_engine_api_service.update_instance_default_configs(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                body={
                    'ae.spark.history-server.cores': '1',
                    'ae.spark.history-server.memory': '4G',
                },
            )
            instance_default_configs = response.get_result()

            print(json.dumps(instance_default_configs, indent=2))

            # end-update_instance_default_configs

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_instance_default_runtime_example(self):
        """
        get_instance_default_runtime request example
        """
        try:
            print('\nget_instance_default_runtime() result:')
            # begin-get_instance_default_runtime

            response = ibm_analytics_engine_api_service.get_instance_default_runtime(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            runtime = response.get_result()

            print(json.dumps(runtime, indent=2))

            # end-get_instance_default_runtime

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_instance_default_runtime_example(self):
        """
        replace_instance_default_runtime request example
        """
        try:
            print('\nreplace_instance_default_runtime() result:')
            # begin-replace_instance_default_runtime

            response = ibm_analytics_engine_api_service.replace_instance_default_runtime(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            runtime = response.get_result()

            print(json.dumps(runtime, indent=2))

            # end-replace_instance_default_runtime

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_create_application_example(self):
        """
        create_application request example
        """
        try:
            print('\ncreate_application() result:')
            # begin-create_application

            runtime_model = {
                'spark_version': '3.3',
            }

            application_request_application_details_model = {
                'application': '/opt/ibm/spark/examples/src/main/python/wordcount.py',
                'runtime': runtime_model,
                'arguments': ['/opt/ibm/spark/examples/src/main/resources/people.txt'],
            }

            response = ibm_analytics_engine_api_service.create_application(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                application_details=application_request_application_details_model,
            )
            application_response = response.get_result()

            print(json.dumps(application_response, indent=2))

            # end-create_application

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_list_applications_example(self):
        """
        list_applications request example
        """
        try:
            print('\nlist_applications() result:')
            # begin-list_applications

            all_results = []
            pager = ApplicationsPager(
                client=ibm_analytics_engine_api_service,
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                state=['accepted', 'running', 'finished', 'failed'],
                limit=10,
            )
            while pager.has_next():
                next_page = pager.get_next()
                assert next_page is not None
                all_results.extend(next_page)

            print(json.dumps(all_results, indent=2))

            # end-list_applications
        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_application_example(self):
        """
        get_application request example
        """
        try:
            print('\nget_application() result:')
            # begin-get_application

            response = ibm_analytics_engine_api_service.get_application(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                application_id='ff48cc19-0e7e-4627-aac6-0b4ad080397b',
            )
            application_get_response = response.get_result()

            print(json.dumps(application_get_response, indent=2))

            # end-get_application

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_application_state_example(self):
        """
        get_application_state request example
        """
        try:
            print('\nget_application_state() result:')
            # begin-get_application_state

            response = ibm_analytics_engine_api_service.get_application_state(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                application_id='ff48cc19-0e7e-4627-aac6-0b4ad080397b',
            )
            application_get_state_response = response.get_result()

            print(json.dumps(application_get_state_response, indent=2))

            # end-get_application_state

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_current_resource_consumption_example(self):
        """
        get_current_resource_consumption request example
        """
        try:
            print('\nget_current_resource_consumption() result:')
            # begin-get_current_resource_consumption

            response = ibm_analytics_engine_api_service.get_current_resource_consumption(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            current_resource_consumption_response = response.get_result()

            print(json.dumps(current_resource_consumption_response, indent=2))

            # end-get_current_resource_consumption

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_resource_consumption_limits_example(self):
        """
        get_resource_consumption_limits request example
        """
        try:
            print('\nget_resource_consumption_limits() result:')
            # begin-get_resource_consumption_limits

            response = ibm_analytics_engine_api_service.get_resource_consumption_limits(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            resource_consumption_limits_response = response.get_result()

            print(json.dumps(resource_consumption_limits_response, indent=2))

            # end-get_resource_consumption_limits

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_replace_log_forwarding_config_example(self):
        """
        replace_log_forwarding_config request example
        """
        try:
            print('\nreplace_log_forwarding_config() result:')
            # begin-replace_log_forwarding_config

            response = ibm_analytics_engine_api_service.replace_log_forwarding_config(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            log_forwarding_config_response = response.get_result()

            print(json.dumps(log_forwarding_config_response, indent=2))

            # end-replace_log_forwarding_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_log_forwarding_config_example(self):
        """
        get_log_forwarding_config request example
        """
        try:
            print('\nget_log_forwarding_config() result:')
            # begin-get_log_forwarding_config

            response = ibm_analytics_engine_api_service.get_log_forwarding_config(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            log_forwarding_config_response = response.get_result()

            print(json.dumps(log_forwarding_config_response, indent=2))

            # end-get_log_forwarding_config

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_configure_platform_logging_example(self):
        """
        configure_platform_logging request example
        """
        try:
            print('\nconfigure_platform_logging() result:')
            # begin-configure_platform_logging

            response = ibm_analytics_engine_api_service.configure_platform_logging(
                instance_guid='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            logging_configuration_response = response.get_result()

            print(json.dumps(logging_configuration_response, indent=2))

            # end-configure_platform_logging

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_logging_configuration_example(self):
        """
        get_logging_configuration request example
        """
        try:
            print('\nget_logging_configuration() result:')
            # begin-get_logging_configuration

            response = ibm_analytics_engine_api_service.get_logging_configuration(
                instance_guid='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            logging_configuration_response = response.get_result()

            print(json.dumps(logging_configuration_response, indent=2))

            # end-get_logging_configuration

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_start_spark_history_server_example(self):
        """
        start_spark_history_server request example
        """
        try:
            print('\nstart_spark_history_server() result:')
            # begin-start_spark_history_server

            response = ibm_analytics_engine_api_service.start_spark_history_server(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            spark_history_server_response = response.get_result()

            print(json.dumps(spark_history_server_response, indent=2))

            # end-start_spark_history_server

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_get_spark_history_server_example(self):
        """
        get_spark_history_server request example
        """
        try:
            print('\nget_spark_history_server() result:')
            # begin-get_spark_history_server

            response = ibm_analytics_engine_api_service.get_spark_history_server(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )
            spark_history_server_response = response.get_result()

            print(json.dumps(spark_history_server_response, indent=2))

            # end-get_spark_history_server

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_delete_application_example(self):
        """
        delete_application request example
        """
        try:
            # begin-delete_application

            response = ibm_analytics_engine_api_service.delete_application(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                application_id='ff48cc19-0e7e-4627-aac6-0b4ad080397b',
            )

            # end-delete_application
            print('\ndelete_application() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

    @needscredentials
    def test_stop_spark_history_server_example(self):
        """
        stop_spark_history_server request example
        """
        try:
            # begin-stop_spark_history_server

            response = ibm_analytics_engine_api_service.stop_spark_history_server(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
            )

            # end-stop_spark_history_server
            print('\nstop_spark_history_server() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))


# endregion
##############################################################################
# End of Examples for Service: IbmAnalyticsEngineApiV3
##############################################################################
