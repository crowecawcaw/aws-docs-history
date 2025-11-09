# AWS IoT Greengrass V2 endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

### Control plane

operations

The following table contains AWS Region-specific endpoints that AWS IoT Greengrass V2 supports
for operations to manage components, devices, and deployments.

| Region Name              | Region         | Endpoint                                                                                                                                                       | Protocol |
| ------------------------ | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------- |
| US East (Ohio)           | us-east-2      | greengrass.us-east-2.amazonaws.com<br>greengrass-fips.us-east-2.amazonaws.com<br>greengrass.us-east-2.api.aws<br>greengrass-fips.us-east-2.api.aws             | HTTPS    |
| US East (N. Virginia)    | us-east-1      | greengrass.us-east-1.amazonaws.com<br>greengrass-fips.us-east-1.amazonaws.com<br>greengrass.us-east-1.api.aws<br>greengrass-fips.us-east-1.api.aws             | HTTPS    |
| US West (Oregon)         | us-west-2      | greengrass.us-west-2.amazonaws.com<br>greengrass-fips.us-west-2.amazonaws.com<br>greengrass.us-west-2.api.aws<br>greengrass-fips.us-west-2.api.aws             | HTTPS    |
| Asia Pacific (Malaysia)  | ap-southeast-5 | greengrass.ap-southeast-5.amazonaws.com<br>greengrass.ap-southeast-5.api.aws                                                                                   | HTTPS    |
| Asia Pacific (Mumbai)    | ap-south-1     | greengrass.ap-south-1.amazonaws.com<br>greengrass.ap-south-1.api.aws                                                                                           | HTTPS    |
| Asia Pacific (Seoul)     | ap-northeast-2 | greengrass.ap-northeast-2.amazonaws.com<br>greengrass.ap-northeast-2.api.aws                                                                                   | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | greengrass.ap-southeast-1.amazonaws.com<br>greengrass.ap-southeast-1.api.aws                                                                                   | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | greengrass.ap-southeast-2.amazonaws.com<br>greengrass.ap-southeast-2.api.aws                                                                                   | HTTPS    |
| Asia Pacific (Tokyo)     | ap-northeast-1 | greengrass.ap-northeast-1.amazonaws.com<br>greengrass.ap-northeast-1.api.aws                                                                                   | HTTPS    |
| Canada (Central)         | ca-central-1   | greengrass.ca-central-1.amazonaws.com<br>greengrass-fips.ca-central-1.amazonaws.com<br>greengrass.ca-central-1.api.aws<br>greengrass-fips.ca-central-1.api.aws | HTTPS    |
| China (Beijing)          | cn-north-1     | greengrass.cn-north-1.amazonaws.com.cn                                                                                                                         | HTTPS    |
| Europe (Frankfurt)       | eu-central-1   | greengrass.eu-central-1.amazonaws.com<br>greengrass.eu-central-1.api.aws                                                                                       | HTTPS    |
| Europe (Ireland)         | eu-west-1      | greengrass.eu-west-1.amazonaws.com<br>greengrass.eu-west-1.api.aws                                                                                             | HTTPS    |
| Europe (London)          | eu-west-2      | greengrass.eu-west-2.amazonaws.com<br>greengrass.eu-west-2.api.aws                                                                                             | HTTPS    |
| Europe (Spain)           | eu-south-2     | greengrass.eu-south-2.amazonaws.com<br>greengrass.eu-south-2.api.aws                                                                                           | HTTPS    |
| AWS GovCloud (US-West)   | us-gov-west-1  | greengrass.us-gov-west-1.amazonaws.com<br>greengrass.us-gov-west-1.api.aws                                                                                     | HTTPS    |
| AWS GovCloud (US-East)   | us-gov-east-1  | greengrass.us-gov-east-1.amazonaws.com<br>greengrass.us-gov-east-1.api.aws                                                                                     | HTTPS    |

### AWS IoT device operations

