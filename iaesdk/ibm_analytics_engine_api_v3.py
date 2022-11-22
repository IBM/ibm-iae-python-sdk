# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.54.1-1d9808a7-20220817-143039
 
"""
Manage serverless Spark instances and run applications.

API Version: 3.0.0
"""

from datetime import datetime
from enum import Enum
from typing import Dict, List
import json

from ibm_cloud_sdk_core import BaseService, DetailedResponse
from ibm_cloud_sdk_core.authenticators.authenticator import Authenticator
from ibm_cloud_sdk_core.get_authenticator import get_authenticator_from_environment
from ibm_cloud_sdk_core.utils import convert_list, convert_model, datetime_to_string, string_to_datetime

from .common import get_sdk_headers

##############################################################################
# Service
##############################################################################

class IbmAnalyticsEngineApiV3(BaseService):
    """The IBM Analytics Engine API V3 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.ae.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'ibm_analytics_engine_api'

    REGIONAL_ENDPOINTS = {
        'us-south': 'https://api.us-south.ae.cloud.ibm.com',
        'eu-de': 'https://api.eu-de.ae.cloud.ibm.com',
    }

    @classmethod
    def new_instance(cls,
                     service_name: str = DEFAULT_SERVICE_NAME,
                    ) -> 'IbmAnalyticsEngineApiV3':
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

    @classmethod
    def get_service_url_for_region(
        cls,
        region: str,
    ) -> str:
        """
        Returns the service URL associated with the specified region.
        :param str region: a string representing the region
        :return: The service URL associated with the specified region or None
                 if no mapping for the region exists
        :rtype: str
        """
        return cls.REGIONAL_ENDPOINTS.get(region, None)

    def __init__(self,
                 authenticator: Authenticator = None,
                ) -> None:
        """
        Construct a new client for the IBM Analytics Engine API service.

        :param Authenticator authenticator: The authenticator specifies the authentication mechanism.
               Get up to date information from https://github.com/IBM/python-sdk-core/blob/main/README.md
               about initializing the authenticator of your choice.
        """
        BaseService.__init__(self,
                             service_url=self.DEFAULT_SERVICE_URL,
                             authenticator=authenticator)


    #########################
    # Analytics Engines V3
    #########################


    def get_instance(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Find Analytics Engine by id.

        Retrieve the details of a single Analytics Engine instance.

        :param str instance_id: GUID of the Analytics Engine service instance to
               retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Instance` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_instance')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_instance_state(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Find Analytics Engine state by id.

        Retrieve the state of a single Analytics Engine instance.

        :param str instance_id: GUID of the Analytics Engine service instance to
               retrieve state.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InstanceGetStateResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_instance_state')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/state'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def set_instance_home(self,
        instance_id: str,
        *,
        new_instance_id: str = None,
        new_provider: str = None,
        new_type: str = None,
        new_region: str = None,
        new_endpoint: str = None,
        new_hmac_access_key: str = None,
        new_hmac_secret_key: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Set instance home.

        Provide the details of the Cloud Object Storage instance to associate with the
        Analytics Engine instance and use as 'instance home' if 'instance home' has not
        already been set.
        **Note**: You can set 'instance home' again if the instance is in
        'instance_home_creation_failure' state.

        :param str instance_id: The ID of the Analytics Engine instance for which
               'instance home' is to be set.
        :param str new_instance_id: (optional) UUID of the instance home storage
               instance.
        :param str new_provider: (optional) Currently only ibm-cos (IBM Cloud
               Object Storage) is supported.
        :param str new_type: (optional) Type of the instance home storage.
               Currently, only objectstore (Cloud Object Storage) is supported.
        :param str new_region: (optional) Region of the Cloud Object Storage
               instance.
        :param str new_endpoint: (optional) Endpoint to access the Cloud Object
               Storage instance.
        :param str new_hmac_access_key: (optional) Cloud Object Storage access key.
        :param str new_hmac_secret_key: (optional) Cloud Object Storage secret key.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InstanceHomeResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='set_instance_home')
        headers.update(sdk_headers)

        data = {
            'instance_id': new_instance_id,
            'provider': new_provider,
            'type': new_type,
            'region': new_region,
            'endpoint': new_endpoint,
            'hmac_access_key': new_hmac_access_key,
            'hmac_secret_key': new_hmac_secret_key
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/instance_home'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_instance_default_configs(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get instance default Spark configurations.

        Get the default Spark configuration properties that will be applied to all
        applications of the instance.

        :param str instance_id: The ID of the Analytics Engine instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_instance_default_configs')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/default_configs'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def replace_instance_default_configs(self,
        instance_id: str,
        body: dict,
        **kwargs
    ) -> DetailedResponse:
        """
        Replace instance default Spark configurations.

        Replace the default Spark configuration properties that will be applied to all
        applications of the instance.

        :param str instance_id: The ID of the Analytics Engine instance.
        :param dict body: Spark configuration properties to replace existing
               instance default Spark configurations.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if body is None:
            raise ValueError('body must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='replace_instance_default_configs')
        headers.update(sdk_headers)

        data = json.dumps(body)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/default_configs'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def update_instance_default_configs(self,
        instance_id: str,
        body: dict,
        **kwargs
    ) -> DetailedResponse:
        """
        Update instance default Spark configurations.

        Update the default Spark configuration properties that will be applied to all
        applications of the instance.

        :param str instance_id: The ID of the Analytics Engine instance.
        :param dict body: Spark configuration properties to be updated. Properties
               will be merged with existing configuration properties. Set a property value
               to `null` in order to unset it.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if body is None:
            raise ValueError('body must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='update_instance_default_configs')
        headers.update(sdk_headers)

        data = json.dumps(body)
        headers['content-type'] = 'application/merge-patch+json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/default_configs'.format(**path_param_dict)
        request = self.prepare_request(method='PATCH',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_instance_default_runtime(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get instance default runtime.

        Get the default runtime environment on which all workloads of the instance will
        run.

        :param str instance_id: The ID of the Analytics Engine instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Runtime` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_instance_default_runtime')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/default_runtime'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def replace_instance_default_runtime(self,
        instance_id: str,
        *,
        spark_version: str = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Replace instance default runtime.

        Replace the default runtime environment on which all workloads of the instance
        will run.

        :param str instance_id: The ID of the Analytics Engine instance.
        :param str spark_version: (optional) Spark version of the runtime
               environment.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `Runtime` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='replace_instance_default_runtime')
        headers.update(sdk_headers)

        data = {
            'spark_version': spark_version
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/default_runtime'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def create_application(self,
        instance_id: str,
        *,
        application_details: 'ApplicationRequestApplicationDetails' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Deploy a Spark application.

        Deploys a Spark application on a given serverless Spark instance.

        :param str instance_id: The identifier of the Analytics Engine instance
               associated with the Spark application(s).
        :param ApplicationRequestApplicationDetails application_details: (optional)
               Application details.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApplicationResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if application_details is not None:
            application_details = convert_model(application_details)
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='create_application')
        headers.update(sdk_headers)

        data = {
            'application_details': application_details
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark_applications'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def list_applications(self,
        instance_id: str,
        *,
        state: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        List all Spark applications.

        Returns a list of all Spark applications submitted to the specified Analytics
        Engine instance. The result can be filtered by specifying query parameters.

        :param str instance_id: The identifier of the Analytics Engine instance
               associated with the Spark application(s).
        :param List[str] state: (optional) List of Spark application states that
               will be used to filter the response.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApplicationCollection` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='list_applications')
        headers.update(sdk_headers)

        params = {
            'state': convert_list(state)
        }

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark_applications'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers,
                                       params=params)

        response = self.send(request, **kwargs)
        return response


    def get_application(self,
        instance_id: str,
        application_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the details of a given Spark application.

        Gets the details of a given Spark application.

        :param str instance_id: Identifier of the instance to which the application
               belongs.
        :param str application_id: Identifier of the application for which details
               are requested.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApplicationGetResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if application_id is None:
            raise ValueError('application_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_application')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'application_id']
        path_param_values = self.encode_path_vars(instance_id, application_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark_applications/{application_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_application(self,
        instance_id: str,
        application_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stop application.

        Stops a running application identified by the app_id identifier. This is an
        idempotent operation. Performs no action if the requested application is already
        stopped or completed.

        :param str instance_id: Identifier of the instance to which the application
               belongs.
        :param str application_id: Identifier of the application that needs to be
               stopped.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if application_id is None:
            raise ValueError('application_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='delete_application')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']

        path_param_keys = ['instance_id', 'application_id']
        path_param_values = self.encode_path_vars(instance_id, application_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark_applications/{application_id}'.format(**path_param_dict)
        request = self.prepare_request(method='DELETE',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_application_state(self,
        instance_id: str,
        application_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get the status of the application.

        Returns the status of the given Spark application.

        :param str instance_id: Identifier of the instance to which the
               applications belongs.
        :param str application_id: Identifier of the application for which details
               are requested.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApplicationGetStateResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        if application_id is None:
            raise ValueError('application_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_application_state')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'application_id']
        path_param_values = self.encode_path_vars(instance_id, application_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark_applications/{application_id}/state'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_current_resource_consumption(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get current resource consumption.

        Gives the total memory and virtual processor cores allotted to all the
        applications running in the service instance at this point in time. When
        auto-scaled applications are running, the resources allotted will change over
        time, based on the applications's demands. Note: The consumption is not an
        indication of actual resource consumption by Spark processes. It is the sum of
        resources allocated to the currently running applications at the time of
        application submission.

        :param str instance_id: ID of the Analytics Engine instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `CurrentResourceConsumptionResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_current_resource_consumption')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/current_resource_consumption'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_resource_consumption_limits(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get resource consumption limits.

        Returns the maximum total memory and virtual processor cores that can be allotted
        across all the applications running in the service instance at any point in time.

        :param str instance_id: ID of the Analytics Engine instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ResourceConsumptionLimitsResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_resource_consumption_limits')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/resource_consumption_limits'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def replace_log_forwarding_config(self,
        instance_id: str,
        *,
        enabled: bool = None,
        sources: List[str] = None,
        tags: List[str] = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Replace log forwarding configuration.

        Modify the configuration for forwarding logs from the Analytics Engine instance to
        IBM Log Analysis server. Use this endpoint to enable or disable log forwarding.

        :param str instance_id: ID of the Analytics Engine instance.
        :param bool enabled: (optional) Enable or disable log forwarding.
        :param List[str] sources: (optional) List of sources of logs that will be
               forwarded. By default, only 'spark-driver' logs are forwarded.
        :param List[str] tags: (optional) List of tags to be applied to the logs
               being forwarded. They can be used to filter the logs in the IBM Log
               Analysis server.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogForwardingConfigResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='replace_log_forwarding_config')
        headers.update(sdk_headers)

        data = {
            'enabled': enabled,
            'sources': sources,
            'tags': tags
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/log_forwarding_config'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_log_forwarding_config(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Get log forwarding configuration.

        Retrieve the log forwarding configuration of the Analytics Engine instance.

        :param str instance_id: ID of the Analytics Engine instance.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LogForwardingConfigResponse` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_log_forwarding_config')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/log_forwarding_config'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def configure_platform_logging(self,
        instance_guid: str,
        *,
        enable: bool = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Enable or disable log forwarding.

        Enable or disable log forwarding from IBM Analytics Engine to IBM Log Analysis
        server.

        :param str instance_guid: GUID of the instance details for which log
               forwarding is to be configured.
        :param bool enable: (optional) Enable or disable log forwarding.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoggingConfigurationResponse` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='configure_platform_logging')
        headers.update(sdk_headers)

        data = {
            'enable': enable
        }
        data = {k: v for (k, v) in data.items() if v is not None}
        data = json.dumps(data)
        headers['content-type'] = 'application/json'

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_guid']
        path_param_values = self.encode_path_vars(instance_guid)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_guid}/logging'.format(**path_param_dict)
        request = self.prepare_request(method='PUT',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_logging_configuration(self,
        instance_guid: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Retrieve the logging configuration for a given instance id.

        Retrieve the logging configuration of a given Analytics Engine instance.

        :param str instance_guid: GUID of the Analytics Engine service instance to
               retrieve log configuration.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `LoggingConfigurationResponse` object
        """

        if instance_guid is None:
            raise ValueError('instance_guid must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_logging_configuration')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
            del kwargs['headers']
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_guid']
        path_param_values = self.encode_path_vars(instance_guid)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_guid}/logging'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


