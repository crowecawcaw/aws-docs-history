# Amazon EC2 endpoints and quotas

###### Important

AWS Regions launched after **October 30, 2021**
will no longer support Amazon EC2 API requests over connections that are established
using TLSv1, TLSv1.1, or unencrypted HTTP.

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                          | Protocol                         |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | ec2.us-east-2.amazonaws.com<br>ec2-fips.us-east-2.amazonaws.com<br>ec2.us-east-2.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | ec2.us-east-1.amazonaws.com<br>ec2-fips.us-east-1.amazonaws.com<br>ec2.us-east-1.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | ec2.us-west-1.amazonaws.com<br>ec2-fips.us-west-1.amazonaws.com<br>ec2.us-west-1.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | ec2.us-west-2.amazonaws.com<br>ec2-fips.us-west-2.amazonaws.com<br>ec2.us-west-2.api.aws          | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | ec2.af-south-1.amazonaws.com<br>ec2.af-south-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Hong Kong)   | ap-east-1      | ec2.ap-east-1.amazonaws.com<br>ec2.ap-east-1.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Hyderabad)   | ap-south-2     | ec2.ap-south-2.amazonaws.com                                                                      | HTTPS                            |
| Asia Pacific (Jakarta)     | ap-southeast-3 | ec2.ap-southeast-3.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Malaysia)    | ap-southeast-5 | ec2.ap-southeast-5.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Melbourne)   | ap-southeast-4 | ec2.ap-southeast-4.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Mumbai)      | ap-south-1     | ec2.ap-south-1.amazonaws.com<br>ec2.ap-south-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (New Zealand) | ap-southeast-6 | ec2.ap-southeast-6.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Osaka)       | ap-northeast-3 | ec2.ap-northeast-3.amazonaws.com                                                                  | HTTP and HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | ec2.ap-northeast-2.amazonaws.com<br>ec2.ap-northeast-2.api.aws                                    | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Singapore)   | ap-southeast-1 | ec2.ap-southeast-1.amazonaws.com<br>ec2.ap-southeast-1.api.aws                                    | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Sydney)      | ap-southeast-2 | ec2.ap-southeast-2.amazonaws.com<br>ec2.ap-southeast-2.api.aws                                    | HTTP and HTTPS<br>HTTPS          |
| Asia Pacific (Taipei)      | ap-east-2      | ec2.ap-east-2.amazonaws.com                                                                       | HTTPS                            |
| Asia Pacific (Thailand)    | ap-southeast-7 | ec2.ap-southeast-7.amazonaws.com                                                                  | HTTPS                            |
| Asia Pacific (Tokyo)       | ap-northeast-1 | ec2.ap-northeast-1.amazonaws.com<br>ec2.ap-northeast-1.api.aws                                    | HTTP and HTTPS<br>HTTPS          |
| Canada (Central)           | ca-central-1   | ec2.ca-central-1.amazonaws.com<br>ec2-fips.ca-central-1.amazonaws.com<br>ec2.ca-central-1.api.aws | HTTP and HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | ec2.ca-west-1.amazonaws.com<br>ec2-fips.ca-west-1.amazonaws.com                                   | HTTPS<br>HTTPS                   |
| Europe (Frankfurt)         | eu-central-1   | ec2.eu-central-1.amazonaws.com<br>ec2.eu-central-1.api.aws                                        | HTTP and HTTPS<br>HTTPS          |
| Europe (Ireland)           | eu-west-1      | ec2.eu-west-1.amazonaws.com<br>ec2.eu-west-1.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| Europe (London)            | eu-west-2      | ec2.eu-west-2.amazonaws.com<br>ec2.eu-west-2.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| Europe (Milan)             | eu-south-1     | ec2.eu-south-1.amazonaws.com<br>ec2.eu-south-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Europe (Paris)             | eu-west-3      | ec2.eu-west-3.amazonaws.com<br>ec2.eu-west-3.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| Europe (Spain)             | eu-south-2     | ec2.eu-south-2.amazonaws.com                                                                      | HTTPS                            |
| Europe (Stockholm)         | eu-north-1     | ec2.eu-north-1.amazonaws.com<br>ec2.eu-north-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Europe (Zurich)            | eu-central-2   | ec2.eu-central-2.amazonaws.com                                                                    | HTTPS                            |
| Israel (Tel Aviv)          | il-central-1   | ec2.il-central-1.amazonaws.com                                                                    | HTTPS                            |
| Mexico (Central)           | mx-central-1   | ec2.mx-central-1.amazonaws.com                                                                    | HTTPS                            |
| Middle East (Bahrain)      | me-south-1     | ec2.me-south-1.amazonaws.com<br>ec2.me-south-1.api.aws                                            | HTTP and HTTPS<br>HTTPS          |
| Middle East (UAE)          | me-central-1   | ec2.me-central-1.amazonaws.com                                                                    | HTTPS                            |
| South America (São Paulo)  | sa-east-1      | ec2.sa-east-1.amazonaws.com<br>ec2.sa-east-1.api.aws                                              | HTTP and HTTPS<br>HTTPS          |
| AWS GovCloud (US-East)     | us-gov-east-1  | ec2.us-gov-east-1.amazonaws.com<br>ec2.us-gov-east-1.api.aws                                      | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | ec2.us-gov-west-1.amazonaws.com<br>ec2.us-gov-west-1.api.aws                                      | HTTPS<br>HTTPS                   |