The following table contains AWS Region-specific Amazon Trust Services (ATS)
endpoints for AWS IoT device management operations, such as shadow sync. This is a
data plane API.

To look up your account-specific endpoint, use the [aws iot describe-endpoint
--endpoint-type iot:Data-ATS](../../../cli/latest/reference/iot/describe-endpoint.md "../../../cli/latest/reference/iot/describe-endpoint.md") command.

| Region name              | Region         | Endpoint                                      | Protocol    |
| ------------------------ | -------------- | --------------------------------------------- | ----------- |
| US East (Ohio)           | us-east-2      | _prefix_-ats.iot.us-east-2.amazonaws.com      | HTTPS, MQTT |
| US East (N. Virginia)    | us-east-1      | _prefix_-ats.iot.us-east-1.amazonaws.com      | HTTPS, MQTT |
| US West (Oregon)         | us-west-2      | _prefix_-ats.iot.us-west-2.amazonaws.com      | HTTPS, MQTT |
| Asia Pacific (Malaysia)  | ap-southeast-5 | _prefix_-ats.iot.ap-southeast-5.amazonaws.com | HTTPS, MQTT |
| Asia Pacific (Mumbai)    | ap-south-1     | _prefix_-ats.iot.ap-south-1.amazonaws.com     | HTTPS, MQTT |
| Asia Pacific (Seoul)     | ap-northeast-2 | _prefix_-ats.iot.ap-northeast-2.amazonaws.com | HTTPS, MQTT |
| Asia Pacific (Singapore) | ap-southeast-1 | _prefix_-ats.iot.ap-southeast-1.amazonaws.com | HTTPS, MQTT |
| Asia Pacific (Sydney)    | ap-southeast-2 | _prefix_-ats.iot.ap-southeast-2.amazonaws.com | HTTPS, MQTT |
| Asia Pacific (Tokyo)     | ap-northeast-1 | _prefix_-ats.iot.ap-northeast-1.amazonaws.com | HTTPS, MQTT |
| Canada (Central)         | ca-central-1   | _prefix_-ats.iot.ca-central-1.amazonaws.com   | HTTPS, MQTT |
| China (Beijing)          | cn-north-1     | _prefix_.ats.iot.cn-north-1.amazonaws.com.cn  | HTTPS, MQTT |
| Europe (Frankfurt)       | eu-central-1   | _prefix_-ats.iot.eu-central-1.amazonaws.com   | HTTPS, MQTT |
| Europe (Ireland)         | eu-west-1      | _prefix_-ats.iot.eu-west-1.amazonaws.com      | HTTPS, MQTT |
| Europe (London)          | eu-west-2      | _prefix_-ats.iot.eu-west-2.amazonaws.com      | HTTPS, MQTT |
| Europe (Spain)           | eu-south-2     | _prefix_-ats.iot.eu-south-2.amazonaws.com     | HTTPS, MQTT |
| AWS GovCloud (US-West)   | us-gov-west-1  | _prefix_-ats.iot.us-gov-west-1.amazonaws.com  | HTTPS, MQTT |
| AWS GovCloud (US-East)   | us-gov-east-1  | _prefix_-ats.iot.us-gov-east-1.amazonaws.com  | HTTPS, MQTT |

###### Note

