# -*- coding: utf-8 -*-
# (C) Copyright IBM Corp. 2023.
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

from ibm_cloud_sdk_core import *
import os
import pytest
from iaesdk.ibm_analytics_engine_api_v3 import *

# Config file name
config_file = "ibm_analytics_engine_api_v3.env"
application_id = ""


class TestIbmAnalyticsEngineApiV3:
    """
    Integration Test Class for IbmAnalyticsEngineApiV3
    """

    @classmethod
    def setup_class(cls):
        if os.path.exists(config_file):
            os.environ["IBM_CREDENTIALS_FILE"] = config_file

            cls.ibm_analytics_engine_api_service = (
                IbmAnalyticsEngineApiV3.new_instance()
            )
            assert cls.ibm_analytics_engine_api_service is not None

            cls.config = read_external_sources(
                IbmAnalyticsEngineApiV3.DEFAULT_SERVICE_NAME
            )
            assert cls.config is not None

            cls.instance_id = cls.config["INSTANCE_GUID"]
            cls.instance_id_without_instance_home = cls.config[
                "INSTANCE_GUID_WO_INSTANCE_HOME"
            ]
            cls.hmac_access_key = cls.config["HMAC_ACCESS_KEY"]
            cls.hmac_secret_key = cls.config["HMAC_SECRET_KEY"]
            cls.alternate_hmac_access_key = cls.config["ALTERNATE_HMAC_ACCESS_KEY"]
            cls.alternate_hmac_secret_key = cls.config["ALTERNATE_HMAC_SECRET_KEY"]

            cls.ibm_analytics_engine_api_service.enable_retries()

        print("Setup complete.")

    needscredentials = pytest.mark.skipif(
        not os.path.exists(config_file),
        reason="External configuration not available, skipping...",
    )

    @needscredentials
    def test_get_instance(self):
        response = self.ibm_analytics_engine_api_service.get_instance(
            instance_id=self.instance_id,
        )

        assert response.get_status_code() == 200
        instance = response.get_result()
        assert instance is not None

    @needscredentials
    def test_get_instance_state(self):
        response = self.ibm_analytics_engine_api_service.get_instance_state(
            instance_id=self.instance_id,
        )

        assert response.get_status_code() == 200
        instance_get_state_response = response.get_result()
        assert instance_get_state_response is not None

    @needscredentials
    def test_set_instance_home(self):
        response = self.ibm_analytics_engine_api_service.set_instance_home(
            instance_id=self.instance_id_without_instance_home,
            new_instance_id="testString",
            new_provider="ibm-cos",
            new_type="objectstore",
            new_region="us-south",
            new_endpoint="s3.direct.us-south.cloud-object-storage.appdomain.cloud",
            new_hmac_access_key=self.hmac_access_key,
            new_hmac_secret_key=self.hmac_secret_key,
        )

        assert response.get_status_code() == 200
        instance_home_response = response.get_result()
        assert instance_home_response is not None

    @needscredentials
    def test_update_instance_home_credentials(self):
        response = (
            self.ibm_analytics_engine_api_service.update_instance_home_credentials(
                instance_id=self.instance_id,
                hmac_access_key=self.alternate_hmac_access_key,
                hmac_secret_key=self.alternate_hmac_secret_key,
            )
        )

        assert response.get_status_code() == 200
        instance_home_response = response.get_result()
        assert instance_home_response is not None

    @needscredentials
    def test_get_instance_default_configs(self):
        response = self.ibm_analytics_engine_api_service.get_instance_default_configs(
            instance_id=self.instance_id,
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_replace_instance_default_configs(self):
        response = (
            self.ibm_analytics_engine_api_service.replace_instance_default_configs(
                instance_id=self.instance_id,
                body={
                    "spark.driver.memory": "8G",
                    "spark.driver.cores": "2",
                },
            )
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_update_instance_default_configs(self):
        response = (
            self.ibm_analytics_engine_api_service.update_instance_default_configs(
                instance_id=self.instance_id,
                body={
                    "ae.spark.history-server.cores": "1",
                    "ae.spark.history-server.memory": "4G",
                },
            )
        )

        assert response.get_status_code() == 200
        result = response.get_result()
        assert result is not None

    @needscredentials
    def test_get_instance_default_runtime(self):
        response = self.ibm_analytics_engine_api_service.get_instance_default_runtime(
            instance_id=self.instance_id,
        )

        assert response.get_status_code() == 200
        runtime = response.get_result()
        assert runtime is not None

    @needscredentials
    def test_replace_instance_default_runtime(self):
        response = (
            self.ibm_analytics_engine_api_service.replace_instance_default_runtime(
                instance_id=self.instance_id,
                spark_version="3.3",
            )
        )

        assert response.get_status_code() == 200
        runtime = response.get_result()
        assert runtime is not None

    @needscredentials
    def test_create_application(self):
        # Construct a dict representation of a Runtime model
        runtime_model = {
            "spark_version": "3.3",
        }

        # Construct a dict representation of a ApplicationRequestApplicationDetails model
        application_request_application_details_model = {
            "application": "/opt/ibm/spark/examples/src/main/python/wordcount.py",
            "arguments": ["/opt/ibm/spark/examples/src/main/resources/people.txt"],
            "runtime": runtime_model,
        }

        response = self.ibm_analytics_engine_api_service.create_application(
            instance_id=self.instance_id,
            application_details=application_request_application_details_model,
        )

        assert response.get_status_code() == 202
        application_response = response.get_result()
        assert application_response is not None

        global application_id
        application_id = application_response.get("id")

    @needscredentials
    def test_list_applications(self):
        response = self.ibm_analytics_engine_api_service.list_applications(
            instance_id=self.instance_id,
            state=["accepted", "submitted", "waiting", "running", "finished", "failed"],
        )

        assert response.get_status_code() == 200
        application_collection = response.get_result()
        assert application_collection is not None

    @needscredentials
    def test_get_application(self):
        response = self.ibm_analytics_engine_api_service.get_application(
            instance_id=self.instance_id,
            application_id=application_id,
        )

        assert response.get_status_code() == 200
        application_get_response = response.get_result()
        assert application_get_response is not None

    @needscredentials
    def test_get_application_state(self):
        response = self.ibm_analytics_engine_api_service.get_application_state(
            instance_id=self.instance_id,
            application_id=application_id,
        )

        assert response.get_status_code() == 200
        application_get_state_response = response.get_result()
        assert application_get_state_response is not None

    @needscredentials
    def test_get_current_resource_consumption(self):
        response = (
            self.ibm_analytics_engine_api_service.get_current_resource_consumption(
                instance_id=self.instance_id,
            )
        )

        assert response.get_status_code() == 200
        current_resource_consumption_response = response.get_result()
        assert current_resource_consumption_response is not None

    @needscredentials
    def test_get_resource_consumption_limits(self):
        response = (
            self.ibm_analytics_engine_api_service.get_resource_consumption_limits(
                instance_id=self.instance_id,
            )
        )

        assert response.get_status_code() == 200
        resource_consumption_limits_response = response.get_result()
        assert resource_consumption_limits_response is not None

    @needscredentials
    def test_replace_log_forwarding_config(self):
        response = self.ibm_analytics_engine_api_service.replace_log_forwarding_config(
            instance_id=self.instance_id,
            enabled=True,
            sources=["spark-driver", "spark-executor"],
            tags=["<tag_1>", "<tag_2>", "<tag_n"],
        )

        assert response.get_status_code() == 200
        log_forwarding_config_response = response.get_result()
        assert log_forwarding_config_response is not None

    @needscredentials
    def test_get_log_forwarding_config(self):
        response = self.ibm_analytics_engine_api_service.get_log_forwarding_config(
            instance_id=self.instance_id,
        )

        assert response.get_status_code() == 200
        log_forwarding_config_response = response.get_result()
        assert log_forwarding_config_response is not None

    @needscredentials
    def test_configure_platform_logging(self):
        response = self.ibm_analytics_engine_api_service.configure_platform_logging(
            instance_guid=self.instance_id,
            enable=True,
        )

        assert response.get_status_code() == 201
        logging_configuration_response = response.get_result()
        assert logging_configuration_response is not None

    @needscredentials
    def test_get_logging_configuration(self):
        response = self.ibm_analytics_engine_api_service.get_logging_configuration(
            instance_guid=self.instance_id,
        )

        assert response.get_status_code() == 200
        logging_configuration_response = response.get_result()
        assert logging_configuration_response is not None

    @needscredentials
    def test_start_spark_history_server(self):
        response = self.ibm_analytics_engine_api_service.start_spark_history_server(
            instance_id=self.instance_id,
        )

        assert response.get_status_code() == 202
        spark_history_server_response = response.get_result()
        assert spark_history_server_response is not None

    @needscredentials
    def test_get_spark_history_server(self):
        response = self.ibm_analytics_engine_api_service.get_spark_history_server(
            instance_id=self.instance_id,
        )

        assert response.get_status_code() == 200
        spark_history_server_response = response.get_result()
        assert spark_history_server_response is not None

    @needscredentials
    def test_delete_application(self):
        response = self.ibm_analytics_engine_api_service.delete_application(
            instance_id=self.instance_id,
            application_id=application_id,
        )

        assert response.get_status_code() == 204

    @needscredentials
    def test_stop_spark_history_server(self):
        response = self.ibm_analytics_engine_api_service.stop_spark_history_server(
            instance_id=self.instance_id,
        )

        assert response.get_status_code() == 204