If you specify the general endpoint (ec2.amazonaws.com),
Amazon EC2 directs your request to the endpoint for `us-east-1`.

## Service quotas

###### Amazon EC2

The following are the quotas for Amazon EC2.

| Name                             | Default | Adjustable                                                                                                                                                                 | Description                                                                                                                                                                                                                                                                                                                       |
| -------------------------------- | ------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Amazon FPGA images (AFIs)        | 100     | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8FBBDF0C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-8FBBDF0C") | The maximum number of available Amazon FPGA images (AFIs) that you can own in this Region.                                                                                                                                                                                                                                        |
| AMI sharing                      | 1,000   | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-70015FFA "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-70015FFA") | The maximum number of entities (organizations, organizational units, and accounts) that an AMI can be shared with in this Region. Note that if you share an AMI with an organization, the number of accounts in the organization does not count towards the quota.                                                                |
| AMIs                             | 50,000  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B665C33B "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-B665C33B") | The maximum number of public and private AMIs allowed in this Region. These include available, disabled, and pending AMIs, and AMIs in the Recycle Bin.                                                                                                                                                                           |
| EC2-VPC Elastic IPs              | 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0263D0A3 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0263D0A3") | The maximum number of Elastic IP addresses that you can allocate for EC2-VPC in this Region.                                                                                                                                                                                                                                      |
| Launch template versions         | 10,000  | No                                                                                                                                                                         | Maximum number of launch template versions per launch template per Region per account.                                                                                                                                                                                                                                            |
| Launch templates                 | 5,000   | No                                                                                                                                                                         | Maximum number of launch templates per Region per account.<br>For more information, see [Launch template restrictions](../../../AWSEC2/latest/UserGuide/launch-template-restrictions.md "../../../AWSEC2/latest/UserGuide/launch-template-restrictions.md").                                                                      |
| New Reserved Instances per month | 20      | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D0B7243C "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-D0B7243C") | The maximum number of Reserved Instances (RIs) that you can purchase per month in the current account. For regional RIs, this is the maximum number of RIs that you can purchase for the current Region. For zonal RIs, this is the maximum number of RIs that you can purchase for each Availability Zone in the current Region. |
| Public AMIs                      | 5       | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0E3CBAB9 "https://console.aws.amazon.com/servicequotas/home/services/ec2/quotas/L-0E3CBAB9") | The maximum number of public AMIs, including public AMIs in the Recycle Bin, allowed in this Region.                                                                                                                                                                                                                              |

###### Instance types

For details, see [Quotas](../../../ec2/latest/instancetypes/ec2-instance-quotas.md "../../../ec2/latest/instancetypes/ec2-instance-quotas.md") in the _Amazon EC2 Instance Types_ guide.

###### EC2 Fast Launch

The following quotas are for EC2 Fast Launch.

| Name                       | Default                   | Adjustable                                                                                                                                                                                     | Description                                                                                                                                                                                                                                                                                                                                         |
| -------------------------- | ------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Parallel instance launches | Each supported Region: 40 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/ec2fastlaunch/quotas/L-DC79B53E "https://console.aws.amazon.com/servicequotas/home/services/ec2fastlaunch/quotas/L-DC79B53E") | A setting that you configure for the EC2 Fast Launch feature that defines the maximum number of Windows instances it can launch at the same time to create pre-provisioned snapshots in the owner’s account in the current Region. For more information, see https://docs.aws.amazon.com/AWSEC2/latest/WindowsGuide/win-ami-config-fast-launch.html |

###### VM Import/Export

The following quotas are for VM Import/Export.

| Name                                                                                 | Default                   | Adjustable                                                                                                                                                                                       | Description                                                                                                                                                              |
| ------------------------------------------------------------------------------------ | ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| Concurrent task limit for ImportImage, ImportSnapshot, and ExportImage               | Each supported Region: 20 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vmimportexport/quotas/L-66ABAAD5 "https://console.aws.amazon.com/servicequotas/home/services/vmimportexport/quotas/L-66ABAAD5") | The maximum number of concurrent tasks for a given account initiated by the following VM Import/Export APIs: ImportImage, ImportSnapshot, and ExportImage.               |
| Concurrent task limit for ImportInstance, ImportVolume, and CreateInstanceExportTask | Each supported Region: 5  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/vmimportexport/quotas/L-0994E50B "https://console.aws.amazon.com/servicequotas/home/services/vmimportexport/quotas/L-0994E50B") | The maximum number of concurrent tasks for a given account initiated by the following VM Import/Export APIs: ImportInstance, ImportVolume, and CreateInstanceExportTask. |
