# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2020.
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

from datetime import datetime, timezone
from ibm_cloud_sdk_core.authenticators.no_auth_authenticator import NoAuthAuthenticator
import inspect
import json
import pytest
import responses
from iaesdk.ibm_analytics_engine_api_v2 import *


service = IbmAnalyticsEngineApiV2(
    authenticator=NoAuthAuthenticator()
    )

base_url = 'https://gateway.watsonplatform.net/'
service.set_service_url(base_url)

##############################################################################
# Start of Service: AnalyticsEngines
##############################################################################
# region

#-----------------------------------------------------------------------------
# Test Class for analytics_engines_get
#-----------------------------------------------------------------------------
class TestAnalyticsEnginesGet():

    #--------------------------------------------------------
    # analytics_engines_get()
    #--------------------------------------------------------
    @responses.activate
    def test_analytics_engines_get_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Invoke method
        response = service.analytics_engines_get()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_analytics_engines_get_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_analytics_engines_get_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines'
        responses.add(responses.GET,
                      url,
                      status=200)

        # Invoke method
        response = service.analytics_engines_get()


        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_analytics_engine_by_id
#-----------------------------------------------------------------------------
class TestGetAnalyticsEngineById():

    #--------------------------------------------------------
    # get_analytics_engine_by_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_analytics_engine_by_id_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString'
        mock_response = '{"id": "id", "name": "name", "service_plan": "service_plan", "hardware_size": "hardware_size", "software_package": "software_package", "domain": "domain", "creation_time": "2019-01-01T12:00:00", "commision_time": "2019-01-01T12:00:00", "decommision_time": "2019-01-01T12:00:00", "deletion_time": "2019-01-01T12:00:00", "state_change_time": "2019-01-01T12:00:00", "state": "state", "nodes": [{"id": "id", "fqdn": "fqdn", "type": "type", "state": "state", "public_ip": "public_ip", "private_ip": "private_ip", "state_change_time": "2019-01-01T12:00:00", "commission_time": "2019-01-01T12:00:00"}], "user_credentials": {"user": "user"}, "service_endpoints": {"phoenix_jdbc": "phoenix_jdbc", "ambari_console": "ambari_console", "livy": "livy", "spark_history_server": "spark_history_server", "oozie_rest": "oozie_rest", "hive_jdbc": "hive_jdbc", "notebook_gateway_websocket": "notebook_gateway_websocket", "notebook_gateway": "notebook_gateway", "webhdfs": "webhdfs", "ssh": "ssh", "spark_sql": "spark_sql"}, "service_endpoints_ip": {"phoenix_jdbc": "phoenix_jdbc", "ambari_console": "ambari_console", "livy": "livy", "spark_history_server": "spark_history_server", "oozie_rest": "oozie_rest", "hive_jdbc": "hive_jdbc", "notebook_gateway_websocket": "notebook_gateway_websocket", "notebook_gateway": "notebook_gateway", "webhdfs": "webhdfs", "ssh": "ssh", "spark_sql": "spark_sql"}}'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.get_analytics_engine_by_id(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_analytics_engine_by_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_analytics_engine_by_id_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString'
        mock_response = '{"id": "id", "name": "name", "service_plan": "service_plan", "hardware_size": "hardware_size", "software_package": "software_package", "domain": "domain", "creation_time": "2019-01-01T12:00:00", "commision_time": "2019-01-01T12:00:00", "decommision_time": "2019-01-01T12:00:00", "deletion_time": "2019-01-01T12:00:00", "state_change_time": "2019-01-01T12:00:00", "state": "state", "nodes": [{"id": "id", "fqdn": "fqdn", "type": "type", "state": "state", "public_ip": "public_ip", "private_ip": "private_ip", "state_change_time": "2019-01-01T12:00:00", "commission_time": "2019-01-01T12:00:00"}], "user_credentials": {"user": "user"}, "service_endpoints": {"phoenix_jdbc": "phoenix_jdbc", "ambari_console": "ambari_console", "livy": "livy", "spark_history_server": "spark_history_server", "oozie_rest": "oozie_rest", "hive_jdbc": "hive_jdbc", "notebook_gateway_websocket": "notebook_gateway_websocket", "notebook_gateway": "notebook_gateway", "webhdfs": "webhdfs", "ssh": "ssh", "spark_sql": "spark_sql"}, "service_endpoints_ip": {"phoenix_jdbc": "phoenix_jdbc", "ambari_console": "ambari_console", "livy": "livy", "spark_history_server": "spark_history_server", "oozie_rest": "oozie_rest", "hive_jdbc": "hive_jdbc", "notebook_gateway_websocket": "notebook_gateway_websocket", "notebook_gateway": "notebook_gateway", "webhdfs": "webhdfs", "ssh": "ssh", "spark_sql": "spark_sql"}}'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.get_analytics_engine_by_id(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_analytics_engine_state_by_id
#-----------------------------------------------------------------------------
class TestGetAnalyticsEngineStateById():

    #--------------------------------------------------------
    # get_analytics_engine_state_by_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_analytics_engine_state_by_id_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/state'
        mock_response = '{"state": "state"}'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.get_analytics_engine_state_by_id(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_analytics_engine_state_by_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_analytics_engine_state_by_id_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/state'
        mock_response = '{"state": "state"}'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.get_analytics_engine_state_by_id(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for create_customization_request
#-----------------------------------------------------------------------------
class TestCreateCustomizationRequest():

    #--------------------------------------------------------
    # create_customization_request()
    #--------------------------------------------------------
    @responses.activate
    def test_create_customization_request_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/customization_requests'
        mock_response = '{"request_id": "request_id"}'
        responses.add(responses.POST,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AnalyticsEngineCustomActionScript model
        analytics_engine_custom_action_script_model =  {
            'source_type': 'http',
            'script_path': 'testString',
            'source_props': 'unknown type: object'
        }
        # Construct a dict representation of a AnalyticsEngineCustomAction model
        analytics_engine_custom_action_model =  {
            'name': 'testString',
            'type': 'bootstrap',
            'script': analytics_engine_custom_action_script_model,
            'script_params': ['testString']
        }

        # Set up parameter values
        instance_guid = 'testString'
        target = 'all'
        custom_actions = [analytics_engine_custom_action_model]

        # Invoke method
        response = service.create_customization_request(
            instance_guid,
            target,
            custom_actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(responses.calls[0].request.body)
        assert req_body['target'] == target
        assert req_body['custom_actions'] == custom_actions


    #--------------------------------------------------------
    # test_create_customization_request_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_create_customization_request_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/customization_requests'
        mock_response = '{"request_id": "request_id"}'
        responses.add(responses.POST,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Construct a dict representation of a AnalyticsEngineCustomActionScript model
        analytics_engine_custom_action_script_model =  {
            'source_type': 'http',
            'script_path': 'testString',
            'source_props': 'unknown type: object'
        }
        # Construct a dict representation of a AnalyticsEngineCustomAction model
        analytics_engine_custom_action_model =  {
            'name': 'testString',
            'type': 'bootstrap',
            'script': analytics_engine_custom_action_script_model,
            'script_params': ['testString']
        }

        # Set up parameter values
        instance_guid = 'testString'
        target = 'all'
        custom_actions = [analytics_engine_custom_action_model]

        # Invoke method
        response = service.create_customization_request(
            instance_guid,
            target,
            custom_actions,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(responses.calls[0].request.body)
        assert req_body['target'] == target
        assert req_body['custom_actions'] == custom_actions


#-----------------------------------------------------------------------------
# Test Class for get_all_customization_requests
#-----------------------------------------------------------------------------
class TestGetAllCustomizationRequests():

    #--------------------------------------------------------
    # get_all_customization_requests()
    #--------------------------------------------------------
    @responses.activate
    def test_get_all_customization_requests_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/customization_requests'
        mock_response = '[{}]'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.get_all_customization_requests(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_all_customization_requests_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_all_customization_requests_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/customization_requests'
        mock_response = '[{}]'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.get_all_customization_requests(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for get_customization_request_by_id
#-----------------------------------------------------------------------------
class TestGetCustomizationRequestById():

    #--------------------------------------------------------
    # get_customization_request_by_id()
    #--------------------------------------------------------
    @responses.activate
    def test_get_customization_request_by_id_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/customization_requests/testString'
        mock_response = '{"id": "id", "run_status": "run_status", "run_details": {"overall_status": "overall_status", "details": [{"node_name": "node_name", "node_type": "node_type", "start_time": "start_time", "end_time": "end_time", "time_taken": "time_taken", "status": "status", "log_file": "log_file"}]}}'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'
        request_id = 'testString'

        # Invoke method
        response = service.get_customization_request_by_id(
            instance_guid,
            request_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_customization_request_by_id_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_customization_request_by_id_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/customization_requests/testString'
        mock_response = '{"id": "id", "run_status": "run_status", "run_details": {"overall_status": "overall_status", "details": [{"node_name": "node_name", "node_type": "node_type", "start_time": "start_time", "end_time": "end_time", "time_taken": "time_taken", "status": "status", "log_file": "log_file"}]}}'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'
        request_id = 'testString'

        # Invoke method
        response = service.get_customization_request_by_id(
            instance_guid,
            request_id
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for resize_cluster
#-----------------------------------------------------------------------------
class TestResizeCluster():

    #--------------------------------------------------------
    # resize_cluster()
    #--------------------------------------------------------
    @responses.activate
    def test_resize_cluster_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/resize'
        mock_response = '{"request_id": "request_id"}'
        responses.add(responses.POST,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'
        compute_nodes_count = 38

        # Invoke method
        response = service.resize_cluster(
            instance_guid,
            compute_nodes_count=compute_nodes_count,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(responses.calls[0].request.body)
        assert req_body['compute_nodes_count'] == compute_nodes_count


    #--------------------------------------------------------
    # test_resize_cluster_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_resize_cluster_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/resize'
        mock_response = '{"request_id": "request_id"}'
        responses.add(responses.POST,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'
        compute_nodes_count = 38

        # Invoke method
        response = service.resize_cluster(
            instance_guid,
            compute_nodes_count=compute_nodes_count,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200
        # Validate body params
        req_body = json.loads(responses.calls[0].request.body)
        assert req_body['compute_nodes_count'] == compute_nodes_count


#-----------------------------------------------------------------------------
# Test Class for reset_cluster_password
#-----------------------------------------------------------------------------
class TestResetClusterPassword():

    #--------------------------------------------------------
    # reset_cluster_password()
    #--------------------------------------------------------
    @responses.activate
    def test_reset_cluster_password_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/reset_password'
        mock_response = '{"id": "id", "user_credentials": {"user": "user", "password": "password"}}'
        responses.add(responses.POST,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.reset_cluster_password(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_reset_cluster_password_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_reset_cluster_password_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/reset_password'
        mock_response = '{"id": "id", "user_credentials": {"user": "user", "password": "password"}}'
        responses.add(responses.POST,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.reset_cluster_password(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for configure_logging
#-----------------------------------------------------------------------------
class TestConfigureLogging():

    #--------------------------------------------------------
    # configure_logging()
    #--------------------------------------------------------
    @responses.activate
    def test_configure_logging_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/log_config'
        responses.add(responses.PUT,
                      url,
                      status=202)

        # Construct a dict representation of a AnalyticsEngineLoggingNodeSpec model
        analytics_engine_logging_node_spec_model =  {
            'node_type': 'management',
            'components': ['ambari-server']
        }
        # Construct a dict representation of a AnalyticsEngineLoggingServer model
        analytics_engine_logging_server_model =  {
            'type': 'logdna',
            'credential': 'testString',
            'api_host': 'testString',
            'log_host': 'testString',
            'owner': 'testString'
        }

        # Set up parameter values
        instance_guid = 'testString'
        log_specs = [analytics_engine_logging_node_spec_model]
        log_server = analytics_engine_logging_server_model

        # Invoke method
        response = service.configure_logging(
            instance_guid,
            log_specs,
            log_server,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(responses.calls[0].request.body)
        assert req_body['log_specs'] == log_specs
        assert req_body['log_server'] == log_server


    #--------------------------------------------------------
    # test_configure_logging_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_configure_logging_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/log_config'
        responses.add(responses.PUT,
                      url,
                      status=202)

        # Construct a dict representation of a AnalyticsEngineLoggingNodeSpec model
        analytics_engine_logging_node_spec_model =  {
            'node_type': 'management',
            'components': ['ambari-server']
        }
        # Construct a dict representation of a AnalyticsEngineLoggingServer model
        analytics_engine_logging_server_model =  {
            'type': 'logdna',
            'credential': 'testString',
            'api_host': 'testString',
            'log_host': 'testString',
            'owner': 'testString'
        }

        # Set up parameter values
        instance_guid = 'testString'
        log_specs = [analytics_engine_logging_node_spec_model]
        log_server = analytics_engine_logging_server_model

        # Invoke method
        response = service.configure_logging(
            instance_guid,
            log_specs,
            log_server,
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202
        # Validate body params
        req_body = json.loads(responses.calls[0].request.body)
        assert req_body['log_specs'] == log_specs
        assert req_body['log_server'] == log_server


#-----------------------------------------------------------------------------
# Test Class for get_logging_config
#-----------------------------------------------------------------------------
class TestGetLoggingConfig():

    #--------------------------------------------------------
    # get_logging_config()
    #--------------------------------------------------------
    @responses.activate
    def test_get_logging_config_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/log_config'
        mock_response = '{"log_specs": [{"node_type": "management", "components": ["ambari-server"]}], "log_server": {"type": "logdna", "credential": "credential", "api_host": "api_host", "log_host": "log_host", "owner": "owner"}, "log_config_status": [{"node_type": "management", "node_id": "node_id", "action": "action", "status": "status"}]}'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.get_logging_config(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


    #--------------------------------------------------------
    # test_get_logging_config_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_get_logging_config_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/log_config'
        mock_response = '{"log_specs": [{"node_type": "management", "components": ["ambari-server"]}], "log_server": {"type": "logdna", "credential": "credential", "api_host": "api_host", "log_host": "log_host", "owner": "owner"}, "log_config_status": [{"node_type": "management", "node_id": "node_id", "action": "action", "status": "status"}]}'
        responses.add(responses.GET,
                      url,
                      body=json.dumps(mock_response),
                      content_type='application/json',
                      status=200)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.get_logging_config(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 200


#-----------------------------------------------------------------------------
# Test Class for delete_logging_config
#-----------------------------------------------------------------------------
class TestDeleteLoggingConfig():

    #--------------------------------------------------------
    # delete_logging_config()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_logging_config_all_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/log_config'
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.delete_logging_config(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


    #--------------------------------------------------------
    # test_delete_logging_config_required_params()
    #--------------------------------------------------------
    @responses.activate
    def test_delete_logging_config_required_params(self):
        # Set up mock
        url = base_url + '/v2/analytics_engines/testString/log_config'
        responses.add(responses.DELETE,
                      url,
                      status=202)

        # Set up parameter values
        instance_guid = 'testString'

        # Invoke method
        response = service.delete_logging_config(
            instance_guid
        )

        # Check for correct operation
        assert len(responses.calls) == 1
        assert response.status_code == 202


# endregion
##############################################################################
# End of Service: AnalyticsEngines
##############################################################################

