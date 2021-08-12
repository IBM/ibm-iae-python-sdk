# How to run tests

## Pre-requisites
1. Install local iaesdk package, pytest and pytest-dotenv
    ```
    pip install . -r requirements-dev.txt
    ```

## Integration Tests

1. Create a `ibmanalyticsengine-service.env` file in the `ibm-iae-python-sdk` directory using `ibmanalyticsengine-service.env.hide` as an example.
1. Update `ibmanalyticsengine-service.env` file with your own **APIKEY**.
1. export your instance guid as `IBM_ANALYTICS_ENGINE_INSTANCE_GUID` environment variable.
1. Go to `/test/integration/` directory.
1. Run `pytest`.

## Unit Tests

1. Go to `/test/unit/` directory.
1. Run `pytest`.