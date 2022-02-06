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

import os
import pytest
from ibm_cloud_sdk_core import *
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
            cls.instance_id = os.getenv('IBM_ANALYTICS_ENGINE_INSTANCE_GUID')  
            cls.instance_id_instance_home = os.getenv('IBM_ANALYTICS_ENGINE_INSTANCE_GUID_INSTANCE_HOME') 
            cls.hmacAccessKey = os.getenv('HMAC_ACCESS_KEY') 
            cls.hmacSecretKey = os.getenv('HMAC_SECRET_KEY')  
            assert cls.ibm_analytics_engine_api_service is not None

            cls.config = read_external_sources(
                IbmAnalyticsEngineApiV3.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

            cls.ibm_analytics_engine_api_service.enable_retries()

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_instance(self):

        get_instance_response = self.ibm_analytics_engine_api_service.get_instance(
            self.instance_id
        )

        assert get_instance_response.get_status_code() == 200
        instance = get_instance_response.get_result()
        assert instance is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_get_instance_state(self):
        get_instance_state_response = self.ibm_analytics_engine_api_service.get_instance_state(
            self.instance_id
        )

        assert get_instance_state_response.get_status_code() == 200
        instance_get_state_response = get_instance_state_response.get_result()
        assert instance_get_state_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_create_instance_home(self):

        create_instance_home_response = self.ibm_analytics_engine_api_service.create_instance_home(
            self.instance_id_instance_home,
            new_instance_id='testString',
            new_provider='ibm-cos',
            new_type='objectstore',
            new_region='us-south',
            new_endpoint='s3.direct.us-south.cloud-object-storage.appdomain.cloud',
            new_hmac_access_key=self.hmacAccessKey,
            new_hmac_secret_key=self.hmacSecretKey
        )

        assert create_instance_home_response.get_status_code() == 200
        instance_home_response = create_instance_home_response.get_result()
        assert instance_home_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_get_default_configs(self):

        get_default_configs_response = self.ibm_analytics_engine_api_service.get_default_configs(
            self.instance_id
        )

        assert get_default_configs_response.get_status_code() == 200

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_update_default_configs(self):

        update_default_configs_response = self.ibm_analytics_engine_api_service.update_default_configs(
            self.instance_id,
            body={"key1": "value1"}
        )

        assert update_default_configs_response.get_status_code() == 200

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_edit_default_configs(self):

        edit_default_configs_response = self.ibm_analytics_engine_api_service.edit_default_configs(
            self.instance_id,
            body={"key2": "value2"}
        )

        assert edit_default_configs_response.get_status_code() == 200

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_create_application(self):
        global application_id

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {
            'application': '/opt/ibm/spark/examples/src/main/python/wordcount.py',
            'arguments': ['/opt/ibm/spark/examples/src/main/resources/people.txt'],
        }

        create_application_response = self.ibm_analytics_engine_api_service.create_application(
            self.instance_id,
            application_details=application_request_application_details_model
        )

        assert create_application_response.get_status_code() == 202
        application_response = create_application_response.get_result()
        application_id=application_response.get('id')
        assert application_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_list_applications(self):

        list_applications_response = self.ibm_analytics_engine_api_service.list_applications(
            self.instance_id
        )

        assert list_applications_response.get_status_code() == 200
        application_collection = list_applications_response.get_result()
        assert application_collection is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_get_application(self):

        get_application_response = self.ibm_analytics_engine_api_service.get_application(
            self.instance_id,
            application_id
        )

        assert get_application_response.get_status_code() == 200
        application_get_response = get_application_response.get_result()
        assert application_get_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_get_application_state(self):

        get_application_state_response = self.ibm_analytics_engine_api_service.get_application_state(
            self.instance_id,
            application_id
        )

        assert get_application_state_response.get_status_code() == 200
        application_get_state_response = get_application_state_response.get_result()
        assert application_get_state_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_enable_platform_logging(self):

        enable_platform_logging_response = self.ibm_analytics_engine_api_service.enable_platform_logging(
            self.instance_id,
            enable=True
        )

        assert enable_platform_logging_response.get_status_code() == 201
        logging_configuration_response = enable_platform_logging_response.get_result()
        assert logging_configuration_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_disable_platform_logging(self):

        disable_platform_logging_response = self.ibm_analytics_engine_api_service.disable_platform_logging(
            self.instance_id,
            enable=False
        )

        assert disable_platform_logging_response.get_status_code() == 200
        logging_configuration_response = disable_platform_logging_response.get_result()
        assert logging_configuration_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_get_logging_configuration(self):

        get_logging_configuration_response = self.ibm_analytics_engine_api_service.get_logging_configuration(
            self.instance_id
        )

        assert get_logging_configuration_response.get_status_code() == 200
        logging_configuration_response = get_logging_configuration_response.get_result()
        assert logging_configuration_response is not None

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_delete_logging_configuration(self):

        delete_logging_configuration_response = self.ibm_analytics_engine_api_service.delete_logging_configuration(
            self.instance_id
        )

        assert delete_logging_configuration_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

    @needscredentials
    def test_delete_application(self):

        delete_application_response = self.ibm_analytics_engine_api_service.delete_application(
            self.instance_id,
            application_id
        )

        assert delete_application_response.get_status_code() == 204

        #
        # The following status codes aren't covered by tests.
        # Please provide integration tests for these too.
        #
        # 400
        # 401
        # 403
        # 404
        # 500
        #

