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
            )

class TestGetInstance():
    """
    Test Class for get_instance
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_instance_all_params(self):
        """
        get_instance()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09')
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


    @responses.activate
    def test_get_instance_value_error(self):
        """
        test_get_instance_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09')
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



class TestCreateApplication():
    """
    Test Class for create_application
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_create_application_all_params(self):
        """
        create_application()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications')
        mock_response = '{"id": "id", "state": "accepted"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {}
        application_request_application_details_model['application'] = 'cos://bucket_name.my_cos/my_spark_app.py'
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


    @responses.activate
    def test_create_application_value_error(self):
        """
        test_create_application_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications')
        mock_response = '{"id": "id", "state": "accepted"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=202)

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {}
        application_request_application_details_model['application'] = 'cos://bucket_name.my_cos/my_spark_app.py'
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



class TestListApplications():
    """
    Test Class for list_applications
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_list_applications_all_params(self):
        """
        list_applications()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications')
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


    @responses.activate
    def test_list_applications_value_error(self):
        """
        test_list_applications_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications')
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



class TestGetApplication():
    """
    Test Class for get_application
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_application_all_params(self):
        """
        get_application()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b')
        mock_response = '{"application_details": {"application": "cos://bucket_name.my_cos/my_spark_app.py", "class": "com.company.path.ClassName", "arguments": ["[arg1, arg2, arg3]"], "conf": {"mapKey": "anyValue"}, "env": {"mapKey": "anyValue"}}, "id": "2b83d31c-397b-48ad-ad76-b83347c982db", "state": "accepted", "start_time": "2021-01-30T08:30:00.000Z", "finish_time": "2021-01-30T08:30:00.000Z"}'
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


    @responses.activate
    def test_get_application_value_error(self):
        """
        test_get_application_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b')
        mock_response = '{"application_details": {"application": "cos://bucket_name.my_cos/my_spark_app.py", "class": "com.company.path.ClassName", "arguments": ["[arg1, arg2, arg3]"], "conf": {"mapKey": "anyValue"}, "env": {"mapKey": "anyValue"}}, "id": "2b83d31c-397b-48ad-ad76-b83347c982db", "state": "accepted", "start_time": "2021-01-30T08:30:00.000Z", "finish_time": "2021-01-30T08:30:00.000Z"}'
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



class TestDeleteApplication():
    """
    Test Class for delete_application
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_delete_application_all_params(self):
        """
        delete_application()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b')
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


    @responses.activate
    def test_delete_application_value_error(self):
        """
        test_delete_application_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b')
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



class TestGetApplicationState():
    """
    Test Class for get_application_state
    """

    def preprocess_url(self, request_url: str):
        """
        Preprocess the request URL to ensure the mock response will be found.
        """
        request_url = urllib.parse.unquote(request_url) # don't double-encode if already encoded
        request_url = urllib.parse.quote(request_url, safe=':/')
        if re.fullmatch('.*/+', request_url) is None:
            return request_url
        else:
            return re.compile(request_url.rstrip('/') + '/+')

    @responses.activate
    def test_get_application_state_all_params(self):
        """
        get_application_state()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b/state')
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


    @responses.activate
    def test_get_application_state_value_error(self):
        """
        test_get_application_state_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/e64c907a-e82f-46fd-addc-ccfafbd28b09/spark_applications/ff48cc19-0e7e-4627-aac6-0b4ad080397b/state')
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
        application_details_model['class'] = 'com.company.path.ClassName'
        application_details_model['arguments'] = ['[arg1, arg2, arg3]']
        application_details_model['conf'] = {}
        application_details_model['env'] = {}

        # Construct a json representation of a ApplicationGetResponse model
        application_get_response_model_json = {}
        application_get_response_model_json['application_details'] = application_details_model
        application_get_response_model_json['id'] = '2b83d31c-397b-48ad-ad76-b83347c982db'
        application_get_response_model_json['state'] = 'accepted'
        application_get_response_model_json['start_time'] = "2021-01-30T08:30:00Z"
        application_get_response_model_json['finish_time'] = "2021-01-30T08:30:00Z"

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
        instance_model_json['state_change_time'] = "2021-01-30T08:30:00Z"
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


# endregion
##############################################################################
# End of Model Tests
##############################################################################