Legacy Verisign endpoints are currently supported for [some Regions](#greengrassv2-legacy-endpoints "#greengrassv2-legacy-endpoints"), but we
recommend that you use ATS endpoints with ATS root certificate authority (CA)
certificates. For more information, see [Server Authentication](../../../iot/latest/developerguide/server-authentication.md "../../../iot/latest/developerguide/server-authentication.md") in the
_AWS IoT Developer Guide_.

### Data plane operations

AWS IoT Greengrass uses the AWS IoT Core Region-specific ATS endpoints for data plane operations,
such as [ResolveComponentCandidates](../../../greengrass/v2/APIReference/API_ResolveComponentCandidates.md "../../../greengrass/v2/APIReference/API_ResolveComponentCandidates.md"). For a complete list, see [AWS IoT Core - data plane endpoints](iot-core.md#iot-core-data-plane-endpoints "iot-core.md#iot-core-data-plane-endpoints"). You must set
`greengrassDataPlaneEndpoint` to `iotdata`. For
more information, see [AWS IoT Greengrass nucleus configuration](../../../greengrass/v2/developerguide/greengrass-nucleus-component.md#greengrass-nucleus-component-configuration "../../../greengrass/v2/developerguide/greengrass-nucleus-component.md#greengrass-nucleus-component-configuration").

We recommend you use the AWS IoT endpoints for data plane operations. For backwards
compatibility, AWS IoT Greengrass supports the following legacy endpoints.

| Region name              | Region         | Endpoint                                        | Protocol |
| ------------------------ | -------------- | ----------------------------------------------- | -------- |
| US East (Ohio)           | us-east-2      | greengrass-ats.iot.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)    | us-east-1      | greengrass-ats.iot.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)         | us-west-2      | greengrass-ats.iot.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Malaysia)  | ap-southeast-5 | greengrass-ats.iot.ap-southeast-5.amazonaws.com | HTTPS    |
| Asia Pacific (Mumbai)    | ap-south-1     | greengrass-ats.iot.ap-south-1.amazonaws.com     | HTTPS    |
| Asia Pacific (Seoul)     | ap-northeast-2 | greengrass-ats.iot.ap-northeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | greengrass-ats.iot.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | greengrass-ats.iot.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)     | ap-northeast-1 | greengrass-ats.iot.ap-northeast-1.amazonaws.com | HTTPS    |
| Canada (Central)         | ca-central-1   | greengrass-ats.iot.ap-northeast-1.amazonaws.com | HTTPS    |
| China (Beijing)          | cn-north-1     | greengrass.ats.iot.cn-north-1.amazonaws.com.cn  | HTTPS    |
| Europe (Frankfurt)       | eu-central-1   | greengrass-ats.iot.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)         | eu-west-1      | greengrass-ats.iot.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)          | eu-west-2      | greengrass-ats.iot.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Spain)           | eu-south-2     | greengrass-ats.iot.eu-south-2.amazonaws.com     | HTTPS    |
| AWS GovCloud (US-West)   | us-gov-west-1  | greengrass-ats.iot.us-gov-west-1.amazonaws.com  | HTTPS    |
| AWS GovCloud (US-East)   | us-gov-east-1  | greengrass-ats.iot.us-gov-east-1.amazonaws.com  | HTTPS    |

###### Note

