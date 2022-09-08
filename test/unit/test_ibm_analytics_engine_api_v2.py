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
Unit Tests for IbmAnalyticsEngineApiV2
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
from iaesdk.ibm_analytics_engine_api_v2 import *


_service = IbmAnalyticsEngineApiV2(
    authenticator=NoAuthAuthenticator()
)

_base_url = 'https://fake'
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


##############################################################################
# Start of Service: AnalyticsEnginesV2
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

        service = IbmAnalyticsEngineApiV2.new_instance(
            service_name='TEST_SERVICE',
        )

        assert service is not None
        assert isinstance(service, IbmAnalyticsEngineApiV2)

    def test_new_instance_without_authenticator(self):
        """
        new_instance_without_authenticator()
        """
        with pytest.raises(ValueError, match='authenticator must be provided'):
            service = IbmAnalyticsEngineApiV2.new_instance(
                service_name='TEST_SERVICE_NOT_FOUND',
            )

class TestGetAllAnalyticsEngines():
    """
    Test Class for get_all_analytics_engines
    """

    @responses.activate
    def test_get_all_analytics_engines_all_params(self):
        """
        get_all_analytics_engines()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines')
        responses.add(responses.GET,
                      url,
                      status=200)

        # Invoke method
        response = _service.get_all_analytics_engines()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_all_analytics_engines_all_params_with_retries(self):
        # Enable retries and run test_get_all_analytics_engines_all_params.
        _service.enable_retries()
        self.test_get_all_analytics_engines_all_params()

        # Disable retries and run test_get_all_analytics_engines_all_params.
        _service.disable_retries()
        self.test_get_all_analytics_engines_all_params()

class TestGetAnalyticsEngineById():
    """
    Test Class for get_analytics_engine_by_id
    """

    @responses.activate
    def test_get_analytics_engine_by_id_all_params(self):
        """
        get_analytics_engine_by_id()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString')
        mock_response = '{"id": "id", "name": "name", "service_plan": "service_plan", "hardware_size": "hardware_size", "software_package": "software_package", "domain": "domain", "creation_time": "2019-01-01T12:00:00.000Z", "commision_time": "2019-01-01T12:00:00.000Z", "decommision_time": "2019-01-01T12:00:00.000Z", "deletion_time": "2019-01-01T12:00:00.000Z", "state_change_time": "2019-01-01T12:00:00.000Z", "state": "state", "nodes": [{"id": 2, "fqdn": "fqdn", "type": "type", "state": "state", "public_ip": "public_ip", "private_ip": "private_ip", "state_change_time": "2019-01-01T12:00:00.000Z", "commission_time": "2019-01-01T12:00:00.000Z"}], "user_credentials": {"user": "user"}, "service_endpoints": {"phoenix_jdbc": "phoenix_jdbc", "ambari_console": "ambari_console", "livy": "livy", "spark_history_server": "spark_history_server", "oozie_rest": "oozie_rest", "hive_jdbc": "hive_jdbc", "notebook_gateway_websocket": "notebook_gateway_websocket", "notebook_gateway": "notebook_gateway", "webhdfs": "webhdfs", "ssh": "ssh", "spark_sql": "spark_sql"}, "service_endpoints_ip": {"phoenix_jdbc": "phoenix_jdbc", "ambari_console": "ambari_console", "livy": "livy", "spark_history_server": "spark_history_server", "oozie_rest": "oozie_rest", "hive_jdbc": "hive_jdbc", "notebook_gateway_websocket": "notebook_gateway_websocket", "notebook_gateway": "notebook_gateway", "webhdfs": "webhdfs", "ssh": "ssh", "spark_sql": "spark_sql"}, "private_endpoint_whitelist": ["private_endpoint_whitelist"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = _service.get_analytics_engine_by_id(
            instance_guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_analytics_engine_by_id_all_params_with_retries(self):
        # Enable retries and run test_get_analytics_engine_by_id_all_params.
        _service.enable_retries()
        self.test_get_analytics_engine_by_id_all_params()

        # Disable retries and run test_get_analytics_engine_by_id_all_params.
        _service.disable_retries()
        self.test_get_analytics_engine_by_id_all_params()

    @responses.activate
    def test_get_analytics_engine_by_id_value_error(self):
        """
        test_get_analytics_engine_by_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString')
        mock_response = '{"id": "id", "name": "name", "service_plan": "service_plan", "hardware_size": "hardware_size", "software_package": "software_package", "domain": "domain", "creation_time": "2019-01-01T12:00:00.000Z", "commision_time": "2019-01-01T12:00:00.000Z", "decommision_time": "2019-01-01T12:00:00.000Z", "deletion_time": "2019-01-01T12:00:00.000Z", "state_change_time": "2019-01-01T12:00:00.000Z", "state": "state", "nodes": [{"id": 2, "fqdn": "fqdn", "type": "type", "state": "state", "public_ip": "public_ip", "private_ip": "private_ip", "state_change_time": "2019-01-01T12:00:00.000Z", "commission_time": "2019-01-01T12:00:00.000Z"}], "user_credentials": {"user": "user"}, "service_endpoints": {"phoenix_jdbc": "phoenix_jdbc", "ambari_console": "ambari_console", "livy": "livy", "spark_history_server": "spark_history_server", "oozie_rest": "oozie_rest", "hive_jdbc": "hive_jdbc", "notebook_gateway_websocket": "notebook_gateway_websocket", "notebook_gateway": "notebook_gateway", "webhdfs": "webhdfs", "ssh": "ssh", "spark_sql": "spark_sql"}, "service_endpoints_ip": {"phoenix_jdbc": "phoenix_jdbc", "ambari_console": "ambari_console", "livy": "livy", "spark_history_server": "spark_history_server", "oozie_rest": "oozie_rest", "hive_jdbc": "hive_jdbc", "notebook_gateway_websocket": "notebook_gateway_websocket", "notebook_gateway": "notebook_gateway", "webhdfs": "webhdfs", "ssh": "ssh", "spark_sql": "spark_sql"}, "private_endpoint_whitelist": ["private_endpoint_whitelist"]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_analytics_engine_by_id(**req_copy)

    def test_get_analytics_engine_by_id_value_error_with_retries(self):
        # Enable retries and run test_get_analytics_engine_by_id_value_error.
        _service.enable_retries()
        self.test_get_analytics_engine_by_id_value_error()

        # Disable retries and run test_get_analytics_engine_by_id_value_error.
        _service.disable_retries()
        self.test_get_analytics_engine_by_id_value_error()

class TestGetAnalyticsEngineStateById():
    """
    Test Class for get_analytics_engine_state_by_id
    """

    @responses.activate
    def test_get_analytics_engine_state_by_id_all_params(self):
        """
        get_analytics_engine_state_by_id()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/state')
        mock_response = '{"state": "state"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = _service.get_analytics_engine_state_by_id(
            instance_guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_analytics_engine_state_by_id_all_params_with_retries(self):
        # Enable retries and run test_get_analytics_engine_state_by_id_all_params.
        _service.enable_retries()
        self.test_get_analytics_engine_state_by_id_all_params()

        # Disable retries and run test_get_analytics_engine_state_by_id_all_params.
        _service.disable_retries()
        self.test_get_analytics_engine_state_by_id_all_params()

    @responses.activate
    def test_get_analytics_engine_state_by_id_value_error(self):
        """
        test_get_analytics_engine_state_by_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/state')
        mock_response = '{"state": "state"}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_analytics_engine_state_by_id(**req_copy)

    def test_get_analytics_engine_state_by_id_value_error_with_retries(self):
        # Enable retries and run test_get_analytics_engine_state_by_id_value_error.
        _service.enable_retries()
        self.test_get_analytics_engine_state_by_id_value_error()

        # Disable retries and run test_get_analytics_engine_state_by_id_value_error.
        _service.disable_retries()
        self.test_get_analytics_engine_state_by_id_value_error()

class TestCreateCustomizationRequest():
    """
    Test Class for create_customization_request
    """

    @responses.activate
    def test_create_customization_request_all_params(self):
        """
        create_customization_request()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/customization_requests')
        mock_response = '{"request_id": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AnalyticsEngineCustomActionScript model
        analytics_engine_custom_action_script_model = {}
        analytics_engine_custom_action_script_model['source_type'] = 'http'
        analytics_engine_custom_action_script_model['script_path'] = 'testString'
        analytics_engine_custom_action_script_model['source_props'] = {'foo': 'bar'}

        # Construct a dict representation of a AnalyticsEngineCustomAction model
        analytics_engine_custom_action_model = {}
        analytics_engine_custom_action_model['name'] = 'testString'
        analytics_engine_custom_action_model['type'] = 'bootstrap'
        analytics_engine_custom_action_model['script'] = analytics_engine_custom_action_script_model
        analytics_engine_custom_action_model['script_params'] = ['testString']

        # Set up parameter values
        instance_guid = 'testString'
        target = 'all'
        custom_actions = [analytics_engine_custom_action_model]

        # Invoke method
        response = _service.create_customization_request(
            instance_guid,
            target,
            custom_actions,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['target'] == 'all'
        assert req_body['custom_actions'] == [analytics_engine_custom_action_model]

    def test_create_customization_request_all_params_with_retries(self):
        # Enable retries and run test_create_customization_request_all_params.
        _service.enable_retries()
        self.test_create_customization_request_all_params()

        # Disable retries and run test_create_customization_request_all_params.
        _service.disable_retries()
        self.test_create_customization_request_all_params()

    @responses.activate
    def test_create_customization_request_value_error(self):
        """
        test_create_customization_request_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/customization_requests')
        mock_response = '{"request_id": 10}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AnalyticsEngineCustomActionScript model
        analytics_engine_custom_action_script_model = {}
        analytics_engine_custom_action_script_model['source_type'] = 'http'
        analytics_engine_custom_action_script_model['script_path'] = 'testString'
        analytics_engine_custom_action_script_model['source_props'] = {'foo': 'bar'}

        # Construct a dict representation of a AnalyticsEngineCustomAction model
        analytics_engine_custom_action_model = {}
        analytics_engine_custom_action_model['name'] = 'testString'
        analytics_engine_custom_action_model['type'] = 'bootstrap'
        analytics_engine_custom_action_model['script'] = analytics_engine_custom_action_script_model
        analytics_engine_custom_action_model['script_params'] = ['testString']

        # Set up parameter values
        instance_guid = 'testString'
        target = 'all'
        custom_actions = [analytics_engine_custom_action_model]

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
            "target": target,
            "custom_actions": custom_actions,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.create_customization_request(**req_copy)

    def test_create_customization_request_value_error_with_retries(self):
        # Enable retries and run test_create_customization_request_value_error.
        _service.enable_retries()
        self.test_create_customization_request_value_error()

        # Disable retries and run test_create_customization_request_value_error.
        _service.disable_retries()
        self.test_create_customization_request_value_error()

class TestGetAllCustomizationRequests():
    """
    Test Class for get_all_customization_requests
    """

    @responses.activate
    def test_get_all_customization_requests_all_params(self):
        """
        get_all_customization_requests()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/customization_requests')
        mock_response = '[{"id": "id"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = _service.get_all_customization_requests(
            instance_guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_all_customization_requests_all_params_with_retries(self):
        # Enable retries and run test_get_all_customization_requests_all_params.
        _service.enable_retries()
        self.test_get_all_customization_requests_all_params()

        # Disable retries and run test_get_all_customization_requests_all_params.
        _service.disable_retries()
        self.test_get_all_customization_requests_all_params()

    @responses.activate
    def test_get_all_customization_requests_value_error(self):
        """
        test_get_all_customization_requests_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/customization_requests')
        mock_response = '[{"id": "id"}]'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_all_customization_requests(**req_copy)

    def test_get_all_customization_requests_value_error_with_retries(self):
        # Enable retries and run test_get_all_customization_requests_value_error.
        _service.enable_retries()
        self.test_get_all_customization_requests_value_error()

        # Disable retries and run test_get_all_customization_requests_value_error.
        _service.disable_retries()
        self.test_get_all_customization_requests_value_error()

class TestGetCustomizationRequestById():
    """
    Test Class for get_customization_request_by_id
    """

    @responses.activate
    def test_get_customization_request_by_id_all_params(self):
        """
        get_customization_request_by_id()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/customization_requests/testString')
        mock_response = '{"id": "id", "run_status": "run_status", "run_details": {"overall_status": "overall_status", "details": [{"node_name": "node_name", "node_type": "node_type", "start_time": "start_time", "end_time": "end_time", "time_taken": "time_taken", "status": "status", "log_file": "log_file"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'
        request_id = 'testString'

        # Invoke method
        response = _service.get_customization_request_by_id(
            instance_guid,
            request_id,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_customization_request_by_id_all_params_with_retries(self):
        # Enable retries and run test_get_customization_request_by_id_all_params.
        _service.enable_retries()
        self.test_get_customization_request_by_id_all_params()

        # Disable retries and run test_get_customization_request_by_id_all_params.
        _service.disable_retries()
        self.test_get_customization_request_by_id_all_params()

    @responses.activate
    def test_get_customization_request_by_id_value_error(self):
        """
        test_get_customization_request_by_id_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/customization_requests/testString')
        mock_response = '{"id": "id", "run_status": "run_status", "run_details": {"overall_status": "overall_status", "details": [{"node_name": "node_name", "node_type": "node_type", "start_time": "start_time", "end_time": "end_time", "time_taken": "time_taken", "status": "status", "log_file": "log_file"}]}}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'
        request_id = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
            "request_id": request_id,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_customization_request_by_id(**req_copy)

    def test_get_customization_request_by_id_value_error_with_retries(self):
        # Enable retries and run test_get_customization_request_by_id_value_error.
        _service.enable_retries()
        self.test_get_customization_request_by_id_value_error()

        # Disable retries and run test_get_customization_request_by_id_value_error.
        _service.disable_retries()
        self.test_get_customization_request_by_id_value_error()

class TestResizeCluster():
    """
    Test Class for resize_cluster
    """

    @responses.activate
    def test_resize_cluster_all_params(self):
        """
        resize_cluster()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/resize')
        mock_response = '{"request_id": "request_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest model
        resize_cluster_request_model = {}
        resize_cluster_request_model['compute_nodes_count'] = 38

        # Set up parameter values
        instance_guid = 'testString'
        body = resize_cluster_request_model

        # Invoke method
        response = _service.resize_cluster(
            instance_guid,
            body,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body == body

    def test_resize_cluster_all_params_with_retries(self):
        # Enable retries and run test_resize_cluster_all_params.
        _service.enable_retries()
        self.test_resize_cluster_all_params()

        # Disable retries and run test_resize_cluster_all_params.
        _service.disable_retries()
        self.test_resize_cluster_all_params()

    @responses.activate
    def test_resize_cluster_value_error(self):
        """
        test_resize_cluster_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/resize')
        mock_response = '{"request_id": "request_id"}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest model
        resize_cluster_request_model = {}
        resize_cluster_request_model['compute_nodes_count'] = 38

        # Set up parameter values
        instance_guid = 'testString'
        body = resize_cluster_request_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
            "body": body,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.resize_cluster(**req_copy)

    def test_resize_cluster_value_error_with_retries(self):
        # Enable retries and run test_resize_cluster_value_error.
        _service.enable_retries()
        self.test_resize_cluster_value_error()

        # Disable retries and run test_resize_cluster_value_error.
        _service.disable_retries()
        self.test_resize_cluster_value_error()

class TestResetClusterPassword():
    """
    Test Class for reset_cluster_password
    """

    @responses.activate
    def test_reset_cluster_password_all_params(self):
        """
        reset_cluster_password()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/reset_password')
        mock_response = '{"id": "id", "user_credentials": {"user": "user", "password": "password"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = _service.reset_cluster_password(
            instance_guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_reset_cluster_password_all_params_with_retries(self):
        # Enable retries and run test_reset_cluster_password_all_params.
        _service.enable_retries()
        self.test_reset_cluster_password_all_params()

        # Disable retries and run test_reset_cluster_password_all_params.
        _service.disable_retries()
        self.test_reset_cluster_password_all_params()

    @responses.activate
    def test_reset_cluster_password_value_error(self):
        """
        test_reset_cluster_password_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/reset_password')
        mock_response = '{"id": "id", "user_credentials": {"user": "user", "password": "password"}}'
        responses.add(responses.POST,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.reset_cluster_password(**req_copy)

    def test_reset_cluster_password_value_error_with_retries(self):
        # Enable retries and run test_reset_cluster_password_value_error.
        _service.enable_retries()
        self.test_reset_cluster_password_value_error()

        # Disable retries and run test_reset_cluster_password_value_error.
        _service.disable_retries()
        self.test_reset_cluster_password_value_error()

class TestConfigureLogging():
    """
    Test Class for configure_logging
    """

    @responses.activate
    def test_configure_logging_all_params(self):
        """
        configure_logging()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/log_config')
        responses.add(responses.PUT,
                      url,
                      status=202)

        # Construct a dict representation of a AnalyticsEngineLoggingNodeSpec model
        analytics_engine_logging_node_spec_model = {}
        analytics_engine_logging_node_spec_model['node_type'] = 'management'
        analytics_engine_logging_node_spec_model['components'] = ['ambari-server']

        # Construct a dict representation of a AnalyticsEngineLoggingServer model
        analytics_engine_logging_server_model = {}
        analytics_engine_logging_server_model['type'] = 'logdna'
        analytics_engine_logging_server_model['credential'] = 'testString'
        analytics_engine_logging_server_model['api_host'] = 'testString'
        analytics_engine_logging_server_model['log_host'] = 'testString'
        analytics_engine_logging_server_model['owner'] = 'testString'

        # Set up parameter values
        instance_guid = 'testString'
        log_specs = [analytics_engine_logging_node_spec_model]
        log_server = analytics_engine_logging_server_model

        # Invoke method
        response = _service.configure_logging(
            instance_guid,
            log_specs,
            log_server,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['log_specs'] == [analytics_engine_logging_node_spec_model]
        assert req_body['log_server'] == analytics_engine_logging_server_model

    def test_configure_logging_all_params_with_retries(self):
        # Enable retries and run test_configure_logging_all_params.
        _service.enable_retries()
        self.test_configure_logging_all_params()

        # Disable retries and run test_configure_logging_all_params.
        _service.disable_retries()
        self.test_configure_logging_all_params()

    @responses.activate
    def test_configure_logging_value_error(self):
        """
        test_configure_logging_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/log_config')
        responses.add(responses.PUT,
                      url,
                      status=202)

        # Construct a dict representation of a AnalyticsEngineLoggingNodeSpec model
        analytics_engine_logging_node_spec_model = {}
        analytics_engine_logging_node_spec_model['node_type'] = 'management'
        analytics_engine_logging_node_spec_model['components'] = ['ambari-server']

        # Construct a dict representation of a AnalyticsEngineLoggingServer model
        analytics_engine_logging_server_model = {}
        analytics_engine_logging_server_model['type'] = 'logdna'
        analytics_engine_logging_server_model['credential'] = 'testString'
        analytics_engine_logging_server_model['api_host'] = 'testString'
        analytics_engine_logging_server_model['log_host'] = 'testString'
        analytics_engine_logging_server_model['owner'] = 'testString'

        # Set up parameter values
        instance_guid = 'testString'
        log_specs = [analytics_engine_logging_node_spec_model]
        log_server = analytics_engine_logging_server_model

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
            "log_specs": log_specs,
            "log_server": log_server,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.configure_logging(**req_copy)

    def test_configure_logging_value_error_with_retries(self):
        # Enable retries and run test_configure_logging_value_error.
        _service.enable_retries()
        self.test_configure_logging_value_error()

        # Disable retries and run test_configure_logging_value_error.
        _service.disable_retries()
        self.test_configure_logging_value_error()

class TestGetLoggingConfig():
    """
    Test Class for get_logging_config
    """

    @responses.activate
    def test_get_logging_config_all_params(self):
        """
        get_logging_config()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/log_config')
        mock_response = '{"log_specs": [{"node_type": "management", "components": ["ambari-server"]}], "log_server": {"type": "logdna", "credential": "credential", "api_host": "api_host", "log_host": "log_host", "owner": "owner"}, "log_config_status": [{"node_type": "management", "node_id": "node_id", "action": "action", "status": "status"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = _service.get_logging_config(
            instance_guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200

    def test_get_logging_config_all_params_with_retries(self):
        # Enable retries and run test_get_logging_config_all_params.
        _service.enable_retries()
        self.test_get_logging_config_all_params()

        # Disable retries and run test_get_logging_config_all_params.
        _service.disable_retries()
        self.test_get_logging_config_all_params()

    @responses.activate
    def test_get_logging_config_value_error(self):
        """
        test_get_logging_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/log_config')
        mock_response = '{"log_specs": [{"node_type": "management", "components": ["ambari-server"]}], "log_server": {"type": "logdna", "credential": "credential", "api_host": "api_host", "log_host": "log_host", "owner": "owner"}, "log_config_status": [{"node_type": "management", "node_id": "node_id", "action": "action", "status": "status"}]}'
        responses.add(responses.GET,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.get_logging_config(**req_copy)

    def test_get_logging_config_value_error_with_retries(self):
        # Enable retries and run test_get_logging_config_value_error.
        _service.enable_retries()
        self.test_get_logging_config_value_error()

        # Disable retries and run test_get_logging_config_value_error.
        _service.disable_retries()
        self.test_get_logging_config_value_error()

class TestDeleteLoggingConfig():
    """
    Test Class for delete_logging_config
    """

    @responses.activate
    def test_delete_logging_config_all_params(self):
        """
        delete_logging_config()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/log_config')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = _service.delete_logging_config(
            instance_guid,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202

    def test_delete_logging_config_all_params_with_retries(self):
        # Enable retries and run test_delete_logging_config_all_params.
        _service.enable_retries()
        self.test_delete_logging_config_all_params()

        # Disable retries and run test_delete_logging_config_all_params.
        _service.disable_retries()
        self.test_delete_logging_config_all_params()

    @responses.activate
    def test_delete_logging_config_value_error(self):
        """
        test_delete_logging_config_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/log_config')
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        instance_guid = 'testString'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.delete_logging_config(**req_copy)

    def test_delete_logging_config_value_error_with_retries(self):
        # Enable retries and run test_delete_logging_config_value_error.
        _service.enable_retries()
        self.test_delete_logging_config_value_error()

        # Disable retries and run test_delete_logging_config_value_error.
        _service.disable_retries()
        self.test_delete_logging_config_value_error()

class TestUpdatePrivateEndpointWhitelist():
    """
    Test Class for update_private_endpoint_whitelist
    """

    @responses.activate
    def test_update_private_endpoint_whitelist_all_params(self):
        """
        update_private_endpoint_whitelist()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/private_endpoint_whitelist')
        mock_response = '{"private_endpoint_whitelist": ["private_endpoint_whitelist"]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'
        ip_ranges = ['testString']
        action = 'add'

        # Invoke method
        response = _service.update_private_endpoint_whitelist(
            instance_guid,
            ip_ranges,
            action,
            headers={}
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(str(responses.calls[0].request.body, 'utf-8'))
        assert req_body['ip_ranges'] == ['testString']
        assert req_body['action'] == 'add'

    def test_update_private_endpoint_whitelist_all_params_with_retries(self):
        # Enable retries and run test_update_private_endpoint_whitelist_all_params.
        _service.enable_retries()
        self.test_update_private_endpoint_whitelist_all_params()

        # Disable retries and run test_update_private_endpoint_whitelist_all_params.
        _service.disable_retries()
        self.test_update_private_endpoint_whitelist_all_params()

    @responses.activate
    def test_update_private_endpoint_whitelist_value_error(self):
        """
        test_update_private_endpoint_whitelist_value_error()
        """
        # Set up mock
        url = preprocess_url('/v2/analytics_engines/testString/private_endpoint_whitelist')
        mock_response = '{"private_endpoint_whitelist": ["private_endpoint_whitelist"]}'
        responses.add(responses.PATCH,
                      url,
                      body=mock_response,
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'
        ip_ranges = ['testString']
        action = 'add'

        # Pass in all but one required param and check for a ValueError
        req_param_dict = {
            "instance_guid": instance_guid,
            "ip_ranges": ip_ranges,
            "action": action,
        }
        for param in req_param_dict.keys():
            req_copy = {key:val if key is not param else None for (key,val) in req_param_dict.items()}
            with pytest.raises(ValueError):
                _service.update_private_endpoint_whitelist(**req_copy)

    def test_update_private_endpoint_whitelist_value_error_with_retries(self):
        # Enable retries and run test_update_private_endpoint_whitelist_value_error.
        _service.enable_retries()
        self.test_update_private_endpoint_whitelist_value_error()

        # Disable retries and run test_update_private_endpoint_whitelist_value_error.
        _service.disable_retries()
        self.test_update_private_endpoint_whitelist_value_error()

# endregion
##############################################################################
# End of Service: AnalyticsEnginesV2
##############################################################################


##############################################################################
# Start of Model Tests
##############################################################################
# region
class TestModel_AnalyticsEngine():
    """
    Test Class for AnalyticsEngine
    """

    def test_analytics_engine_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngine
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analytics_engine_cluster_node_model = {} # AnalyticsEngineClusterNode
        analytics_engine_cluster_node_model['id'] = 38
        analytics_engine_cluster_node_model['fqdn'] = 'testString'
        analytics_engine_cluster_node_model['type'] = 'testString'
        analytics_engine_cluster_node_model['state'] = 'testString'
        analytics_engine_cluster_node_model['public_ip'] = 'testString'
        analytics_engine_cluster_node_model['private_ip'] = 'testString'
        analytics_engine_cluster_node_model['state_change_time'] = '2019-01-01T12:00:00Z'
        analytics_engine_cluster_node_model['commission_time'] = '2019-01-01T12:00:00Z'

        analytics_engine_user_credentials_model = {} # AnalyticsEngineUserCredentials
        analytics_engine_user_credentials_model['user'] = 'testString'

        service_endpoints_model = {} # ServiceEndpoints
        service_endpoints_model['phoenix_jdbc'] = 'testString'
        service_endpoints_model['ambari_console'] = 'testString'
        service_endpoints_model['livy'] = 'testString'
        service_endpoints_model['spark_history_server'] = 'testString'
        service_endpoints_model['oozie_rest'] = 'testString'
        service_endpoints_model['hive_jdbc'] = 'testString'
        service_endpoints_model['notebook_gateway_websocket'] = 'testString'
        service_endpoints_model['notebook_gateway'] = 'testString'
        service_endpoints_model['webhdfs'] = 'testString'
        service_endpoints_model['ssh'] = 'testString'
        service_endpoints_model['spark_sql'] = 'testString'

        # Construct a json representation of a AnalyticsEngine model
        analytics_engine_model_json = {}
        analytics_engine_model_json['id'] = 'testString'
        analytics_engine_model_json['name'] = 'testString'
        analytics_engine_model_json['service_plan'] = 'testString'
        analytics_engine_model_json['hardware_size'] = 'testString'
        analytics_engine_model_json['software_package'] = 'testString'
        analytics_engine_model_json['domain'] = 'testString'
        analytics_engine_model_json['creation_time'] = '2019-01-01T12:00:00Z'
        analytics_engine_model_json['commision_time'] = '2019-01-01T12:00:00Z'
        analytics_engine_model_json['decommision_time'] = '2019-01-01T12:00:00Z'
        analytics_engine_model_json['deletion_time'] = '2019-01-01T12:00:00Z'
        analytics_engine_model_json['state_change_time'] = '2019-01-01T12:00:00Z'
        analytics_engine_model_json['state'] = 'testString'
        analytics_engine_model_json['nodes'] = [analytics_engine_cluster_node_model]
        analytics_engine_model_json['user_credentials'] = analytics_engine_user_credentials_model
        analytics_engine_model_json['service_endpoints'] = service_endpoints_model
        analytics_engine_model_json['service_endpoints_ip'] = service_endpoints_model
        analytics_engine_model_json['private_endpoint_whitelist'] = ['testString']

        # Construct a model instance of AnalyticsEngine by calling from_dict on the json representation
        analytics_engine_model = AnalyticsEngine.from_dict(analytics_engine_model_json)
        assert analytics_engine_model != False

        # Construct a model instance of AnalyticsEngine by calling from_dict on the json representation
        analytics_engine_model_dict = AnalyticsEngine.from_dict(analytics_engine_model_json).__dict__
        analytics_engine_model2 = AnalyticsEngine(**analytics_engine_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_model == analytics_engine_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_model_json2 = analytics_engine_model.to_dict()
        assert analytics_engine_model_json2 == analytics_engine_model_json

class TestModel_AnalyticsEngineClusterNode():
    """
    Test Class for AnalyticsEngineClusterNode
    """

    def test_analytics_engine_cluster_node_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineClusterNode
        """

        # Construct a json representation of a AnalyticsEngineClusterNode model
        analytics_engine_cluster_node_model_json = {}
        analytics_engine_cluster_node_model_json['id'] = 38
        analytics_engine_cluster_node_model_json['fqdn'] = 'testString'
        analytics_engine_cluster_node_model_json['type'] = 'testString'
        analytics_engine_cluster_node_model_json['state'] = 'testString'
        analytics_engine_cluster_node_model_json['public_ip'] = 'testString'
        analytics_engine_cluster_node_model_json['private_ip'] = 'testString'
        analytics_engine_cluster_node_model_json['state_change_time'] = '2019-01-01T12:00:00Z'
        analytics_engine_cluster_node_model_json['commission_time'] = '2019-01-01T12:00:00Z'

        # Construct a model instance of AnalyticsEngineClusterNode by calling from_dict on the json representation
        analytics_engine_cluster_node_model = AnalyticsEngineClusterNode.from_dict(analytics_engine_cluster_node_model_json)
        assert analytics_engine_cluster_node_model != False

        # Construct a model instance of AnalyticsEngineClusterNode by calling from_dict on the json representation
        analytics_engine_cluster_node_model_dict = AnalyticsEngineClusterNode.from_dict(analytics_engine_cluster_node_model_json).__dict__
        analytics_engine_cluster_node_model2 = AnalyticsEngineClusterNode(**analytics_engine_cluster_node_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_cluster_node_model == analytics_engine_cluster_node_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_cluster_node_model_json2 = analytics_engine_cluster_node_model.to_dict()
        assert analytics_engine_cluster_node_model_json2 == analytics_engine_cluster_node_model_json

class TestModel_AnalyticsEngineCreateCustomizationResponse():
    """
    Test Class for AnalyticsEngineCreateCustomizationResponse
    """

    def test_analytics_engine_create_customization_response_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineCreateCustomizationResponse
        """

        # Construct a json representation of a AnalyticsEngineCreateCustomizationResponse model
        analytics_engine_create_customization_response_model_json = {}
        analytics_engine_create_customization_response_model_json['request_id'] = 38

        # Construct a model instance of AnalyticsEngineCreateCustomizationResponse by calling from_dict on the json representation
        analytics_engine_create_customization_response_model = AnalyticsEngineCreateCustomizationResponse.from_dict(analytics_engine_create_customization_response_model_json)
        assert analytics_engine_create_customization_response_model != False

        # Construct a model instance of AnalyticsEngineCreateCustomizationResponse by calling from_dict on the json representation
        analytics_engine_create_customization_response_model_dict = AnalyticsEngineCreateCustomizationResponse.from_dict(analytics_engine_create_customization_response_model_json).__dict__
        analytics_engine_create_customization_response_model2 = AnalyticsEngineCreateCustomizationResponse(**analytics_engine_create_customization_response_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_create_customization_response_model == analytics_engine_create_customization_response_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_create_customization_response_model_json2 = analytics_engine_create_customization_response_model.to_dict()
        assert analytics_engine_create_customization_response_model_json2 == analytics_engine_create_customization_response_model_json

class TestModel_AnalyticsEngineCustomAction():
    """
    Test Class for AnalyticsEngineCustomAction
    """

    def test_analytics_engine_custom_action_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineCustomAction
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analytics_engine_custom_action_script_model = {} # AnalyticsEngineCustomActionScript
        analytics_engine_custom_action_script_model['source_type'] = 'http'
        analytics_engine_custom_action_script_model['script_path'] = 'testString'
        analytics_engine_custom_action_script_model['source_props'] = {'foo': 'bar'}

        # Construct a json representation of a AnalyticsEngineCustomAction model
        analytics_engine_custom_action_model_json = {}
        analytics_engine_custom_action_model_json['name'] = 'testString'
        analytics_engine_custom_action_model_json['type'] = 'bootstrap'
        analytics_engine_custom_action_model_json['script'] = analytics_engine_custom_action_script_model
        analytics_engine_custom_action_model_json['script_params'] = ['testString']

        # Construct a model instance of AnalyticsEngineCustomAction by calling from_dict on the json representation
        analytics_engine_custom_action_model = AnalyticsEngineCustomAction.from_dict(analytics_engine_custom_action_model_json)
        assert analytics_engine_custom_action_model != False

        # Construct a model instance of AnalyticsEngineCustomAction by calling from_dict on the json representation
        analytics_engine_custom_action_model_dict = AnalyticsEngineCustomAction.from_dict(analytics_engine_custom_action_model_json).__dict__
        analytics_engine_custom_action_model2 = AnalyticsEngineCustomAction(**analytics_engine_custom_action_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_custom_action_model == analytics_engine_custom_action_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_custom_action_model_json2 = analytics_engine_custom_action_model.to_dict()
        assert analytics_engine_custom_action_model_json2 == analytics_engine_custom_action_model_json

class TestModel_AnalyticsEngineCustomActionScript():
    """
    Test Class for AnalyticsEngineCustomActionScript
    """

    def test_analytics_engine_custom_action_script_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineCustomActionScript
        """

        # Construct a json representation of a AnalyticsEngineCustomActionScript model
        analytics_engine_custom_action_script_model_json = {}
        analytics_engine_custom_action_script_model_json['source_type'] = 'http'
        analytics_engine_custom_action_script_model_json['script_path'] = 'testString'
        analytics_engine_custom_action_script_model_json['source_props'] = {'foo': 'bar'}

        # Construct a model instance of AnalyticsEngineCustomActionScript by calling from_dict on the json representation
        analytics_engine_custom_action_script_model = AnalyticsEngineCustomActionScript.from_dict(analytics_engine_custom_action_script_model_json)
        assert analytics_engine_custom_action_script_model != False

        # Construct a model instance of AnalyticsEngineCustomActionScript by calling from_dict on the json representation
        analytics_engine_custom_action_script_model_dict = AnalyticsEngineCustomActionScript.from_dict(analytics_engine_custom_action_script_model_json).__dict__
        analytics_engine_custom_action_script_model2 = AnalyticsEngineCustomActionScript(**analytics_engine_custom_action_script_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_custom_action_script_model == analytics_engine_custom_action_script_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_custom_action_script_model_json2 = analytics_engine_custom_action_script_model.to_dict()
        assert analytics_engine_custom_action_script_model_json2 == analytics_engine_custom_action_script_model_json

class TestModel_AnalyticsEngineCustomizationRequestCollectionItem():
    """
    Test Class for AnalyticsEngineCustomizationRequestCollectionItem
    """

    def test_analytics_engine_customization_request_collection_item_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineCustomizationRequestCollectionItem
        """

        # Construct a json representation of a AnalyticsEngineCustomizationRequestCollectionItem model
        analytics_engine_customization_request_collection_item_model_json = {}
        analytics_engine_customization_request_collection_item_model_json['id'] = 'testString'

        # Construct a model instance of AnalyticsEngineCustomizationRequestCollectionItem by calling from_dict on the json representation
        analytics_engine_customization_request_collection_item_model = AnalyticsEngineCustomizationRequestCollectionItem.from_dict(analytics_engine_customization_request_collection_item_model_json)
        assert analytics_engine_customization_request_collection_item_model != False

        # Construct a model instance of AnalyticsEngineCustomizationRequestCollectionItem by calling from_dict on the json representation
        analytics_engine_customization_request_collection_item_model_dict = AnalyticsEngineCustomizationRequestCollectionItem.from_dict(analytics_engine_customization_request_collection_item_model_json).__dict__
        analytics_engine_customization_request_collection_item_model2 = AnalyticsEngineCustomizationRequestCollectionItem(**analytics_engine_customization_request_collection_item_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_customization_request_collection_item_model == analytics_engine_customization_request_collection_item_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_customization_request_collection_item_model_json2 = analytics_engine_customization_request_collection_item_model.to_dict()
        assert analytics_engine_customization_request_collection_item_model_json2 == analytics_engine_customization_request_collection_item_model_json

class TestModel_AnalyticsEngineCustomizationRunDetails():
    """
    Test Class for AnalyticsEngineCustomizationRunDetails
    """

    def test_analytics_engine_customization_run_details_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineCustomizationRunDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analytics_engine_node_level_customization_run_details_model = {} # AnalyticsEngineNodeLevelCustomizationRunDetails
        analytics_engine_node_level_customization_run_details_model['node_name'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['node_type'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['start_time'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['end_time'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['time_taken'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['status'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['log_file'] = 'testString'

        analytics_engine_customization_run_details_run_details_model = {} # AnalyticsEngineCustomizationRunDetailsRunDetails
        analytics_engine_customization_run_details_run_details_model['overall_status'] = 'testString'
        analytics_engine_customization_run_details_run_details_model['details'] = [analytics_engine_node_level_customization_run_details_model]

        # Construct a json representation of a AnalyticsEngineCustomizationRunDetails model
        analytics_engine_customization_run_details_model_json = {}
        analytics_engine_customization_run_details_model_json['id'] = 'testString'
        analytics_engine_customization_run_details_model_json['run_status'] = 'testString'
        analytics_engine_customization_run_details_model_json['run_details'] = analytics_engine_customization_run_details_run_details_model

        # Construct a model instance of AnalyticsEngineCustomizationRunDetails by calling from_dict on the json representation
        analytics_engine_customization_run_details_model = AnalyticsEngineCustomizationRunDetails.from_dict(analytics_engine_customization_run_details_model_json)
        assert analytics_engine_customization_run_details_model != False

        # Construct a model instance of AnalyticsEngineCustomizationRunDetails by calling from_dict on the json representation
        analytics_engine_customization_run_details_model_dict = AnalyticsEngineCustomizationRunDetails.from_dict(analytics_engine_customization_run_details_model_json).__dict__
        analytics_engine_customization_run_details_model2 = AnalyticsEngineCustomizationRunDetails(**analytics_engine_customization_run_details_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_customization_run_details_model == analytics_engine_customization_run_details_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_customization_run_details_model_json2 = analytics_engine_customization_run_details_model.to_dict()
        assert analytics_engine_customization_run_details_model_json2 == analytics_engine_customization_run_details_model_json

class TestModel_AnalyticsEngineCustomizationRunDetailsRunDetails():
    """
    Test Class for AnalyticsEngineCustomizationRunDetailsRunDetails
    """

    def test_analytics_engine_customization_run_details_run_details_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineCustomizationRunDetailsRunDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analytics_engine_node_level_customization_run_details_model = {} # AnalyticsEngineNodeLevelCustomizationRunDetails
        analytics_engine_node_level_customization_run_details_model['node_name'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['node_type'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['start_time'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['end_time'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['time_taken'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['status'] = 'testString'
        analytics_engine_node_level_customization_run_details_model['log_file'] = 'testString'

        # Construct a json representation of a AnalyticsEngineCustomizationRunDetailsRunDetails model
        analytics_engine_customization_run_details_run_details_model_json = {}
        analytics_engine_customization_run_details_run_details_model_json['overall_status'] = 'testString'
        analytics_engine_customization_run_details_run_details_model_json['details'] = [analytics_engine_node_level_customization_run_details_model]

        # Construct a model instance of AnalyticsEngineCustomizationRunDetailsRunDetails by calling from_dict on the json representation
        analytics_engine_customization_run_details_run_details_model = AnalyticsEngineCustomizationRunDetailsRunDetails.from_dict(analytics_engine_customization_run_details_run_details_model_json)
        assert analytics_engine_customization_run_details_run_details_model != False

        # Construct a model instance of AnalyticsEngineCustomizationRunDetailsRunDetails by calling from_dict on the json representation
        analytics_engine_customization_run_details_run_details_model_dict = AnalyticsEngineCustomizationRunDetailsRunDetails.from_dict(analytics_engine_customization_run_details_run_details_model_json).__dict__
        analytics_engine_customization_run_details_run_details_model2 = AnalyticsEngineCustomizationRunDetailsRunDetails(**analytics_engine_customization_run_details_run_details_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_customization_run_details_run_details_model == analytics_engine_customization_run_details_run_details_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_customization_run_details_run_details_model_json2 = analytics_engine_customization_run_details_run_details_model.to_dict()
        assert analytics_engine_customization_run_details_run_details_model_json2 == analytics_engine_customization_run_details_run_details_model_json

class TestModel_AnalyticsEngineLoggingConfigDetails():
    """
    Test Class for AnalyticsEngineLoggingConfigDetails
    """

    def test_analytics_engine_logging_config_details_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineLoggingConfigDetails
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analytics_engine_logging_node_spec_model = {} # AnalyticsEngineLoggingNodeSpec
        analytics_engine_logging_node_spec_model['node_type'] = 'management'
        analytics_engine_logging_node_spec_model['components'] = ['ambari-server']

        analytics_engine_logging_server_model = {} # AnalyticsEngineLoggingServer
        analytics_engine_logging_server_model['type'] = 'logdna'
        analytics_engine_logging_server_model['credential'] = 'testString'
        analytics_engine_logging_server_model['api_host'] = 'testString'
        analytics_engine_logging_server_model['log_host'] = 'testString'
        analytics_engine_logging_server_model['owner'] = 'testString'

        analytics_engine_logging_config_status_model = {} # AnalyticsEngineLoggingConfigStatus
        analytics_engine_logging_config_status_model['node_type'] = 'management'
        analytics_engine_logging_config_status_model['node_id'] = 'testString'
        analytics_engine_logging_config_status_model['action'] = 'testString'
        analytics_engine_logging_config_status_model['status'] = 'testString'

        # Construct a json representation of a AnalyticsEngineLoggingConfigDetails model
        analytics_engine_logging_config_details_model_json = {}
        analytics_engine_logging_config_details_model_json['log_specs'] = [analytics_engine_logging_node_spec_model]
        analytics_engine_logging_config_details_model_json['log_server'] = analytics_engine_logging_server_model
        analytics_engine_logging_config_details_model_json['log_config_status'] = [analytics_engine_logging_config_status_model]

        # Construct a model instance of AnalyticsEngineLoggingConfigDetails by calling from_dict on the json representation
        analytics_engine_logging_config_details_model = AnalyticsEngineLoggingConfigDetails.from_dict(analytics_engine_logging_config_details_model_json)
        assert analytics_engine_logging_config_details_model != False

        # Construct a model instance of AnalyticsEngineLoggingConfigDetails by calling from_dict on the json representation
        analytics_engine_logging_config_details_model_dict = AnalyticsEngineLoggingConfigDetails.from_dict(analytics_engine_logging_config_details_model_json).__dict__
        analytics_engine_logging_config_details_model2 = AnalyticsEngineLoggingConfigDetails(**analytics_engine_logging_config_details_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_logging_config_details_model == analytics_engine_logging_config_details_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_logging_config_details_model_json2 = analytics_engine_logging_config_details_model.to_dict()
        assert analytics_engine_logging_config_details_model_json2 == analytics_engine_logging_config_details_model_json

class TestModel_AnalyticsEngineLoggingConfigStatus():
    """
    Test Class for AnalyticsEngineLoggingConfigStatus
    """

    def test_analytics_engine_logging_config_status_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineLoggingConfigStatus
        """

        # Construct a json representation of a AnalyticsEngineLoggingConfigStatus model
        analytics_engine_logging_config_status_model_json = {}
        analytics_engine_logging_config_status_model_json['node_type'] = 'management'
        analytics_engine_logging_config_status_model_json['node_id'] = 'testString'
        analytics_engine_logging_config_status_model_json['action'] = 'testString'
        analytics_engine_logging_config_status_model_json['status'] = 'testString'

        # Construct a model instance of AnalyticsEngineLoggingConfigStatus by calling from_dict on the json representation
        analytics_engine_logging_config_status_model = AnalyticsEngineLoggingConfigStatus.from_dict(analytics_engine_logging_config_status_model_json)
        assert analytics_engine_logging_config_status_model != False

        # Construct a model instance of AnalyticsEngineLoggingConfigStatus by calling from_dict on the json representation
        analytics_engine_logging_config_status_model_dict = AnalyticsEngineLoggingConfigStatus.from_dict(analytics_engine_logging_config_status_model_json).__dict__
        analytics_engine_logging_config_status_model2 = AnalyticsEngineLoggingConfigStatus(**analytics_engine_logging_config_status_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_logging_config_status_model == analytics_engine_logging_config_status_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_logging_config_status_model_json2 = analytics_engine_logging_config_status_model.to_dict()
        assert analytics_engine_logging_config_status_model_json2 == analytics_engine_logging_config_status_model_json

class TestModel_AnalyticsEngineLoggingNodeSpec():
    """
    Test Class for AnalyticsEngineLoggingNodeSpec
    """

    def test_analytics_engine_logging_node_spec_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineLoggingNodeSpec
        """

        # Construct a json representation of a AnalyticsEngineLoggingNodeSpec model
        analytics_engine_logging_node_spec_model_json = {}
        analytics_engine_logging_node_spec_model_json['node_type'] = 'management'
        analytics_engine_logging_node_spec_model_json['components'] = ['ambari-server']

        # Construct a model instance of AnalyticsEngineLoggingNodeSpec by calling from_dict on the json representation
        analytics_engine_logging_node_spec_model = AnalyticsEngineLoggingNodeSpec.from_dict(analytics_engine_logging_node_spec_model_json)
        assert analytics_engine_logging_node_spec_model != False

        # Construct a model instance of AnalyticsEngineLoggingNodeSpec by calling from_dict on the json representation
        analytics_engine_logging_node_spec_model_dict = AnalyticsEngineLoggingNodeSpec.from_dict(analytics_engine_logging_node_spec_model_json).__dict__
        analytics_engine_logging_node_spec_model2 = AnalyticsEngineLoggingNodeSpec(**analytics_engine_logging_node_spec_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_logging_node_spec_model == analytics_engine_logging_node_spec_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_logging_node_spec_model_json2 = analytics_engine_logging_node_spec_model.to_dict()
        assert analytics_engine_logging_node_spec_model_json2 == analytics_engine_logging_node_spec_model_json

class TestModel_AnalyticsEngineLoggingServer():
    """
    Test Class for AnalyticsEngineLoggingServer
    """

    def test_analytics_engine_logging_server_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineLoggingServer
        """

        # Construct a json representation of a AnalyticsEngineLoggingServer model
        analytics_engine_logging_server_model_json = {}
        analytics_engine_logging_server_model_json['type'] = 'logdna'
        analytics_engine_logging_server_model_json['credential'] = 'testString'
        analytics_engine_logging_server_model_json['api_host'] = 'testString'
        analytics_engine_logging_server_model_json['log_host'] = 'testString'
        analytics_engine_logging_server_model_json['owner'] = 'testString'

        # Construct a model instance of AnalyticsEngineLoggingServer by calling from_dict on the json representation
        analytics_engine_logging_server_model = AnalyticsEngineLoggingServer.from_dict(analytics_engine_logging_server_model_json)
        assert analytics_engine_logging_server_model != False

        # Construct a model instance of AnalyticsEngineLoggingServer by calling from_dict on the json representation
        analytics_engine_logging_server_model_dict = AnalyticsEngineLoggingServer.from_dict(analytics_engine_logging_server_model_json).__dict__
        analytics_engine_logging_server_model2 = AnalyticsEngineLoggingServer(**analytics_engine_logging_server_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_logging_server_model == analytics_engine_logging_server_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_logging_server_model_json2 = analytics_engine_logging_server_model.to_dict()
        assert analytics_engine_logging_server_model_json2 == analytics_engine_logging_server_model_json

class TestModel_AnalyticsEngineNodeLevelCustomizationRunDetails():
    """
    Test Class for AnalyticsEngineNodeLevelCustomizationRunDetails
    """

    def test_analytics_engine_node_level_customization_run_details_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineNodeLevelCustomizationRunDetails
        """

        # Construct a json representation of a AnalyticsEngineNodeLevelCustomizationRunDetails model
        analytics_engine_node_level_customization_run_details_model_json = {}
        analytics_engine_node_level_customization_run_details_model_json['node_name'] = 'testString'
        analytics_engine_node_level_customization_run_details_model_json['node_type'] = 'testString'
        analytics_engine_node_level_customization_run_details_model_json['start_time'] = 'testString'
        analytics_engine_node_level_customization_run_details_model_json['end_time'] = 'testString'
        analytics_engine_node_level_customization_run_details_model_json['time_taken'] = 'testString'
        analytics_engine_node_level_customization_run_details_model_json['status'] = 'testString'
        analytics_engine_node_level_customization_run_details_model_json['log_file'] = 'testString'

        # Construct a model instance of AnalyticsEngineNodeLevelCustomizationRunDetails by calling from_dict on the json representation
        analytics_engine_node_level_customization_run_details_model = AnalyticsEngineNodeLevelCustomizationRunDetails.from_dict(analytics_engine_node_level_customization_run_details_model_json)
        assert analytics_engine_node_level_customization_run_details_model != False

        # Construct a model instance of AnalyticsEngineNodeLevelCustomizationRunDetails by calling from_dict on the json representation
        analytics_engine_node_level_customization_run_details_model_dict = AnalyticsEngineNodeLevelCustomizationRunDetails.from_dict(analytics_engine_node_level_customization_run_details_model_json).__dict__
        analytics_engine_node_level_customization_run_details_model2 = AnalyticsEngineNodeLevelCustomizationRunDetails(**analytics_engine_node_level_customization_run_details_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_node_level_customization_run_details_model == analytics_engine_node_level_customization_run_details_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_node_level_customization_run_details_model_json2 = analytics_engine_node_level_customization_run_details_model.to_dict()
        assert analytics_engine_node_level_customization_run_details_model_json2 == analytics_engine_node_level_customization_run_details_model_json

class TestModel_AnalyticsEngineResetClusterPasswordResponse():
    """
    Test Class for AnalyticsEngineResetClusterPasswordResponse
    """

    def test_analytics_engine_reset_cluster_password_response_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineResetClusterPasswordResponse
        """

        # Construct dict forms of any model objects needed in order to build this model.

        analytics_engine_reset_cluster_password_response_user_credentials_model = {} # AnalyticsEngineResetClusterPasswordResponseUserCredentials
        analytics_engine_reset_cluster_password_response_user_credentials_model['user'] = 'testString'
        analytics_engine_reset_cluster_password_response_user_credentials_model['password'] = 'testString'

        # Construct a json representation of a AnalyticsEngineResetClusterPasswordResponse model
        analytics_engine_reset_cluster_password_response_model_json = {}
        analytics_engine_reset_cluster_password_response_model_json['id'] = 'testString'
        analytics_engine_reset_cluster_password_response_model_json['user_credentials'] = analytics_engine_reset_cluster_password_response_user_credentials_model

        # Construct a model instance of AnalyticsEngineResetClusterPasswordResponse by calling from_dict on the json representation
        analytics_engine_reset_cluster_password_response_model = AnalyticsEngineResetClusterPasswordResponse.from_dict(analytics_engine_reset_cluster_password_response_model_json)
        assert analytics_engine_reset_cluster_password_response_model != False

        # Construct a model instance of AnalyticsEngineResetClusterPasswordResponse by calling from_dict on the json representation
        analytics_engine_reset_cluster_password_response_model_dict = AnalyticsEngineResetClusterPasswordResponse.from_dict(analytics_engine_reset_cluster_password_response_model_json).__dict__
        analytics_engine_reset_cluster_password_response_model2 = AnalyticsEngineResetClusterPasswordResponse(**analytics_engine_reset_cluster_password_response_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_reset_cluster_password_response_model == analytics_engine_reset_cluster_password_response_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_reset_cluster_password_response_model_json2 = analytics_engine_reset_cluster_password_response_model.to_dict()
        assert analytics_engine_reset_cluster_password_response_model_json2 == analytics_engine_reset_cluster_password_response_model_json

class TestModel_AnalyticsEngineResetClusterPasswordResponseUserCredentials():
    """
    Test Class for AnalyticsEngineResetClusterPasswordResponseUserCredentials
    """

    def test_analytics_engine_reset_cluster_password_response_user_credentials_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineResetClusterPasswordResponseUserCredentials
        """

        # Construct a json representation of a AnalyticsEngineResetClusterPasswordResponseUserCredentials model
        analytics_engine_reset_cluster_password_response_user_credentials_model_json = {}
        analytics_engine_reset_cluster_password_response_user_credentials_model_json['user'] = 'testString'
        analytics_engine_reset_cluster_password_response_user_credentials_model_json['password'] = 'testString'

        # Construct a model instance of AnalyticsEngineResetClusterPasswordResponseUserCredentials by calling from_dict on the json representation
        analytics_engine_reset_cluster_password_response_user_credentials_model = AnalyticsEngineResetClusterPasswordResponseUserCredentials.from_dict(analytics_engine_reset_cluster_password_response_user_credentials_model_json)
        assert analytics_engine_reset_cluster_password_response_user_credentials_model != False

        # Construct a model instance of AnalyticsEngineResetClusterPasswordResponseUserCredentials by calling from_dict on the json representation
        analytics_engine_reset_cluster_password_response_user_credentials_model_dict = AnalyticsEngineResetClusterPasswordResponseUserCredentials.from_dict(analytics_engine_reset_cluster_password_response_user_credentials_model_json).__dict__
        analytics_engine_reset_cluster_password_response_user_credentials_model2 = AnalyticsEngineResetClusterPasswordResponseUserCredentials(**analytics_engine_reset_cluster_password_response_user_credentials_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_reset_cluster_password_response_user_credentials_model == analytics_engine_reset_cluster_password_response_user_credentials_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_reset_cluster_password_response_user_credentials_model_json2 = analytics_engine_reset_cluster_password_response_user_credentials_model.to_dict()
        assert analytics_engine_reset_cluster_password_response_user_credentials_model_json2 == analytics_engine_reset_cluster_password_response_user_credentials_model_json

class TestModel_AnalyticsEngineResizeClusterResponse():
    """
    Test Class for AnalyticsEngineResizeClusterResponse
    """

    def test_analytics_engine_resize_cluster_response_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineResizeClusterResponse
        """

        # Construct a json representation of a AnalyticsEngineResizeClusterResponse model
        analytics_engine_resize_cluster_response_model_json = {}
        analytics_engine_resize_cluster_response_model_json['request_id'] = 'testString'

        # Construct a model instance of AnalyticsEngineResizeClusterResponse by calling from_dict on the json representation
        analytics_engine_resize_cluster_response_model = AnalyticsEngineResizeClusterResponse.from_dict(analytics_engine_resize_cluster_response_model_json)
        assert analytics_engine_resize_cluster_response_model != False

        # Construct a model instance of AnalyticsEngineResizeClusterResponse by calling from_dict on the json representation
        analytics_engine_resize_cluster_response_model_dict = AnalyticsEngineResizeClusterResponse.from_dict(analytics_engine_resize_cluster_response_model_json).__dict__
        analytics_engine_resize_cluster_response_model2 = AnalyticsEngineResizeClusterResponse(**analytics_engine_resize_cluster_response_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_resize_cluster_response_model == analytics_engine_resize_cluster_response_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_resize_cluster_response_model_json2 = analytics_engine_resize_cluster_response_model.to_dict()
        assert analytics_engine_resize_cluster_response_model_json2 == analytics_engine_resize_cluster_response_model_json

class TestModel_AnalyticsEngineState():
    """
    Test Class for AnalyticsEngineState
    """

    def test_analytics_engine_state_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineState
        """

        # Construct a json representation of a AnalyticsEngineState model
        analytics_engine_state_model_json = {}
        analytics_engine_state_model_json['state'] = 'testString'

        # Construct a model instance of AnalyticsEngineState by calling from_dict on the json representation
        analytics_engine_state_model = AnalyticsEngineState.from_dict(analytics_engine_state_model_json)
        assert analytics_engine_state_model != False

        # Construct a model instance of AnalyticsEngineState by calling from_dict on the json representation
        analytics_engine_state_model_dict = AnalyticsEngineState.from_dict(analytics_engine_state_model_json).__dict__
        analytics_engine_state_model2 = AnalyticsEngineState(**analytics_engine_state_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_state_model == analytics_engine_state_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_state_model_json2 = analytics_engine_state_model.to_dict()
        assert analytics_engine_state_model_json2 == analytics_engine_state_model_json

class TestModel_AnalyticsEngineUserCredentials():
    """
    Test Class for AnalyticsEngineUserCredentials
    """

    def test_analytics_engine_user_credentials_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineUserCredentials
        """

        # Construct a json representation of a AnalyticsEngineUserCredentials model
        analytics_engine_user_credentials_model_json = {}
        analytics_engine_user_credentials_model_json['user'] = 'testString'

        # Construct a model instance of AnalyticsEngineUserCredentials by calling from_dict on the json representation
        analytics_engine_user_credentials_model = AnalyticsEngineUserCredentials.from_dict(analytics_engine_user_credentials_model_json)
        assert analytics_engine_user_credentials_model != False

        # Construct a model instance of AnalyticsEngineUserCredentials by calling from_dict on the json representation
        analytics_engine_user_credentials_model_dict = AnalyticsEngineUserCredentials.from_dict(analytics_engine_user_credentials_model_json).__dict__
        analytics_engine_user_credentials_model2 = AnalyticsEngineUserCredentials(**analytics_engine_user_credentials_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_user_credentials_model == analytics_engine_user_credentials_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_user_credentials_model_json2 = analytics_engine_user_credentials_model.to_dict()
        assert analytics_engine_user_credentials_model_json2 == analytics_engine_user_credentials_model_json

class TestModel_AnalyticsEngineWhitelistResponse():
    """
    Test Class for AnalyticsEngineWhitelistResponse
    """

    def test_analytics_engine_whitelist_response_serialization(self):
        """
        Test serialization/deserialization for AnalyticsEngineWhitelistResponse
        """

        # Construct a json representation of a AnalyticsEngineWhitelistResponse model
        analytics_engine_whitelist_response_model_json = {}
        analytics_engine_whitelist_response_model_json['private_endpoint_whitelist'] = ['testString']

        # Construct a model instance of AnalyticsEngineWhitelistResponse by calling from_dict on the json representation
        analytics_engine_whitelist_response_model = AnalyticsEngineWhitelistResponse.from_dict(analytics_engine_whitelist_response_model_json)
        assert analytics_engine_whitelist_response_model != False

        # Construct a model instance of AnalyticsEngineWhitelistResponse by calling from_dict on the json representation
        analytics_engine_whitelist_response_model_dict = AnalyticsEngineWhitelistResponse.from_dict(analytics_engine_whitelist_response_model_json).__dict__
        analytics_engine_whitelist_response_model2 = AnalyticsEngineWhitelistResponse(**analytics_engine_whitelist_response_model_dict)

        # Verify the model instances are equivalent
        assert analytics_engine_whitelist_response_model == analytics_engine_whitelist_response_model2

        # Convert model instance back to dict and verify no loss of data
        analytics_engine_whitelist_response_model_json2 = analytics_engine_whitelist_response_model.to_dict()
        assert analytics_engine_whitelist_response_model_json2 == analytics_engine_whitelist_response_model_json

class TestModel_ServiceEndpoints():
    """
    Test Class for ServiceEndpoints
    """

    def test_service_endpoints_serialization(self):
        """
        Test serialization/deserialization for ServiceEndpoints
        """

        # Construct a json representation of a ServiceEndpoints model
        service_endpoints_model_json = {}
        service_endpoints_model_json['phoenix_jdbc'] = 'testString'
        service_endpoints_model_json['ambari_console'] = 'testString'
        service_endpoints_model_json['livy'] = 'testString'
        service_endpoints_model_json['spark_history_server'] = 'testString'
        service_endpoints_model_json['oozie_rest'] = 'testString'
        service_endpoints_model_json['hive_jdbc'] = 'testString'
        service_endpoints_model_json['notebook_gateway_websocket'] = 'testString'
        service_endpoints_model_json['notebook_gateway'] = 'testString'
        service_endpoints_model_json['webhdfs'] = 'testString'
        service_endpoints_model_json['ssh'] = 'testString'
        service_endpoints_model_json['spark_sql'] = 'testString'

        # Construct a model instance of ServiceEndpoints by calling from_dict on the json representation
        service_endpoints_model = ServiceEndpoints.from_dict(service_endpoints_model_json)
        assert service_endpoints_model != False

        # Construct a model instance of ServiceEndpoints by calling from_dict on the json representation
        service_endpoints_model_dict = ServiceEndpoints.from_dict(service_endpoints_model_json).__dict__
        service_endpoints_model2 = ServiceEndpoints(**service_endpoints_model_dict)

        # Verify the model instances are equivalent
        assert service_endpoints_model == service_endpoints_model2

        # Convert model instance back to dict and verify no loss of data
        service_endpoints_model_json2 = service_endpoints_model.to_dict()
        assert service_endpoints_model_json2 == service_endpoints_model_json

class TestModel_ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest():
    """
    Test Class for ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest
    """

    def test_resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_serialization(self):
        """
        Test serialization/deserialization for ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest
        """

        # Construct a json representation of a ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest model
        resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_json = {}
        resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_json['compute_nodes_count'] = 38

        # Construct a model instance of ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest by calling from_dict on the json representation
        resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model = ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest.from_dict(resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_json)
        assert resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model != False

        # Construct a model instance of ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest by calling from_dict on the json representation
        resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_dict = ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest.from_dict(resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_json).__dict__
        resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model2 = ResizeClusterRequestAnalyticsEngineResizeClusterByComputeNodesRequest(**resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_dict)

        # Verify the model instances are equivalent
        assert resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model == resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model2

        # Convert model instance back to dict and verify no loss of data
        resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_json2 = resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model.to_dict()
        assert resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_json2 == resize_cluster_request_analytics_engine_resize_cluster_by_compute_nodes_request_model_json

class TestModel_ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest():
    """
    Test Class for ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest
    """

    def test_resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_serialization(self):
        """
        Test serialization/deserialization for ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest
        """

        # Construct a json representation of a ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest model
        resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_json = {}
        resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_json['task_nodes_count'] = 38

        # Construct a model instance of ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest by calling from_dict on the json representation
        resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model = ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest.from_dict(resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_json)
        assert resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model != False

        # Construct a model instance of ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest by calling from_dict on the json representation
        resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_dict = ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest.from_dict(resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_json).__dict__
        resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model2 = ResizeClusterRequestAnalyticsEngineResizeClusterByTaskNodesRequest(**resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_dict)

        # Verify the model instances are equivalent
        assert resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model == resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model2

        # Convert model instance back to dict and verify no loss of data
        resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_json2 = resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model.to_dict()
        assert resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_json2 == resize_cluster_request_analytics_engine_resize_cluster_by_task_nodes_request_model_json


# endregion
##############################################################################
# End of Model Tests
##############################################################################
