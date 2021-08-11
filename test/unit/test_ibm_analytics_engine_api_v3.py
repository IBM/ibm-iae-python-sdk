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

class TestGetInstanceById():
    """
    Test Class for get_instance_by_id
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
    def test_get_instance_by_id_all_params(self):
        """
        get_instance_by_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString')
        mock_response = '{"instance_id": "instance_id", "state": "created", "state_change_time": "2019-01-01T12:00:00.000Z", "default_runtime": {"spark_version": "spark_version", "additional_packages": ["additional_packages"]}, "instance_home": {"guid": "guid", "provider": "provider", "type": "type", "region": "region", "endpoint": "endpoint", "bucket": "bucket", "hmac_access_key": "hmac_access_key", "hmac_secret_key": "hmac_secret_key"}, "default_config": {"key": "key"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.get_instance_by_id(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_instance_by_id_value_error(self):
        """
        test_get_instance_by_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString')
        mock_response = '{"instance_id": "instance_id", "state": "created", "state_change_time": "2019-01-01T12:00:00.000Z", "default_runtime": {"spark_version": "spark_version", "additional_packages": ["additional_packages"]}, "instance_home": {"guid": "guid", "provider": "provider", "type": "type", "region": "region", "endpoint": "endpoint", "bucket": "bucket", "hmac_access_key": "hmac_access_key", "hmac_secret_key": "hmac_secret_key"}, "default_config": {"key": "key"}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_instance_by_id(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications')
        mock_response = '{"application_id": "application_id", "state": "accepted", "start_time": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {}
        application_request_application_details_model['application'] = 'testString'
        application_request_application_details_model['class'] = 'testString'
        application_request_application_details_model['application_arguments'] = ['testString']
        application_request_application_details_model['conf'] = {}
        application_request_application_details_model['env'] = {}

        # Set up parameter values
        instance_id = 'testString'
        application_details = application_request_application_details_model

        # Invoke method
        response = _service.create_application(
            instance_id,
            application_details=application_details,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 201
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['application_details'] == application_request_application_details_model


    @responses.activate
    def test_create_application_value_error(self):
        """
        test_create_application_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications')
        mock_response = '{"application_id": "application_id", "state": "accepted", "start_time": "2019-01-01T12:00:00.000Z"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=201)

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {}
        application_request_application_details_model['application'] = 'testString'
        application_request_application_details_model['class'] = 'testString'
        application_request_application_details_model['application_arguments'] = ['testString']
        application_request_application_details_model['conf'] = {}
        application_request_application_details_model['env'] = {}

        # Set up parameter values
        instance_id = 'testString'
        application_details = application_request_application_details_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_application(**req_copy)



