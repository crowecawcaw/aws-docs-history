# AWS AppConfig endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

AWS AppConfig is a capability of AWS Systems Manager. To view endpoints and quotas of other Systems Manager
capabilities, see [AWS Systems Manager endpoints and quotas](ssm.md "ssm.md").

## Service endpoints

The following sections describe the service endpoints for AWS AppConfig. AWS AppConfig uses
_control plane_ APIs for setting up and configuring AWS AppConfig
applications, environments, configuration profiles, and deployment strategies. AWS AppConfig
uses the AWS AppConfig Data service to call _data plane_ APIs for
retrieving stored configurations.

###### Topics

- [Control plane endpoints](#appconfig_control_plane "#appconfig_control_plane")
- [Data plane endpoints](#appconfigdata_data_plane "#appconfigdata_data_plane")

### Control plane endpoints

The following table contains AWS Region-specific endpoints that AWS AppConfig supports
for control plane operations. Control plane operations are used for creating,
updating, and managing configuration data. For more information, see [AWS AppConfig
operations](../../../appconfig/2019-10-09/APIReference/API_Operations_Amazon_AppConfig.md "../../../appconfig/2019-10-09/APIReference/API_Operations_Amazon_AppConfig.md") in the _AWS AppConfig API Reference_.

| Region Name                | Region         | Endpoint                                                                                                                                                       | Protocol                         |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | appconfig.us-east-2.amazonaws.com<br>appconfig-fips.us-east-2.api.aws<br>appconfig-fips.us-east-2.amazonaws.com<br>appconfig.us-east-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | appconfig.us-east-1.amazonaws.com<br>appconfig-fips.us-east-1.api.aws<br>appconfig-fips.us-east-1.amazonaws.com<br>appconfig.us-east-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | appconfig.us-west-1.amazonaws.com<br>appconfig-fips.us-west-1.api.aws<br>appconfig-fips.us-west-1.amazonaws.com<br>appconfig.us-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | appconfig.us-west-2.amazonaws.com<br>appconfig-fips.us-west-2.api.aws<br>appconfig-fips.us-west-2.amazonaws.com<br>appconfig.us-west-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | appconfig.af-south-1.amazonaws.com<br>appconfig.af-south-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | appconfig.ap-east-1.amazonaws.com<br>appconfig.ap-east-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | appconfig.ap-south-2.amazonaws.com<br>appconfig.ap-south-2.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | appconfig.ap-southeast-3.amazonaws.com<br>appconfig.ap-southeast-3.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | appconfig.ap-southeast-5.amazonaws.com<br>appconfig.ap-southeast-5.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | appconfig.ap-southeast-4.amazonaws.com<br>appconfig.ap-southeast-4.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | appconfig.ap-south-1.amazonaws.com<br>appconfig.ap-south-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | appconfig.ap-southeast-6.amazonaws.com<br>appconfig.ap-southeast-6.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | appconfig.ap-northeast-3.amazonaws.com<br>appconfig.ap-northeast-3.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | appconfig.ap-northeast-2.amazonaws.com<br>appconfig.ap-northeast-2.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | appconfig.ap-southeast-1.amazonaws.com<br>appconfig.ap-southeast-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | appconfig.ap-southeast-2.amazonaws.com<br>appconfig.ap-southeast-2.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | appconfig.ap-east-2.amazonaws.com<br>appconfig.ap-east-2.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | appconfig.ap-southeast-7.amazonaws.com<br>appconfig.ap-southeast-7.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | appconfig.ap-northeast-1.amazonaws.com<br>appconfig.ap-northeast-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | appconfig.ca-central-1.amazonaws.com<br>appconfig-fips.ca-central-1.api.aws<br>appconfig-fips.ca-central-1.amazonaws.com<br>appconfig.ca-central-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | appconfig.ca-west-1.amazonaws.com<br>appconfig-fips.ca-west-1.api.aws<br>appconfig-fips.ca-west-1.amazonaws.com<br>appconfig.ca-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | appconfig.eu-central-1.amazonaws.com<br>appconfig.eu-central-1.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | appconfig.eu-west-1.amazonaws.com<br>appconfig.eu-west-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | appconfig.eu-west-2.amazonaws.com<br>appconfig.eu-west-2.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | appconfig.eu-south-1.amazonaws.com<br>appconfig.eu-south-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | appconfig.eu-west-3.amazonaws.com<br>appconfig.eu-west-3.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | appconfig.eu-south-2.amazonaws.com<br>appconfig.eu-south-2.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | appconfig.eu-north-1.amazonaws.com<br>appconfig.eu-north-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | appconfig.eu-central-2.amazonaws.com<br>appconfig.eu-central-2.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | appconfig.il-central-1.amazonaws.com<br>appconfig.il-central-1.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | appconfig.mx-central-1.amazonaws.com<br>appconfig.mx-central-1.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | appconfig.me-south-1.amazonaws.com<br>appconfig.me-south-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | appconfig.me-central-1.amazonaws.com<br>appconfig.me-central-1.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | appconfig.sa-east-1.amazonaws.com<br>appconfig.sa-east-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | appconfig.us-gov-east-1.amazonaws.com<br>appconfig-fips.us-gov-east-1.api.aws<br>appconfig-fips.us-gov-east-1.amazonaws.com<br>appconfig.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | appconfig.us-gov-west-1.amazonaws.com<br>appconfig-fips.us-gov-west-1.api.aws<br>appconfig-fips.us-gov-west-1.amazonaws.com<br>appconfig.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

### Data plane endpoints

The following table contains AWS Region-specific endpoints that AWS AppConfig Data
supports for data plane operations. Data plane operations are used for retrieving
configuration data. For more information, see [AWS AppConfig Data
operations](../../../appconfig/2019-10-09/APIReference/API_Operations_AWS_AppConfig_Data.md "../../../appconfig/2019-10-09/APIReference/API_Operations_AWS_AppConfig_Data.md") in the _AWS AppConfig API Reference_.

| Region Name                | Region         | Endpoint                                                                                                                                                                   | Protocol                         |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | appconfigdata.us-east-2.amazonaws.com<br>appconfigdata-fips.us-east-2.api.aws<br>appconfigdata-fips.us-east-2.amazonaws.com<br>appconfigdata.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | appconfigdata.us-east-1.amazonaws.com<br>appconfigdata-fips.us-east-1.api.aws<br>appconfigdata-fips.us-east-1.amazonaws.com<br>appconfigdata.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | appconfigdata.us-west-1.amazonaws.com<br>appconfigdata-fips.us-west-1.api.aws<br>appconfigdata-fips.us-west-1.amazonaws.com<br>appconfigdata.us-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | appconfigdata.us-west-2.amazonaws.com<br>appconfigdata-fips.us-west-2.api.aws<br>appconfigdata-fips.us-west-2.amazonaws.com<br>appconfigdata.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | appconfigdata.af-south-1.amazonaws.com<br>appconfigdata.af-south-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | appconfigdata.ap-east-1.amazonaws.com<br>appconfigdata.ap-east-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | appconfigdata.ap-south-2.amazonaws.com<br>appconfigdata.ap-south-2.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | appconfigdata.ap-southeast-3.amazonaws.com<br>appconfigdata.ap-southeast-3.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | appconfigdata.ap-southeast-5.amazonaws.com                                                                                                                                 | HTTPS                            |
| Asia Pacific (Melbourne)   | ap-southeast-4 | appconfigdata.ap-southeast-4.amazonaws.com<br>appconfigdata.ap-southeast-4.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | appconfigdata.ap-south-1.amazonaws.com<br>appconfigdata.ap-south-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | appconfigdata.ap-southeast-6.amazonaws.com<br>appconfigdata.ap-southeast-6.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | appconfigdata.ap-northeast-3.amazonaws.com<br>appconfigdata.ap-northeast-3.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | appconfigdata.ap-northeast-2.amazonaws.com<br>appconfigdata.ap-northeast-2.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | appconfigdata.ap-southeast-1.amazonaws.com<br>appconfigdata.ap-southeast-1.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | appconfigdata.ap-southeast-2.amazonaws.com<br>appconfigdata.ap-southeast-2.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | appconfigdata.ap-east-2.amazonaws.com                                                                                                                                      | HTTPS                            |
| Asia Pacific (Thailand)    | ap-southeast-7 | appconfigdata.ap-southeast-7.amazonaws.com                                                                                                                                 | HTTPS                            |
| Asia Pacific (Tokyo)       | ap-northeast-1 | appconfigdata.ap-northeast-1.amazonaws.com<br>appconfigdata.ap-northeast-1.api.aws                                                                                         | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | appconfigdata.ca-central-1.amazonaws.com<br>appconfigdata-fips.ca-central-1.api.aws<br>appconfigdata-fips.ca-central-1.amazonaws.com<br>appconfigdata.ca-central-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | appconfigdata.ca-west-1.amazonaws.com<br>appconfigdata-fips.ca-west-1.api.aws<br>appconfigdata-fips.ca-west-1.amazonaws.com<br>appconfigdata.ca-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | appconfigdata.eu-central-1.amazonaws.com<br>appconfigdata.eu-central-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | appconfigdata.eu-west-1.amazonaws.com<br>appconfigdata.eu-west-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | appconfigdata.eu-west-2.amazonaws.com<br>appconfigdata.eu-west-2.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | appconfigdata.eu-south-1.amazonaws.com<br>appconfigdata.eu-south-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | appconfigdata.eu-west-3.amazonaws.com<br>appconfigdata.eu-west-3.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | appconfigdata.eu-south-2.amazonaws.com<br>appconfigdata.eu-south-2.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | appconfigdata.eu-north-1.amazonaws.com<br>appconfigdata.eu-north-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | appconfigdata.eu-central-2.amazonaws.com<br>appconfigdata.eu-central-2.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | appconfigdata.il-central-1.amazonaws.com<br>appconfigdata.il-central-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | appconfigdata.mx-central-1.amazonaws.com                                                                                                                                   | HTTPS                            |
| Middle East (Bahrain)      | me-south-1     | appconfigdata.me-south-1.amazonaws.com<br>appconfigdata.me-south-1.api.aws                                                                                                 | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | appconfigdata.me-central-1.amazonaws.com<br>appconfigdata.me-central-1.api.aws                                                                                             | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | appconfigdata.sa-east-1.amazonaws.com<br>appconfigdata.sa-east-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | appconfigdata.us-gov-east-1.amazonaws.com<br>appconfigdata.us-gov-east-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | appconfigdata.us-gov-west-1.amazonaws.com<br>appconfigdata.us-gov-west-1.api.aws                                                                                           | HTTPS<br>HTTPS                   |

## Service quotas

| Name                                                                 | Default                                | Adjustable                                                                                                                                                                             | Description                                                                                                                                                                                                                                                                                                                                       |
| -------------------------------------------------------------------- | -------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Configuration size limit in AWS AppConfig hosted configuration store | Each supported Region: 2,048 Kilobytes | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-48F9B951 "https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-48F9B951") | The current maximum approval limit of a hosted configuration is 4,000 Kilobytes per version. There is no additional cost to use hosted configurations. To reduce configuration size, remove unnecessary configuration data, or segment data across multiple configuration profiles.                                                               |
| Deployment size limit                                                | Each supported Region: 2,048 Kilobytes | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-A5FC0339 "https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-A5FC0339") | The current maximum approval limit of an AWS AppConfig deployment is 4,000 Kilobytes per deployment. To reduce configuration size, remove unnecessary configuration data, or segment configuration data across multiple configuration profiles.                                                                                                   |
| Maximum number of applications                                       | Each supported Region: 100             | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-EEB0151E "https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-EEB0151E") | An application in AWS AppConfig is a logical unit of code (a namespace) that provides capabilities for your customers. Limit increase requests will be automatically approved for values less than or equal to 300.                                                                                                                               |
| Maximum number of configuration profiles per application             | Each supported Region: 100             | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-FA210A1F "https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-FA210A1F") | A configuration profile contains metadata about a particular set of configuration data used by your application. To reduce the number of configuration profiles required per application, split configuration profiles across multiple applications. Limit increase requests will be automatically approved for values less than or equal to 500. |
| Maximum number of deployment strategies                              | Each supported Region: 20              | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-F59D302B "https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-F59D302B") | A deployment strategy defines how configuration deploys, or rolls out, across a collection of instances within a specific application environment. Limit increase requests will be automatically approved for values less than or equal to 100.                                                                                                   |
| Maximum number of environments per application                       | Each supported Region: 20              | [Yes](https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-A52E46BE "https://console.aws.amazon.com/servicequotas/home/services/appconfig/quotas/L-A52E46BE") | An environment corresponds to a grouping of instances associated with an application. Environments examples include stages, such as beta and prod, or application subcomponents, such as web, mobile, and service. Limit increase requests will be automatically approved for values less than or equal to 100.                                   |