class ListApplicationsEnums:
    """
    Enums for list_applications parameters.
    """

    class State(str, Enum):
        """
        List of Spark application states that will be used to filter the response.
        """
        FINISHED = 'finished'
        RUNNING = 'running'
        FAILED = 'failed'
        ERROR = 'error'
        ACCEPTED = 'accepted'
        SUBMITTED = 'submitted'
        WAITING = 'waiting'
        UNKNOWN = 'unknown'
        STOPPED = 'stopped'
        AUTO_TERMINATED = 'auto_terminated'
        OPS_TERMINATED = 'ops_terminated'


##############################################################################
# Models
##############################################################################


class Application():
    """
    Details of a Spark application.

    :attr str id: (optional) Identifier provided by Analytics Engine service for the
          Spark application.
    :attr str href: (optional) Full URL of the resource.
    :attr Runtime runtime: (optional) Runtime enviroment for applications and other
          workloads.
    :attr str spark_application_id: (optional) Identifier provided by Apache Spark
          for the application.
    :attr str spark_application_name: (optional) Name of the Spark application.
    :attr str state: (optional) State of the Spark application.
    :attr str start_time: (optional) Time when the application was started.
    :attr str end_time: (optional) Time when the application run ended in success,
          failure or was stopped.
    :attr str finish_time: (optional) Time when the application was completed.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 href: str = None,
                 runtime: 'Runtime' = None,
                 spark_application_id: str = None,
                 spark_application_name: str = None,
                 state: str = None,
                 start_time: str = None,
                 end_time: str = None,
                 finish_time: str = None) -> None:
        """
        Initialize a Application object.

        :param str id: (optional) Identifier provided by Analytics Engine service
               for the Spark application.
        :param str href: (optional) Full URL of the resource.
        :param Runtime runtime: (optional) Runtime enviroment for applications and
               other workloads.
        :param str spark_application_id: (optional) Identifier provided by Apache
               Spark for the application.
        :param str spark_application_name: (optional) Name of the Spark
               application.
        :param str state: (optional) State of the Spark application.
        :param str start_time: (optional) Time when the application was started.
        :param str end_time: (optional) Time when the application run ended in
               success, failure or was stopped.
        :param str finish_time: (optional) Time when the application was completed.
        """
        self.id = id
        self.href = href
        self.runtime = runtime
        self.spark_application_id = spark_application_id
        self.spark_application_name = spark_application_name
        self.state = state
        self.start_time = start_time
        self.end_time = end_time
        self.finish_time = finish_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Application':
        """Initialize a Application object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'runtime' in _dict:
            args['runtime'] = Runtime.from_dict(_dict.get('runtime'))
        if 'spark_application_id' in _dict:
            args['spark_application_id'] = _dict.get('spark_application_id')
        if 'spark_application_name' in _dict:
            args['spark_application_name'] = _dict.get('spark_application_name')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        if 'finish_time' in _dict:
            args['finish_time'] = _dict.get('finish_time')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Application object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'runtime') and self.runtime is not None:
            _dict['runtime'] = self.runtime.to_dict()
        if hasattr(self, 'spark_application_id') and self.spark_application_id is not None:
            _dict['spark_application_id'] = self.spark_application_id
        if hasattr(self, 'spark_application_name') and self.spark_application_name is not None:
            _dict['spark_application_name'] = self.spark_application_name
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'finish_time') and self.finish_time is not None:
            _dict['finish_time'] = self.finish_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Application object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Application') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Application') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of the Spark application.
        """
        FINISHED = 'finished'
        RUNNING = 'running'
        FAILED = 'failed'
        ERROR = 'error'
        ACCEPTED = 'accepted'
        SUBMITTED = 'submitted'
        WAITING = 'waiting'
        UNKNOWN = 'unknown'
        STOPPED = 'stopped'
        AUTO_TERMINATED = 'auto_terminated'
        OPS_TERMINATED = 'ops_terminated'


class ApplicationCollection():
    """
    An array of application details.

    :attr List[Application] applications: (optional) List of applications.
    """

    def __init__(self,
                 *,
                 applications: List['Application'] = None) -> None:
        """
        Initialize a ApplicationCollection object.

        :param List[Application] applications: (optional) List of applications.
        """
        self.applications = applications

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationCollection':
        """Initialize a ApplicationCollection object from a json dictionary."""
        args = {}
        if 'applications' in _dict:
            args['applications'] = [Application.from_dict(x) for x in _dict.get('applications')]
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationCollection object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'applications') and self.applications is not None:
            _dict['applications'] = [x.to_dict() for x in self.applications]
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicationCollection object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicationCollection') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicationCollection') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApplicationDetails():
    """
    Application details.

    :attr str application: (optional) Path of the application to run.
    :attr Runtime runtime: (optional) Runtime enviroment for applications and other
          workloads.
    :attr str jars: (optional) Path of the jar files containing the application.
    :attr str packages: (optional) Package names.
    :attr str repositories: (optional) Repositories names.
    :attr str files: (optional) File names.
    :attr str archives: (optional) Archive Names.
    :attr str name: (optional) Name of the application.
    :attr str class_: (optional) Entry point for a Spark application bundled as a
          '.jar' file. This is applicable only for Java or Scala applications.
    :attr List[str] arguments: (optional) An array of arguments to be passed to the
          application.
    :attr dict conf: (optional) Application configurations to override the value
          specified at instance level. See [Spark environment variables](
          https://spark.apache.org/docs/latest/configuration.html#available-properties)
          for a list of the supported variables.
    :attr dict env: (optional) Application environment configurations to use. See
          [Spark environment
          variables](https://spark.apache.org/docs/latest/configuration.html#environment-variables)
          for a list of the supported variables.
    """

    def __init__(self,
                 *,
                 application: str = None,
                 runtime: 'Runtime' = None,
                 jars: str = None,
                 packages: str = None,
                 repositories: str = None,
                 files: str = None,
                 archives: str = None,
                 name: str = None,
                 class_: str = None,
                 arguments: List[str] = None,
                 conf: dict = None,
                 env: dict = None) -> None:
        """
        Initialize a ApplicationDetails object.

        :param str application: (optional) Path of the application to run.
        :param Runtime runtime: (optional) Runtime enviroment for applications and
               other workloads.
        :param str jars: (optional) Path of the jar files containing the
               application.
        :param str packages: (optional) Package names.
        :param str repositories: (optional) Repositories names.
        :param str files: (optional) File names.
        :param str archives: (optional) Archive Names.
        :param str name: (optional) Name of the application.
        :param str class_: (optional) Entry point for a Spark application bundled
               as a '.jar' file. This is applicable only for Java or Scala applications.
        :param List[str] arguments: (optional) An array of arguments to be passed
               to the application.
        :param dict conf: (optional) Application configurations to override the
               value specified at instance level. See [Spark environment variables](
               https://spark.apache.org/docs/latest/configuration.html#available-properties)
               for a list of the supported variables.
        :param dict env: (optional) Application environment configurations to use.
               See [Spark environment
               variables](https://spark.apache.org/docs/latest/configuration.html#environment-variables)
               for a list of the supported variables.
        """
        self.application = application
        self.runtime = runtime
        self.jars = jars
        self.packages = packages
        self.repositories = repositories
        self.files = files
        self.archives = archives
        self.name = name
        self.class_ = class_
        self.arguments = arguments
        self.conf = conf
        self.env = env

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationDetails':
        """Initialize a ApplicationDetails object from a json dictionary."""
        args = {}
        if 'application' in _dict:
            args['application'] = _dict.get('application')
        if 'runtime' in _dict:
            args['runtime'] = Runtime.from_dict(_dict.get('runtime'))
        if 'jars' in _dict:
            args['jars'] = _dict.get('jars')
        if 'packages' in _dict:
            args['packages'] = _dict.get('packages')
        if 'repositories' in _dict:
            args['repositories'] = _dict.get('repositories')
        if 'files' in _dict:
            args['files'] = _dict.get('files')
        if 'archives' in _dict:
            args['archives'] = _dict.get('archives')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'class' in _dict:
            args['class_'] = _dict.get('class')
        if 'arguments' in _dict:
            args['arguments'] = _dict.get('arguments')
        if 'conf' in _dict:
            args['conf'] = _dict.get('conf')
        if 'env' in _dict:
            args['env'] = _dict.get('env')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application') and self.application is not None:
            _dict['application'] = self.application
        if hasattr(self, 'runtime') and self.runtime is not None:
            _dict['runtime'] = self.runtime.to_dict()
        if hasattr(self, 'jars') and self.jars is not None:
            _dict['jars'] = self.jars
        if hasattr(self, 'packages') and self.packages is not None:
            _dict['packages'] = self.packages
        if hasattr(self, 'repositories') and self.repositories is not None:
            _dict['repositories'] = self.repositories
        if hasattr(self, 'files') and self.files is not None:
            _dict['files'] = self.files
        if hasattr(self, 'archives') and self.archives is not None:
            _dict['archives'] = self.archives
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'class_') and self.class_ is not None:
            _dict['class'] = self.class_
        if hasattr(self, 'arguments') and self.arguments is not None:
            _dict['arguments'] = self.arguments
        if hasattr(self, 'conf') and self.conf is not None:
            _dict['conf'] = self.conf
        if hasattr(self, 'env') and self.env is not None:
            _dict['env'] = self.env
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicationDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicationDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicationDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApplicationGetResponse():
    """
    Response of the Application Get API.

    :attr ApplicationDetails application_details: (optional) Application details.
    :attr str id: (optional) Application ID.
    :attr str spark_application_id: (optional) Identifier provided by Apache Spark
          for the application.
    :attr str spark_application_name: (optional) Name of the Spark application.
    :attr str state: (optional) State of the Spark application.
    :attr List[ApplicationGetResponseStateDetailsItem] state_details: (optional)
          List of additional information messages on the current state of the application.
    :attr datetime start_time: (optional) Application start time in the format
          YYYY-MM-DDTHH:mm:ssZ.
    :attr datetime end_time: (optional) Application end time in the format
          YYYY-MM-DDTHH:mm:ssZ.
    :attr datetime finish_time: (optional) Application finish time in the format
          YYYY-MM-DDTHH:mm:ssZ.
    """

    def __init__(self,
                 *,
                 application_details: 'ApplicationDetails' = None,
                 id: str = None,
                 spark_application_id: str = None,
                 spark_application_name: str = None,
                 state: str = None,
                 state_details: List['ApplicationGetResponseStateDetailsItem'] = None,
                 start_time: datetime = None,
                 end_time: datetime = None,
                 finish_time: datetime = None) -> None:
        """
        Initialize a ApplicationGetResponse object.

        :param ApplicationDetails application_details: (optional) Application
               details.
        :param str id: (optional) Application ID.
        :param str spark_application_id: (optional) Identifier provided by Apache
               Spark for the application.
        :param str spark_application_name: (optional) Name of the Spark
               application.
        :param str state: (optional) State of the Spark application.
        :param List[ApplicationGetResponseStateDetailsItem] state_details:
               (optional) List of additional information messages on the current state of
               the application.
        :param datetime start_time: (optional) Application start time in the format
               YYYY-MM-DDTHH:mm:ssZ.
        :param datetime end_time: (optional) Application end time in the format
               YYYY-MM-DDTHH:mm:ssZ.
        :param datetime finish_time: (optional) Application finish time in the
               format YYYY-MM-DDTHH:mm:ssZ.
        """
        self.application_details = application_details
        self.id = id
        self.spark_application_id = spark_application_id
        self.spark_application_name = spark_application_name
        self.state = state
        self.state_details = state_details
        self.start_time = start_time
        self.end_time = end_time
        self.finish_time = finish_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationGetResponse':
        """Initialize a ApplicationGetResponse object from a json dictionary."""
        args = {}
        if 'application_details' in _dict:
            args['application_details'] = ApplicationDetails.from_dict(_dict.get('application_details'))
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'spark_application_id' in _dict:
            args['spark_application_id'] = _dict.get('spark_application_id')
        if 'spark_application_name' in _dict:
            args['spark_application_name'] = _dict.get('spark_application_name')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'state_details' in _dict:
            args['state_details'] = [ApplicationGetResponseStateDetailsItem.from_dict(x) for x in _dict.get('state_details')]
        if 'start_time' in _dict:
            args['start_time'] = string_to_datetime(_dict.get('start_time'))
        if 'end_time' in _dict:
            args['end_time'] = string_to_datetime(_dict.get('end_time'))
        if 'finish_time' in _dict:
            args['finish_time'] = string_to_datetime(_dict.get('finish_time'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationGetResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application_details') and self.application_details is not None:
            _dict['application_details'] = self.application_details.to_dict()
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'spark_application_id') and self.spark_application_id is not None:
            _dict['spark_application_id'] = self.spark_application_id
        if hasattr(self, 'spark_application_name') and self.spark_application_name is not None:
            _dict['spark_application_name'] = self.spark_application_name
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'state_details') and self.state_details is not None:
            _dict['state_details'] = [x.to_dict() for x in self.state_details]
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = datetime_to_string(self.start_time)
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = datetime_to_string(self.end_time)
        if hasattr(self, 'finish_time') and self.finish_time is not None:
            _dict['finish_time'] = datetime_to_string(self.finish_time)
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicationGetResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicationGetResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicationGetResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of the Spark application.
        """
        FINISHED = 'finished'
        RUNNING = 'running'
        FAILED = 'failed'
        ERROR = 'error'
        ACCEPTED = 'accepted'
        SUBMITTED = 'submitted'
        WAITING = 'waiting'
        UNKNOWN = 'unknown'
        STOPPED = 'stopped'
        AUTO_TERMINATED = 'auto_terminated'
        OPS_TERMINATED = 'ops_terminated'


class ApplicationGetResponseStateDetailsItem():
    """
    Additional information message on the current state of the application.

    :attr str type: (optional) Type of the message.
    :attr str code: (optional) Fixed code for the message.
    :attr str message: (optional) A descriptive message providing additional
          information on the current application state.
    """

    def __init__(self,
                 *,
                 type: str = None,
                 code: str = None,
                 message: str = None) -> None:
        """
        Initialize a ApplicationGetResponseStateDetailsItem object.

        :param str type: (optional) Type of the message.
        :param str code: (optional) Fixed code for the message.
        :param str message: (optional) A descriptive message providing additional
               information on the current application state.
        """
        self.type = type
        self.code = code
        self.message = message

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationGetResponseStateDetailsItem':
        """Initialize a ApplicationGetResponseStateDetailsItem object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'code' in _dict:
            args['code'] = _dict.get('code')
        if 'message' in _dict:
            args['message'] = _dict.get('message')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationGetResponseStateDetailsItem object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'code') and self.code is not None:
            _dict['code'] = self.code
        if hasattr(self, 'message') and self.message is not None:
            _dict['message'] = self.message
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicationGetResponseStateDetailsItem object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicationGetResponseStateDetailsItem') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicationGetResponseStateDetailsItem') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class TypeEnum(str, Enum):
        """
        Type of the message.
        """
        USER_ERROR = 'user_error'
        SERVER_ERROR = 'server_error'
        INFO = 'info'


class ApplicationGetStateResponse():
    """
    State of a given application.

    :attr str id: (optional) Identifier of the application.
    :attr str state: (optional) State of the Spark application.
    :attr str start_time: (optional) Time when the application was started.
    :attr str end_time: (optional) Time when the application run ended in success,
          failure or was stopped.
    :attr str finish_time: (optional) Time when the application was completed.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 state: str = None,
                 start_time: str = None,
                 end_time: str = None,
                 finish_time: str = None) -> None:
        """
        Initialize a ApplicationGetStateResponse object.

        :param str id: (optional) Identifier of the application.
        :param str state: (optional) State of the Spark application.
        :param str start_time: (optional) Time when the application was started.
        :param str end_time: (optional) Time when the application run ended in
               success, failure or was stopped.
        :param str finish_time: (optional) Time when the application was completed.
        """
        self.id = id
        self.state = state
        self.start_time = start_time
        self.end_time = end_time
        self.finish_time = finish_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationGetStateResponse':
        """Initialize a ApplicationGetStateResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        if 'end_time' in _dict:
            args['end_time'] = _dict.get('end_time')
        if 'finish_time' in _dict:
            args['finish_time'] = _dict.get('finish_time')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationGetStateResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'end_time') and self.end_time is not None:
            _dict['end_time'] = self.end_time
        if hasattr(self, 'finish_time') and self.finish_time is not None:
            _dict['finish_time'] = self.finish_time
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicationGetStateResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicationGetStateResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicationGetStateResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of the Spark application.
        """
        FINISHED = 'finished'
        RUNNING = 'running'
        FAILED = 'failed'
        ERROR = 'error'
        ACCEPTED = 'accepted'
        SUBMITTED = 'submitted'
        WAITING = 'waiting'
        UNKNOWN = 'unknown'
        STOPPED = 'stopped'
        AUTO_TERMINATED = 'auto_terminated'
        OPS_TERMINATED = 'ops_terminated'


class ApplicationRequestApplicationDetails():
    """
    Application details.

    :attr str application: (optional) Path of the application to run.
    :attr Runtime runtime: (optional) Runtime enviroment for applications and other
          workloads.
    :attr str jars: (optional) Path of the jar files containing the application.
    :attr str packages: (optional) Package names.
    :attr str repositories: (optional) Repositories names.
    :attr str files: (optional) File names.
    :attr str archives: (optional) Archive Names.
    :attr str name: (optional) Name of the application.
    :attr str class_: (optional) Entry point for a Spark application bundled as a
          '.jar' file. This is applicable only for Java or Scala applications.
    :attr List[str] arguments: (optional) An array of arguments to be passed to the
          application.
    :attr dict conf: (optional) Application configurations to override the value
          specified at instance level. See [Spark environment variables](
          https://spark.apache.org/docs/latest/configuration.html#available-properties)
          for a list of the supported variables.
    :attr dict env: (optional) Application environment configurations to use. See
          [Spark environment
          variables](https://spark.apache.org/docs/latest/configuration.html#environment-variables)
          for a list of the supported variables.
    """

    def __init__(self,
                 *,
                 application: str = None,
                 runtime: 'Runtime' = None,
                 jars: str = None,
                 packages: str = None,
                 repositories: str = None,
                 files: str = None,
                 archives: str = None,
                 name: str = None,
                 class_: str = None,
                 arguments: List[str] = None,
                 conf: dict = None,
                 env: dict = None) -> None:
        """
        Initialize a ApplicationRequestApplicationDetails object.

        :param str application: (optional) Path of the application to run.
        :param Runtime runtime: (optional) Runtime enviroment for applications and
               other workloads.
        :param str jars: (optional) Path of the jar files containing the
               application.
        :param str packages: (optional) Package names.
        :param str repositories: (optional) Repositories names.
        :param str files: (optional) File names.
        :param str archives: (optional) Archive Names.
        :param str name: (optional) Name of the application.
        :param str class_: (optional) Entry point for a Spark application bundled
               as a '.jar' file. This is applicable only for Java or Scala applications.
        :param List[str] arguments: (optional) An array of arguments to be passed
               to the application.
        :param dict conf: (optional) Application configurations to override the
               value specified at instance level. See [Spark environment variables](
               https://spark.apache.org/docs/latest/configuration.html#available-properties)
               for a list of the supported variables.
        :param dict env: (optional) Application environment configurations to use.
               See [Spark environment
               variables](https://spark.apache.org/docs/latest/configuration.html#environment-variables)
               for a list of the supported variables.
        """
        self.application = application
        self.runtime = runtime
        self.jars = jars
        self.packages = packages
        self.repositories = repositories
        self.files = files
        self.archives = archives
        self.name = name
        self.class_ = class_
        self.arguments = arguments
        self.conf = conf
        self.env = env

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationRequestApplicationDetails':
        """Initialize a ApplicationRequestApplicationDetails object from a json dictionary."""
        args = {}
        if 'application' in _dict:
            args['application'] = _dict.get('application')
        if 'runtime' in _dict:
            args['runtime'] = Runtime.from_dict(_dict.get('runtime'))
        if 'jars' in _dict:
            args['jars'] = _dict.get('jars')
        if 'packages' in _dict:
            args['packages'] = _dict.get('packages')
        if 'repositories' in _dict:
            args['repositories'] = _dict.get('repositories')
        if 'files' in _dict:
            args['files'] = _dict.get('files')
        if 'archives' in _dict:
            args['archives'] = _dict.get('archives')
        if 'name' in _dict:
            args['name'] = _dict.get('name')
        if 'class' in _dict:
            args['class_'] = _dict.get('class')
        if 'arguments' in _dict:
            args['arguments'] = _dict.get('arguments')
        if 'conf' in _dict:
            args['conf'] = _dict.get('conf')
        if 'env' in _dict:
            args['env'] = _dict.get('env')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationRequestApplicationDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application') and self.application is not None:
            _dict['application'] = self.application
        if hasattr(self, 'runtime') and self.runtime is not None:
            _dict['runtime'] = self.runtime.to_dict()
        if hasattr(self, 'jars') and self.jars is not None:
            _dict['jars'] = self.jars
        if hasattr(self, 'packages') and self.packages is not None:
            _dict['packages'] = self.packages
        if hasattr(self, 'repositories') and self.repositories is not None:
            _dict['repositories'] = self.repositories
        if hasattr(self, 'files') and self.files is not None:
            _dict['files'] = self.files
        if hasattr(self, 'archives') and self.archives is not None:
            _dict['archives'] = self.archives
        if hasattr(self, 'name') and self.name is not None:
            _dict['name'] = self.name
        if hasattr(self, 'class_') and self.class_ is not None:
            _dict['class'] = self.class_
        if hasattr(self, 'arguments') and self.arguments is not None:
            _dict['arguments'] = self.arguments
        if hasattr(self, 'conf') and self.conf is not None:
            _dict['conf'] = self.conf
        if hasattr(self, 'env') and self.env is not None:
            _dict['env'] = self.env
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicationRequestApplicationDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicationRequestApplicationDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicationRequestApplicationDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApplicationResponse():
    """
    Application response details.

    :attr str id: (optional) Identifier of the application that was submitted.
    :attr str state: (optional) State of the Spark application.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 state: str = None) -> None:
        """
        Initialize a ApplicationResponse object.

        :param str id: (optional) Identifier of the application that was submitted.
        :param str state: (optional) State of the Spark application.
        """
        self.id = id
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationResponse':
        """Initialize a ApplicationResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicationResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicationResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicationResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of the Spark application.
        """
        FINISHED = 'finished'
        RUNNING = 'running'
        FAILED = 'failed'
        ERROR = 'error'
        ACCEPTED = 'accepted'
        SUBMITTED = 'submitted'
        WAITING = 'waiting'
        UNKNOWN = 'unknown'
        STOPPED = 'stopped'
        AUTO_TERMINATED = 'auto_terminated'
        OPS_TERMINATED = 'ops_terminated'


class CurrentResourceConsumptionResponse():
    """
    Current resource consumption of the instance.

    :attr str cores: (optional) Number of virtual processor cores used.
    :attr str memory: (optional) Amount of memory used.
    """

    def __init__(self,
                 *,
                 cores: str = None,
                 memory: str = None) -> None:
        """
        Initialize a CurrentResourceConsumptionResponse object.

        :param str cores: (optional) Number of virtual processor cores used.
        :param str memory: (optional) Amount of memory used.
        """
        self.cores = cores
        self.memory = memory

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'CurrentResourceConsumptionResponse':
        """Initialize a CurrentResourceConsumptionResponse object from a json dictionary."""
        args = {}
        if 'cores' in _dict:
            args['cores'] = _dict.get('cores')
        if 'memory' in _dict:
            args['memory'] = _dict.get('memory')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a CurrentResourceConsumptionResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'cores') and self.cores is not None:
            _dict['cores'] = self.cores
        if hasattr(self, 'memory') and self.memory is not None:
            _dict['memory'] = self.memory
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this CurrentResourceConsumptionResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'CurrentResourceConsumptionResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'CurrentResourceConsumptionResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Instance():
    """
    Details of Analytics Engine instance.

    :attr str id: (optional) GUID of the Analytics Engine instance.
    :attr str href: (optional) Full URL of the resource.
    :attr str state: (optional) State of the Analytics Engine instance.
    :attr datetime state_change_time: (optional) Timestamp when the state of the
          instance was changed, in the format YYYY-MM-DDTHH:mm:ssZ.
    :attr Runtime default_runtime: (optional) Runtime enviroment for applications
          and other workloads.
    :attr InstanceHome instance_home: (optional) Object storage instance that acts
          as the home for custom libraries and Spark events.
    :attr InstanceDefaultConfig default_config: (optional) Instance level default
          configuration for Spark workloads.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 href: str = None,
                 state: str = None,
                 state_change_time: datetime = None,
                 default_runtime: 'Runtime' = None,
                 instance_home: 'InstanceHome' = None,
                 default_config: 'InstanceDefaultConfig' = None) -> None:
        """
        Initialize a Instance object.

        :param str id: (optional) GUID of the Analytics Engine instance.
        :param str href: (optional) Full URL of the resource.
        :param str state: (optional) State of the Analytics Engine instance.
        :param datetime state_change_time: (optional) Timestamp when the state of
               the instance was changed, in the format YYYY-MM-DDTHH:mm:ssZ.
        :param Runtime default_runtime: (optional) Runtime enviroment for
               applications and other workloads.
        :param InstanceHome instance_home: (optional) Object storage instance that
               acts as the home for custom libraries and Spark events.
        :param InstanceDefaultConfig default_config: (optional) Instance level
               default configuration for Spark workloads.
        """
        self.id = id
        self.href = href
        self.state = state
        self.state_change_time = state_change_time
        self.default_runtime = default_runtime
        self.instance_home = instance_home
        self.default_config = default_config

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Instance':
        """Initialize a Instance object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'href' in _dict:
            args['href'] = _dict.get('href')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'state_change_time' in _dict:
            args['state_change_time'] = string_to_datetime(_dict.get('state_change_time'))
        if 'default_runtime' in _dict:
            args['default_runtime'] = Runtime.from_dict(_dict.get('default_runtime'))
        if 'instance_home' in _dict:
            args['instance_home'] = InstanceHome.from_dict(_dict.get('instance_home'))
        if 'default_config' in _dict:
            args['default_config'] = InstanceDefaultConfig.from_dict(_dict.get('default_config'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Instance object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'href') and self.href is not None:
            _dict['href'] = self.href
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'state_change_time') and self.state_change_time is not None:
            _dict['state_change_time'] = datetime_to_string(self.state_change_time)
        if hasattr(self, 'default_runtime') and self.default_runtime is not None:
            _dict['default_runtime'] = self.default_runtime.to_dict()
        if hasattr(self, 'instance_home') and self.instance_home is not None:
            _dict['instance_home'] = self.instance_home.to_dict()
        if hasattr(self, 'default_config') and self.default_config is not None:
            _dict['default_config'] = self.default_config.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Instance object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Instance') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Instance') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of the Analytics Engine instance.
        """
        CREATION_ACCEPTED = 'creation_accepted'
        INITIALIZED = 'initialized'
        PREPARING = 'preparing'
        ACTIVE = 'active'
        DELETED = 'deleted'
        DISABLED = 'disabled'
        CREATION_FAILED = 'creation_failed'


class InstanceDefaultConfig():
    """
    Instance level default configuration for Spark workloads.

    :attr str key: (optional) Value of the Spark configuration key.
    """

    def __init__(self,
                 *,
                 key: str = None) -> None:
        """
        Initialize a InstanceDefaultConfig object.

        :param str key: (optional) Value of the Spark configuration key.
        """
        self.key = key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceDefaultConfig':
        """Initialize a InstanceDefaultConfig object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstanceDefaultConfig object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'key') and self.key is not None:
            _dict['key'] = self.key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstanceDefaultConfig object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceDefaultConfig') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceDefaultConfig') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstanceGetStateResponse():
    """
    State details of Analytics Engine instance.

    :attr str id: (optional) GUID of the Analytics Engine instance.
    :attr str state: (optional) State of the Analytics Engine instance.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 state: str = None) -> None:
        """
        Initialize a InstanceGetStateResponse object.

        :param str id: (optional) GUID of the Analytics Engine instance.
        :param str state: (optional) State of the Analytics Engine instance.
        """
        self.id = id
        self.state = state

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceGetStateResponse':
        """Initialize a InstanceGetStateResponse object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstanceGetStateResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstanceGetStateResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceGetStateResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceGetStateResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        State of the Analytics Engine instance.
        """
        CREATION_ACCEPTED = 'creation_accepted'
        INITIALIZED = 'initialized'
        PREPARING = 'preparing'
        ACTIVE = 'active'
        DELETED = 'deleted'
        DISABLED = 'disabled'
        CREATION_FAILED = 'creation_failed'


class InstanceHome():
    """
    Object storage instance that acts as the home for custom libraries and Spark events.

    :attr str id: (optional) UUID of the instance home storage instance.
    :attr str provider: (optional) Currently only ibm-cos (IBM Cloud Object Storage)
          is supported.
    :attr str type: (optional) Type of the instance home storage. Currently, only
          objectstore (Cloud Object Storage) is supported.
    :attr str region: (optional) Region of the Cloud Object Storage instance.
    :attr str endpoint: (optional) Endpoint to access the Cloud Object Storage
          instance.
    :attr str bucket: (optional) Cloud Object Storage bucket used as instance home.
    :attr str hmac_access_key: (optional) Cloud Object Storage access key. Masked
          for security reasons.
    :attr str hmac_secret_key: (optional) Cloud Object Storage secret key. Masked
          for security reasons.
    """

    def __init__(self,
                 *,
                 id: str = None,
                 provider: str = None,
                 type: str = None,
                 region: str = None,
                 endpoint: str = None,
                 bucket: str = None,
                 hmac_access_key: str = None,
                 hmac_secret_key: str = None) -> None:
        """
        Initialize a InstanceHome object.

        :param str id: (optional) UUID of the instance home storage instance.
        :param str provider: (optional) Currently only ibm-cos (IBM Cloud Object
               Storage) is supported.
        :param str type: (optional) Type of the instance home storage. Currently,
               only objectstore (Cloud Object Storage) is supported.
        :param str region: (optional) Region of the Cloud Object Storage instance.
        :param str endpoint: (optional) Endpoint to access the Cloud Object Storage
               instance.
        :param str bucket: (optional) Cloud Object Storage bucket used as instance
               home.
        :param str hmac_access_key: (optional) Cloud Object Storage access key.
               Masked for security reasons.
        :param str hmac_secret_key: (optional) Cloud Object Storage secret key.
               Masked for security reasons.
        """
        self.id = id
        self.provider = provider
        self.type = type
        self.region = region
        self.endpoint = endpoint
        self.bucket = bucket
        self.hmac_access_key = hmac_access_key
        self.hmac_secret_key = hmac_secret_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceHome':
        """Initialize a InstanceHome object from a json dictionary."""
        args = {}
        if 'id' in _dict:
            args['id'] = _dict.get('id')
        if 'provider' in _dict:
            args['provider'] = _dict.get('provider')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        if 'endpoint' in _dict:
            args['endpoint'] = _dict.get('endpoint')
        if 'bucket' in _dict:
            args['bucket'] = _dict.get('bucket')
        if 'hmac_access_key' in _dict:
            args['hmac_access_key'] = _dict.get('hmac_access_key')
        if 'hmac_secret_key' in _dict:
            args['hmac_secret_key'] = _dict.get('hmac_secret_key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstanceHome object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'id') and self.id is not None:
            _dict['id'] = self.id
        if hasattr(self, 'provider') and self.provider is not None:
            _dict['provider'] = self.provider
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        if hasattr(self, 'bucket') and self.bucket is not None:
            _dict['bucket'] = self.bucket
        if hasattr(self, 'hmac_access_key') and self.hmac_access_key is not None:
            _dict['hmac_access_key'] = self.hmac_access_key
        if hasattr(self, 'hmac_secret_key') and self.hmac_secret_key is not None:
            _dict['hmac_secret_key'] = self.hmac_secret_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstanceHome object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceHome') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceHome') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstanceHomeResponse():
    """
    Response of Instance home API.

    :attr str instance_id: (optional) UUID of the instance home storage instance.
    :attr str provider: (optional) Currently only ibm-cos (IBM Cloud Object Storage)
          is supported.
    :attr str type: (optional) Type of the instance home storage. Currently, only
          objectstore (Cloud Object Storage) is supported.
    :attr str region: (optional) Region of the Cloud Object Storage instance.
    :attr str endpoint: (optional) Endpoint to access the Cloud Object Storage
          instance.
    :attr str hmac_access_key: (optional) Cloud Object Storage access key.
    :attr str hmac_secret_key: (optional) Cloud Object Storage secret key.
    """

    def __init__(self,
                 *,
                 instance_id: str = None,
                 provider: str = None,
                 type: str = None,
                 region: str = None,
                 endpoint: str = None,
                 hmac_access_key: str = None,
                 hmac_secret_key: str = None) -> None:
        """
        Initialize a InstanceHomeResponse object.

        :param str instance_id: (optional) UUID of the instance home storage
               instance.
        :param str provider: (optional) Currently only ibm-cos (IBM Cloud Object
               Storage) is supported.
        :param str type: (optional) Type of the instance home storage. Currently,
               only objectstore (Cloud Object Storage) is supported.
        :param str region: (optional) Region of the Cloud Object Storage instance.
        :param str endpoint: (optional) Endpoint to access the Cloud Object Storage
               instance.
        :param str hmac_access_key: (optional) Cloud Object Storage access key.
        :param str hmac_secret_key: (optional) Cloud Object Storage secret key.
        """
        self.instance_id = instance_id
        self.provider = provider
        self.type = type
        self.region = region
        self.endpoint = endpoint
        self.hmac_access_key = hmac_access_key
        self.hmac_secret_key = hmac_secret_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceHomeResponse':
        """Initialize a InstanceHomeResponse object from a json dictionary."""
        args = {}
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'provider' in _dict:
            args['provider'] = _dict.get('provider')
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        if 'region' in _dict:
            args['region'] = _dict.get('region')
        if 'endpoint' in _dict:
            args['endpoint'] = _dict.get('endpoint')
        if 'hmac_access_key' in _dict:
            args['hmac_access_key'] = _dict.get('hmac_access_key')
        if 'hmac_secret_key' in _dict:
            args['hmac_secret_key'] = _dict.get('hmac_secret_key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstanceHomeResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
        if hasattr(self, 'provider') and self.provider is not None:
            _dict['provider'] = self.provider
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        if hasattr(self, 'region') and self.region is not None:
            _dict['region'] = self.region
        if hasattr(self, 'endpoint') and self.endpoint is not None:
            _dict['endpoint'] = self.endpoint
        if hasattr(self, 'hmac_access_key') and self.hmac_access_key is not None:
            _dict['hmac_access_key'] = self.hmac_access_key
        if hasattr(self, 'hmac_secret_key') and self.hmac_secret_key is not None:
            _dict['hmac_secret_key'] = self.hmac_secret_key
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstanceHomeResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceHomeResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceHomeResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LogForwardingConfigResponse():
    """
    Log forwarding configuration details.

    :attr List[str] sources: (optional) List of sources of logs that are being
          forwarded.
    :attr List[str] tags: (optional) List of tags that are applied to the logs being
          forwarded.
    :attr LogForwardingConfigResponseLogServer log_server: (optional) Log server
          properties.
    :attr bool enabled: (optional) Indicates whether log forwarding is enabled or
          not.
    """

    def __init__(self,
                 *,
                 sources: List[str] = None,
                 tags: List[str] = None,
                 log_server: 'LogForwardingConfigResponseLogServer' = None,
                 enabled: bool = None) -> None:
        """
        Initialize a LogForwardingConfigResponse object.

        :param List[str] sources: (optional) List of sources of logs that are being
               forwarded.
        :param List[str] tags: (optional) List of tags that are applied to the logs
               being forwarded.
        :param LogForwardingConfigResponseLogServer log_server: (optional) Log
               server properties.
        :param bool enabled: (optional) Indicates whether log forwarding is enabled
               or not.
        """
        self.sources = sources
        self.tags = tags
        self.log_server = log_server
        self.enabled = enabled

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogForwardingConfigResponse':
        """Initialize a LogForwardingConfigResponse object from a json dictionary."""
        args = {}
        if 'sources' in _dict:
            args['sources'] = _dict.get('sources')
        if 'tags' in _dict:
            args['tags'] = _dict.get('tags')
        if 'log_server' in _dict:
            args['log_server'] = LogForwardingConfigResponseLogServer.from_dict(_dict.get('log_server'))
        if 'enabled' in _dict:
            args['enabled'] = _dict.get('enabled')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogForwardingConfigResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'sources') and self.sources is not None:
            _dict['sources'] = self.sources
        if hasattr(self, 'tags') and self.tags is not None:
            _dict['tags'] = self.tags
        if hasattr(self, 'log_server') and self.log_server is not None:
            _dict['log_server'] = self.log_server.to_dict()
        if hasattr(self, 'enabled') and self.enabled is not None:
            _dict['enabled'] = self.enabled
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogForwardingConfigResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogForwardingConfigResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogForwardingConfigResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LogForwardingConfigResponseLogServer():
    """
    Log server properties.

    :attr str type: (optional) Type of the log server.
    """

    def __init__(self,
                 *,
                 type: str = None) -> None:
        """
        Initialize a LogForwardingConfigResponseLogServer object.

        :param str type: (optional) Type of the log server.
        """
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LogForwardingConfigResponseLogServer':
        """Initialize a LogForwardingConfigResponseLogServer object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LogForwardingConfigResponseLogServer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LogForwardingConfigResponseLogServer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LogForwardingConfigResponseLogServer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LogForwardingConfigResponseLogServer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoggingConfigurationResponse():
    """
    Response of logging API.

    :attr List[str] components: (optional) component array.
    :attr LoggingConfigurationResponseLogServer log_server: (optional) log server
          properties.
    :attr bool enable: (optional) enable.
    """

    def __init__(self,
                 *,
                 components: List[str] = None,
                 log_server: 'LoggingConfigurationResponseLogServer' = None,
                 enable: bool = None) -> None:
        """
        Initialize a LoggingConfigurationResponse object.

        :param List[str] components: (optional) component array.
        :param LoggingConfigurationResponseLogServer log_server: (optional) log
               server properties.
        :param bool enable: (optional) enable.
        """
        self.components = components
        self.log_server = log_server
        self.enable = enable

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoggingConfigurationResponse':
        """Initialize a LoggingConfigurationResponse object from a json dictionary."""
        args = {}
        if 'components' in _dict:
            args['components'] = _dict.get('components')
        if 'log_server' in _dict:
            args['log_server'] = LoggingConfigurationResponseLogServer.from_dict(_dict.get('log_server'))
        if 'enable' in _dict:
            args['enable'] = _dict.get('enable')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoggingConfigurationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'components') and self.components is not None:
            _dict['components'] = self.components
        if hasattr(self, 'log_server') and self.log_server is not None:
            _dict['log_server'] = self.log_server.to_dict()
        if hasattr(self, 'enable') and self.enable is not None:
            _dict['enable'] = self.enable
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoggingConfigurationResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoggingConfigurationResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoggingConfigurationResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class LoggingConfigurationResponseLogServer():
    """
    log server properties.

    :attr str type: (optional) type of log server.
    """

    def __init__(self,
                 *,
                 type: str = None) -> None:
        """
        Initialize a LoggingConfigurationResponseLogServer object.

        :param str type: (optional) type of log server.
        """
        self.type = type

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'LoggingConfigurationResponseLogServer':
        """Initialize a LoggingConfigurationResponseLogServer object from a json dictionary."""
        args = {}
        if 'type' in _dict:
            args['type'] = _dict.get('type')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a LoggingConfigurationResponseLogServer object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'type') and self.type is not None:
            _dict['type'] = self.type
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this LoggingConfigurationResponseLogServer object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'LoggingConfigurationResponseLogServer') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'LoggingConfigurationResponseLogServer') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ResourceConsumptionLimitsResponse():
    """
    Resource consumption limits for the instance.

    :attr str max_cores: (optional) Maximum number of virtual processor cores that
          be used in the instance.
    :attr str max_memory: (optional) Maximum memory that can be used in the
          instance.
    """

    def __init__(self,
                 *,
                 max_cores: str = None,
                 max_memory: str = None) -> None:
        """
        Initialize a ResourceConsumptionLimitsResponse object.

        :param str max_cores: (optional) Maximum number of virtual processor cores
               that be used in the instance.
        :param str max_memory: (optional) Maximum memory that can be used in the
               instance.
        """
        self.max_cores = max_cores
        self.max_memory = max_memory

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ResourceConsumptionLimitsResponse':
        """Initialize a ResourceConsumptionLimitsResponse object from a json dictionary."""
        args = {}
        if 'max_cores' in _dict:
            args['max_cores'] = _dict.get('max_cores')
        if 'max_memory' in _dict:
            args['max_memory'] = _dict.get('max_memory')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ResourceConsumptionLimitsResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'max_cores') and self.max_cores is not None:
            _dict['max_cores'] = self.max_cores
        if hasattr(self, 'max_memory') and self.max_memory is not None:
            _dict['max_memory'] = self.max_memory
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ResourceConsumptionLimitsResponse object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ResourceConsumptionLimitsResponse') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ResourceConsumptionLimitsResponse') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class Runtime():
    """
    Runtime enviroment for applications and other workloads.

    :attr str spark_version: (optional) Spark version of the runtime environment.
    """

    def __init__(self,
                 *,
                 spark_version: str = None) -> None:
        """
        Initialize a Runtime object.

        :param str spark_version: (optional) Spark version of the runtime
               environment.
        """
        self.spark_version = spark_version

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'Runtime':
        """Initialize a Runtime object from a json dictionary."""
        args = {}
        if 'spark_version' in _dict:
            args['spark_version'] = _dict.get('spark_version')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a Runtime object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'spark_version') and self.spark_version is not None:
            _dict['spark_version'] = self.spark_version
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this Runtime object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'Runtime') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'Runtime') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