class TestGetApplications():
    """
    Test Class for get_applications
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
    def test_get_applications_all_params(self):
        """
        get_applications()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications')
        mock_response = '{"applications": [{"application_id": "application_id", "spark_application_id": "spark_application_id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Invoke method
        response = _service.get_applications(
            instance_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_applications_value_error(self):
        """
        test_get_applications_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications')
        mock_response = '{"applications": [{"application_id": "application_id", "spark_application_id": "spark_application_id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_applications(**req_copy)



class TestGetApplicationById():
    """
    Test Class for get_application_by_id
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
    def test_get_application_by_id_all_params(self):
        """
        get_application_by_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications/testString')
        mock_response = '{"application_details": {"application_details": {"application": "application", "class": "class_", "application_arguments": ["application_arguments"], "conf": {"mapKey": "anyValue"}, "env": {"mapKey": "anyValue"}}}, "mode": "mode", "application_id": "application_id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        application_id = 'testString'

        # Invoke method
        response = _service.get_application_by_id(
            instance_id,
            application_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    @responses.activate
    def test_get_application_by_id_value_error(self):
        """
        test_get_application_by_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications/testString')
        mock_response = '{"application_details": {"application_details": {"application": "application", "class": "class_", "application_arguments": ["application_arguments"], "conf": {"mapKey": "anyValue"}, "env": {"mapKey": "anyValue"}}}, "mode": "mode", "application_id": "application_id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        application_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "application_id": application_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_application_by_id(**req_copy)



class TestDeleteApplicationById():
    """
    Test Class for delete_application_by_id
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
    def test_delete_application_by_id_all_params(self):
        """
        delete_application_by_id()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        application_id = 'testString'

        # Invoke method
        response = _service.delete_application_by_id(
            instance_id,
            application_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 204


    @responses.activate
    def test_delete_application_by_id_value_error(self):
        """
        test_delete_application_by_id_value_error()
        """
        # Set up mock
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications/testString')
        responses.add(responses.DELETE,
                      url,
                      status=204)

        # Set up parameter values
        instance_id = 'testString'
        application_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_id": instance_id,
            "application_id": application_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_application_by_id(**req_copy)



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
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications/testString/state')
        mock_response = '{"application_id": "application_id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        application_id = 'testString'

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
        url = self.preprocess_url(_base_url + '/v3/analytics_engines/testString/spark/applications/testString/state')
        mock_response = '{"application_id": "application_id", "state": "state", "start_time": "start_time", "finish_time": "finish_time"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_id = 'testString'
        application_id = 'testString'

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
class TestModel_ApplicationCollection():
    """
    Test Class for ApplicationCollection
    """

    def test_application_collection_serialization(self):
        """
        Test serialization/deserialization for ApplicationCollection
        """

        # Construct dict forms of any model objects needed in order to build this model.

        application_details_model = {} # ApplicationDetails
        application_details_model['application_id'] = 'testString'
        application_details_model['spark_application_id'] = 'testString'
        application_details_model['state'] = 'testString'
        application_details_model['start_time'] = 'testString'
        application_details_model['finish_time'] = 'testString'

        # Construct a json representation of a ApplicationCollection model
        application_collection_model_json = {}
        application_collection_model_json['applications'] = [application_details_model]

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
        application_details_model_json['application_id'] = 'testString'
        application_details_model_json['spark_application_id'] = 'testString'
        application_details_model_json['state'] = 'testString'
        application_details_model_json['start_time'] = 'testString'
        application_details_model_json['finish_time'] = 'testString'

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

        application_request_application_details_model = {} # ApplicationRequestApplicationDetails
        application_request_application_details_model['application'] = 'testString'
        application_request_application_details_model['class'] = 'testString'
        application_request_application_details_model['application_arguments'] = ['testString']
        application_request_application_details_model['conf'] = {}
        application_request_application_details_model['env'] = {}

        application_request_model = {} # ApplicationRequest
        application_request_model['application_details'] = application_request_application_details_model

        # Construct a json representation of a ApplicationGetResponse model
        application_get_response_model_json = {}
        application_get_response_model_json['application_details'] = application_request_model
        application_get_response_model_json['mode'] = 'testString'
        application_get_response_model_json['application_id'] = 'testString'
        application_get_response_model_json['state'] = 'testString'
        application_get_response_model_json['start_time'] = 'testString'
        application_get_response_model_json['finish_time'] = 'testString'

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
        application_get_state_response_model_json['application_id'] = 'testString'
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

class TestModel_ApplicationRequest():
    """
    Test Class for ApplicationRequest
    """

    def test_application_request_serialization(self):
        """
        Test serialization/deserialization for ApplicationRequest
        """

        # Construct dict forms of any model objects needed in order to build this model.

        application_request_application_details_model = {} # ApplicationRequestApplicationDetails
        application_request_application_details_model['application'] = 'testString'
        application_request_application_details_model['class'] = 'testString'
        application_request_application_details_model['application_arguments'] = ['testString']
        application_request_application_details_model['conf'] = {}
        application_request_application_details_model['env'] = {}

        # Construct a json representation of a ApplicationRequest model
        application_request_model_json = {}
        application_request_model_json['application_details'] = application_request_application_details_model

        # Construct a model instance of ApplicationRequest by calling from_dict on the json representation
        application_request_model = ApplicationRequest.from_dict(application_request_model_json)
        assert application_request_model != False

        # Construct a model instance of ApplicationRequest by calling from_dict on the json representation
        application_request_model_dict = ApplicationRequest.from_dict(application_request_model_json).__dict__
        application_request_model2 = ApplicationRequest(**application_request_model_dict)

        # Verify the model instances are equivalent
        assert application_request_model == application_request_model2

        # Convert model instance back to dict and verify no loss of data
        application_request_model_json2 = application_request_model.to_dict()
        assert application_request_model_json2 == application_request_model_json

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
        application_request_application_details_model_json['application'] = 'testString'
        application_request_application_details_model_json['class'] = 'testString'
        application_request_application_details_model_json['application_arguments'] = ['testString']
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
        application_response_model_json['application_id'] = 'testString'
        application_response_model_json['state'] = 'accepted'
        application_response_model_json['start_time'] = "2019-01-01T12:00:00Z"

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

class TestModel_InstanceDetails():
    """
    Test Class for InstanceDetails
    """

    def test_instance_details_serialization(self):
        """
        Test serialization/deserialization for InstanceDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        instance_details_default_runtime_model = {} # InstanceDetailsDefaultRuntime
        instance_details_default_runtime_model['spark_version'] = 'testString'
        instance_details_default_runtime_model['additional_packages'] = ['testString']

        instance_details_instance_home_model = {} # InstanceDetailsInstanceHome
        instance_details_instance_home_model['guid'] = 'testString'
        instance_details_instance_home_model['provider'] = 'testString'
        instance_details_instance_home_model['type'] = 'testString'
        instance_details_instance_home_model['region'] = 'testString'
        instance_details_instance_home_model['endpoint'] = 'testString'
        instance_details_instance_home_model['bucket'] = 'testString'
        instance_details_instance_home_model['hmac_access_key'] = 'testString'
        instance_details_instance_home_model['hmac_secret_key'] = 'testString'

        instance_details_default_config_model = {} # InstanceDetailsDefaultConfig
        instance_details_default_config_model['key'] = 'testString'

        # Construct a json representation of a InstanceDetails model
        instance_details_model_json = {}
        instance_details_model_json['instance_id'] = 'testString'
        instance_details_model_json['state'] = 'created'
        instance_details_model_json['state_change_time'] = "2019-01-01T12:00:00Z"
        instance_details_model_json['default_runtime'] = instance_details_default_runtime_model
        instance_details_model_json['instance_home'] = instance_details_instance_home_model
        instance_details_model_json['default_config'] = instance_details_default_config_model

        # Construct a model instance of InstanceDetails by calling from_dict on the json representation
        instance_details_model = InstanceDetails.from_dict(instance_details_model_json)
        assert instance_details_model != False

        # Construct a model instance of InstanceDetails by calling from_dict on the json representation
        instance_details_model_dict = InstanceDetails.from_dict(instance_details_model_json).__dict__
        instance_details_model2 = InstanceDetails(**instance_details_model_dict)

        # Verify the model instances are equivalent
        assert instance_details_model == instance_details_model2

        # Convert model instance back to dict and verify no loss of data
        instance_details_model_json2 = instance_details_model.to_dict()
        assert instance_details_model_json2 == instance_details_model_json

class TestModel_InstanceDetailsDefaultConfig():
    """
    Test Class for InstanceDetailsDefaultConfig
    """

    def test_instance_details_default_config_serialization(self):
        """
        Test serialization/deserialization for InstanceDetailsDefaultConfig
        """

        # Construct a json representation of a InstanceDetailsDefaultConfig model
        instance_details_default_config_model_json = {}
        instance_details_default_config_model_json['key'] = 'testString'

        # Construct a model instance of InstanceDetailsDefaultConfig by calling from_dict on the json representation
        instance_details_default_config_model = InstanceDetailsDefaultConfig.from_dict(instance_details_default_config_model_json)
        assert instance_details_default_config_model != False

        # Construct a model instance of InstanceDetailsDefaultConfig by calling from_dict on the json representation
        instance_details_default_config_model_dict = InstanceDetailsDefaultConfig.from_dict(instance_details_default_config_model_json).__dict__
        instance_details_default_config_model2 = InstanceDetailsDefaultConfig(**instance_details_default_config_model_dict)

        # Verify the model instances are equivalent
        assert instance_details_default_config_model == instance_details_default_config_model2

        # Convert model instance back to dict and verify no loss of data
        instance_details_default_config_model_json2 = instance_details_default_config_model.to_dict()
        assert instance_details_default_config_model_json2 == instance_details_default_config_model_json

class TestModel_InstanceDetailsDefaultRuntime():
    """
    Test Class for InstanceDetailsDefaultRuntime
    """

    def test_instance_details_default_runtime_serialization(self):
        """
        Test serialization/deserialization for InstanceDetailsDefaultRuntime
        """

        # Construct a json representation of a InstanceDetailsDefaultRuntime model
        instance_details_default_runtime_model_json = {}
        instance_details_default_runtime_model_json['spark_version'] = 'testString'
        instance_details_default_runtime_model_json['additional_packages'] = ['testString']

        # Construct a model instance of InstanceDetailsDefaultRuntime by calling from_dict on the json representation
        instance_details_default_runtime_model = InstanceDetailsDefaultRuntime.from_dict(instance_details_default_runtime_model_json)
        assert instance_details_default_runtime_model != False

        # Construct a model instance of InstanceDetailsDefaultRuntime by calling from_dict on the json representation
        instance_details_default_runtime_model_dict = InstanceDetailsDefaultRuntime.from_dict(instance_details_default_runtime_model_json).__dict__
        instance_details_default_runtime_model2 = InstanceDetailsDefaultRuntime(**instance_details_default_runtime_model_dict)

        # Verify the model instances are equivalent
        assert instance_details_default_runtime_model == instance_details_default_runtime_model2

        # Convert model instance back to dict and verify no loss of data
        instance_details_default_runtime_model_json2 = instance_details_default_runtime_model.to_dict()
        assert instance_details_default_runtime_model_json2 == instance_details_default_runtime_model_json

class TestModel_InstanceDetailsInstanceHome():
    """
    Test Class for InstanceDetailsInstanceHome
    """

    def test_instance_details_instance_home_serialization(self):
        """
        Test serialization/deserialization for InstanceDetailsInstanceHome
        """

        # Construct a json representation of a InstanceDetailsInstanceHome model
        instance_details_instance_home_model_json = {}
        instance_details_instance_home_model_json['guid'] = 'testString'
        instance_details_instance_home_model_json['provider'] = 'testString'
        instance_details_instance_home_model_json['type'] = 'testString'
        instance_details_instance_home_model_json['region'] = 'testString'
        instance_details_instance_home_model_json['endpoint'] = 'testString'
        instance_details_instance_home_model_json['bucket'] = 'testString'
        instance_details_instance_home_model_json['hmac_access_key'] = 'testString'
        instance_details_instance_home_model_json['hmac_secret_key'] = 'testString'

        # Construct a model instance of InstanceDetailsInstanceHome by calling from_dict on the json representation
        instance_details_instance_home_model = InstanceDetailsInstanceHome.from_dict(instance_details_instance_home_model_json)
        assert instance_details_instance_home_model != False

        # Construct a model instance of InstanceDetailsInstanceHome by calling from_dict on the json representation
        instance_details_instance_home_model_dict = InstanceDetailsInstanceHome.from_dict(instance_details_instance_home_model_json).__dict__
        instance_details_instance_home_model2 = InstanceDetailsInstanceHome(**instance_details_instance_home_model_dict)

        # Verify the model instances are equivalent
        assert instance_details_instance_home_model == instance_details_instance_home_model2

        # Convert model instance back to dict and verify no loss of data
        instance_details_instance_home_model_json2 = instance_details_instance_home_model.to_dict()
        assert instance_details_instance_home_model_json2 == instance_details_instance_home_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
