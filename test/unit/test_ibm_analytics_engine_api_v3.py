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
Unit Tests for IbmAnalyticsEngineApiV3
"""

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
from ibm_cloud_sdk_core.utils import datetime_to_string, string_to_datetime
import inspect
import json
import os
import pytest
import re
import responses
import urllib
from iaesdk.ibm_analytics_engine_api_v3 import *


_service = IbmAnalyticsEngineApiV3(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://api.us-south.ae.cloud.ibm.com'
_service.set_service_url(_base_url)


def preprocess_url(operation_path: str):
    """
    Returns the request url associated with the specified operation path.
    This will be base_url concatenated with a quoted version of operation_path.
    The returned request URL is used to register the mock response so it needs
    to match the request URL that is formed by the requests library.
    """
    # First, unquote the path since it might have some quoted/escaped characters in it
    # due to how the generator inserts the operation paths into the unit test code.
    operation_path = urllib.parse.unquote(operation_path)

    # Next, quote the path using urllib so that we approximate what will
    # happen during request processing.
    operation_path = urllib.parse.quote(operation_path, safe='/')

    # Finally, form the request URL from the base URL and operation path.
    request_url = _base_url + operation_path

    # If the request url does NOT end with a /, then just return it as-is.
    # Otherwise, return a regular expression that matches one or more trailing /.
    if re.fullmatch('.*/+', request_url) is None:
        return request_url
    else:
        return re.compile(request_url.rstrip('/') + '/+')


def test_get_service_url_for_region():
    """
    get_service_url_for_region()
    """
    assert IbmAnalyticsEngineApiV3.get_service_url_for_region('INVALID_REGION') is None
    assert IbmAnalyticsEngineApiV3.get_service_url_for_region('us-south') == 'https://api.us-south.ae.cloud.ibm.com'
    assert IbmAnalyticsEngineApiV3.get_service_url_for_region('eu-de') == 'https://api.eu-de.ae.cloud.ibm.com'


##############################################################################
# Start of Service: AnalyticsEnginesV3
##############################################################################
# region

class TestNewInstance():
    """
    Test Class for new_instance
    """

    def test_new_instance(self):
        """
        new_instance()
        """
        os.environ['TEST_SERVICE_AUTH_TYPE'] = 'noAuth'

        service = IbmAnalyticsEngineApiV3.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IbmAnalyticsEngineApiV3)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IbmAnalyticsEngineApiV3.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetInstance():
    """
    Test Class for get_instance
    """

    @responses.activate
    def test_get_instance_all_params(self):
        """
        get_instance()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09')
        mock_response = '{"id": "id", "href": "href", "state": "created", "state_change_time": "2021-01-30T08:30:00.000Z", "default_runtime": {"spark_version": "spark_version"}, "instance_home": {"id": "id", "provider": "provider", "type": "type", "region": "region", "endpoint": "endpoint", "bucket": "bucket", "hmac_access_key": "hmac_access_key", "hmac_secret_key": "hmac_secret_key"}, "default_config": {"key": "key"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Invoke method
        response = _service.get_instance(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_all_params_with_retries(self):
        # Enable retries and run test_get_instance_all_params.
        _service.enable_retries()
        self.test_get_instance_all_params()

        # Disable retries and run test_get_instance_all_params.
        _service.disable_retries()
        self.test_get_instance_all_params()

    @responses.activate
    def test_get_instance_value_error(self):
        """
        test_get_instance_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09')
        mock_response = '{"id": "id", "href": "href", "state": "created", "state_change_time": "2021-01-30T08:30:00.000Z", "default_runtime": {"spark_version": "spark_version"}, "instance_home": {"id": "id", "provider": "provider", "type": "type", "region": "region", "endpoint": "endpoint", "bucket": "bucket", "hmac_access_key": "hmac_access_key", "hmac_secret_key": "hmac_secret_key"}, "default_config": {"key": "key"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance(**req_copy)


    def test_get_instance_value_error_with_retries(self):
        # Enable retries and run test_get_instance_value_error.
        _service.enable_retries()
        self.test_get_instance_value_error()

        # Disable retries and run test_get_instance_value_error.
        _service.disable_retries()
        self.test_get_instance_value_error()

class TestGetInstanceState():
    """
    Test Class for get_instance_state
    """

    @responses.activate
    def test_get_instance_state_all_params(self):
        """
        get_instance_state()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/state')
        mock_response = '{"id": "id", "state": "created"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Invoke method
        response = _service.get_instance_state(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_instance_state_all_params_with_retries(self):
        # Enable retries and run test_get_instance_state_all_params.
        _service.enable_retries()
        self.test_get_instance_state_all_params()

        # Disable retries and run test_get_instance_state_all_params.
        _service.disable_retries()
        self.test_get_instance_state_all_params()

    @responses.activate
    def test_get_instance_state_value_error(self):
        """
        test_get_instance_state_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/state')
        mock_response = '{"id": "id", "state": "created"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_state(**req_copy)


    def test_get_instance_state_value_error_with_retries(self):
        # Enable retries and run test_get_instance_state_value_error.
        _service.enable_retries()
        self.test_get_instance_state_value_error()

        # Disable retries and run test_get_instance_state_value_error.
        _service.disable_retries()
        self.test_get_instance_state_value_error()

class TestCreateInstanceHome():
    """
    Test Class for create_instance_home
    """

    @responses.activate
    def test_create_instance_home_all_params(self):
        """
        create_instance_home()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/instance_home')
        mock_response = '{"instance_id": "instance_id", "provider": "provider", "type": "type", "region": "region", "endpoint": "endpoint", "hmac_access_key": "hmac_access_key", "hmac_secret_key": "hmac_secret_key"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        new_instance_id = 'testString'
        new_provider = 'ibm-cos'
        new_type = 'objectstore'
        new_region = 'us-south'
        new_endpoint = 's3.direct.us-south.cloud-object-storage.appdomain.cloud'
        new_hmac_access_key = '821**********0ae'
        new_hmac_secret_key = '03e****************4fc3'

        # Invoke method
        response = _service.create_instance_home(
            instance_id,
            new_instance_id=new_instance_id,
            new_provider=new_provider,
            new_type=new_type,
            new_region=new_region,
            new_endpoint=new_endpoint,
            new_hmac_access_key=new_hmac_access_key,
            new_hmac_secret_key=new_hmac_secret_key,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['instance_id'] == 'testString'
        assert req_body['provider'] == 'ibm-cos'
        assert req_body['type'] == 'objectstore'
        assert req_body['region'] == 'us-south'
        assert req_body['endpoint'] == 's3.direct.us-south.cloud-object-storage.appdomain.cloud'
        assert req_body['hmac_access_key'] == '821**********0ae'
        assert req_body['hmac_secret_key'] == '03e****************4fc3'

    def test_create_instance_home_all_params_with_retries(self):
        # Enable retries and run test_create_instance_home_all_params.
        _service.enable_retries()
        self.test_create_instance_home_all_params()

        # Disable retries and run test_create_instance_home_all_params.
        _service.disable_retries()
        self.test_create_instance_home_all_params()

    @responses.activate
    def test_create_instance_home_value_error(self):
        """
        test_create_instance_home_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/instance_home')
        mock_response = '{"instance_id": "instance_id", "provider": "provider", "type": "type", "region": "region", "endpoint": "endpoint", "hmac_access_key": "hmac_access_key", "hmac_secret_key": "hmac_secret_key"}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        new_instance_id = 'testString'
        new_provider = 'ibm-cos'
        new_type = 'objectstore'
        new_region = 'us-south'
        new_endpoint = 's3.direct.us-south.cloud-object-storage.appdomain.cloud'
        new_hmac_access_key = '821**********0ae'
        new_hmac_secret_key = '03e****************4fc3'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_instance_home(**req_copy)


    def test_create_instance_home_value_error_with_retries(self):
        # Enable retries and run test_create_instance_home_value_error.
        _service.enable_retries()
        self.test_create_instance_home_value_error()

        # Disable retries and run test_create_instance_home_value_error.
        _service.disable_retries()
        self.test_create_instance_home_value_error()

class TestCreateApplication():
    """
    Test Class for create_application
    """

    @responses.activate
    def test_create_application_all_params(self):
        """
        create_application()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications')
        mock_response = '{"id": "id", "state": "accepted"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {}
        application_request_application_details_model['application'] = 'cos://bucket_name.my_cos/my_spark_app.py'
        application_request_application_details_model['jars'] = 'cos://cloud-object-storage/jars/tests.jar'
        application_request_application_details_model['packages'] = 'testString'
        application_request_application_details_model['repositories'] = 'testString'
        application_request_application_details_model['files'] = 'testString'
        application_request_application_details_model['archives'] = 'testString'
        application_request_application_details_model['name'] = 'spark-app'
        application_request_application_details_model['class'] = 'com.company.path.ClassName'
        application_request_application_details_model['arguments'] = ['[arg1, arg2, arg3]']
        application_request_application_details_model['conf'] = {}
        application_request_application_details_model['env'] = {}

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        application_details = application_request_application_details_model

        # Invoke method
        response = _service.create_application(
            instance_id,
            application_details=application_details,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['application_details'] == application_request_application_details_model

    def test_create_application_all_params_with_retries(self):
        # Enable retries and run test_create_application_all_params.
        _service.enable_retries()
        self.test_create_application_all_params()

        # Disable retries and run test_create_application_all_params.
        _service.disable_retries()
        self.test_create_application_all_params()

    @responses.activate
    def test_create_application_value_error(self):
        """
        test_create_application_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications')
        mock_response = '{"id": "id", "state": "accepted"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {}
        application_request_application_details_model['application'] = 'cos://bucket_name.my_cos/my_spark_app.py'
        application_request_application_details_model['jars'] = 'cos://cloud-object-storage/jars/tests.jar'
        application_request_application_details_model['packages'] = 'testString'
        application_request_application_details_model['repositories'] = 'testString'
        application_request_application_details_model['files'] = 'testString'
        application_request_application_details_model['archives'] = 'testString'
        application_request_application_details_model['name'] = 'spark-app'
        application_request_application_details_model['class'] = 'com.company.path.ClassName'
        application_request_application_details_model['arguments'] = ['[arg1, arg2, arg3]']
        application_request_application_details_model['conf'] = {}
        application_request_application_details_model['env'] = {}

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        application_details = application_request_application_details_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_application(**req_copy)


    def test_create_application_value_error_with_retries(self):
        # Enable retries and run test_create_application_value_error.
        _service.enable_retries()
        self.test_create_application_value_error()

        # Disable retries and run test_create_application_value_error.
        _service.disable_retries()
        self.test_create_application_value_error()

class TestListApplications():
    """
    Test Class for list_applications
    """

    @responses.activate
    def test_list_applications_all_params(self):
        """
        list_applications()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications')
        mock_response = '{"applications": [{"id": "id", "href": "href", "spark_application_id": "spark_application_id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Invoke method
        response = _service.list_applications(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_list_applications_all_params_with_retries(self):
        # Enable retries and run test_list_applications_all_params.
        _service.enable_retries()
        self.test_list_applications_all_params()

        # Disable retries and run test_list_applications_all_params.
        _service.disable_retries()
        self.test_list_applications_all_params()

    @responses.activate
    def test_list_applications_value_error(self):
        """
        test_list_applications_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications')
        mock_response = '{"applications": [{"id": "id", "href": "href", "spark_application_id": "spark_application_id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.list_applications(**req_copy)


    def test_list_applications_value_error_with_retries(self):
        # Enable retries and run test_list_applications_value_error.
        _service.enable_retries()
        self.test_list_applications_value_error()

        # Disable retries and run test_list_applications_value_error.
        _service.disable_retries()
        self.test_list_applications_value_error()

class TestGetApplication():
    """
    Test Class for get_application
    """

    @responses.activate
    def test_get_application_all_params(self):
        """
        get_application()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b')
        mock_response = '{"application_details": {"application": "cos://bucket_name.my_cos/my_spark_app.py", "jars": "cos://cloud-object-storage/jars/tests.jar", "packages": "packages", "repositories": "repositories", "files": "files", "archives": "archives", "name": "spark-app", "class": "com.company.path.ClassName", "arguments": ["[arg1, arg2, arg3]"], "conf": {"mapKey": "anyValue"}, "env": {"mapKey": "anyValue"}}, "id": "2b83d31c-397b-48ad-ad76-b83347c982db", "state": "accepted", "start_time": "2021-01-30T08:30:00.000Z", "finish_time": "2021-01-30T08:30:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        application_id = 'ff48cc19-0e7e-4627-aac6-0b4ad080397b'

        # Invoke method
        response = _service.get_application(
            instance_id,
            application_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_application_all_params_with_retries(self):
        # Enable retries and run test_get_application_all_params.
        _service.enable_retries()
        self.test_get_application_all_params()

        # Disable retries and run test_get_application_all_params.
        _service.disable_retries()
        self.test_get_application_all_params()

    @responses.activate
    def test_get_application_value_error(self):
        """
        test_get_application_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b')
        mock_response = '{"application_details": {"application": "cos://bucket_name.my_cos/my_spark_app.py", "jars": "cos://cloud-object-storage/jars/tests.jar", "packages": "packages", "repositories": "repositories", "files": "files", "archives": "archives", "name": "spark-app", "class": "com.company.path.ClassName", "arguments": ["[arg1, arg2, arg3]"], "conf": {"mapKey": "anyValue"}, "env": {"mapKey": "anyValue"}}, "id": "2b83d31c-397b-48ad-ad76-b83347c982db", "state": "accepted", "start_time": "2021-01-30T08:30:00.000Z", "finish_time": "2021-01-30T08:30:00.000Z"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        application_id = 'ff48cc19-0e7e-4627-aac6-0b4ad080397b'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "application_id": application_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_application(**req_copy)


    def test_get_application_value_error_with_retries(self):
        # Enable retries and run test_get_application_value_error.
        _service.enable_retries()
        self.test_get_application_value_error()

        # Disable retries and run test_get_application_value_error.
        _service.disable_retries()
        self.test_get_application_value_error()

class TestDeleteApplication():
    """
    Test Class for delete_application
    """

    @responses.activate
    def test_delete_application_all_params(self):
        """
        delete_application()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        application_id = 'ff48cc19-0e7e-4627-aac6-0b4ad080397b'

        # Invoke method
        response = _service.delete_application(
            instance_id,
            application_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_application_all_params_with_retries(self):
        # Enable retries and run test_delete_application_all_params.
        _service.enable_retries()
        self.test_delete_application_all_params()

        # Disable retries and run test_delete_application_all_params.
        _service.disable_retries()
        self.test_delete_application_all_params()

    @responses.activate
    def test_delete_application_value_error(self):
        """
        test_delete_application_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        application_id = 'ff48cc19-0e7e-4627-aac6-0b4ad080397b'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "application_id": application_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_application(**req_copy)


    def test_delete_application_value_error_with_retries(self):
        # Enable retries and run test_delete_application_value_error.
        _service.enable_retries()
        self.test_delete_application_value_error()

        # Disable retries and run test_delete_application_value_error.
        _service.disable_retries()
        self.test_delete_application_value_error()

class TestGetApplicationState():
    """
    Test Class for get_application_state
    """

    @responses.activate
    def test_get_application_state_all_params(self):
        """
        get_application_state()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b/state')
        mock_response = '{"id": "id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        application_id = 'ff48cc19-0e7e-4627-aac6-0b4ad080397b'

        # Invoke method
        response = _service.get_application_state(
            instance_id,
            application_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_application_state_all_params_with_retries(self):
        # Enable retries and run test_get_application_state_all_params.
        _service.enable_retries()
        self.test_get_application_state_all_params()

        # Disable retries and run test_get_application_state_all_params.
        _service.disable_retries()
        self.test_get_application_state_all_params()

    @responses.activate
    def test_get_application_state_value_error(self):
        """
        test_get_application_state_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b/state')
        mock_response = '{"id": "id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        application_id = 'ff48cc19-0e7e-4627-aac6-0b4ad080397b'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "application_id": application_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_application_state(**req_copy)


    def test_get_application_state_value_error_with_retries(self):
        # Enable retries and run test_get_application_state_value_error.
        _service.enable_retries()
        self.test_get_application_state_value_error()

        # Disable retries and run test_get_application_state_value_error.
        _service.disable_retries()
        self.test_get_application_state_value_error()

class TestConfigurePlatformLogging():
    """
    Test Class for configure_platform_logging
    """

    @responses.activate
    def test_configure_platform_logging_all_params(self):
        """
        configure_platform_logging()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/logging')
        mock_response = '{"components": ["components"], "log_server": {"type": "ibm-log-analysis"}, "enable": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        instance_guid = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        enable = True

        # Invoke method
        response = _service.configure_platform_logging(
            instance_guid,
            enable=enable,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['enable'] == True

    def test_configure_platform_logging_all_params_with_retries(self):
        # Enable retries and run test_configure_platform_logging_all_params.
        _service.enable_retries()
        self.test_configure_platform_logging_all_params()

        # Disable retries and run test_configure_platform_logging_all_params.
        _service.disable_retries()
        self.test_configure_platform_logging_all_params()

    @responses.activate
    def test_configure_platform_logging_value_error(self):
        """
        test_configure_platform_logging_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/logging')
        mock_response = '{"components": ["components"], "log_server": {"type": "ibm-log-analysis"}, "enable": true}'
        responses.add(responses.PUT,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Set up parameter values
        instance_guid = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'
        enable = True

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.configure_platform_logging(**req_copy)


    def test_configure_platform_logging_value_error_with_retries(self):
        # Enable retries and run test_configure_platform_logging_value_error.
        _service.enable_retries()
        self.test_configure_platform_logging_value_error()

        # Disable retries and run test_configure_platform_logging_value_error.
        _service.disable_retries()
        self.test_configure_platform_logging_value_error()

class TestGetLoggingConfiguration():
    """
    Test Class for get_logging_configuration
    """

    @responses.activate
    def test_get_logging_configuration_all_params(self):
        """
        get_logging_configuration()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/logging')
        mock_response = '{"components": ["components"], "log_server": {"type": "ibm-log-analysis"}, "enable": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Invoke method
        response = _service.get_logging_configuration(
            instance_guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_logging_configuration_all_params_with_retries(self):
        # Enable retries and run test_get_logging_configuration_all_params.
        _service.enable_retries()
        self.test_get_logging_configuration_all_params()

        # Disable retries and run test_get_logging_configuration_all_params.
        _service.disable_retries()
        self.test_get_logging_configuration_all_params()

    @responses.activate
    def test_get_logging_configuration_value_error(self):
        """
        test_get_logging_configuration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/logging')
        mock_response = '{"components": ["components"], "log_server": {"type": "ibm-log-analysis"}, "enable": true}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_logging_configuration(**req_copy)


    def test_get_logging_configuration_value_error_with_retries(self):
        # Enable retries and run test_get_logging_configuration_value_error.
        _service.enable_retries()
        self.test_get_logging_configuration_value_error()

        # Disable retries and run test_get_logging_configuration_value_error.
        _service.disable_retries()
        self.test_get_logging_configuration_value_error()

class TestDeleteLoggingConfiguration():
    """
    Test Class for delete_logging_configuration
    """

    @responses.activate
    def test_delete_logging_configuration_all_params(self):
        """
        delete_logging_configuration()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/logging')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_guid = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Invoke method
        response = _service.delete_logging_configuration(
            instance_guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_delete_logging_configuration_all_params_with_retries(self):
        # Enable retries and run test_delete_logging_configuration_all_params.
        _service.enable_retries()
        self.test_delete_logging_configuration_all_params()

        # Disable retries and run test_delete_logging_configuration_all_params.
        _service.disable_retries()
        self.test_delete_logging_configuration_all_params()

    @responses.activate
    def test_delete_logging_configuration_value_error(self):
        """
        test_delete_logging_configuration_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/logging')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_guid = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_logging_configuration(**req_copy)


    def test_delete_logging_configuration_value_error_with_retries(self):
        # Enable retries and run test_delete_logging_configuration_value_error.
        _service.enable_retries()
        self.test_delete_logging_configuration_value_error()

        # Disable retries and run test_delete_logging_configuration_value_error.
        _service.disable_retries()
        self.test_delete_logging_configuration_value_error()

class TestStartSparkHistoryServer():
    """
    Test Class for start_spark_history_server
    """

    @responses.activate
    def test_start_spark_history_server_all_params(self):
        """
        start_spark_history_server()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_history_server')
        mock_response = '{"state": "state", "cores": "cores", "memory": "memory", "start_time": "start_time"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Invoke method
        response = _service.start_spark_history_server(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_start_spark_history_server_all_params_with_retries(self):
        # Enable retries and run test_start_spark_history_server_all_params.
        _service.enable_retries()
        self.test_start_spark_history_server_all_params()

        # Disable retries and run test_start_spark_history_server_all_params.
        _service.disable_retries()
        self.test_start_spark_history_server_all_params()

    @responses.activate
    def test_start_spark_history_server_value_error(self):
        """
        test_start_spark_history_server_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_history_server')
        mock_response = '{"state": "state", "cores": "cores", "memory": "memory", "start_time": "start_time"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.start_spark_history_server(**req_copy)


    def test_start_spark_history_server_value_error_with_retries(self):
        # Enable retries and run test_start_spark_history_server_value_error.
        _service.enable_retries()
        self.test_start_spark_history_server_value_error()

        # Disable retries and run test_start_spark_history_server_value_error.
        _service.disable_retries()
        self.test_start_spark_history_server_value_error()

class TestGetSparkHistoryServer():
    """
    Test Class for get_spark_history_server
    """

    @responses.activate
    def test_get_spark_history_server_all_params(self):
        """
        get_spark_history_server()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_history_server')
        mock_response = '{"state": "state", "cores": "cores", "memory": "memory", "start_time": "start_time", "stop_time": "stop_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Invoke method
        response = _service.get_spark_history_server(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_spark_history_server_all_params_with_retries(self):
        # Enable retries and run test_get_spark_history_server_all_params.
        _service.enable_retries()
        self.test_get_spark_history_server_all_params()

        # Disable retries and run test_get_spark_history_server_all_params.
        _service.disable_retries()
        self.test_get_spark_history_server_all_params()

    @responses.activate
    def test_get_spark_history_server_value_error(self):
        """
        test_get_spark_history_server_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_history_server')
        mock_response = '{"state": "state", "cores": "cores", "memory": "memory", "start_time": "start_time", "stop_time": "stop_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_spark_history_server(**req_copy)


    def test_get_spark_history_server_value_error_with_retries(self):
        # Enable retries and run test_get_spark_history_server_value_error.
        _service.enable_retries()
        self.test_get_spark_history_server_value_error()

        # Disable retries and run test_get_spark_history_server_value_error.
        _service.disable_retries()
        self.test_get_spark_history_server_value_error()

class TestStopSparkHistoryServer():
    """
    Test Class for stop_spark_history_server
    """

    @responses.activate
    def test_stop_spark_history_server_all_params(self):
        """
        stop_spark_history_server()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_history_server')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Invoke method
        response = _service.stop_spark_history_server(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204

    def test_stop_spark_history_server_all_params_with_retries(self):
        # Enable retries and run test_stop_spark_history_server_all_params.
        _service.enable_retries()
        self.test_stop_spark_history_server_all_params()

        # Disable retries and run test_stop_spark_history_server_all_params.
        _service.disable_retries()
        self.test_stop_spark_history_server_all_params()

    @responses.activate
    def test_stop_spark_history_server_value_error(self):
        """
        test_stop_spark_history_server_value_error()
        """
        # Set up mock
        url = preprocess_url('/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_history_server')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'e64c907a-e82f-46fd-addc-ccfafbd28b09'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.stop_spark_history_server(**req_copy)


    def test_stop_spark_history_server_value_error_with_retries(self):
        # Enable retries and run test_stop_spark_history_server_value_error.
        _service.enable_retries()
        self.test_stop_spark_history_server_value_error()

        # Disable retries and run test_stop_spark_history_server_value_error.
        _service.disable_retries()
        self.test_stop_spark_history_server_value_error()

# endregion
##############################################################################
# End of Service: AnalyticsEnginesV3
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_Application():
    """
    Test Class for Application
    """

    def test_application_serialization(self):
        """
        Test serialization/deserialization for Application
        """

        # Construct a json representation of a Application model
        application_model_json = {}
        application_model_json['id'] = 'testString'
        application_model_json['href'] = 'testString'
        application_model_json['spark_application_id'] = 'testString'
        application_model_json['state'] = 'testString'
        application_model_json['start_time'] = 'testString'
        application_model_json['finish_time'] = 'testString'

        # Construct a model instance of Application by calling from_dict on the json representation
        application_model = Application.from_dict(application_model_json)
        assert application_model != False

        # Construct a model instance of Application by calling from_dict on the json representation
        application_model_dict = Application.from_dict(application_model_json).__dict__
        application_model2 = Application(**application_model_dict)

        # Verify the model instances are equivalent
        assert application_model == application_model2

        # Convert model instance back to dict and verify no loss of data
        application_model_json2 = application_model.to_dict()
        assert application_model_json2 == application_model_json

class TestModel_ApplicationCollection():
    """
    Test Class for ApplicationCollection
    """

    def test_application_collection_serialization(self):
        """
        Test serialization/deserialization for ApplicationCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        application_model = {} # Application
        application_model['id'] = 'testString'
        application_model['href'] = 'testString'
        application_model['spark_application_id'] = 'testString'
        application_model['state'] = 'testString'
        application_model['start_time'] = 'testString'
        application_model['finish_time'] = 'testString'

        # Construct a json representation of a ApplicationCollection model
        application_collection_model_json = {}
        application_collection_model_json['applications'] = [application_model]

        # Construct a model instance of ApplicationCollection by calling from_dict on the json representation
        application_collection_model = ApplicationCollection.from_dict(application_collection_model_json)
        assert application_collection_model != False

        # Construct a model instance of ApplicationCollection by calling from_dict on the json representation
        application_collection_model_dict = ApplicationCollection.from_dict(application_collection_model_json).__dict__
        application_collection_model2 = ApplicationCollection(**application_collection_model_dict)

        # Verify the model instances are equivalent
        assert application_collection_model == application_collection_model2

        # Convert model instance back to dict and verify no loss of data
        application_collection_model_json2 = application_collection_model.to_dict()
        assert application_collection_model_json2 == application_collection_model_json

class TestModel_ApplicationDetails():
    """
    Test Class for ApplicationDetails
    """

    def test_application_details_serialization(self):
        """
        Test serialization/deserialization for ApplicationDetails
        """

        # Construct a json representation of a ApplicationDetails model
        application_details_model_json = {}
        application_details_model_json['application'] = 'cos://bucket_name.my_cos/my_spark_app.py'
        application_details_model_json['jars'] = 'cos://cloud-object-storage/jars/tests.jar'
        application_details_model_json['packages'] = 'testString'
        application_details_model_json['repositories'] = 'testString'
        application_details_model_json['files'] = 'testString'
        application_details_model_json['archives'] = 'testString'
        application_details_model_json['name'] = 'spark-app'
        application_details_model_json['class'] = 'com.company.path.ClassName'
        application_details_model_json['arguments'] = ['[arg1, arg2, arg3]']
        application_details_model_json['conf'] = {}
        application_details_model_json['env'] = {}

        # Construct a model instance of ApplicationDetails by calling from_dict on the json representation
        application_details_model = ApplicationDetails.from_dict(application_details_model_json)
        assert application_details_model != False

        # Construct a model instance of ApplicationDetails by calling from_dict on the json representation
        application_details_model_dict = ApplicationDetails.from_dict(application_details_model_json).__dict__
        application_details_model2 = ApplicationDetails(**application_details_model_dict)

        # Verify the model instances are equivalent
        assert application_details_model == application_details_model2

        # Convert model instance back to dict and verify no loss of data
        application_details_model_json2 = application_details_model.to_dict()
        assert application_details_model_json2 == application_details_model_json

class TestModel_ApplicationGetResponse():
    """
    Test Class for ApplicationGetResponse
    """

    def test_application_get_response_serialization(self):
        """
        Test serialization/deserialization for ApplicationGetResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        application_details_model = {} # ApplicationDetails
        application_details_model['application'] = 'cos://bucket_name.my_cos/my_spark_app.py'
        application_details_model['jars'] = 'cos://cloud-object-storage/jars/tests.jar'
        application_details_model['packages'] = 'testString'
        application_details_model['repositories'] = 'testString'
        application_details_model['files'] = 'testString'
        application_details_model['archives'] = 'testString'
        application_details_model['name'] = 'spark-app'
        application_details_model['class'] = 'com.company.path.ClassName'
        application_details_model['arguments'] = ['[arg1, arg2, arg3]']
        application_details_model['conf'] = {}
        application_details_model['env'] = {}

        # Construct a json representation of a ApplicationGetResponse model
        application_get_response_model_json = {}
        application_get_response_model_json['application_details'] = application_details_model
        application_get_response_model_json['id'] = '2b83d31c-397b-48ad-ad76-b83347c982db'
        application_get_response_model_json['state'] = 'accepted'
        application_get_response_model_json['start_time'] = '2021-01-30T08:30:00Z'
        application_get_response_model_json['finish_time'] = '2021-01-30T08:30:00Z'

        # Construct a model instance of ApplicationGetResponse by calling from_dict on the json representation
        application_get_response_model = ApplicationGetResponse.from_dict(application_get_response_model_json)
        assert application_get_response_model != False

        # Construct a model instance of ApplicationGetResponse by calling from_dict on the json representation
        application_get_response_model_dict = ApplicationGetResponse.from_dict(application_get_response_model_json).__dict__
        application_get_response_model2 = ApplicationGetResponse(**application_get_response_model_dict)

        # Verify the model instances are equivalent
        assert application_get_response_model == application_get_response_model2

        # Convert model instance back to dict and verify no loss of data
        application_get_response_model_json2 = application_get_response_model.to_dict()
        assert application_get_response_model_json2 == application_get_response_model_json

class TestModel_ApplicationGetStateResponse():
    """
    Test Class for ApplicationGetStateResponse
    """

    def test_application_get_state_response_serialization(self):
        """
        Test serialization/deserialization for ApplicationGetStateResponse
        """

        # Construct a json representation of a ApplicationGetStateResponse model
        application_get_state_response_model_json = {}
        application_get_state_response_model_json['id'] = 'testString'
        application_get_state_response_model_json['state'] = 'testString'
        application_get_state_response_model_json['start_time'] = 'testString'
        application_get_state_response_model_json['finish_time'] = 'testString'

        # Construct a model instance of ApplicationGetStateResponse by calling from_dict on the json representation
        application_get_state_response_model = ApplicationGetStateResponse.from_dict(application_get_state_response_model_json)
        assert application_get_state_response_model != False

        # Construct a model instance of ApplicationGetStateResponse by calling from_dict on the json representation
        application_get_state_response_model_dict = ApplicationGetStateResponse.from_dict(application_get_state_response_model_json).__dict__
        application_get_state_response_model2 = ApplicationGetStateResponse(**application_get_state_response_model_dict)

        # Verify the model instances are equivalent
        assert application_get_state_response_model == application_get_state_response_model2

        # Convert model instance back to dict and verify no loss of data
        application_get_state_response_model_json2 = application_get_state_response_model.to_dict()
        assert application_get_state_response_model_json2 == application_get_state_response_model_json

class TestModel_ApplicationRequestApplicationDetails():
    """
    Test Class for ApplicationRequestApplicationDetails
    """

    def test_application_request_application_details_serialization(self):
        """
        Test serialization/deserialization for ApplicationRequestApplicationDetails
        """

        # Construct a json representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model_json = {}
        application_request_application_details_model_json['application'] = 'cos://bucket_name.my_cos/my_spark_app.py'
        application_request_application_details_model_json['jars'] = 'cos://cloud-object-storage/jars/tests.jar'
        application_request_application_details_model_json['packages'] = 'testString'
        application_request_application_details_model_json['repositories'] = 'testString'
        application_request_application_details_model_json['files'] = 'testString'
        application_request_application_details_model_json['archives'] = 'testString'
        application_request_application_details_model_json['name'] = 'spark-app'
        application_request_application_details_model_json['class'] = 'com.company.path.ClassName'
        application_request_application_details_model_json['arguments'] = ['[arg1, arg2, arg3]']
        application_request_application_details_model_json['conf'] = {}
        application_request_application_details_model_json['env'] = {}

        # Construct a model instance of ApplicationRequestApplicationDetails by calling from_dict on the json representation
        application_request_application_details_model = ApplicationRequestApplicationDetails.from_dict(application_request_application_details_model_json)
        assert application_request_application_details_model != False

        # Construct a model instance of ApplicationRequestApplicationDetails by calling from_dict on the json representation
        application_request_application_details_model_dict = ApplicationRequestApplicationDetails.from_dict(application_request_application_details_model_json).__dict__
        application_request_application_details_model2 = ApplicationRequestApplicationDetails(**application_request_application_details_model_dict)

        # Verify the model instances are equivalent
        assert application_request_application_details_model == application_request_application_details_model2

        # Convert model instance back to dict and verify no loss of data
        application_request_application_details_model_json2 = application_request_application_details_model.to_dict()
        assert application_request_application_details_model_json2 == application_request_application_details_model_json

class TestModel_ApplicationResponse():
    """
    Test Class for ApplicationResponse
    """

    def test_application_response_serialization(self):
        """
        Test serialization/deserialization for ApplicationResponse
        """

        # Construct a json representation of a ApplicationResponse model
        application_response_model_json = {}
        application_response_model_json['id'] = 'testString'
        application_response_model_json['state'] = 'accepted'

        # Construct a model instance of ApplicationResponse by calling from_dict on the json representation
        application_response_model = ApplicationResponse.from_dict(application_response_model_json)
        assert application_response_model != False

        # Construct a model instance of ApplicationResponse by calling from_dict on the json representation
        application_response_model_dict = ApplicationResponse.from_dict(application_response_model_json).__dict__
        application_response_model2 = ApplicationResponse(**application_response_model_dict)

        # Verify the model instances are equivalent
        assert application_response_model == application_response_model2

        # Convert model instance back to dict and verify no loss of data
        application_response_model_json2 = application_response_model.to_dict()
        assert application_response_model_json2 == application_response_model_json

class TestModel_Instance():
    """
    Test Class for Instance
    """

    def test_instance_serialization(self):
        """
        Test serialization/deserialization for Instance
        """

        # Construct dict forms of any model objects needed in order to build this model.

        instance_default_runtime_model = {} # InstanceDefaultRuntime
        instance_default_runtime_model['spark_version'] = 'testString'

        instance_home_model = {} # InstanceHome
        instance_home_model['id'] = 'testString'
        instance_home_model['provider'] = 'testString'
        instance_home_model['type'] = 'testString'
        instance_home_model['region'] = 'testString'
        instance_home_model['endpoint'] = 'testString'
        instance_home_model['bucket'] = 'testString'
        instance_home_model['hmac_access_key'] = 'testString'
        instance_home_model['hmac_secret_key'] = 'testString'

        instance_default_config_model = {} # InstanceDefaultConfig
        instance_default_config_model['key'] = 'testString'

        # Construct a json representation of a Instance model
        instance_model_json = {}
        instance_model_json['id'] = 'testString'
        instance_model_json['href'] = 'testString'
        instance_model_json['state'] = 'created'
        instance_model_json['state_change_time'] = '2021-01-30T08:30:00Z'
        instance_model_json['default_runtime'] = instance_default_runtime_model
        instance_model_json['instance_home'] = instance_home_model
        instance_model_json['default_config'] = instance_default_config_model

        # Construct a model instance of Instance by calling from_dict on the json representation
        instance_model = Instance.from_dict(instance_model_json)
        assert instance_model != False

        # Construct a model instance of Instance by calling from_dict on the json representation
        instance_model_dict = Instance.from_dict(instance_model_json).__dict__
        instance_model2 = Instance(**instance_model_dict)

        # Verify the model instances are equivalent
        assert instance_model == instance_model2

        # Convert model instance back to dict and verify no loss of data
        instance_model_json2 = instance_model.to_dict()
        assert instance_model_json2 == instance_model_json

class TestModel_InstanceDefaultConfig():
    """
    Test Class for InstanceDefaultConfig
    """

    def test_instance_default_config_serialization(self):
        """
        Test serialization/deserialization for InstanceDefaultConfig
        """

        # Construct a json representation of a InstanceDefaultConfig model
        instance_default_config_model_json = {}
        instance_default_config_model_json['key'] = 'testString'

        # Construct a model instance of InstanceDefaultConfig by calling from_dict on the json representation
        instance_default_config_model = InstanceDefaultConfig.from_dict(instance_default_config_model_json)
        assert instance_default_config_model != False

        # Construct a model instance of InstanceDefaultConfig by calling from_dict on the json representation
        instance_default_config_model_dict = InstanceDefaultConfig.from_dict(instance_default_config_model_json).__dict__
        instance_default_config_model2 = InstanceDefaultConfig(**instance_default_config_model_dict)

        # Verify the model instances are equivalent
        assert instance_default_config_model == instance_default_config_model2

        # Convert model instance back to dict and verify no loss of data
        instance_default_config_model_json2 = instance_default_config_model.to_dict()
        assert instance_default_config_model_json2 == instance_default_config_model_json

class TestModel_InstanceDefaultRuntime():
    """
    Test Class for InstanceDefaultRuntime
    """

    def test_instance_default_runtime_serialization(self):
        """
        Test serialization/deserialization for InstanceDefaultRuntime
        """

        # Construct a json representation of a InstanceDefaultRuntime model
        instance_default_runtime_model_json = {}
        instance_default_runtime_model_json['spark_version'] = 'testString'

        # Construct a model instance of InstanceDefaultRuntime by calling from_dict on the json representation
        instance_default_runtime_model = InstanceDefaultRuntime.from_dict(instance_default_runtime_model_json)
        assert instance_default_runtime_model != False

        # Construct a model instance of InstanceDefaultRuntime by calling from_dict on the json representation
        instance_default_runtime_model_dict = InstanceDefaultRuntime.from_dict(instance_default_runtime_model_json).__dict__
        instance_default_runtime_model2 = InstanceDefaultRuntime(**instance_default_runtime_model_dict)

        # Verify the model instances are equivalent
        assert instance_default_runtime_model == instance_default_runtime_model2

        # Convert model instance back to dict and verify no loss of data
        instance_default_runtime_model_json2 = instance_default_runtime_model.to_dict()
        assert instance_default_runtime_model_json2 == instance_default_runtime_model_json

class TestModel_InstanceGetStateResponse():
    """
    Test Class for InstanceGetStateResponse
    """

    def test_instance_get_state_response_serialization(self):
        """
        Test serialization/deserialization for InstanceGetStateResponse
        """

        # Construct a json representation of a InstanceGetStateResponse model
        instance_get_state_response_model_json = {}
        instance_get_state_response_model_json['id'] = 'testString'
        instance_get_state_response_model_json['state'] = 'created'

        # Construct a model instance of InstanceGetStateResponse by calling from_dict on the json representation
        instance_get_state_response_model = InstanceGetStateResponse.from_dict(instance_get_state_response_model_json)
        assert instance_get_state_response_model != False

        # Construct a model instance of InstanceGetStateResponse by calling from_dict on the json representation
        instance_get_state_response_model_dict = InstanceGetStateResponse.from_dict(instance_get_state_response_model_json).__dict__
        instance_get_state_response_model2 = InstanceGetStateResponse(**instance_get_state_response_model_dict)

        # Verify the model instances are equivalent
        assert instance_get_state_response_model == instance_get_state_response_model2

        # Convert model instance back to dict and verify no loss of data
        instance_get_state_response_model_json2 = instance_get_state_response_model.to_dict()
        assert instance_get_state_response_model_json2 == instance_get_state_response_model_json

class TestModel_InstanceHome():
    """
    Test Class for InstanceHome
    """

    def test_instance_home_serialization(self):
        """
        Test serialization/deserialization for InstanceHome
        """

        # Construct a json representation of a InstanceHome model
        instance_home_model_json = {}
        instance_home_model_json['id'] = 'testString'
        instance_home_model_json['provider'] = 'testString'
        instance_home_model_json['type'] = 'testString'
        instance_home_model_json['region'] = 'testString'
        instance_home_model_json['endpoint'] = 'testString'
        instance_home_model_json['bucket'] = 'testString'
        instance_home_model_json['hmac_access_key'] = 'testString'
        instance_home_model_json['hmac_secret_key'] = 'testString'

        # Construct a model instance of InstanceHome by calling from_dict on the json representation
        instance_home_model = InstanceHome.from_dict(instance_home_model_json)
        assert instance_home_model != False

        # Construct a model instance of InstanceHome by calling from_dict on the json representation
        instance_home_model_dict = InstanceHome.from_dict(instance_home_model_json).__dict__
        instance_home_model2 = InstanceHome(**instance_home_model_dict)

        # Verify the model instances are equivalent
        assert instance_home_model == instance_home_model2

        # Convert model instance back to dict and verify no loss of data
        instance_home_model_json2 = instance_home_model.to_dict()
        assert instance_home_model_json2 == instance_home_model_json

class TestModel_InstanceHomeResponse():
    """
    Test Class for InstanceHomeResponse
    """

    def test_instance_home_response_serialization(self):
        """
        Test serialization/deserialization for InstanceHomeResponse
        """

        # Construct a json representation of a InstanceHomeResponse model
        instance_home_response_model_json = {}
        instance_home_response_model_json['instance_id'] = 'testString'
        instance_home_response_model_json['provider'] = 'testString'
        instance_home_response_model_json['type'] = 'testString'
        instance_home_response_model_json['region'] = 'testString'
        instance_home_response_model_json['endpoint'] = 'testString'
        instance_home_response_model_json['hmac_access_key'] = 'testString'
        instance_home_response_model_json['hmac_secret_key'] = 'testString'

        # Construct a model instance of InstanceHomeResponse by calling from_dict on the json representation
        instance_home_response_model = InstanceHomeResponse.from_dict(instance_home_response_model_json)
        assert instance_home_response_model != False

        # Construct a model instance of InstanceHomeResponse by calling from_dict on the json representation
        instance_home_response_model_dict = InstanceHomeResponse.from_dict(instance_home_response_model_json).__dict__
        instance_home_response_model2 = InstanceHomeResponse(**instance_home_response_model_dict)

        # Verify the model instances are equivalent
        assert instance_home_response_model == instance_home_response_model2

        # Convert model instance back to dict and verify no loss of data
        instance_home_response_model_json2 = instance_home_response_model.to_dict()
        assert instance_home_response_model_json2 == instance_home_response_model_json

class TestModel_LoggingConfigurationResponse():
    """
    Test Class for LoggingConfigurationResponse
    """

    def test_logging_configuration_response_serialization(self):
        """
        Test serialization/deserialization for LoggingConfigurationResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        logging_configuration_response_log_server_model = {} # LoggingConfigurationResponseLogServer
        logging_configuration_response_log_server_model['type'] = 'ibm-log-analysis'

        # Construct a json representation of a LoggingConfigurationResponse model
        logging_configuration_response_model_json = {}
        logging_configuration_response_model_json['components'] = ['spark-driver', 'spark-executor']
        logging_configuration_response_model_json['log_server'] = logging_configuration_response_log_server_model
        logging_configuration_response_model_json['enable'] = True

        # Construct a model instance of LoggingConfigurationResponse by calling from_dict on the json representation
        logging_configuration_response_model = LoggingConfigurationResponse.from_dict(logging_configuration_response_model_json)
        assert logging_configuration_response_model != False

        # Construct a model instance of LoggingConfigurationResponse by calling from_dict on the json representation
        logging_configuration_response_model_dict = LoggingConfigurationResponse.from_dict(logging_configuration_response_model_json).__dict__
        logging_configuration_response_model2 = LoggingConfigurationResponse(**logging_configuration_response_model_dict)

        # Verify the model instances are equivalent
        assert logging_configuration_response_model == logging_configuration_response_model2

        # Convert model instance back to dict and verify no loss of data
        logging_configuration_response_model_json2 = logging_configuration_response_model.to_dict()
        assert logging_configuration_response_model_json2 == logging_configuration_response_model_json

class TestModel_LoggingConfigurationResponseLogServer():
    """
    Test Class for LoggingConfigurationResponseLogServer
    """

    def test_logging_configuration_response_log_server_serialization(self):
        """
        Test serialization/deserialization for LoggingConfigurationResponseLogServer
        """

        # Construct a json representation of a LoggingConfigurationResponseLogServer model
        logging_configuration_response_log_server_model_json = {}
        logging_configuration_response_log_server_model_json['type'] = 'ibm-log-analysis'

        # Construct a model instance of LoggingConfigurationResponseLogServer by calling from_dict on the json representation
        logging_configuration_response_log_server_model = LoggingConfigurationResponseLogServer.from_dict(logging_configuration_response_log_server_model_json)
        assert logging_configuration_response_log_server_model != False

        # Construct a model instance of LoggingConfigurationResponseLogServer by calling from_dict on the json representation
        logging_configuration_response_log_server_model_dict = LoggingConfigurationResponseLogServer.from_dict(logging_configuration_response_log_server_model_json).__dict__
        logging_configuration_response_log_server_model2 = LoggingConfigurationResponseLogServer(**logging_configuration_response_log_server_model_dict)

        # Verify the model instances are equivalent
        assert logging_configuration_response_log_server_model == logging_configuration_response_log_server_model2

        # Convert model instance back to dict and verify no loss of data
        logging_configuration_response_log_server_model_json2 = logging_configuration_response_log_server_model.to_dict()
        assert logging_configuration_response_log_server_model_json2 == logging_configuration_response_log_server_model_json

class TestModel_SparkHistoryServerResponse():
    """
    Test Class for SparkHistoryServerResponse
    """

    def test_spark_history_server_response_serialization(self):
        """
        Test serialization/deserialization for SparkHistoryServerResponse
        """

        # Construct a json representation of a SparkHistoryServerResponse model
        spark_history_server_response_model_json = {}
        spark_history_server_response_model_json['state'] = 'testString'
        spark_history_server_response_model_json['cores'] = 'testString'
        spark_history_server_response_model_json['memory'] = 'testString'
        spark_history_server_response_model_json['start_time'] = 'testString'
        spark_history_server_response_model_json['stop_time'] = 'testString'

        # Construct a model instance of SparkHistoryServerResponse by calling from_dict on the json representation
        spark_history_server_response_model = SparkHistoryServerResponse.from_dict(spark_history_server_response_model_json)
        assert spark_history_server_response_model != False

        # Construct a model instance of SparkHistoryServerResponse by calling from_dict on the json representation
        spark_history_server_response_model_dict = SparkHistoryServerResponse.from_dict(spark_history_server_response_model_json).__dict__
        spark_history_server_response_model2 = SparkHistoryServerResponse(**spark_history_server_response_model_dict)

        # Verify the model instances are equivalent
        assert spark_history_server_response_model == spark_history_server_response_model2

        # Convert model instance back to dict and verify no loss of data
        spark_history_server_response_model_json2 = spark_history_server_response_model.to_dict()
        assert spark_history_server_response_model_json2 == spark_history_server_response_model_json

class TestModel_SparkHistoryServerStartResponse():
    """
    Test Class for SparkHistoryServerStartResponse
    """

    def test_spark_history_server_start_response_serialization(self):
        """
        Test serialization/deserialization for SparkHistoryServerStartResponse
        """

        # Construct a json representation of a SparkHistoryServerStartResponse model
        spark_history_server_start_response_model_json = {}
        spark_history_server_start_response_model_json['state'] = 'testString'
        spark_history_server_start_response_model_json['cores'] = 'testString'
        spark_history_server_start_response_model_json['memory'] = 'testString'
        spark_history_server_start_response_model_json['start_time'] = 'testString'

        # Construct a model instance of SparkHistoryServerStartResponse by calling from_dict on the json representation
        spark_history_server_start_response_model = SparkHistoryServerStartResponse.from_dict(spark_history_server_start_response_model_json)
        assert spark_history_server_start_response_model != False

        # Construct a model instance of SparkHistoryServerStartResponse by calling from_dict on the json representation
        spark_history_server_start_response_model_dict = SparkHistoryServerStartResponse.from_dict(spark_history_server_start_response_model_json).__dict__
        spark_history_server_start_response_model2 = SparkHistoryServerStartResponse(**spark_history_server_start_response_model_dict)

        # Verify the model instances are equivalent
        assert spark_history_server_start_response_model == spark_history_server_start_response_model2

        # Convert model instance back to dict and verify no loss of data
        spark_history_server_start_response_model_json2 = spark_history_server_start_response_model.to_dict()
        assert spark_history_server_start_response_model_json2 == spark_history_server_start_response_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
