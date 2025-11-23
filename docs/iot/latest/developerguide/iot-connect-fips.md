# Connect to AWS IoT FIPS endpoints

AWS IoT provides endpoints that support the [Federal Information Processing Standard (FIPS) 140-2](https://aws.amazon.com//compliance/fips/ "https://aws.amazon.com//compliance/fips/"). FIPS
compliant endpoints are different from standard AWS endpoints. To interact with AWS IoT
in a FIPS-compliant manner, you must use the endpoints described below with your FIPS
compliant client. The AWS IoT console is not FIPS compliant.

The following sections describe how to access the FIPS compliant AWS IoT endpoints by
using the REST API, an SDK, or the AWS CLI.

###### Topics

- [AWS IoT Core - control plane endpoints](#iot-connect-fips-control "#iot-connect-fips-control")
- [AWS IoT Core - data plane endpoints](#iot-connect-fips-data "#iot-connect-fips-data")
- [AWS IoT Core - credential provider endpoints](#iot-connect-fips-credential "#iot-connect-fips-credential")
- [AWS IoT Device Management - jobs data endpoints](#iot-connect-fips-jobs "#iot-connect-fips-jobs")
- [AWS IoT Device Management - Fleet Hub endpoints](#iot-connect-fips-fleethub "#iot-connect-fips-fleethub")
- [AWS IoT Device Management - secure tunneling endpoints](#iot-connect-fips-tunnel "#iot-connect-fips-tunnel")
- [AWS IoT Device Management - Managed Integrations endpoints](#mi-fips-endpoints "#mi-fips-endpoints")

## AWS IoT Core - control plane endpoints

The FIPS compliant **AWS IoT Core - control plane** endpoints
that support the [AWS IoT](../apireference/API_Operations_AWS_IoT.md "../apireference/API_Operations_AWS_IoT.md")
operations and their related [CLI commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html") are listed in [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"). In [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"), find the **AWS IoT Core - control plane** service, and look up the endpoint for your
AWS Region.

To use the FIPS compliant endpoint when you access the [AWS IoT](../apireference/API_Operations_AWS_IoT.md "../apireference/API_Operations_AWS_IoT.md")
operations, use the AWS SDK or the REST API with the endpoint that is appropriate
for your AWS Region.

To use the FIPS compliant endpoint when you run [**aws iot** CLI commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot/index.html"), add the
**--endpoint** parameter with the appropriate endpoint for your
AWS Region to the command.

## AWS IoT Core - data plane endpoints

The FIPS compliant **AWS IoT Core - data plane** endpoints
are listed in [FIPS Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"). In [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"), find the **AWS IoT Core - data plane** service, and look up the endpoint for your
AWS Region.

You can use the FIPS compliant endpoint for your AWS Region with a FIPS
compliant client by using the AWS IoT Device SDK and providing the endpoint to the
SDK's connection function in place of your account's default **AWS IoT Core - data plane** endpoint. The connection function is specific to
the AWS IoT Device SDK. For an example of a connection function, see the [Connection function in the AWS IoT Device SDK for Python](https://aws.github.io/aws-iot-device-sdk-python-v2/awsiot/mqtt_connection_builder.html "https://aws.github.io/aws-iot-device-sdk-python-v2/awsiot/mqtt_connection_builder.html").

###### Note

AWS IoT doesn't support AWS account-specific **AWS IoT Core - data plane** endpoints that are FIPS-compliant. Service
features that require an AWS account-specific endpoint in the [Server Name Indication (SNI)](transport-security.md "transport-security.md") can't be
used. FIPS-compliant **AWS IoT Core - data plane**
endpoints can't support [Multi-Account
Registration Certificates](x509-client-certs.md#multiple-account-cert "x509-client-certs.md#multiple-account-cert"), [Custom Domains](iot-custom-endpoints-configurable-custom.md "iot-custom-endpoints-configurable-custom.md"),
[Custom Authorizers](custom-authentication.md "custom-authentication.md"), and [Configurable Endpoints](iot-custom-endpoints-configurable.md "iot-custom-endpoints-configurable.md")
(including supported [TLS
policies](transport-security.md#tls-policy-table "transport-security.md#tls-policy-table")).

## AWS IoT Core - credential provider endpoints

The FIPS compliant **AWS IoT Core - credential provider** endpoints
are listed in [FIPS Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"). In [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"), find the **AWS IoT Core - credential provider** service, and look up the endpoint for your
AWS Region.

###### Note

AWS IoT doesn't support AWS account-specific **AWS IoT Core - credential provider** endpoints that are FIPS-compliant. Service
features that require an AWS account-specific endpoint in the [Server Name Indication (SNI)](transport-security.md "transport-security.md") can't be
used. FIPS-compliant **AWS IoT Core - credential provider**
endpoints can't support [Multi-Account
Registration Certificates](x509-client-certs.md#multiple-account-cert "x509-client-certs.md#multiple-account-cert"), [Custom Domains](iot-custom-endpoints-configurable-custom.md "iot-custom-endpoints-configurable-custom.md"),
[Custom Authorizers](custom-authentication.md "custom-authentication.md"), and [Configurable Endpoints](iot-custom-endpoints-configurable.md "iot-custom-endpoints-configurable.md")
(including supported [TLS
policies](transport-security.md#tls-policy-table "transport-security.md#tls-policy-table")).

## AWS IoT Device Management - jobs data endpoints

The FIPS compliant **AWS IoT Device Management - jobs data** endpoints are
listed in [FIPS Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"). In [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"), find the **AWS IoT Device Management - jobs data** service, and look up the endpoint for your
AWS Region.

To use the FIPS compliant **AWS IoT Device Management - jobs data**
endpoint when you run [**aws iot-jobs-data** CLI commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iot-jobs-data/index.html"), add the
**--endpoint** parameter with the appropriate endpoint for your
AWS Region to the command. You can also use the REST API with this
endpoint.

We recommend using `Data-ATS` instead of `iot:Jobs`.
`iot:Data-ATS` supports dual-stack endpoints (IPv4 and IPv6) while
`iot:Jobs` supports only IPv4.

You can use the FIPS compliant endpoint for your AWS Region with a FIPS
compliant client by using the AWS IoT Device SDK and providing the endpoint to the
SDK's connection function in place of your account's default **AWS IoT Device Management - jobs data** endpoint. The connection function is specific to the
AWS IoT Device SDK. For an example of a connection function, see the [Connection function in the AWS IoT Device SDK for Python](https://aws.github.io/aws-iot-device-sdk-python-v2/awsiot/mqtt_connection_builder.html "https://aws.github.io/aws-iot-device-sdk-python-v2/awsiot/mqtt_connection_builder.html").

## AWS IoT Device Management - Fleet Hub endpoints

The FIPS compliant **AWS IoT Device Management - Fleet Hub** endpoints to use
with [Fleet Hub for AWS IoT Device Management](../fleethubuserguide/what-is-aws-iot-monitor.md "../fleethubuserguide/what-is-aws-iot-monitor.md")
[CLI
commands](../../../cli/latest/reference/iotfleethub/index.md "../../../cli/latest/reference/iotfleethub/index.md") are listed in [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"). In [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"), find the **AWS IoT Device Management - Fleet Hub** service, and look up the endpoint for your
AWS Region.

To use the FIPS compliant **AWS IoT Device Management - Fleet Hub** endpoint
when you run [**aws iotfleethub** CLI commands](../../../cli/latest/reference/iotfleethub/index.md "../../../cli/latest/reference/iotfleethub/index.md"),
add the **--endpoint** parameter with the appropriate endpoint for
your AWS Region to the command. You can also use the REST API with this
endpoint.

## AWS IoT Device Management - secure tunneling endpoints

The FIPS compliant **AWS IoT Device Management - secure tunneling** endpoints
for the [AWS IoT secure tunneling API](../apireference/API_Operations_AWS_IoT_Secure_Tunneling.md "../apireference/API_Operations_AWS_IoT_Secure_Tunneling.md") and the corresponding [CLI commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/index.html") are listed in [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"). In [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"), find the **AWS IoT Device Management - secure tunneling** service, and look up the endpoint for your
AWS Region.

To use the FIPS compliant **AWS IoT Device Management - secure tunneling**
endpoint when you run [**aws iotsecuretunneling** CLI commands](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/index.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iotsecuretunneling/index.html"), add the
**--endpoint** parameter with the appropriate endpoint for your
AWS Region to the command. You can also use the REST API with this
endpoint.

## AWS IoT Device Management - Managed Integrations endpoints

The FIPS compliant **control plane** endpoints
that support the managed integrations
operations and their related AWS CLI commands are listed in [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"). In [FIPS
Endpoints by Service](https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service "https://aws.amazon.com//compliance/fips/#FIPS_Endpoints_by_Service"), find the **AWS IoT Device Management - Managed integrations** service, and look up the endpoint for your
AWS Region.

To use the FIPS compliant endpoint when you access the managed integrations
operations, use the AWS SDK or the REST API with the endpoint that is appropriate
for your AWS Region.

To use the FIPS compliant endpoint when you run managed integrations CLI commands, add the
**--endpoint** parameter with the appropriate endpoint for your
AWS Region to the command.