Legacy Verisign endpoints are currently supported for [some Regions](#greengrassv2-legacy-endpoints "#greengrassv2-legacy-endpoints"), but we
recommend that you use ATS endpoints with ATS root CA certificates. For more
information, see [Server authentication](../../../iot/latest/developerguide/server-authentication.md "../../../iot/latest/developerguide/server-authentication.md") in the
_AWS IoT Developer Guide_.

### Supported legacy endpoints

We recommend that you use the ATS endpoints in the preceding tables with ATS root
CA certificates. For backward compatibility, AWS IoT Greengrass V2 currently supports legacy
Verisign endpoints in the following AWS Regions. This support is expected to end
in the future. For more information, see [Server authentication](../../../iot/latest/developerguide/server-authentication.md "../../../iot/latest/developerguide/server-authentication.md") in the
_AWS IoT Developer Guide_.

When using legacy Verisign endpoints, you must use Verisign root CA
certificates.

AWS IoT device operations (legacy endpoints)

| Region name           | Region         | Endpoint                                  | Protocol    |
| --------------------- | -------------- | ----------------------------------------- | ----------- |
| US East (N. Virginia) | us-east-1      | _prefix_.iot.us-east-1.amazonaws.com      | HTTPS, MQTT |
| US West (Oregon)      | us-west-2      | _prefix_.iot.us-west-2.amazonaws.com      | HTTPS, MQTT |
| Asia Pacific (Sydney) | ap-southeast-2 | _prefix_.iot.ap-southeast-2.amazonaws.com | HTTPS, MQTT |
| Asia Pacific (Tokyo)  | ap-northeast-1 | _prefix_.iot.ap-northeast-1.amazonaws.com | HTTPS, MQTT |
| Europe (Frankfurt)    | eu-central-1   | _prefix_.iot.eu-central-1.amazonaws.com   | HTTPS, MQTT |
| Europe (Ireland)      | eu-west-1      | _prefix_.iot.eu-west-1.amazonaws.com      | HTTPS, MQTT |

To look up your account-specific legacy endpoint, use the [aws iot
describe-endpoint --endpoint-type iot:Data](../../../cli/latest/reference/iot/describe-endpoint.md "../../../cli/latest/reference/iot/describe-endpoint.md") command.

Data plane operations (legacy endpoints)

| Region name           | Region         | Endpoint                                    | Protocol |
| --------------------- | -------------- | ------------------------------------------- | -------- |
| US East (N. Virginia) | us-east-1      | greengrass.iot.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)      | us-west-2      | greengrass.iot.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Sydney) | ap-southeast-2 | greengrass.iot.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)  | ap-northeast-1 | greengrass.iot.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Frankfurt)    | eu-central-1   | greengrass.iot.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)      | eu-west-1      | greengrass.iot.eu-west-1.amazonaws.com      | HTTPS    |

## Service quotas

The following tables describe quotas in AWS IoT Greengrass V2. For more information about quotas and
how to request quota increases, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

| Quotas for core devices                    | Resource                              | Quota | Adjustable |
| ------------------------------------------ | ------------------------------------- | ----- | ---------- |
| Maximum length of a core device thing name | 124 bytes of UTF-8 encoded characters | No    |

| Quotas for components                     | Resource                                | Quota | Adjustable                                                         | Notes |
| ----------------------------------------- | --------------------------------------- | ----- | ------------------------------------------------------------------ | ----- |
| Maximum number of components              | 5,000 components per Region             | No    |                                                                    |
| Maximum number of component versions      | 5,000 versions per component per Region | No    |                                                                    |
| Maximum size of component recipe          | 16 KB                                   | No    |                                                                    |
| Maximum total size of component artifacts | 2 GB                                    | No    | This quota applies to the sum of all artifacts for a<br>component. |

| Quotas for deployments                                                                                    | Resource | Quota | Adjustable                                                                                                         | Notes |
| --------------------------------------------------------------------------------------------------------- | -------- | ----- | ------------------------------------------------------------------------------------------------------------------ | ----- |
| Maximum size of deployment document for a thing deployment (without<br>large configuration support)       | 7 KB     | No    | The deployment document includes the component configurations,<br>deployment configurations, and payload overhead. |
| Maximum size of deployment document for a thing group deployment<br>(without large configuration support) | 31 KB    | No    | The deployment document includes the component configurations,<br>deployment configurations, and payload overhead. |
| Maximum size of deployment document with large configuration<br>support                                   | 6 MB     | No    | The deployment document includes the component configurations,<br>deployment configurations, and payload overhead. |

| Quotas for API operations               | Resource                          | Quota | Adjustable                                                                                                                                                                                                                                                                                                 | Notes |
| --------------------------------------- | --------------------------------- | ----- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----- |
| Request rate for CreateComponentVersion | 1 request per second per Region   | No    |                                                                                                                                                                                                                                                                                                            |
| Request rate for other API operations   | 30 requests per second per Region | No    | This quota applies to the combination of API requests for all<br>control plane operations.<br>Exceptions<br>• China (Beijing) – 10 requests per second per<br>Region<br>• AWS GovCloud (US-West) – 10 requests per second per<br>Region<br>• AWS GovCloud (US-East) – 10 requests per second per<br>Region |
