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
class TestIbmAnalyticsEngineApiV3Examples():
    """
    Example Test Class for IbmAnalyticsEngineApiV3
    """

    @classmethod
    def setup_class(cls):
        global ibm_analytics_engine_api_service
        if os.path.exists(config_file):
            os.environ['IBM_CREDENTIALS_FILE'] = config_file

            # begin-common

            ibm_analytics_engine_api_service = IbmAnalyticsEngineApiV3.new_instance(
            )

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

            instance = ibm_analytics_engine_api_service.get_instance(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09'
            ).get_result()

            print(json.dumps(instance, indent=2))

            # end-get_instance

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

            application_request_application_details_model = {
                'application': '/opt/ibm/spark/examples/src/main/python/wordcount.py',
                'arguments': ['/opt/ibm/spark/examples/src/main/resources/people.txt']
            }

            application_response = ibm_analytics_engine_api_service.create_application(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                application_details = application_request_application_details_model,
            ).get_result()

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

            application_collection = ibm_analytics_engine_api_service.list_applications(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09'
            ).get_result()

            print(json.dumps(application_collection, indent=2))

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

            application_get_response = ibm_analytics_engine_api_service.get_application(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                application_id='ff48cc19-0e7e-4627-aac6-0b4ad080397b'
            ).get_result()

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

            application_get_state_response = ibm_analytics_engine_api_service.get_application_state(
                instance_id='e64c907a-e82f-46fd-addc-ccfafbd28b09',
                application_id='ff48cc19-0e7e-4627-aac6-0b4ad080397b'
            ).get_result()

            print(json.dumps(application_get_state_response, indent=2))

            # end-get_application_state

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
                application_id='ff48cc19-0e7e-4627-aac6-0b4ad080397b'
            )

            # end-delete_application
            print('\ndelete_application() response status code: ', response.get_status_code())

        except ApiException as e:
            pytest.fail(str(e))

# endregion
##############################################################################
# End of Examples for Service: IbmAnalyticsEngineApiV3
##############################################################################