### Control plane default

limits

| API name              | Transactions per second | Adjustable |
| --------------------- | ----------------------- | ---------- |
| Create\*              | 10                      | No         |
| Delete\*              | 10                      | No         |
| Get\*                 | 100                     | No         |
| List\*                | 10                      | No         |
| StartDeployment       | 10                      | No         |
| StopDeployment        | 10                      | No         |
| TagResource           | 20                      | No         |
| UntagResource         | 20                      | No         |
| Update\*              | 10                      | No         |
| ValidateConfiguration | 10                      | No         |

### Data plane default limits

| Action                                                                                                                                             | API limit                                                      | Adjustable |
| -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------- | ---------- |
| GetConfiguration ([deprecated](../../../appconfig/latest/userguide/about-data-plane.md "../../../appconfig/latest/userguide/about-data-plane.md")) | 500 TPS                                                        | No         |
| GetLatestConfiguration                                                                                                                             | 1,000 TPS                                                      | Yes        |
| StartConfigurationSession                                                                                                                          | 500 TPS                                                        | Yes        |
| Configurations received                                                                                                                            | 1 million (burst) per day if not using the AWS AppConfig agent | Yes        |

To request an increase for `GetLatestConfiguration`,
`StartConfigurationSession`, or `Configurations received`
contact Support. To improve performance, availability, and reduce costs, we
recommended you cache configurations locally when using AWS AppConfig. [AWS AppConfig
Agent](../../../appconfig/latest/userguide/appconfig-agent-how-to-use.md "../../../appconfig/latest/userguide/appconfig-agent-how-to-use.md") caches configurations on your behalf.
