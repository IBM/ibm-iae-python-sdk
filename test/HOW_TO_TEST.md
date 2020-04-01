# How to run tests

## Pre-requisites
1. Install pytest and pytest-dotenv
    ```
    pip install pytest
    pip install pytest-dotenv
    ```

## Integration Tests

1. Create a `.env` file in the `ibm-iae-python-sdk` directory using `env_example` as an example.
1. Update `.env` file with your own **APIKEY** and **INSTANCE GUID**.
1. Go to `/test/integartion/` directory.
1. Run `pytest`.

## Unit Tests

1. Go to `/test/unit/` directory.
1. Run `pytest`.