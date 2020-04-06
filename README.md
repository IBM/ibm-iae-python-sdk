# IBM Cloud Analytics Engine Python SDK

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

Service Name | Imported Class Name
--- | --- 
[IBM Analytics Engine](https://cloud.ibm.com/apidocs/ibm-analytics-engine) | IbmAnalyticsEngineApiV2

## Prerequisites

[ibm-cloud-onboarding]: https://cloud.ibm.com/registration?target=%2Fdeveloper%2Fwatson&

* An [IBM Cloud][ibm-cloud-onboarding] account.
* An IAM API key to allow the SDK to access your account. Create one [here](https://cloud.ibm.com/iam/apikeys).
* Python 3.5 or above.

## Installation

To install, use `pip` or `easy_install`:

```bash
pip install --upgrade "iaesdk>=0.0.1"
```

or

```bash
easy_install --upgrade "iaesdk>=0.0.1"
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
