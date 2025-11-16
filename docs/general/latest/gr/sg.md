# AWS Storage Gateway endpoints and quotas

The following are the service endpoints and service quotas for this service.
To connect to an AWS service, you use an endpoint. In addition to the standard
AWS endpoints, some AWS services offer FIPS endpoints in selected Regions. For more information,
see [AWS service endpoints](rande.md "rande.md"). Service quotas, also referred to as
limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

## Service endpoints

### Storage Gateway

| Region Name                | Region         | Endpoint                                                                                                                                                                           | Protocol                         |
| -------------------------- | -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | storagegateway.us-east-2.amazonaws.com<br>storagegateway-fips.us-east-2.api.aws<br>storagegateway.us-east-2.api.aws<br>storagegateway-fips.us-east-2.amazonaws.com                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | storagegateway.us-east-1.amazonaws.com<br>storagegateway-fips.us-east-1.api.aws<br>storagegateway-fips.us-east-1.amazonaws.com<br>storagegateway.us-east-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | storagegateway.us-west-1.amazonaws.com<br>storagegateway.us-west-1.api.aws<br>storagegateway-fips.us-west-1.amazonaws.com<br>storagegateway-fips.us-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | storagegateway.us-west-2.amazonaws.com<br>storagegateway-fips.us-west-2.amazonaws.com<br>storagegateway.us-west-2.api.aws<br>storagegateway-fips.us-west-2.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | storagegateway.af-south-1.amazonaws.com<br>storagegateway.af-south-1.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | storagegateway.ap-east-1.amazonaws.com<br>storagegateway.ap-east-1.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | storagegateway.ap-south-2.amazonaws.com<br>storagegateway.ap-south-2.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | storagegateway.ap-southeast-3.amazonaws.com<br>storagegateway.ap-southeast-3.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | storagegateway.ap-southeast-5.amazonaws.com<br>storagegateway.ap-southeast-5.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | storagegateway.ap-southeast-4.amazonaws.com<br>storagegateway.ap-southeast-4.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | storagegateway.ap-south-1.amazonaws.com<br>storagegateway.ap-south-1.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | storagegateway.ap-southeast-6.amazonaws.com<br>storagegateway.ap-southeast-6.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | storagegateway.ap-northeast-3.amazonaws.com<br>storagegateway.ap-northeast-3.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | storagegateway.ap-northeast-2.amazonaws.com<br>storagegateway.ap-northeast-2.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | storagegateway.ap-southeast-1.amazonaws.com<br>storagegateway.ap-southeast-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | storagegateway.ap-southeast-2.amazonaws.com<br>storagegateway.ap-southeast-2.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | storagegateway.ap-east-2.amazonaws.com<br>storagegateway.ap-east-2.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | storagegateway.ap-southeast-7.amazonaws.com<br>storagegateway.ap-southeast-7.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | storagegateway.ap-northeast-1.amazonaws.com<br>storagegateway.ap-northeast-1.api.aws                                                                                               | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | storagegateway.ca-central-1.amazonaws.com<br>storagegateway.ca-central-1.api.aws<br>storagegateway-fips.ca-central-1.amazonaws.com<br>storagegateway-fips.ca-central-1.api.aws     | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | storagegateway.ca-west-1.amazonaws.com<br>storagegateway-fips.ca-west-1.api.aws<br>storagegateway-fips.ca-west-1.amazonaws.com<br>storagegateway.ca-west-1.api.aws                 | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | storagegateway.eu-central-1.amazonaws.com<br>storagegateway.eu-central-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | storagegateway.eu-west-1.amazonaws.com<br>storagegateway.eu-west-1.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | storagegateway.eu-west-2.amazonaws.com<br>storagegateway.eu-west-2.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | storagegateway.eu-south-1.amazonaws.com<br>storagegateway.eu-south-1.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | storagegateway.eu-west-3.amazonaws.com<br>storagegateway.eu-west-3.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | storagegateway.eu-south-2.amazonaws.com<br>storagegateway.eu-south-2.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | storagegateway.eu-north-1.amazonaws.com<br>storagegateway.eu-north-1.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | storagegateway.eu-central-2.amazonaws.com<br>storagegateway.eu-central-2.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | storagegateway.il-central-1.amazonaws.com<br>storagegateway.il-central-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | storagegateway.mx-central-1.amazonaws.com<br>storagegateway.mx-central-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | storagegateway.me-south-1.amazonaws.com<br>storagegateway.me-south-1.api.aws                                                                                                       | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | storagegateway.me-central-1.amazonaws.com<br>storagegateway.me-central-1.api.aws                                                                                                   | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | storagegateway.sa-east-1.amazonaws.com<br>storagegateway.sa-east-1.api.aws                                                                                                         | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | storagegateway.us-gov-east-1.amazonaws.com<br>storagegateway-fips.us-gov-east-1.amazonaws.com<br>storagegateway-fips.us-gov-east-1.api.aws<br>storagegateway.us-gov-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| AWS GovCloud (US-West)     | us-gov-west-1  | storagegateway.us-gov-west-1.amazonaws.com<br>storagegateway-fips.us-gov-west-1.amazonaws.com<br>storagegateway.us-gov-west-1.api.aws<br>storagegateway-fips.us-gov-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |

