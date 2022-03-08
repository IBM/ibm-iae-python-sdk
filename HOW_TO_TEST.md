# How to run tests

## Pre-requisites
1. Download [SDK generation code](https://github.ibm.com/CloudEngineering/openapi-sdkgen/releases) 
2. Clone [`Python SDK`] https://github.com/IBM/ibm-iae-python-sdk/
3. Clone [`Cloud API Doc`] https://github.ibm.com/cloud-api-docs/analytics-engine
4. Generate the sdk code with: 
    `openapi-sdkgen/openapi-sdkgen.sh generate -g ibm-python -i ibmanalyticsengine-v3.json -o Users/git/ibm-iae-python-sdk --genITs --genExamples`
5. Install local iaesdk package, pytest and pytest-dotenv
    ```
    pip install . -r requirements-dev.txt
    ```

## Integration Tests

1. The SDK has been generated from the latest ibmanalyticsengine-v3.json which contains modifications and newly added api methods.
The Integration tests have to run on the generated SDK not on the sdk from git. 
2. To merge with remote version pick the code marked between and update `IbmAnalyticsEngineApiIT.java`
    `# !!! Start of custom content to be copied !!!`
    `# !!! End of custom content to be copied !!!`
3. Create a `ibm_analytics_engine_api_v3.env` file in the `ibm-iae-python-sdk` directory using `ibmanalyticsengine-service.env.hide` as an example.
4. Update `ibm_analytics_engine_api_v3.env` file with your own **APIKEY** and other details.
5. export instance guid as `IBM_ANALYTICS_ENGINE_INSTANCE_GUID` environment variable.
6. export instance guid to cretae instance home as `IBM_ANALYTICS_ENGINE_INSTANCE_GUID_INSTANCE_HOME` environment variable.
7. export HMAC access key as `IBM_ANALYTICS_ENGINE_HMAC_ACCESS_KEY` environment variable.
8. export HMAC secret key as `IBM_ANALYTICS_ENGINE_HMAC_SECRET_KEY` environment variable.
9. Go to `/test/integration/` directory.
10. Run `pytest test_ibm_analytics_engine_api_v3.py -s`.

## Unit Tests

1. Go to `/test/unit/` directory.
1. Run `pytest test_ibm_analytics_engine_api_v3.py -s`.