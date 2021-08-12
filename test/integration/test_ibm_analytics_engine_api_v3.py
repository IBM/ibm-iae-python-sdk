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
Integration Tests for IbmAnalyticsEngineApiV3
"""

import os
import pytest
from ibm_cloud_sdk_core import *
from iaesdk.ibm_analytics_engine_api_v3 import *

# Config file name
config_file = 'ibmanalyticsengine-service.env'
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
            cls.instance_guid = os.getenv('IBM_ANALYTICS_ENGINE_INSTANCE_GUID')    
            assert cls.ibm_analytics_engine_api_service is not None

            cls.config = read_external_sources(
                IbmAnalyticsEngineApiV3.DEFAULT_SERVICE_NAME)
            assert cls.config is not None

        print('Setup complete.')

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file), reason="External configuration not available, skipping..."
    )

    @needscredentials
    def test_get_instance_by_id(self):
        print('Instance Id - ***********************')
        print(self.instance_guid)
        get_instance_by_id_response = self.ibm_analytics_engine_api_service.get_instance_by_id(self.instance_guid)

        assert get_instance_by_id_response.get_status_code() == 200
        instance_details = get_instance_by_id_response.get_result()
        assert instance_details is not None

    @needscredentials
    def test_create_application(self):
        global application_id 
        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {
            'application': '/opt/ibm/spark/examples/src/main/python/wordcount.py',
            'application_arguments': ['/opt/ibm/spark/examples/src/main/resources/people.txt']
        }

        create_application_response = self.ibm_analytics_engine_api_service.create_application(
            self.instance_guid,
            application_details=application_request_application_details_model
        )

        assert create_application_response.get_status_code() == 202
        application_response = create_application_response.get_result()
        print('Application Response - ***********************')
        print(application_response)
        
        application_id=application_response.get('application_id')
        print('Application Id - ***********************')
        print(application_id)
        assert application_response is not None

    @needscredentials
    def test_get_applications(self):

        get_applications_response = self.ibm_analytics_engine_api_service.get_applications(
            self.instance_guid
        )

        assert get_applications_response.get_status_code() == 200
        application_collection = get_applications_response.get_result()
        assert application_collection is not None

    @needscredentials
    def test_get_application_by_id(self):

        get_application_by_id_response = self.ibm_analytics_engine_api_service.get_application_by_id(
            self.instance_guid,
            application_id
        )

        assert get_application_by_id_response.get_status_code() == 200
        application_get_response = get_application_by_id_response.get_result()
        assert application_get_response is not None

    @needscredentials
    def test_get_application_state(self):

        get_application_state_response = self.ibm_analytics_engine_api_service.get_application_state(
            self.instance_guid,
            application_id
        )

        assert get_application_state_response.get_status_code() == 200
        application_get_state_response = get_application_state_response.get_result()
        assert application_get_state_response is not None

    @needscredentials
    def test_delete_application_by_id(self):

        delete_application_by_id_response = self.ibm_analytics_engine_api_service.delete_application_by_id(
            self.instance_guid,
            application_id
        )

        assert delete_application_by_id_response.get_status_code() == 204