### Storage Gateway hardware appliance

regions

The Storage Gateway hardware appliance is available for shipping worldwide where it
is legally allowed and permitted for exporting by the US government.

Storage Gateway hardware appliance is supported in the following AWS
Regions.

- US East (Ohio)
- US East (N. Virginia)
- US West (N. California)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Seoul)
- Asia Pacific (Singapore)
- Asia Pacific (Sydney)
- Asia Pacific (Tokyo)
- Canada (Central)
- Europe (Frankfurt)
- Europe (Ireland)
- Europe (London)
- Europe (Paris)
- Europe (Stockholm)
- South America (São Paulo)

## Service quotas

| Name                                                 | Default                            | Adjustable | Description                                                                                            |
| ---------------------------------------------------- | ---------------------------------- | ---------- | ------------------------------------------------------------------------------------------------------ |
| Cached volume gateway Cache Maximum in TiB           | Each supported Region: 64          | No         | Maximum cache size for Cached Volume Gateway                                                           |
| Cached volume gateway Cache Minimum in GiB           | Each supported Region: 150         | No         | Minimum cache size for Cached Volume Gateway                                                           |
| Cached volume gateway Upload Buffer Maximum in TiB   | Each supported Region: 2           | No         | Maximum upload buffer size for Cached Volume Gateway                                                   |
| Cached volume gateway Upload Buffer Minimum in GiB   | Each supported Region: 150         | No         | Minimum upload buffer size for Cached Volume Gateway                                                   |
| Cached volume size in TiB                            | Each supported Region: 32          | No         | Maximum size of a cached volume                                                                        |
| Cached volumes per gateway                           | Each supported Region: 32          | No         | Maximum number of cached volumes per gateway                                                           |
| File gateway Cache Maximum in TiB                    | Each supported Region: 64          | No         | Maximum cache size for File Gateway                                                                    |
| File gateway Cache Minimum in GiB                    | Each supported Region: 150         | No         | Minimum cache size for File Gateway                                                                    |
| File shares per S3 bucket                            | Each supported Region: 1           | No         | Maximum number of file shares per Amazon S3 bucket                                                     |
| File shares per gateway                              | Each supported Region: 50          | No         | Maximum number of file shares per gateway                                                              |
| File size                                            | Each supported Region: 5 Terabytes | No         | The maximum size of an individual file, which is the maximum size of an individual object in Amazon S3 |
| Max size of a virtual tape in TiB                    | Each supported Region: 15          | No         | Maximum size of a virtual tape                                                                         |
| Max virtual tapes in a VTL                           | Each supported Region: 1,500       | No         | Maximum number of virtual tapes for a virtual tape library (VTL)                                       |
| Minimum size of a virtual tape in GiB                | Each supported Region: 100         | No         | Minimum size of a virtual tape                                                                         |
| Path length                                          | Each supported Region: 1,024 Bytes | No         | Maximum path length                                                                                    |
| Size of all cached volumes per gateway in TiB        | Each supported Region: 1,024       | No         | Total size of all cached volumes for a gateway                                                         |
| Size of all stored volumes per gateway in TiB        | Each supported Region: 512         | No         | Total size of all stored volumes for a gateway                                                         |
| Stored volume gateway Upload Buffer Maximum in TiB   | Each supported Region: 2           | No         | Maximum upload buffer size for Stored Volume Gateway                                                   |
| Stored volume gateway Upload Buffer Minimum in GiB   | Each supported Region: 150         | No         | Minimum upload buffer size for Stored Volume Gateway                                                   |
| Stored volume size in TiB                            | Each supported Region: 16          | No         | Maximum size of a stored volume                                                                        |
| Stored volumes per gateway                           | Each supported Region: 32          | No         | Maximum number of stored volumes per gateway                                                           |
| Tape gateway Cache Maximum in TiB                    | Each supported Region: 64          | No         | Maximum cache size for Tape Gateway                                                                    |
| Tape gateway Cache Minimum in GiB                    | Each supported Region: 150         | No         | Minimum cache size for Tape Gateway                                                                    |
| Tape gateway Upload Buffer Maximum in TiB            | Each supported Region: 2           | No         | Maximum upload buffer size for Tape Gateway                                                            |
| Tape gateway Upload Buffer Minimum in GiB            | Each supported Region: 150         | No         | Minimum upload buffer size for Tape Gateway                                                            |
| Total size of tapes in a virtual tape library in PiB | Each supported Region: 1           | No         | Total size of all tapes in a virtual tape library (VTL)                                                |

For more information, see [Storage Gateway
quotas](../../../storagegateway/latest/userguide/resource-gateway-limits.md "../../../storagegateway/latest/userguide/resource-gateway-limits.md") in the _AWS Storage Gateway User Guide_.
