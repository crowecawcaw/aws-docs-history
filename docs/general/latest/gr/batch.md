# AWS Batch endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                       | Protocol                         |
| -------------------------- | -------------- | ------------------------------------------------------------------------------------------------------------------------------ | -------------------------------- |
| US East (Ohio)             | us-east-2      | batch.us-east-2.amazonaws.com<br>fips.batch.us-east-2.amazonaws.com<br>batch-fips.us-east-2.api.aws<br>batch.us-east-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | batch.us-east-1.amazonaws.com<br>fips.batch.us-east-1.amazonaws.com<br>batch-fips.us-east-1.api.aws<br>batch.us-east-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | batch.us-west-1.amazonaws.com<br>fips.batch.us-west-1.amazonaws.com<br>batch-fips.us-west-1.api.aws<br>batch.us-west-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | batch.us-west-2.amazonaws.com<br>fips.batch.us-west-2.amazonaws.com<br>batch-fips.us-west-2.api.aws<br>batch.us-west-2.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | batch.af-south-1.amazonaws.com<br>batch.af-south-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | batch.ap-east-1.amazonaws.com<br>batch.ap-east-1.api.aws                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | batch.ap-south-2.amazonaws.com<br>batch.ap-south-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | batch.ap-southeast-3.amazonaws.com<br>batch.ap-southeast-3.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | batch.ap-southeast-5.amazonaws.com<br>batch.ap-southeast-5.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | batch.ap-southeast-4.amazonaws.com<br>batch.ap-southeast-4.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | batch.ap-south-1.amazonaws.com<br>batch.ap-south-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | batch.ap-southeast-6.amazonaws.com<br>batch.ap-southeast-6.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | batch.ap-northeast-3.amazonaws.com<br>batch.ap-northeast-3.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | batch.ap-northeast-2.amazonaws.com<br>batch.ap-northeast-2.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | batch.ap-southeast-1.amazonaws.com<br>batch.ap-southeast-1.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | batch.ap-southeast-2.amazonaws.com<br>batch.ap-southeast-2.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | batch.ap-east-2.amazonaws.com<br>batch.ap-east-2.api.aws                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | batch.ap-southeast-7.amazonaws.com<br>batch.ap-southeast-7.api.aws                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | batch.ap-northeast-1.amazonaws.com<br>batch.ap-northeast-1.api.aws                                                             | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | batch.ca-central-1.amazonaws.com<br>batch.ca-central-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Canada West (Calgary)      | ca-west-1      | batch.ca-west-1.amazonaws.com<br>batch.ca-west-1.api.aws                                                                       | HTTPS<br>HTTPS                   |
| Europe (Frankfurt)         | eu-central-1   | batch.eu-central-1.amazonaws.com<br>batch.eu-central-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | batch.eu-west-1.amazonaws.com<br>batch.eu-west-1.api.aws                                                                       | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | batch.eu-west-2.amazonaws.com<br>batch.eu-west-2.api.aws                                                                       | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | batch.eu-south-1.amazonaws.com<br>batch.eu-south-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | batch.eu-west-3.amazonaws.com<br>batch.eu-west-3.api.aws                                                                       | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | batch.eu-south-2.amazonaws.com<br>batch.eu-south-2.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | batch.eu-north-1.amazonaws.com<br>batch.eu-north-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | batch.eu-central-2.amazonaws.com<br>batch.eu-central-2.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | batch.il-central-1.amazonaws.com<br>batch.il-central-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | batch.mx-central-1.amazonaws.com<br>batch.mx-central-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | batch.me-south-1.amazonaws.com<br>batch.me-south-1.api.aws                                                                     | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | batch.me-central-1.amazonaws.com<br>batch.me-central-1.api.aws                                                                 | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | batch.sa-east-1.amazonaws.com<br>batch.sa-east-1.api.aws                                                                       | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | batch.us-gov-east-1.amazonaws.com<br>batch-fips.us-gov-east-1.api.aws<br>batch.us-gov-east-1.api.aws                           | HTTPS<br>HTTPS<br>HTTPS          |
| AWS GovCloud (US-West)     | us-gov-west-1  | batch.us-gov-west-1.amazonaws.com<br>batch-fips.us-gov-west-1.api.aws<br>batch.us-gov-west-1.api.aws                           | HTTPS<br>HTTPS<br>HTTPS          |

## Service quotas

| Name                                         | Default                          | Adjustable | Description                                                                                       |
| -------------------------------------------- | -------------------------------- | ---------- | ------------------------------------------------------------------------------------------------- |
| Compute environment limit                    | Each supported Region: 50        | No         | Maximum number of compute environments per account, per region.                                   |
| Compute environments per job queue limit.    | Each supported Region: 3         | No         | Maximum number of compute environments per job queue.                                             |
| Job definition size limit                    | Each supported Region: 24        | No         | Maximum job definition size (for RegisterJobDefinition API operations), measured in KiB.          |
| Job dependencies limit                       | Each supported Region: 20        | No         | Maximum number of job dependencies per job.                                                       |
| Job payload size limit                       | Each supported Region: 30        | No         | Maximum job payload size (for SubmitJob API operations), measured in KiB.                         |
| Job queue limit                              | Each supported Region: 50        | No         | Maximum number of job queues per account, per region.                                             |
| Maximum array size limit                     | Each supported Region: 10,000    | No         | Maximum array size for array jobs.                                                                |
| Service Job serviceRequestPayload size       | Each supported Region: 10        | No         | Maximum serviceRequestpayload size (within SubmitServiceJob API operations), measured in KiB.     |
| Service Job total payload size               | Each supported Region: 30        | No         | Maximum total job payload size (for SubmitServiceJob API operations), measured in KiB.            |
| Service environment                          | Each supported Region: 50        | No         | Maximum number of service environments per account, per region.                                   |
| Service environments per job queue           | Each supported Region: 1         | No         | Maximum number of service environments per job queue.                                             |
| Share identifiers per job queue limit.       | Each supported Region: 500       | No         | Maximum number of share identifiers per job queue.                                                |
| Submitted state jobs limit                   | Each supported Region: 1,000,000 | No         | Maximum number of jobs in SUBMITTED state.                                                        |
| Transactions per second for SubmitJob limit  | Each supported Region: 50        | No         | Maximum number of transactions per second (TPS) for each account for SubmitJob operations.        |
| Transactions per second for SubmitServiceJob | Each supported Region: 5         | No         | Maximum number of transactions per second (TPS) for each account for SubmitServiceJob operations. |

For more information, see [Service Quotas](../../../batch/latest/userguide/service_limits.md "../../../batch/latest/userguide/service_limits.md")
in the _AWS Batch User Guide_.
