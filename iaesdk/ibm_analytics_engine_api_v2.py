# coding: utf-8

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

"""
With IBM Analytics Engine you can create Apache Spark and Apache Hadoop clusters and
customize these clusters by using scripts. You can work with data in IBM Cloud Object
Storage, as well as integrate other Watson Data Platform services like IBM Watson Studio
and Machine Learning.
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class IbmAnalyticsEngineApiV2(BaseService):
    """The IBM Analytics Engine API V2 service."""

    DEFAULT_SERVICE_URL = 'https://ibm-analytics-engine-api.cloud.ibm.com/'
    DEFAULT_SERVICE_NAME = 'ibm_analytics_engine_api'

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'IbmAnalyticsEngineApiV2':
        """
        Return a new client for the IBM Analytics Engine API service using the
               specified parameters and external configuration.
        """
        authenticator = get_authenticator_from_environment(service_name)
        service = cls(
            authenticator
            )
        service.configure_service(service_name)
        return service

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the IBM Analytics Engine API service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/master/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Analytics Engines
    #########################


    def get_all_analytics_engines(self, **kwargs) -> DetailedResponse:
        """
        List all Analytics Engines.

        Currently, you cannot fetch the list of all IBM Analytics Engine service instances
        through this REST API. You should use the IBM Cloud CLI instead.  For example,
        ```ibmcloud resource service-instances --service-name ibmanalyticsengine```.

        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_all_analytics_engines')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines'
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_analytics_engine_by_id(self, instance_guid: str, **kwargs) -> DetailedResponse:
        """
        Get details of Analytics Engine.

        Retrieves the following details of the IBM Analytics Engine service instance:
        * Hardware size and software package
         * Timestamps at which the cluster was created, deleted or updated
         * Service endpoint URLs
         **NOTE:** No credentials are returned. You can get the IBM Analytics Engine
        service instance credentials by invoking the reset_password REST API.

        :param str instance_guid: GUID of the service instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsEngine` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_analytics_engine_by_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_analytics_engine_state_by_id(self, instance_guid: str, **kwargs) -> DetailedResponse:
        """
        Get state of Analytics Engine.

        Returns the state of the Analytics Engine cluster. The following states exist:
        * Preparing : A cluster is being created.
        * Active : The cluster is created and running.
        * Deleted : The cluster was deleted.
        * Failed : A cluster couldn't be created.
        * Expired : The service instance has expired. The cluster has been deleted.
        * ResizeFailed : The cluster couldn't be resized. The cluster will be reactivated
        based on the old settings.

        :param str instance_guid: GUID of the service instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsEngineState` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_analytics_engine_state_by_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/state'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def create_customization_request(self, instance_guid: str, target: str, custom_actions: List['AnalyticsEngineCustomAction'], **kwargs) -> DetailedResponse:
        """
        Create an adhoc customization request.

        Creates a new adhoc customization request. Adhoc customization scripts can be run
        only once. They are not persisted with the cluster and are not run automatically
        when more nodes are added to the cluster.

        :param str instance_guid: GUID of the service instance.
        :param str target: Type of nodes to target for this customization.
        :param List[AnalyticsEngineCustomAction] custom_actions: List of custom
               actions.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsEngineCreateCustomizationResponse` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        if target is None:
            raise ValueError('target must be provided')
        if custom_actions is None:
            raise ValueError('custom_actions must be provided')
        custom_actions = [ convert_model(x) for x in custom_actions ]
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='create_customization_request')
        headers.update(sdk_headers)

        data = {
            'target': target,
            'custom_actions': custom_actions
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/customization_requests'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_all_customization_requests(self, instance_guid: str, **kwargs) -> DetailedResponse:
        """
        Get all customization requests run on an Analytics Engine cluster.

        Retrieves the request_id of all customization requests submitted to the specified
        Analytics Engine cluster.

        :param str instance_guid: service instance GUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `List[AnalyticsEngineCustomizationRequestCollectionItem]` result
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_all_customization_requests')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/customization_requests'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def get_customization_request_by_id(self, instance_guid: str, request_id: str, **kwargs) -> DetailedResponse:
        """
        Retrieve details of specified customization request ID.

        Retrieves the status of the specified customization request, along with pointers
        to log files generated during the run.

        :param str instance_guid: Service instance GUID.
        :param str request_id: customization request ID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsEngineCustomizationRunDetails` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        if request_id is None:
            raise ValueError('request_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_customization_request_by_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/customization_requests/{1}'.format(*self.encode_path_vars(instance_guid, request_id))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def resize_cluster(self, instance_guid: str, *, compute_nodes_count: int = None, **kwargs) -> DetailedResponse:
        """
        Add nodes to the cluster.

        Resizes the cluster by adding compute nodes.
        **Note:** You can't resize the cluster if the software package on the cluster is
        deprecated or if the software package doesn't permit cluster resizing. See
        [here](https://cloud.ibm.com/docs/AnalyticsEngine?topic=AnalyticsEngine-unsupported-operations).

        :param str instance_guid: Service instance GUID.
        :param int compute_nodes_count: (optional) Expected number of nodes in the
               cluster after the resize operation.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsEngineResizeClusterResponse` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='resize_cluster')
        headers.update(sdk_headers)

        data = {
            'compute_nodes_count': compute_nodes_count
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/resize'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def reset_cluster_password(self, instance_guid: str, **kwargs) -> DetailedResponse:
        """
        Reset cluster password.

        Resets the cluster's password to a new system-generated crytographically strong
        value.  The new password is included in the response and you should make a note of
        it.  This password is displayed only once here and cannot be retrieved later.

        :param str instance_guid: Service instance GUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsEngineResetClusterPasswordResponse` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='reset_cluster_password')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/reset_password'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def configure_logging(self, instance_guid: str, log_specs: List['AnalyticsEngineLoggingNodeSpec'], log_server: 'AnalyticsEngineLoggingServer', **kwargs) -> DetailedResponse:
        """
        Configure log aggregation.

        Collects the logs for the following components in an IBM Analytics Engine cluster:
        * IBM Analytics Engine daemon logs, for example those for Spark, Hive, Yarn, and
        Knox on the management and data nodes
        * Yarn application job logs.

        :param str instance_guid: GUID of the service instance.
        :param List[AnalyticsEngineLoggingNodeSpec] log_specs: Logging
               specifications on each node.
        :param AnalyticsEngineLoggingServer log_server: Logging server
               configuration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        if log_specs is None:
            raise ValueError('log_specs must be provided')
        if log_server is None:
            raise ValueError('log_server must be provided')
        log_specs = [ convert_model(x) for x in log_specs ]
        log_server = convert_model(log_server)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='configure_logging')
        headers.update(sdk_headers)

        data = {
            'log_specs': log_specs,
            'log_server': log_server
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/log_config'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


    def get_logging_config(self, instance_guid: str, **kwargs) -> DetailedResponse:
        """
        Retrieve the status of log configuration.

        Retrieves the status and details of the log configuration for your cluster.

        :param str instance_guid: Service instance GUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsEngineLoggingConfigDetails` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='get_logging_config')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/log_config'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def delete_logging_config(self, instance_guid: str, **kwargs) -> DetailedResponse:
        """
        Delete the log configuration.

        Deletes the log configuration. This operation stops sending logs to the
        centralized log server.

        :param str instance_guid: Service instance GUID.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='delete_logging_config')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/log_config'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request)
        return response


    def update_private_endpoint_whitelist(self, instance_guid: str, ip_ranges: List[str], action: str, **kwargs) -> DetailedResponse:
        """
        Update private endpoint whitelist.

        Updates the list of whitelisted private endpoints. This operation either adds ip
        ranges to the whitelist or deletes them.

        :param str instance_guid: GUID of the service instance.
        :param List[str] ip_ranges: List of IP ranges to add to or remove from the
               whitelist.
        :param str action: Update Whitelist IP ranges. Add (or) Delete.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `AnalyticsEngineWhitelistResponse` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        if ip_ranges is None:
            raise ValueError('ip_ranges must be provided')
        if action is None:
            raise ValueError('action must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME, service_version='V2', operation_id='update_private_endpoint_whitelist')
        headers.update(sdk_headers)

        data = {
            'ip_ranges': ip_ranges,
            'action': action
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        url = '/v2/analytics_engines/{0}/private_endpoint_whitelist'.format(*self.encode_path_vars(instance_guid))
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request)
        return response


##############################################################################
# Models
##############################################################################


class AnalyticsEngine():
    """
    Analytics Engine cluster details.

    :attr str id: Instance GUID.
    :attr str name: Analytics Engine.
    :attr str service_plan: ID of Analytics Engine service plan.
    :attr str hardware_size: Hardware size.
    :attr str software_package: Software package.
    :attr str domain: Domain.
    :attr datetime creation_time: Cluster creation time.
    :attr datetime commision_time: Cluster commision time.
    :attr datetime decommision_time: Cluster decommision time.
    :attr datetime deletion_time: Cluster deletion time.
    :attr datetime state_change_time: Cluster state change time.
    :attr str state: Cluster state.
    :attr List[AnalyticsEngineClusterNode] nodes: (optional) List of nodes in the
          cluster.
    :attr AnalyticsEngineUserCredentials user_credentials: User credentials.
    :attr ServiceEndpoints service_endpoints: (optional) Service endpoint URLs with
          host names. Endpoints will vary based on software package chosen for the
          cluster.
    :attr ServiceEndpoints service_endpoints_ip: (optional) Service endpoint URLs
          with host IPS. Endpoints will vary based on software package chosen for the
          cluster.
    :attr List[str] private_endpoint_whitelist: (optional) Whitelisted IP Ranges for
          Analytics Engine Service with private endpoints.
    """

    def __init__(self, id: str, name: str, service_plan: str, hardware_size: str, software_package: str, domain: str, creation_time: datetime, commision_time: datetime, decommision_time: datetime, deletion_time: datetime, state_change_time: datetime, state: str, user_credentials: 'AnalyticsEngineUserCredentials', *, nodes: List['AnalyticsEngineClusterNode'] = None, service_endpoints: 'ServiceEndpoints' = None, service_endpoints_ip: 'ServiceEndpoints' = None, private_endpoint_whitelist: List[str] = None) -> None:
        """
        Initialize a AnalyticsEngine object.

        :param str id: Instance GUID.
        :param str name: Analytics Engine.
        :param str service_plan: ID of Analytics Engine service plan.
        :param str hardware_size: Hardware size.
        :param str software_package: Software package.
        :param str domain: Domain.
        :param datetime creation_time: Cluster creation time.
        :param datetime commision_time: Cluster commision time.
        :param datetime decommision_time: Cluster decommision time.
        :param datetime deletion_time: Cluster deletion time.
        :param datetime state_change_time: Cluster state change time.
        :param str state: Cluster state.
        :param AnalyticsEngineUserCredentials user_credentials: User credentials.
        :param List[AnalyticsEngineClusterNode] nodes: (optional) List of nodes in
               the cluster.
        :param ServiceEndpoints service_endpoints: (optional) Service endpoint URLs
               with host names. Endpoints will vary based on software package chosen for
               the cluster.
        :param ServiceEndpoints service_endpoints_ip: (optional) Service endpoint
               URLs with host IPS. Endpoints will vary based on software package chosen
               for the cluster.
        :param List[str] private_endpoint_whitelist: (optional) Whitelisted IP
               Ranges for Analytics Engine Service with private endpoints.
        """
        self.id = id
        self.name = name
        self.service_plan = service_plan
        self.hardware_size = hardware_size
        self.software_package = software_package
        self.domain = domain
        self.creation_time = creation_time
        self.commision_time = commision_time
        self.decommision_time = decommision_time
        self.deletion_time = deletion_time
        self.state_change_time = state_change_time
        self.state = state
        self.nodes = nodes
        self.user_credentials = user_credentials
        self.service_endpoints = service_endpoints
        self.service_endpoints_ip = service_endpoints_ip
        self.private_endpoint_whitelist = private_endpoint_whitelist

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngine':
        """Initialize a AnalyticsEngine object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        else:
            raise ValueError('Required property \'id\' not present in AnalyticsEngine JSON')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in AnalyticsEngine JSON')
        if 'service_plan' in _dict:
            args['service_plan'] = _dict.get('service_plan')
        else:
            raise ValueError('Required property \'service_plan\' not present in AnalyticsEngine JSON')
        if 'hardware_size' in _dict:
            args['hardware_size'] = _dict.get('hardware_size')
        else:
            raise ValueError('Required property \'hardware_size\' not present in AnalyticsEngine JSON')
        if 'software_package' in _dict:
            args['software_package'] = _dict.get('software_package')
        else:
            raise ValueError('Required property \'software_package\' not present in AnalyticsEngine JSON')
        if 'domain' in _dict:
            args['domain'] = _dict.get('domain')
        else:
            raise ValueError('Required property \'domain\' not present in AnalyticsEngine JSON')
        if 'creation_time' in _dict:
            args['creation_time'] = string_to_datetime(_dict.get('creation_time'))
        else:
            raise ValueError('Required property \'creation_time\' not present in AnalyticsEngine JSON')
        if 'commision_time' in _dict:
            args['commision_time'] = string_to_datetime(_dict.get('commision_time'))
        else:
            raise ValueError('Required property \'commision_time\' not present in AnalyticsEngine JSON')
        if 'decommision_time' in _dict:
            args['decommision_time'] = string_to_datetime(_dict.get('decommision_time'))
        else:
            raise ValueError('Required property \'decommision_time\' not present in AnalyticsEngine JSON')
        if 'deletion_time' in _dict:
            args['deletion_time'] = string_to_datetime(_dict.get('deletion_time'))
        else:
            raise ValueError('Required property \'deletion_time\' not present in AnalyticsEngine JSON')
        if 'state_change_time' in _dict:
            args['state_change_time'] = string_to_datetime(_dict.get('state_change_time'))
        else:
            raise ValueError('Required property \'state_change_time\' not present in AnalyticsEngine JSON')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in AnalyticsEngine JSON')
        if 'nodes' in _dict:
            args['nodes'] = [AnalyticsEngineClusterNode.from_dict(x) for x in _dict.get('nodes')]
        if 'user_credentials' in _dict:
            args['user_credentials'] = AnalyticsEngineUserCredentials.from_dict(_dict.get('user_credentials'))
        else:
            raise ValueError('Required property \'user_credentials\' not present in AnalyticsEngine JSON')
        if 'service_endpoints' in _dict:
            args['service_endpoints'] = ServiceEndpoints.from_dict(_dict.get('service_endpoints'))
        if 'service_endpoints_ip' in _dict:
            args['service_endpoints_ip'] = ServiceEndpoints.from_dict(_dict.get('service_endpoints_ip'))
        if 'private_endpoint_whitelist' in _dict:
            args['private_endpoint_whitelist'] = _dict.get('private_endpoint_whitelist')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngine object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'service_plan') and self.service_plan is not None:
            _dict['service_plan'] = self.service_plan
        if hasattr(self, 'hardware_size') and self.hardware_size is not None:
            _dict['hardware_size'] = self.hardware_size
        if hasattr(self, 'software_package') and self.software_package is not None:
            _dict['software_package'] = self.software_package
        if hasattr(self, 'domain') and self.domain is not None:
            _dict['domain'] = self.domain
        if hasattr(self, 'creation_time') and self.creation_time is not None:
            _dict['creation_time'] = datetime_to_string(self.creation_time)
        if hasattr(self, 'commision_time') and self.commision_time is not None:
            _dict['commision_time'] = datetime_to_string(self.commision_time)
        if hasattr(self, 'decommision_time') and self.decommision_time is not None:
            _dict['decommision_time'] = datetime_to_string(self.decommision_time)
        if hasattr(self, 'deletion_time') and self.deletion_time is not None:
            _dict['deletion_time'] = datetime_to_string(self.deletion_time)
        if hasattr(self, 'state_change_time') and self.state_change_time is not None:
            _dict['state_change_time'] = datetime_to_string(self.state_change_time)
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'nodes') and self.nodes is not None:
            _dict['nodes'] = [x.to_dict() for x in self.nodes]
        if hasattr(self, 'user_credentials') and self.user_credentials is not None:
            _dict['user_credentials'] = self.user_credentials.to_dict()
        if hasattr(self, 'service_endpoints') and self.service_endpoints is not None:
            _dict['service_endpoints'] = self.service_endpoints.to_dict()
        if hasattr(self, 'service_endpoints_ip') and self.service_endpoints_ip is not None:
            _dict['service_endpoints_ip'] = self.service_endpoints_ip.to_dict()
        if hasattr(self, 'private_endpoint_whitelist') and self.private_endpoint_whitelist is not None:
            _dict['private_endpoint_whitelist'] = self.private_endpoint_whitelist
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngine object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngine') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngine') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineClusterNode():
    """
    Cluster node details.

    :attr float id: (optional) Node ID.
    :attr str fqdn: (optional) Fully qualified domain name.
    :attr str type: (optional) Node type.
    :attr str state: (optional) State of node.
    :attr str public_ip: (optional) Public IP address.
    :attr str private_ip: (optional) Private IP address.
    :attr datetime state_change_time: (optional) State change time.
    :attr datetime commission_time: (optional) Commission time.
    """

    def __init__(self, *, id: float = None, fqdn: str = None, type: str = None, state: str = None, public_ip: str = None, private_ip: str = None, state_change_time: datetime = None, commission_time: datetime = None) -> None:
        """
        Initialize a AnalyticsEngineClusterNode object.

        :param float id: (optional) Node ID.
        :param str fqdn: (optional) Fully qualified domain name.
        :param str type: (optional) Node type.
        :param str state: (optional) State of node.
        :param str public_ip: (optional) Public IP address.
        :param str private_ip: (optional) Private IP address.
        :param datetime state_change_time: (optional) State change time.
        :param datetime commission_time: (optional) Commission time.
        """
        self.id = id
        self.fqdn = fqdn
        self.type = type
        self.state = state
        self.public_ip = public_ip
        self.private_ip = private_ip
        self.state_change_time = state_change_time
        self.commission_time = commission_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineClusterNode':
        """Initialize a AnalyticsEngineClusterNode object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'fqdn' in _dict:
            args['fqdn'] = _dict.get('fqdn')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'public_ip' in _dict:
            args['public_ip'] = _dict.get('public_ip')
        if 'private_ip' in _dict:
            args['private_ip'] = _dict.get('private_ip')
        if 'state_change_time' in _dict:
            args['state_change_time'] = string_to_datetime(_dict.get('state_change_time'))
        if 'commission_time' in _dict:
            args['commission_time'] = string_to_datetime(_dict.get('commission_time'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineClusterNode object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'fqdn') and self.fqdn is not None:
            _dict['fqdn'] = self.fqdn
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'public_ip') and self.public_ip is not None:
            _dict['public_ip'] = self.public_ip
        if hasattr(self, 'private_ip') and self.private_ip is not None:
            _dict['private_ip'] = self.private_ip
        if hasattr(self, 'state_change_time') and self.state_change_time is not None:
            _dict['state_change_time'] = datetime_to_string(self.state_change_time)
        if hasattr(self, 'commission_time') and self.commission_time is not None:
            _dict['commission_time'] = datetime_to_string(self.commission_time)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineClusterNode object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineClusterNode') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineClusterNode') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineCreateCustomizationResponse():
    """
    Create customization request response.

    :attr float request_id: (optional) Customization request ID.
    """

    def __init__(self, *, request_id: float = None) -> None:
        """
        Initialize a AnalyticsEngineCreateCustomizationResponse object.

        :param float request_id: (optional) Customization request ID.
        """
        self.request_id = request_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineCreateCustomizationResponse':
        """Initialize a AnalyticsEngineCreateCustomizationResponse object from a json dictionary."""
        args = {}
        if 'request_id' in _dict:
            args['request_id'] = _dict.get('request_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineCreateCustomizationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request_id') and self.request_id is not None:
            _dict['request_id'] = self.request_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineCreateCustomizationResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineCreateCustomizationResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineCreateCustomizationResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineCustomAction():
    """
    Custom action details for customization.

    :attr str name: Custom action name.
    :attr str type: (optional) Customization type.
    :attr AnalyticsEngineCustomActionScript script: (optional) Customization script
          details.
    :attr List[str] script_params: (optional) Customization script parameters.
    """

    def __init__(self, name: str, *, type: str = None, script: 'AnalyticsEngineCustomActionScript' = None, script_params: List[str] = None) -> None:
        """
        Initialize a AnalyticsEngineCustomAction object.

        :param str name: Custom action name.
        :param str type: (optional) Customization type.
        :param AnalyticsEngineCustomActionScript script: (optional) Customization
               script details.
        :param List[str] script_params: (optional) Customization script parameters.
        """
        self.name = name
        self.type = type
        self.script = script
        self.script_params = script_params

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineCustomAction':
        """Initialize a AnalyticsEngineCustomAction object from a json dictionary."""
        args = {}
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        else:
            raise ValueError('Required property \'name\' not present in AnalyticsEngineCustomAction JSON')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'script' in _dict:
            args['script'] = AnalyticsEngineCustomActionScript.from_dict(_dict.get('script'))
        if 'script_params' in _dict:
            args['script_params'] = _dict.get('script_params')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineCustomAction object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'script') and self.script is not None:
            _dict['script'] = self.script.to_dict()
        if hasattr(self, 'script_params') and self.script_params is not None:
            _dict['script_params'] = self.script_params
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineCustomAction object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineCustomAction') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineCustomAction') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class TypeEnum(Enum):
        """
        Customization type.
        """
        BOOTSTRAP = "bootstrap"


class AnalyticsEngineCustomActionScript():
    """
    Customization script details.

    :attr str source_type: (optional) Defines where to access the customization
          script.
    :attr str script_path: (optional) Path to the customization script.
    :attr object source_props: (optional) Customization script properties.
    """

    def __init__(self, *, source_type: str = None, script_path: str = None, source_props: object = None) -> None:
        """
        Initialize a AnalyticsEngineCustomActionScript object.

        :param str source_type: (optional) Defines where to access the
               customization script.
        :param str script_path: (optional) Path to the customization script.
        :param object source_props: (optional) Customization script properties.
        """
        self.source_type = source_type
        self.script_path = script_path
        self.source_props = source_props

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineCustomActionScript':
        """Initialize a AnalyticsEngineCustomActionScript object from a json dictionary."""
        args = {}
        if 'source_type' in _dict:
            args['source_type'] = _dict.get('source_type')
        if 'script_path' in _dict:
            args['script_path'] = _dict.get('script_path')
        if 'source_props' in _dict:
            args['source_props'] = _dict.get('source_props')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineCustomActionScript object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'source_type') and self.source_type is not None:
            _dict['source_type'] = self.source_type
        if hasattr(self, 'script_path') and self.script_path is not None:
            _dict['script_path'] = self.script_path
        if hasattr(self, 'source_props') and self.source_props is not None:
            _dict['source_props'] = self.source_props
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineCustomActionScript object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineCustomActionScript') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineCustomActionScript') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class SourceTypeEnum(Enum):
        """
        Defines where to access the customization script.
        """
        HTTP = "http"
        HTTPS = "https"
        BLUEMIXSWIFT = "BluemixSwift"
        SOFTLAYERSWIFT = "SoftLayerSwift"
        COSS3 = "CosS3"


class AnalyticsEngineCustomizationRequestCollectionItem():
    """
    AnalyticsEngineCustomizationRequestCollectionItem.

    :attr str id: (optional) Customization request ID.
    """

    def __init__(self, *, id: str = None) -> None:
        """
        Initialize a AnalyticsEngineCustomizationRequestCollectionItem object.

        :param str id: (optional) Customization request ID.
        """
        self.id = id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineCustomizationRequestCollectionItem':
        """Initialize a AnalyticsEngineCustomizationRequestCollectionItem object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineCustomizationRequestCollectionItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineCustomizationRequestCollectionItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineCustomizationRequestCollectionItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineCustomizationRequestCollectionItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineCustomizationRunDetails():
    """
    Customization run details for the cluster.

    :attr str id: (optional) Instance GUID.
    :attr str run_status: (optional) Customization run status.
    :attr AnalyticsEngineCustomizationRunDetailsRunDetails run_details: (optional)
          Customization run details.
    """

    def __init__(self, *, id: str = None, run_status: str = None, run_details: 'AnalyticsEngineCustomizationRunDetailsRunDetails' = None) -> None:
        """
        Initialize a AnalyticsEngineCustomizationRunDetails object.

        :param str id: (optional) Instance GUID.
        :param str run_status: (optional) Customization run status.
        :param AnalyticsEngineCustomizationRunDetailsRunDetails run_details:
               (optional) Customization run details.
        """
        self.id = id
        self.run_status = run_status
        self.run_details = run_details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineCustomizationRunDetails':
        """Initialize a AnalyticsEngineCustomizationRunDetails object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'run_status' in _dict:
            args['run_status'] = _dict.get('run_status')
        if 'run_details' in _dict:
            args['run_details'] = AnalyticsEngineCustomizationRunDetailsRunDetails.from_dict(_dict.get('run_details'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineCustomizationRunDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'run_status') and self.run_status is not None:
            _dict['run_status'] = self.run_status
        if hasattr(self, 'run_details') and self.run_details is not None:
            _dict['run_details'] = self.run_details.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineCustomizationRunDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineCustomizationRunDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineCustomizationRunDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineCustomizationRunDetailsRunDetails():
    """
    Customization run details.

    :attr str overall_status: (optional) Customization run overall status.
    :attr List[AnalyticsEngineNodeLevelCustomizationRunDetails] details: (optional)
          Customization run details for each node.
    """

    def __init__(self, *, overall_status: str = None, details: List['AnalyticsEngineNodeLevelCustomizationRunDetails'] = None) -> None:
        """
        Initialize a AnalyticsEngineCustomizationRunDetailsRunDetails object.

        :param str overall_status: (optional) Customization run overall status.
        :param List[AnalyticsEngineNodeLevelCustomizationRunDetails] details:
               (optional) Customization run details for each node.
        """
        self.overall_status = overall_status
        self.details = details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineCustomizationRunDetailsRunDetails':
        """Initialize a AnalyticsEngineCustomizationRunDetailsRunDetails object from a json dictionary."""
        args = {}
        if 'overall_status' in _dict:
            args['overall_status'] = _dict.get('overall_status')
        if 'details' in _dict:
            args['details'] = [AnalyticsEngineNodeLevelCustomizationRunDetails.from_dict(x) for x in _dict.get('details')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineCustomizationRunDetailsRunDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'overall_status') and self.overall_status is not None:
            _dict['overall_status'] = self.overall_status
        if hasattr(self, 'details') and self.details is not None:
            _dict['details'] = [x.to_dict() for x in self.details]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineCustomizationRunDetailsRunDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineCustomizationRunDetailsRunDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineCustomizationRunDetailsRunDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineLoggingConfigDetails():
    """
    Logging configuration.

    :attr List[AnalyticsEngineLoggingNodeSpec] log_specs: Log specifications for
          nodes.
    :attr AnalyticsEngineLoggingServer log_server: Logging server configuration.
    :attr List[AnalyticsEngineLoggingConfigStatus] log_config_status: Log
          configuration status.
    """

    def __init__(self, log_specs: List['AnalyticsEngineLoggingNodeSpec'], log_server: 'AnalyticsEngineLoggingServer', log_config_status: List['AnalyticsEngineLoggingConfigStatus']) -> None:
        """
        Initialize a AnalyticsEngineLoggingConfigDetails object.

        :param List[AnalyticsEngineLoggingNodeSpec] log_specs: Log specifications
               for nodes.
        :param AnalyticsEngineLoggingServer log_server: Logging server
               configuration.
        :param List[AnalyticsEngineLoggingConfigStatus] log_config_status: Log
               configuration status.
        """
        self.log_specs = log_specs
        self.log_server = log_server
        self.log_config_status = log_config_status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineLoggingConfigDetails':
        """Initialize a AnalyticsEngineLoggingConfigDetails object from a json dictionary."""
        args = {}
        if 'log_specs' in _dict:
            args['log_specs'] = [AnalyticsEngineLoggingNodeSpec.from_dict(x) for x in _dict.get('log_specs')]
        else:
            raise ValueError('Required property \'log_specs\' not present in AnalyticsEngineLoggingConfigDetails JSON')
        if 'log_server' in _dict:
            args['log_server'] = AnalyticsEngineLoggingServer.from_dict(_dict.get('log_server'))
        else:
            raise ValueError('Required property \'log_server\' not present in AnalyticsEngineLoggingConfigDetails JSON')
        if 'log_config_status' in _dict:
            args['log_config_status'] = [AnalyticsEngineLoggingConfigStatus.from_dict(x) for x in _dict.get('log_config_status')]
        else:
            raise ValueError('Required property \'log_config_status\' not present in AnalyticsEngineLoggingConfigDetails JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineLoggingConfigDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'log_specs') and self.log_specs is not None:
            _dict['log_specs'] = [x.to_dict() for x in self.log_specs]
        if hasattr(self, 'log_server') and self.log_server is not None:
            _dict['log_server'] = self.log_server.to_dict()
        if hasattr(self, 'log_config_status') and self.log_config_status is not None:
            _dict['log_config_status'] = [x.to_dict() for x in self.log_config_status]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineLoggingConfigDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineLoggingConfigDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineLoggingConfigDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineLoggingConfigStatus():
    """
    Log configuration status.

    :attr str node_type: Node type.
    :attr str node_id: Node ID.
    :attr str action: Action.
    :attr str status: Log configuration status.
    """

    def __init__(self, node_type: str, node_id: str, action: str, status: str) -> None:
        """
        Initialize a AnalyticsEngineLoggingConfigStatus object.

        :param str node_type: Node type.
        :param str node_id: Node ID.
        :param str action: Action.
        :param str status: Log configuration status.
        """
        self.node_type = node_type
        self.node_id = node_id
        self.action = action
        self.status = status

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineLoggingConfigStatus':
        """Initialize a AnalyticsEngineLoggingConfigStatus object from a json dictionary."""
        args = {}
        if 'node_type' in _dict:
            args['node_type'] = _dict.get('node_type')
        else:
            raise ValueError('Required property \'node_type\' not present in AnalyticsEngineLoggingConfigStatus JSON')
        if 'node_id' in _dict:
            args['node_id'] = _dict.get('node_id')
        else:
            raise ValueError('Required property \'node_id\' not present in AnalyticsEngineLoggingConfigStatus JSON')
        if 'action' in _dict:
            args['action'] = _dict.get('action')
        else:
            raise ValueError('Required property \'action\' not present in AnalyticsEngineLoggingConfigStatus JSON')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        else:
            raise ValueError('Required property \'status\' not present in AnalyticsEngineLoggingConfigStatus JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineLoggingConfigStatus object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'node_type') and self.node_type is not None:
            _dict['node_type'] = self.node_type
        if hasattr(self, 'node_id') and self.node_id is not None:
            _dict['node_id'] = self.node_id
        if hasattr(self, 'action') and self.action is not None:
            _dict['action'] = self.action
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineLoggingConfigStatus object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineLoggingConfigStatus') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineLoggingConfigStatus') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class NodeTypeEnum(Enum):
        """
        Node type.
        """
        MANAGEMENT = "management"
        DATA = "data"


class AnalyticsEngineLoggingNodeSpec():
    """
    Log specifications for node.

    :attr str node_type: Node type.
    :attr List[str] components: Node components to be monitored.
    """

    def __init__(self, node_type: str, components: List[str]) -> None:
        """
        Initialize a AnalyticsEngineLoggingNodeSpec object.

        :param str node_type: Node type.
        :param List[str] components: Node components to be monitored.
        """
        self.node_type = node_type
        self.components = components

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineLoggingNodeSpec':
        """Initialize a AnalyticsEngineLoggingNodeSpec object from a json dictionary."""
        args = {}
        if 'node_type' in _dict:
            args['node_type'] = _dict.get('node_type')
        else:
            raise ValueError('Required property \'node_type\' not present in AnalyticsEngineLoggingNodeSpec JSON')
        if 'components' in _dict:
            args['components'] = _dict.get('components')
        else:
            raise ValueError('Required property \'components\' not present in AnalyticsEngineLoggingNodeSpec JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineLoggingNodeSpec object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'node_type') and self.node_type is not None:
            _dict['node_type'] = self.node_type
        if hasattr(self, 'components') and self.components is not None:
            _dict['components'] = self.components
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineLoggingNodeSpec object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineLoggingNodeSpec') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineLoggingNodeSpec') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class NodeTypeEnum(Enum):
        """
        Node type.
        """
        MANAGEMENT = "management"
        DATA = "data"

    
    class ComponentsEnum(Enum):
        """
        Node components to be logged.
        """
        AMBARI_SERVER = "ambari-server"
        HADOOP_MAPREDUCE = "hadoop-mapreduce"
        HADOOP_YARN = "hadoop-yarn"
        HBASE = "hbase"
        HIVE = "hive"
        JNBG = "jnbg"
        KNOX = "knox"
        LIVY2 = "livy2"
        SPARK2 = "spark2"
        YARN_APPS = "yarn-apps"


class AnalyticsEngineLoggingServer():
    """
    Logging server configuration.

    :attr str type: Logging server type.
    :attr str credential: Logging server credential.
    :attr str api_host: Logging server API host.
    :attr str log_host: Logging server host.
    :attr str owner: (optional) Logging server owner.
    """

    def __init__(self, type: str, credential: str, api_host: str, log_host: str, *, owner: str = None) -> None:
        """
        Initialize a AnalyticsEngineLoggingServer object.

        :param str type: Logging server type.
        :param str credential: Logging server credential.
        :param str api_host: Logging server API host.
        :param str log_host: Logging server host.
        :param str owner: (optional) Logging server owner.
        """
        self.type = type
        self.credential = credential
        self.api_host = api_host
        self.log_host = log_host
        self.owner = owner

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineLoggingServer':
        """Initialize a AnalyticsEngineLoggingServer object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        else:
            raise ValueError('Required property \'type\' not present in AnalyticsEngineLoggingServer JSON')
        if 'credential' in _dict:
            args['credential'] = _dict.get('credential')
        else:
            raise ValueError('Required property \'credential\' not present in AnalyticsEngineLoggingServer JSON')
        if 'api_host' in _dict:
            args['api_host'] = _dict.get('api_host')
        else:
            raise ValueError('Required property \'api_host\' not present in AnalyticsEngineLoggingServer JSON')
        if 'log_host' in _dict:
            args['log_host'] = _dict.get('log_host')
        else:
            raise ValueError('Required property \'log_host\' not present in AnalyticsEngineLoggingServer JSON')
        if 'owner' in _dict:
            args['owner'] = _dict.get('owner')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineLoggingServer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'credential') and self.credential is not None:
            _dict['credential'] = self.credential
        if hasattr(self, 'api_host') and self.api_host is not None:
            _dict['api_host'] = self.api_host
        if hasattr(self, 'log_host') and self.log_host is not None:
            _dict['log_host'] = self.log_host
        if hasattr(self, 'owner') and self.owner is not None:
            _dict['owner'] = self.owner
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineLoggingServer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineLoggingServer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineLoggingServer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    
    class TypeEnum(Enum):
        """
        Logging server type.
        """
        LOGDNA = "logdna"


