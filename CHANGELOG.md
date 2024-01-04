# [3.3.0](https://github.com/IBM/ibm-iae-python-sdk/compare/v3.2.0...v3.3.0) (2024-01-04)


### Bug Fixes

* bump up min supported python version to 3.8 ([7ed431a](https://github.com/IBM/ibm-iae-python-sdk/commit/7ed431aa1471780c66774b6ac4e3ee021fedd5bc))
* fix lint issues ([378b7a6](https://github.com/IBM/ibm-iae-python-sdk/commit/378b7a6ad9b03e4ebbcacf7ce5c9d827b341c8cd))


### Features

* add support for time based application list filters ([b3ebb9d](https://github.com/IBM/ibm-iae-python-sdk/commit/b3ebb9d32a97e5d74ae17a7a912e61c4e01ceca2))

# [3.2.0](https://github.com/IBM/ibm-iae-python-sdk/compare/v3.1.0...v3.2.0) (2023-05-24)


### Features

* add support for application list pagination ([be68d67](https://github.com/IBM/ibm-iae-python-sdk/commit/be68d67574618d454d9e0bf53b54c42901c8966f))

# [3.1.0](https://github.com/IBM/ibm-iae-python-sdk/compare/v3.0.0...v3.1.0) (2023-03-23)


### Bug Fixes

* fix lint error ([fe78649](https://github.com/IBM/ibm-iae-python-sdk/commit/fe786496c4606a11e205051f29c5b8028c452351))


### Features

* add new sdk method to update instance home credentials ([f62af2a](https://github.com/IBM/ibm-iae-python-sdk/commit/f62af2ae5035b612a0c2f2f5528f8da6ea860ff0))

# [3.0.0](https://github.com/IBM/ibm-iae-python-sdk/compare/v2.2.0...v3.0.0) (2023-01-06)


### Bug Fixes

* documentation and version ([938c1e5](https://github.com/IBM/ibm-iae-python-sdk/commit/938c1e516eb02b80ff3cbe8843adaea4151ef99b))


### BREAKING CHANGES

* The type of timestamp fields in Application response models has been changed to `datetime`.

Fields in Application and ApplicationGetResponse objects like start_time, end_time, finish_time will now have values of type `datetime` instead of plain strings.

Signed-off-by: Subin Shekhar <subinpc@gmail.com>

# [2.2.0](https://github.com/IBM/ibm-iae-python-sdk/compare/v2.1.0...v2.2.0) (2023-01-05)


### Features

* add spark history server api ([ab7bcfd](https://github.com/IBM/ibm-iae-python-sdk/commit/ab7bcfdc665ba6d3c537c53f4b40301dbed9bdef))

# [2.1.0](https://github.com/IBM/ibm-iae-python-sdk/compare/v2.0.0...v2.1.0) (2022-11-24)


### Features

* add new sdk methods and update existing ([af7fe8d](https://github.com/IBM/ibm-iae-python-sdk/commit/af7fe8db5c5a0118b1c4f69ac50af94950eeb56f))

# [2.0.0](https://github.com/IBM/ibm-iae-python-sdk/compare/v1.1.1...v2.0.0) (2022-09-08)


### Features

* update sdk methods and dependencies ([dea7bcf](https://github.com/IBM/ibm-iae-python-sdk/commit/dea7bcf430c641f97426cdce41af073dbb3d6399))


### BREAKING CHANGES

* Minimum supported python version

The minimum supported python version is now 3.7.

Signed-off-by: Subin Shekhar <subinpc@gmail.com>

## [1.1.1](https://github.com/IBM/ibm-iae-python-sdk/compare/v1.1.0...v1.1.1) (2021-09-08)


### Bug Fixes

* **analytics engine:** fixed Spark application submit path and payload ([#6](https://github.com/IBM/ibm-iae-python-sdk/issues/6)) ([522d541](https://github.com/IBM/ibm-iae-python-sdk/commit/522d5416a744ec3fca7393da653750e29876c281))

# [1.1.0](https://github.com/IBM/ibm-iae-python-sdk/compare/v1.0.3...v1.1.0) (2021-08-17)


### Features

* analytics engine v3 feature changes ([d23cbc0](https://github.com/IBM/ibm-iae-python-sdk/commit/d23cbc081b07f5a72982656c027808c0312ab486))
* analytics engine v3 feature changes ([2bd89ef](https://github.com/IBM/ibm-iae-python-sdk/commit/2bd89ef9695298e25dd7952d1e603e11a9eb51a2))
* analytics engine v3 feature changes ([fc7835b](https://github.com/IBM/ibm-iae-python-sdk/commit/fc7835b6ea611aaf4d373026158405bdf0a6279a))

## [1.0.2](https://github.com/IBM/ibm-iae-python-sdk/compare/v1.0.1...v1.0.2) (2020-05-28)


### Bug Fixes

* **build:** updating build files ([bb2474d](https://github.com/IBM/ibm-iae-python-sdk/commit/bb2474daf0d43c670593aa3bbb26e70b9a4da97f))
