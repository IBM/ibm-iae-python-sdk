# coding: utf-8

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

# IBM OpenAPI SDK Code Generator Version: 3.37.0-a85661cd-20210802-190136
 
"""
Create and manage serverless Spark instances and run applications.
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

class IbmAnalyticsEngineApiV3(BaseService):
    """The IBM Analytics Engine API V3 service."""

    DEFAULT_SERVICE_URL = 'https://api.us-south.ae.cloud.ibm.com'
    DEFAULT_SERVICE_NAME = 'ibm_analytics_engine_api'

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
    # Analytics Engines V3
    #########################


    def get_instance_by_id(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Find instance by id.

        Retrieve the details of a single instance.

        :param str instance_id: Identifier of the instance to retrieve.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `InstanceDetails` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_instance_by_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
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


    def create_application(self,
        instance_id: str,
        *,
        application_details: 'ApplicationRequestApplicationDetails' = None,
        **kwargs
    ) -> DetailedResponse:
        """
        Deploys a Spark application in the Analytics Engine instance.

        Deploy a Spark application on a given serverless Spark instance.

        :param str instance_id: The identifier of the instance where the Spark
               application is submitted.
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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark/applications'.format(**path_param_dict)
        request = self.prepare_request(method='POST',
                                       url=url,
                                       headers=headers,
                                       data=data)

        response = self.send(request, **kwargs)
        return response


    def get_applications(self,
        instance_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Gets all applications submitted in an instance with a specified inst_id.

        Retrieve all Spark applications run on a given instance.

        :param str instance_id: Identifier of the instance where the applications
               run.
        :param dict headers: A `dict` containing the request headers
        :return: A `DetailedResponse` containing the result, headers and HTTP status code.
        :rtype: DetailedResponse with `dict` result representing a `ApplicationCollection` object
        """

        if instance_id is None:
            raise ValueError('instance_id must be provided')
        headers = {}
        sdk_headers = get_sdk_headers(service_name=self.DEFAULT_SERVICE_NAME,
                                      service_version='V3',
                                      operation_id='get_applications')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id']
        path_param_values = self.encode_path_vars(instance_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark/applications'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def get_application_by_id(self,
        instance_id: str,
        application_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Gets the details of the application identified by the app_id identifier.

        Retrieve the details of a given Spark application.

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
                                      operation_id='get_application_by_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'application_id']
        path_param_values = self.encode_path_vars(instance_id, application_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark/applications/{application_id}'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


    def delete_application_by_id(self,
        instance_id: str,
        application_id: str,
        **kwargs
    ) -> DetailedResponse:
        """
        Stops the specified application.

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
                                      operation_id='delete_application_by_id')
        headers.update(sdk_headers)

        if 'headers' in kwargs:
            headers.update(kwargs.get('headers'))

        path_param_keys = ['instance_id', 'application_id']
        path_param_values = self.encode_path_vars(instance_id, application_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark/applications/{application_id}'.format(**path_param_dict)
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
        Gets the status of the application identified by the app_id identifier.

        Returns the status of the application identified by the app_id identifier.

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
        headers['Accept'] = 'application/json'

        path_param_keys = ['instance_id', 'application_id']
        path_param_values = self.encode_path_vars(instance_id, application_id)
        path_param_dict = dict(zip(path_param_keys, path_param_values))
        url = '/v3/analytics_engines/{instance_id}/spark/applications/{application_id}/state'.format(**path_param_dict)
        request = self.prepare_request(method='GET',
                                       url=url,
                                       headers=headers)

        response = self.send(request, **kwargs)
        return response


##############################################################################
# Models
##############################################################################


class ApplicationCollection():
    """
    An array of application details.

    :attr List[ApplicationDetails] applications: (optional) List of applications.
    """

    def __init__(self,
                 *,
                 applications: List['ApplicationDetails'] = None) -> None:
        """
        Initialize a ApplicationCollection object.

        :param List[ApplicationDetails] applications: (optional) List of
               applications.
        """
        self.applications = applications

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationCollection':
        """Initialize a ApplicationCollection object from a json dictionary."""
        args = {}
        if 'applications' in _dict:
            args['applications'] = [ApplicationDetails.from_dict(x) for x in _dict.get('applications')]
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
    Details of an application.

    :attr str application_id: (optional) Identifier of the application.
    :attr str spark_application_id: (optional) Identifier of the Spark application.
    :attr str state: (optional) Status of the application.
    :attr str start_time: (optional) Time when the application was started.
    :attr str finish_time: (optional) Time when the application was completed.
    """

    def __init__(self,
                 *,
                 application_id: str = None,
                 spark_application_id: str = None,
                 state: str = None,
                 start_time: str = None,
                 finish_time: str = None) -> None:
        """
        Initialize a ApplicationDetails object.

        :param str application_id: (optional) Identifier of the application.
        :param str spark_application_id: (optional) Identifier of the Spark
               application.
        :param str state: (optional) Status of the application.
        :param str start_time: (optional) Time when the application was started.
        :param str finish_time: (optional) Time when the application was completed.
        """
        self.application_id = application_id
        self.spark_application_id = spark_application_id
        self.state = state
        self.start_time = start_time
        self.finish_time = finish_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationDetails':
        """Initialize a ApplicationDetails object from a json dictionary."""
        args = {}
        if 'application_id' in _dict:
            args['application_id'] = _dict.get('application_id')
        if 'spark_application_id' in _dict:
            args['spark_application_id'] = _dict.get('spark_application_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        if 'finish_time' in _dict:
            args['finish_time'] = _dict.get('finish_time')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application_id') and self.application_id is not None:
            _dict['application_id'] = self.application_id
        if hasattr(self, 'spark_application_id') and self.spark_application_id is not None:
            _dict['spark_application_id'] = self.spark_application_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'finish_time') and self.finish_time is not None:
            _dict['finish_time'] = self.finish_time
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

    :attr ApplicationRequest application_details: (optional) Application request
          details.
    :attr str mode: (optional) Application mode.
    :attr str application_id: (optional) Application ID.
    :attr str state: (optional) Application state.
    :attr str start_time: (optional) Application start time.
    :attr str finish_time: (optional) Application end time.
    """

    def __init__(self,
                 *,
                 application_details: 'ApplicationRequest' = None,
                 mode: str = None,
                 application_id: str = None,
                 state: str = None,
                 start_time: str = None,
                 finish_time: str = None) -> None:
        """
        Initialize a ApplicationGetResponse object.

        :param ApplicationRequest application_details: (optional) Application
               request details.
        :param str mode: (optional) Application mode.
        :param str application_id: (optional) Application ID.
        :param str state: (optional) Application state.
        :param str start_time: (optional) Application start time.
        :param str finish_time: (optional) Application end time.
        """
        self.application_details = application_details
        self.mode = mode
        self.application_id = application_id
        self.state = state
        self.start_time = start_time
        self.finish_time = finish_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationGetResponse':
        """Initialize a ApplicationGetResponse object from a json dictionary."""
        args = {}
        if 'application_details' in _dict:
            args['application_details'] = ApplicationRequest.from_dict(_dict.get('application_details'))
        if 'mode' in _dict:
            args['mode'] = _dict.get('mode')
        if 'application_id' in _dict:
            args['application_id'] = _dict.get('application_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
        if 'finish_time' in _dict:
            args['finish_time'] = _dict.get('finish_time')
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
        if hasattr(self, 'mode') and self.mode is not None:
            _dict['mode'] = self.mode
        if hasattr(self, 'application_id') and self.application_id is not None:
            _dict['application_id'] = self.application_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
        if hasattr(self, 'finish_time') and self.finish_time is not None:
            _dict['finish_time'] = self.finish_time
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

class ApplicationGetStateResponse():
    """
    State of a given application.

    :attr str application_id: (optional) Identifier of the application.
    :attr str state: (optional) Status of the application.
    :attr str start_time: (optional) Time when the application was started.
    :attr str finish_time: (optional) Time when the application was completed.
    """

    def __init__(self,
                 *,
                 application_id: str = None,
                 state: str = None,
                 start_time: str = None,
                 finish_time: str = None) -> None:
        """
        Initialize a ApplicationGetStateResponse object.

        :param str application_id: (optional) Identifier of the application.
        :param str state: (optional) Status of the application.
        :param str start_time: (optional) Time when the application was started.
        :param str finish_time: (optional) Time when the application was completed.
        """
        self.application_id = application_id
        self.state = state
        self.start_time = start_time
        self.finish_time = finish_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationGetStateResponse':
        """Initialize a ApplicationGetStateResponse object from a json dictionary."""
        args = {}
        if 'application_id' in _dict:
            args['application_id'] = _dict.get('application_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'start_time' in _dict:
            args['start_time'] = _dict.get('start_time')
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
        if hasattr(self, 'application_id') and self.application_id is not None:
            _dict['application_id'] = self.application_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = self.start_time
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

class ApplicationRequest():
    """
    Application request details.

    :attr ApplicationRequestApplicationDetails application_details: (optional)
          Application details.
    """

    def __init__(self,
                 *,
                 application_details: 'ApplicationRequestApplicationDetails' = None) -> None:
        """
        Initialize a ApplicationRequest object.

        :param ApplicationRequestApplicationDetails application_details: (optional)
               Application details.
        """
        self.application_details = application_details

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationRequest':
        """Initialize a ApplicationRequest object from a json dictionary."""
        args = {}
        if 'application_details' in _dict:
            args['application_details'] = ApplicationRequestApplicationDetails.from_dict(_dict.get('application_details'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationRequest object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application_details') and self.application_details is not None:
            _dict['application_details'] = self.application_details.to_dict()
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this ApplicationRequest object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'ApplicationRequest') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'ApplicationRequest') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class ApplicationRequestApplicationDetails():
    """
    Application details.

    :attr str application: (optional) Application name.
    :attr str class_: (optional) The entry point for your application.
    :attr List[str] application_arguments: (optional) Application arguments.
    :attr dict conf: (optional) Application configurations to override. See [Spark
          environment variables](
          https://spark.apache.org/docs/latest/configuration.html#available-properties)
          for a list of the supported variables.
    :attr dict env: (optional) Application environment configurations to override.
          See [Spark environment
          variables](https://spark.apache.org/docs/latest/configuration.html#environment-variables)
          for a list of the supported variables.
    """

    def __init__(self,
                 *,
                 application: str = None,
                 class_: str = None,
                 application_arguments: List[str] = None,
                 conf: dict = None,
                 env: dict = None) -> None:
        """
        Initialize a ApplicationRequestApplicationDetails object.

        :param str application: (optional) Application name.
        :param str class_: (optional) The entry point for your application.
        :param List[str] application_arguments: (optional) Application arguments.
        :param dict conf: (optional) Application configurations to override. See
               [Spark environment variables](
               https://spark.apache.org/docs/latest/configuration.html#available-properties)
               for a list of the supported variables.
        :param dict env: (optional) Application environment configurations to
               override. See [Spark environment
               variables](https://spark.apache.org/docs/latest/configuration.html#environment-variables)
               for a list of the supported variables.
        """
        self.application = application
        self.class_ = class_
        self.application_arguments = application_arguments
        self.conf = conf
        self.env = env

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationRequestApplicationDetails':
        """Initialize a ApplicationRequestApplicationDetails object from a json dictionary."""
        args = {}
        if 'application' in _dict:
            args['application'] = _dict.get('application')
        if 'class' in _dict:
            args['class_'] = _dict.get('class')
        if 'application_arguments' in _dict:
            args['application_arguments'] = _dict.get('application_arguments')
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
        if hasattr(self, 'class_') and self.class_ is not None:
            _dict['class'] = self.class_
        if hasattr(self, 'application_arguments') and self.application_arguments is not None:
            _dict['application_arguments'] = self.application_arguments
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

    :attr str application_id: (optional) Application ID.
    :attr str state: (optional) Application state.
    :attr datetime start_time: (optional) Application start time.
    """

    def __init__(self,
                 *,
                 application_id: str = None,
                 state: str = None,
                 start_time: datetime = None) -> None:
        """
        Initialize a ApplicationResponse object.

        :param str application_id: (optional) Application ID.
        :param str state: (optional) Application state.
        :param datetime start_time: (optional) Application start time.
        """
        self.application_id = application_id
        self.state = state
        self.start_time = start_time

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'ApplicationResponse':
        """Initialize a ApplicationResponse object from a json dictionary."""
        args = {}
        if 'application_id' in _dict:
            args['application_id'] = _dict.get('application_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'start_time' in _dict:
            args['start_time'] = string_to_datetime(_dict.get('start_time'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a ApplicationResponse object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'application_id') and self.application_id is not None:
            _dict['application_id'] = self.application_id
        if hasattr(self, 'state') and self.state is not None:
            _dict['state'] = self.state
        if hasattr(self, 'start_time') and self.start_time is not None:
            _dict['start_time'] = datetime_to_string(self.start_time)
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
        Application state.
        """
        ACCEPTED = 'accepted'
        FINISHED = 'finished'
        KILLED = 'killed'
        FAILED = 'failed'
        ERROR = 'error'
        RUNNING = 'running'
        SUBMITTED = 'submitted'
        STOPPED = 'stopped'
        WAITING = 'waiting'


class InstanceDetails():
    """
    Instance details.

    :attr str instance_id: (optional) Instance id.
    :attr str state: (optional) Instance state.
    :attr datetime state_change_time: (optional) Timestamp when the state of the
          instance was changed.
    :attr InstanceDetailsDefaultRuntime default_runtime: (optional) Specifies the
          default runtime to use for all workloads that run in this instance.
    :attr InstanceDetailsInstanceHome instance_home: (optional) Instance home
          storage associated with the instance.
    :attr InstanceDetailsDefaultConfig default_config: (optional) Instance level
          default configuration for Spark workloads.
    """

    def __init__(self,
                 *,
                 instance_id: str = None,
                 state: str = None,
                 state_change_time: datetime = None,
                 default_runtime: 'InstanceDetailsDefaultRuntime' = None,
                 instance_home: 'InstanceDetailsInstanceHome' = None,
                 default_config: 'InstanceDetailsDefaultConfig' = None) -> None:
        """
        Initialize a InstanceDetails object.

        :param str instance_id: (optional) Instance id.
        :param str state: (optional) Instance state.
        :param datetime state_change_time: (optional) Timestamp when the state of
               the instance was changed.
        :param InstanceDetailsDefaultRuntime default_runtime: (optional) Specifies
               the default runtime to use for all workloads that run in this instance.
        :param InstanceDetailsInstanceHome instance_home: (optional) Instance home
               storage associated with the instance.
        :param InstanceDetailsDefaultConfig default_config: (optional) Instance
               level default configuration for Spark workloads.
        """
        self.instance_id = instance_id
        self.state = state
        self.state_change_time = state_change_time
        self.default_runtime = default_runtime
        self.instance_home = instance_home
        self.default_config = default_config

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceDetails':
        """Initialize a InstanceDetails object from a json dictionary."""
        args = {}
        if 'instance_id' in _dict:
            args['instance_id'] = _dict.get('instance_id')
        if 'state' in _dict:
            args['state'] = _dict.get('state')
        if 'state_change_time' in _dict:
            args['state_change_time'] = string_to_datetime(_dict.get('state_change_time'))
        if 'default_runtime' in _dict:
            args['default_runtime'] = InstanceDetailsDefaultRuntime.from_dict(_dict.get('default_runtime'))
        if 'instance_home' in _dict:
            args['instance_home'] = InstanceDetailsInstanceHome.from_dict(_dict.get('instance_home'))
        if 'default_config' in _dict:
            args['default_config'] = InstanceDetailsDefaultConfig.from_dict(_dict.get('default_config'))
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstanceDetails object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'instance_id') and self.instance_id is not None:
            _dict['instance_id'] = self.instance_id
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
        """Return a `str` version of this InstanceDetails object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceDetails') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceDetails') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

    class StateEnum(str, Enum):
        """
        Instance state.
        """
        CREATED = 'created'
        DELETED = 'deleted'
        FAILED = 'failed'


class InstanceDetailsDefaultConfig():
    """
    Instance level default configuration for Spark workloads.

    :attr str key: (optional) Value of the Spark configuration key.
    """

    def __init__(self,
                 *,
                 key: str = None) -> None:
        """
        Initialize a InstanceDetailsDefaultConfig object.

        :param str key: (optional) Value of the Spark configuration key.
        """
        self.key = key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceDetailsDefaultConfig':
        """Initialize a InstanceDetailsDefaultConfig object from a json dictionary."""
        args = {}
        if 'key' in _dict:
            args['key'] = _dict.get('key')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstanceDetailsDefaultConfig object from a json dictionary."""
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
        """Return a `str` version of this InstanceDetailsDefaultConfig object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceDetailsDefaultConfig') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceDetailsDefaultConfig') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstanceDetailsDefaultRuntime():
    """
    Specifies the default runtime to use for all workloads that run in this instance.

    :attr str spark_version: (optional) Version of Spark runtime to use. Currently,
          only 3.0 is supported.
    :attr List[str] additional_packages: (optional) Add-on packages.
    """

    def __init__(self,
                 *,
                 spark_version: str = None,
                 additional_packages: List[str] = None) -> None:
        """
        Initialize a InstanceDetailsDefaultRuntime object.

        :param str spark_version: (optional) Version of Spark runtime to use.
               Currently, only 3.0 is supported.
        :param List[str] additional_packages: (optional) Add-on packages.
        """
        self.spark_version = spark_version
        self.additional_packages = additional_packages

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceDetailsDefaultRuntime':
        """Initialize a InstanceDetailsDefaultRuntime object from a json dictionary."""
        args = {}
        if 'spark_version' in _dict:
            args['spark_version'] = _dict.get('spark_version')
        if 'additional_packages' in _dict:
            args['additional_packages'] = _dict.get('additional_packages')
        return cls(**args)

    @classmethod
    def _from_dict(cls, _dict):
        """Initialize a InstanceDetailsDefaultRuntime object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'spark_version') and self.spark_version is not None:
            _dict['spark_version'] = self.spark_version
        if hasattr(self, 'additional_packages') and self.additional_packages is not None:
            _dict['additional_packages'] = self.additional_packages
        return _dict

    def _to_dict(self):
        """Return a json dictionary representing this model."""
        return self.to_dict()

    def __str__(self) -> str:
        """Return a `str` version of this InstanceDetailsDefaultRuntime object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceDetailsDefaultRuntime') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceDetailsDefaultRuntime') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other

class InstanceDetailsInstanceHome():
    """
    Instance home storage associated with the instance.

    :attr str guid: (optional) UUID of the instance home storage instance.
    :attr str provider: (optional) Currently only ibm-cos (IBM Cloud Object Storage)
          is supported.
    :attr str type: (optional) Type of the instance home storage. Currently, only
          objectstore (Cloud Object Storage)is supported.
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
                 guid: str = None,
                 provider: str = None,
                 type: str = None,
                 region: str = None,
                 endpoint: str = None,
                 bucket: str = None,
                 hmac_access_key: str = None,
                 hmac_secret_key: str = None) -> None:
        """
        Initialize a InstanceDetailsInstanceHome object.

        :param str guid: (optional) UUID of the instance home storage instance.
        :param str provider: (optional) Currently only ibm-cos (IBM Cloud Object
               Storage) is supported.
        :param str type: (optional) Type of the instance home storage. Currently,
               only objectstore (Cloud Object Storage)is supported.
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
        self.guid = guid
        self.provider = provider
        self.type = type
        self.region = region
        self.endpoint = endpoint
        self.bucket = bucket
        self.hmac_access_key = hmac_access_key
        self.hmac_secret_key = hmac_secret_key

    @classmethod
    def from_dict(cls, _dict: Dict) -> 'InstanceDetailsInstanceHome':
        """Initialize a InstanceDetailsInstanceHome object from a json dictionary."""
        args = {}
        if 'guid' in _dict:
            args['guid'] = _dict.get('guid')
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
        """Initialize a InstanceDetailsInstanceHome object from a json dictionary."""
        return cls.from_dict(_dict)

    def to_dict(self) -> Dict:
        """Return a json dictionary representing this model."""
        _dict = {}
        if hasattr(self, 'guid') and self.guid is not None:
            _dict['guid'] = self.guid
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
        """Return a `str` version of this InstanceDetailsInstanceHome object."""
        return json.dumps(self.to_dict(), indent=2)

    def __eq__(self, other: 'InstanceDetailsInstanceHome') -> bool:
        """Return `true` when self and other are equal, false otherwise."""
        if not isinstance(other, self.__class__):
            return False
        return self.__dict__ == other.__dict__

    def __ne__(self, other: 'InstanceDetailsInstanceHome') -> bool:
        """Return `true` when self and other are not equal, false otherwise."""
        return not self == other