class AnalyticsEngineNodeLevelCustomizationRunDetails():
    """
    Customization run details for the node.

    :attr str node_name: (optional) Node name.
    :attr str node_type: (optional) Node type.
    :attr str start_time: (optional) Customization request start time.
    :attr str end_time: (optional) Customization request end time.
    :attr str time_taken: (optional) Total time taken for customization request.
    :attr str status: (optional) Status of customization request.
    :attr str log_file: (optional) Log file to track for customization run
          information.
    """

    def __init__(self, *, node_name: str = None, node_type: str = None, start_time: str = None, end_time: str = None, time_taken: str = None, status: str = None, log_file: str = None) -> None:
        """
        Initialize a AnalyticsEngineNodeLevelCustomizationRunDetails object.

        :param str node_name: (optional) Node name.
        :param str node_type: (optional) Node type.
        :param str start_time: (optional) Customization request start time.
        :param str end_time: (optional) Customization request end time.
        :param str time_taken: (optional) Total time taken for customization
               request.
        :param str status: (optional) Status of customization request.
        :param str log_file: (optional) Log file to track for customization run
               information.
        """
        self.node_name = node_name
        self.node_type = node_type
        self.start_time = start_time
        self.end_time = end_time
        self.time_taken = time_taken
        self.status = status
        self.log_file = log_file

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineNodeLevelCustomizationRunDetails':
        """Initialize a AnalyticsEngineNodeLevelCustomizationRunDetails object from a json dictionary."""
        args = {}
        if 'node_name' in _dict:
            args['node_name'] = _dict.get('node_name')
        if 'node_type' in _dict:
            args['node_type'] = _dict.get('node_type')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        if 'time_taken' in _dict:
            args['time_taken'] = _dict.get('time_taken')
        if 'status' in _dict:
            args['status'] = _dict.get('status')
        if 'log_file' in _dict:
            args['log_file'] = _dict.get('log_file')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineNodeLevelCustomizationRunDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'node_name') and self.node_name is not None:
            _dict['node_name'] = self.node_name
        if hasattr(self, 'node_type') and self.node_type is not None:
            _dict['node_type'] = self.node_type
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'time_taken') and self.time_taken is not None:
            _dict['time_taken'] = self.time_taken
        if hasattr(self, 'status') and self.status is not None:
            _dict['status'] = self.status
        if hasattr(self, 'log_file') and self.log_file is not None:
            _dict['log_file'] = self.log_file
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineNodeLevelCustomizationRunDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineNodeLevelCustomizationRunDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineNodeLevelCustomizationRunDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineResetClusterPasswordResponse():
    """
    Response for resetting cluster password.

    :attr str id: (optional) Instance guid.
    :attr AnalyticsEngineResetClusterPasswordResponseUserCredentials
          user_credentials: (optional) User credentials.
    """

    def __init__(self, *, id: str = None, user_credentials: 'AnalyticsEngineResetClusterPasswordResponseUserCredentials' = None) -> None:
        """
        Initialize a AnalyticsEngineResetClusterPasswordResponse object.

        :param str id: (optional) Instance guid.
        :param AnalyticsEngineResetClusterPasswordResponseUserCredentials
               user_credentials: (optional) User credentials.
        """
        self.id = id
        self.user_credentials = user_credentials

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineResetClusterPasswordResponse':
        """Initialize a AnalyticsEngineResetClusterPasswordResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'user_credentials' in _dict:
            args['user_credentials'] = AnalyticsEngineResetClusterPasswordResponseUserCredentials.from_dict(_dict.get('user_credentials'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineResetClusterPasswordResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'user_credentials') and self.user_credentials is not None:
            _dict['user_credentials'] = self.user_credentials.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineResetClusterPasswordResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineResetClusterPasswordResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineResetClusterPasswordResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineResetClusterPasswordResponseUserCredentials():
    """
    User credentials.

    :attr str user: (optional) Username.
    :attr str password: (optional) New password.
    """

    def __init__(self, *, user: str = None, password: str = None) -> None:
        """
        Initialize a AnalyticsEngineResetClusterPasswordResponseUserCredentials object.

        :param str user: (optional) Username.
        :param str password: (optional) New password.
        """
        self.user = user
        self.password = password

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineResetClusterPasswordResponseUserCredentials':
        """Initialize a AnalyticsEngineResetClusterPasswordResponseUserCredentials object from a json dictionary."""
        args = {}
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        if 'password' in _dict:
            args['password'] = _dict.get('password')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineResetClusterPasswordResponseUserCredentials object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        if hasattr(self, 'password') and self.password is not None:
            _dict['password'] = self.password
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineResetClusterPasswordResponseUserCredentials object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineResetClusterPasswordResponseUserCredentials') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineResetClusterPasswordResponseUserCredentials') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineResizeClusterResponse():
    """
    Resize request response.

    :attr str request_id: (optional) Request ID.
    """

    def __init__(self, *, request_id: str = None) -> None:
        """
        Initialize a AnalyticsEngineResizeClusterResponse object.

        :param str request_id: (optional) Request ID.
        """
        self.request_id = request_id

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineResizeClusterResponse':
        """Initialize a AnalyticsEngineResizeClusterResponse object from a json dictionary."""
        args = {}
        if 'request_id' in _dict:
            args['request_id'] = _dict.get('request_id')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineResizeClusterResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'request_id') and self.request_id is not None:
            _dict['request_id'] = self.request_id
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineResizeClusterResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineResizeClusterResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineResizeClusterResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineState():
    """
    Cluster state.

    :attr str state: Cluster state.
    """

    def __init__(self, state: str) -> None:
        """
        Initialize a AnalyticsEngineState object.

        :param str state: Cluster state.
        """
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineState':
        """Initialize a AnalyticsEngineState object from a json dictionary."""
        args = {}
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        else:
            raise ValueError('Required property \'state\' not present in AnalyticsEngineState JSON')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineState object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineState object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineState') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineState') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineUserCredentials():
    """
    User credentials.

    :attr str user: (optional) Username.
    """

    def __init__(self, *, user: str = None) -> None:
        """
        Initialize a AnalyticsEngineUserCredentials object.

        :param str user: (optional) Username.
        """
        self.user = user

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineUserCredentials':
        """Initialize a AnalyticsEngineUserCredentials object from a json dictionary."""
        args = {}
        if 'user' in _dict:
            args['user'] = _dict.get('user')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineUserCredentials object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'user') and self.user is not None:
            _dict['user'] = self.user
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineUserCredentials object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineUserCredentials') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineUserCredentials') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class AnalyticsEngineWhitelistResponse():
    """
    Whitelisted IP Ranges.

    :attr List[str] private_endpoint_whitelist: (optional) Whitelisted IP Ranges.
    """

    def __init__(self, *, private_endpoint_whitelist: List[str] = None) -> None:
        """
        Initialize a AnalyticsEngineWhitelistResponse object.

        :param List[str] private_endpoint_whitelist: (optional) Whitelisted IP
               Ranges.
        """
        self.private_endpoint_whitelist = private_endpoint_whitelist

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'AnalyticsEngineWhitelistResponse':
        """Initialize a AnalyticsEngineWhitelistResponse object from a json dictionary."""
        args = {}
        if 'private_endpoint_whitelist' in _dict:
            args['private_endpoint_whitelist'] = _dict.get('private_endpoint_whitelist')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a AnalyticsEngineWhitelistResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'private_endpoint_whitelist') and self.private_endpoint_whitelist is not None:
            _dict['private_endpoint_whitelist'] = self.private_endpoint_whitelist
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this AnalyticsEngineWhitelistResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'AnalyticsEngineWhitelistResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'AnalyticsEngineWhitelistResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


class ServiceEndpoints():
    """
    Service Endpoints.

    :attr str phoenix_jdbc: (optional) Phoenix JDBC service endpoint.
    :attr str ambari_console: (optional) Amabri console service endpoint.
    :attr str livy: (optional) Livy service endpoint.
    :attr str spark_history_server: (optional) Spark history server serivce
          endpoint.
    :attr str oozie_rest: (optional) Oozie REST service endpi'.
    :attr str hive_jdbc: (optional) Hive JDBC service endpoint.
    :attr str notebook_gateway_websocket: (optional) Notebook gateway websocket
          service endpoint.
    :attr str notebook_gateway: (optional) Notebook gateway service endpoint.
    :attr str webhdfs: (optional) WebHDFS service endpoint.
    :attr str ssh: (optional) SSH service endpoint.
    :attr str spark_sql: (optional) Spark SQL service endpoint.
    """

    def __init__(self, *, phoenix_jdbc: str = None, ambari_console: str = None, livy: str = None, spark_history_server: str = None, oozie_rest: str = None, hive_jdbc: str = None, notebook_gateway_websocket: str = None, notebook_gateway: str = None, webhdfs: str = None, ssh: str = None, spark_sql: str = None) -> None:
        """
        Initialize a ServiceEndpoints object.

        :param str phoenix_jdbc: (optional) Phoenix JDBC service endpoint.
        :param str ambari_console: (optional) Amabri console service endpoint.
        :param str livy: (optional) Livy service endpoint.
        :param str spark_history_server: (optional) Spark history server serivce
               endpoint.
        :param str oozie_rest: (optional) Oozie REST service endpi'.
        :param str hive_jdbc: (optional) Hive JDBC service endpoint.
        :param str notebook_gateway_websocket: (optional) Notebook gateway
               websocket service endpoint.
        :param str notebook_gateway: (optional) Notebook gateway service endpoint.
        :param str webhdfs: (optional) WebHDFS service endpoint.
        :param str ssh: (optional) SSH service endpoint.
        :param str spark_sql: (optional) Spark SQL service endpoint.
        """
        self.phoenix_jdbc = phoenix_jdbc
        self.ambari_console = ambari_console
        self.livy = livy
        self.spark_history_server = spark_history_server
        self.oozie_rest = oozie_rest
        self.hive_jdbc = hive_jdbc
        self.notebook_gateway_websocket = notebook_gateway_websocket
        self.notebook_gateway = notebook_gateway
        self.webhdfs = webhdfs
        self.ssh = ssh
        self.spark_sql = spark_sql

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ServiceEndpoints':
        """Initialize a ServiceEndpoints object from a json dictionary."""
        args = {}
        if 'phoenix_jdbc' in _dict:
            args['phoenix_jdbc'] = _dict.get('phoenix_jdbc')
        if 'ambari_console' in _dict:
            args['ambari_console'] = _dict.get('ambari_console')
        if 'livy' in _dict:
            args['livy'] = _dict.get('livy')
        if 'spark_history_server' in _dict:
            args['spark_history_server'] = _dict.get('spark_history_server')
        if 'oozie_rest' in _dict:
            args['oozie_rest'] = _dict.get('oozie_rest')
        if 'hive_jdbc' in _dict:
            args['hive_jdbc'] = _dict.get('hive_jdbc')
        if 'notebook_gateway_websocket' in _dict:
            args['notebook_gateway_websocket'] = _dict.get('notebook_gateway_websocket')
        if 'notebook_gateway' in _dict:
            args['notebook_gateway'] = _dict.get('notebook_gateway')
        if 'webhdfs' in _dict:
            args['webhdfs'] = _dict.get('webhdfs')
        if 'ssh' in _dict:
            args['ssh'] = _dict.get('ssh')
        if 'spark_sql' in _dict:
            args['spark_sql'] = _dict.get('spark_sql')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ServiceEndpoints object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'phoenix_jdbc') and self.phoenix_jdbc is not None:
            _dict['phoenix_jdbc'] = self.phoenix_jdbc
        if hasattr(self, 'ambari_console') and self.ambari_console is not None:
            _dict['ambari_console'] = self.ambari_console
        if hasattr(self, 'livy') and self.livy is not None:
            _dict['livy'] = self.livy
        if hasattr(self, 'spark_history_server') and self.spark_history_server is not None:
            _dict['spark_history_server'] = self.spark_history_server
        if hasattr(self, 'oozie_rest') and self.oozie_rest is not None:
            _dict['oozie_rest'] = self.oozie_rest
        if hasattr(self, 'hive_jdbc') and self.hive_jdbc is not None:
            _dict['hive_jdbc'] = self.hive_jdbc
        if hasattr(self, 'notebook_gateway_websocket') and self.notebook_gateway_websocket is not None:
            _dict['notebook_gateway_websocket'] = self.notebook_gateway_websocket
        if hasattr(self, 'notebook_gateway') and self.notebook_gateway is not None:
            _dict['notebook_gateway'] = self.notebook_gateway
        if hasattr(self, 'webhdfs') and self.webhdfs is not None:
            _dict['webhdfs'] = self.webhdfs
        if hasattr(self, 'ssh') and self.ssh is not None:
            _dict['ssh'] = self.ssh
        if hasattr(self, 'spark_sql') and self.spark_sql is not None:
            _dict['spark_sql'] = self.spark_sql
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ServiceEndpoints object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ServiceEndpoints') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ServiceEndpoints') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other


