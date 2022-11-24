[![Build Status](https://api.travis-ci.com/IBM/ibm-iae-python-sdk.svg?branch=master)](https://app.travis-ci.com/IBM/ibm-iae-python-sdk)
[![semantic-release](https://img.shields.io/badge/%20%20%F0%9F%93%A6%F0%9F%9A%80-semantic--release-e10079.svg)](https://github.com/semantic-release/semantic-release)
# IBM Cloud Analytics Engine Python SDK Version 2.1.0

Python client library to interact with various [iaesdk Service APIs](https://cloud.ibm.com/apidocs/ibm-analytics-engine).

## Table of Contents

- [Overview](#overview)
- [Prerequisites](#prerequisites)
- [Installation](#installation)
- [Using the SDK](#using-the-sdk)
- [Questions](#questions)
- [Issues](#issues)
- [Open source @ IBM](#open-source--ibm)
- [Contributing](#contributing)
- [License](#license)

## Overview

The IBM Cloud iaesdk Python SDK allows developers to programmatically interact with the following 
IBM Cloud services:

Service Name | Module Name | Service Class Name
--- | --- | --- 
[IBM Analytics Engine v2](https://cloud.ibm.com/apidocs/ibm-analytics-engine/ibm-analytics-engine-v2) | ibm_analytics_engine_api_v2 | IbmAnalyticsEngineApiV2
[IBM Analytics Engine v3](https://cloud.ibm.com/apidocs/ibm-analytics-engine/ibm-analytics-engine-v3) | ibm_analytics_engine_api_v3 | IbmAnalyticsEngineApiV3

**NOTE**

IBM Analytics Engine v2 is for the classic plans : Lite, Standard Hourly and Standard monthly.
The classic plans are now deprecated.

IBM Analytics Engine v3 is for the Standard Serverless for Apache Spark plan


## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration?target=%2Fdeveloper%2Fwatson&

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.7 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "iaesdk>=2.1.0"
```

or

```bash
easy_install --upgrade "iaesdk>=2.1.0"
```

## Using the SDK
For general SDK usage information, please see [this link](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md)

In [setting client options programatically](https://github.com/IBM/ibm-cloud-sdk-common/blob/master/README.md#setting-client-options-programmatically) to instantiate the class, provide the following two values:
1. [IAM API Key](https://cloud.ibm.com/docs/iam?topic=iam-userapikey#create_user_key)
1. [Service URLs](https://cloud.ibm.com/apidocs/ibm-analytics-engine#service-endpoints)

## Questions

If you are having difficulties using this SDK or have a question about the IBM Cloud services,
please ask a question at [dW Answers](https://developer.ibm.com/answers/questions/ask/?topics=ibm-cloud) or
[Stack Overflow](http://stackoverflow.com/questions/ask?tags=ibm-cloud).

## Issues
If you encounter an issue with the project, you are welcome to submit a
[bug report](<github-repo-url>/issues).
Before that, please search for similar issues. It's possible that someone has already reported the problem.

## Open source @ IBM
Find more open source projects on the [IBM Github Page](http://ibm.github.io/)

## Contributing
See [CONTRIBUTING](CONTRIBUTING.md).

## License

This SDK is released under the Apache 2.0 license.
The license's full text can be found in [LICENSE](LICENSE).
