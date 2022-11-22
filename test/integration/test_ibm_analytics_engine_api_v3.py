# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2022.
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
Integration Tests for IbmAnalyticsEngineApiV3
"""

from ibm_cloud_sdk_core import *
import os
import pytest
from iaesdk.ibm_analytics_engine_api_v3 import *

# Config file name
config_file = 'ibm_analytics_engine_api_v3.env'
application_id = ''

class TestIbmAnalyticsEngineApiV3():
    """
    Integration Test Class for IbmAnalyticsEngineApiV3
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            cls.ibm_analytics_engine_api_service = IbmAnalyticsEngineApiV3.new_instance(
            )
            assert cls.ibm_analytics_engine_api_service is not None

            cls.config = read_external_sources(
                IbmAnalyticsEngineApiV3.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.instance_id = cls.config['INSTANCE_GUID']
            cls.instance_id_without_instance_home = cls.config['INSTANCE_GUID_WO_INSTANCE_HOME']
            cls.hmac_access_key = cls.config['HMAC_ACCESS_KEY']
            cls.hmac_secret_key = cls.config['HMAC_SECRET_KEY']

            cls.ibm_analytics_engine_api_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_instance(self):

        get_instance_response = self.ibm_analytics_engine_api_service.get_instance(
            instance_id=self.instance_id
        )

        assert get_instance_response.get_status_code() == 200
        instance = get_instance_response.get_result()
        assert instance is not None

    @needscredentials
    def test_get_instance_state(self):

        get_instance_state_response = self.ibm_analytics_engine_api_service.get_instance_state(
            instance_id=self.instance_id
        )

        assert get_instance_state_response.get_status_code() == 200
        instance_get_state_response = get_instance_state_response.get_result()
        assert instance_get_state_response is not None

    @needscredentials
    def test_set_instance_home(self):

        set_instance_home_response = self.ibm_analytics_engine_api_service.set_instance_home(
            instance_id=self.instance_id_without_instance_home,
            new_instance_id='testString',
            new_provider='ibm-cos',
            new_type='objectstore',
            new_region='us-south',
            new_endpoint='s3.direct.us-south.cloud-object-storage.appdomain.cloud',
            new_hmac_access_key=self.hmac_access_key,
            new_hmac_secret_key=self.hmac_secret_key
        )

        assert set_instance_home_response.get_status_code() == 200
        instance_home_response = set_instance_home_response.get_result()
        assert instance_home_response is not None

    @needscredentials
    def test_get_instance_default_configs(self):

        get_instance_default_configs_response = self.ibm_analytics_engine_api_service.get_instance_default_configs(
            instance_id=self.instance_id
        )

        assert get_instance_default_configs_response.get_status_code() == 200
        result = get_instance_default_configs_response.get_result()
        assert result is not None

    @needscredentials
    def test_replace_instance_default_configs(self):

        replace_instance_default_configs_response = self.ibm_analytics_engine_api_service.replace_instance_default_configs(
            instance_id=self.instance_id,
            body={
                "spark.driver.memory": "8G",
                "spark.driver.cores": "2",
            }
        )

        assert replace_instance_default_configs_response.get_status_code() == 200
        result = replace_instance_default_configs_response.get_result()
        assert result is not None

    @needscredentials
    def test_update_instance_default_configs(self):

        update_instance_default_configs_response = self.ibm_analytics_engine_api_service.update_instance_default_configs(
            instance_id=self.instance_id,
            body={
                "ae.spark.history-server.cores": "1",
                "ae.spark.history-server.memory": "4G",
            }
        )

        assert update_instance_default_configs_response.get_status_code() == 200
        result = update_instance_default_configs_response.get_result()
        assert result is not None

    @needscredentials
    def test_get_instance_default_runtime(self):

        get_instance_default_runtime_response = self.ibm_analytics_engine_api_service.get_instance_default_runtime(
            instance_id=self.instance_id
        )

        assert get_instance_default_runtime_response.get_status_code() == 200
        runtime = get_instance_default_runtime_response.get_result()
        assert runtime is not None

    @needscredentials
    def test_replace_instance_default_runtime(self):

        replace_instance_default_runtime_response = self.ibm_analytics_engine_api_service.replace_instance_default_runtime(
            instance_id=self.instance_id,
            spark_version='3.3'
        )

        assert replace_instance_default_runtime_response.get_status_code() == 200
        runtime = replace_instance_default_runtime_response.get_result()
        assert runtime is not None

    @needscredentials
    def test_create_application(self):

        # Construct a dict representation of a Runtime model
        runtime_model = {
            'spark_version': '3.1',
        }

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {
            'application': '/opt/ibm/spark/examples/src/main/python/wordcount.py',
            'arguments': ['/opt/ibm/spark/examples/src/main/resources/people.txt'],
            'runtime': runtime_model
        }

        create_application_response = self.ibm_analytics_engine_api_service.create_application(
            instance_id=self.instance_id,
            application_details=application_request_application_details_model
        )

        assert create_application_response.get_status_code() == 202
        application_response = create_application_response.get_result()
        assert application_response is not None

        global application_id
        application_id = application_response.get('id')

    @needscredentials
    def test_list_applications(self):

        list_applications_response = self.ibm_analytics_engine_api_service.list_applications(
            instance_id=self.instance_id,
            state=['accepted', 'submitted', 'waiting', 'running', 'finished', 'failed']
        )

        assert list_applications_response.get_status_code() == 200
        application_collection = list_applications_response.get_result()
        assert application_collection is not None

    @needscredentials
    def test_get_application(self):

        get_application_response = self.ibm_analytics_engine_api_service.get_application(
            instance_id=self.instance_id,
            application_id=application_id
        )

        assert get_application_response.get_status_code() == 200
        application_get_response = get_application_response.get_result()
        assert application_get_response is not None

    @needscredentials
    def test_get_application_state(self):

        get_application_state_response = self.ibm_analytics_engine_api_service.get_application_state(
            instance_id=self.instance_id,
            application_id=application_id
        )

        assert get_application_state_response.get_status_code() == 200
        application_get_state_response = get_application_state_response.get_result()
        assert application_get_state_response is not None

    @needscredentials
    def test_get_current_resource_consumption(self):

        get_current_resource_consumption_response = self.ibm_analytics_engine_api_service.get_current_resource_consumption(
            instance_id=self.instance_id
        )

        assert get_current_resource_consumption_response.get_status_code() == 200
        current_resource_consumption_response = get_current_resource_consumption_response.get_result()
        assert current_resource_consumption_response is not None

    @needscredentials
    def test_get_resource_consumption_limits(self):

        get_resource_consumption_limits_response = self.ibm_analytics_engine_api_service.get_resource_consumption_limits(
            instance_id=self.instance_id
        )

        assert get_resource_consumption_limits_response.get_status_code() == 200
        resource_consumption_limits_response = get_resource_consumption_limits_response.get_result()
        assert resource_consumption_limits_response is not None

    @needscredentials
    def test_replace_log_forwarding_config(self):

        replace_log_forwarding_config_response = self.ibm_analytics_engine_api_service.replace_log_forwarding_config(
            instance_id=self.instance_id,
            enabled=True,
            sources=['spark-driver', 'spark-executor'],
            tags=['<tag_1>', '<tag_2>', '<tag_n']
        )

        assert replace_log_forwarding_config_response.get_status_code() == 200
        log_forwarding_config_response = replace_log_forwarding_config_response.get_result()
        assert log_forwarding_config_response is not None

    @needscredentials
    def test_get_log_forwarding_config(self):

        get_log_forwarding_config_response = self.ibm_analytics_engine_api_service.get_log_forwarding_config(
            instance_id=self.instance_id
        )

        assert get_log_forwarding_config_response.get_status_code() == 200
        log_forwarding_config_response = get_log_forwarding_config_response.get_result()
        assert log_forwarding_config_response is not None

    @needscredentials
    def test_configure_platform_logging(self):

        configure_platform_logging_response = self.ibm_analytics_engine_api_service.configure_platform_logging(
            instance_guid=self.instance_id,
            enable=True
        )

        assert configure_platform_logging_response.get_status_code() == 201
        logging_configuration_response = configure_platform_logging_response.get_result()
        assert logging_configuration_response is not None

    @needscredentials
    def test_get_logging_configuration(self):

        get_logging_configuration_response = self.ibm_analytics_engine_api_service.get_logging_configuration(
            instance_guid=self.instance_id
        )

        assert get_logging_configuration_response.get_status_code() == 200
        logging_configuration_response = get_logging_configuration_response.get_result()
        assert logging_configuration_response is not None

    @needscredentials
    def test_delete_application(self):

        delete_application_response = self.ibm_analytics_engine_api_service.delete_application(
            instance_id=self.instance_id,
            application_id=application_id
        )

        assert delete_application_response.get_status_code() == 204
