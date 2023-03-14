# How to run tests

## Pre-requisites
1. Install local iaesdk package and all dev requirements.
    ```
    pip install -r requirements.txt
    pip install -r requirements-dev.txt
    pip install .
    ```

## Integration Tests

1. Create a `ibm_analytics_engine_api_v3.env` file in the `ibm-iae-python-sdk` directory using `ibmanalyticsengine-service.env.hide` as an example.
1. Update `ibm_analytics_engine_api_v3.env` file with your own **APIKEY**.
1. In addition to the above, add the following properties to the file - 
    1. `IBM_ANALYTICS_ENGINE_API_INSTANCE_GUID`=`<Id of your Analytics Engine Serverless plan instance>`
    1. `IBM_ANALYTICS_ENGINE_API_INSTANCE_GUID_WO_INSTANCE_HOME`=`<Id of your Analytics Engine Service plan instance created without instance home>`
    1. `IBM_ANALYTICS_ENGINE_API_HMAC_ACCESS_KEY`=`<HMAC access key of the cos instance to be used as instance home>`
    1. `IBM_ANALYTICS_ENGINE_API_HMAC_SECRET_KEY`=`<HMAC secret key of the cos instance to be used as instance home>`
    1. `IBM_ANALYTICS_ENGINE_API_ALTERNATE_HMAC_ACCESS_KEY`=`<HMAC access key of the cos instance to be used as instance home>`
    1. `IBM_ANALYTICS_ENGINE_API_ALTERNATE_HMAC_SECRET_KEY`=`<HMAC secret key of the cos instance to be used as instance home>`
1. From root directory, run
    ```
    pytest test/integration
    ```

## Unit Tests

1. From root directory, run
    ```
    pytest test/unit
    ```