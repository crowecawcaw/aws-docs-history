# Amazon CodeGuru Profiler endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name              | Region         | Endpoint                                       | Protocol |
| ------------------------ | -------------- | ---------------------------------------------- | -------- |
| US East (Ohio)           | us-east-2      | codeguru-profiler.us-east-2.amazonaws.com      | HTTPS    |
| US East (N. Virginia)    | us-east-1      | codeguru-profiler.us-east-1.amazonaws.com      | HTTPS    |
| US West (Oregon)         | us-west-2      | codeguru-profiler.us-west-2.amazonaws.com      | HTTPS    |
| Asia Pacific (Singapore) | ap-southeast-1 | codeguru-profiler.ap-southeast-1.amazonaws.com | HTTPS    |
| Asia Pacific (Sydney)    | ap-southeast-2 | codeguru-profiler.ap-southeast-2.amazonaws.com | HTTPS    |
| Asia Pacific (Tokyo)     | ap-northeast-1 | codeguru-profiler.ap-northeast-1.amazonaws.com | HTTPS    |
| Europe (Frankfurt)       | eu-central-1   | codeguru-profiler.eu-central-1.amazonaws.com   | HTTPS    |
| Europe (Ireland)         | eu-west-1      | codeguru-profiler.eu-west-1.amazonaws.com      | HTTPS    |
| Europe (London)          | eu-west-2      | codeguru-profiler.eu-west-2.amazonaws.com      | HTTPS    |
| Europe (Stockholm)       | eu-north-1     | codeguru-profiler.eu-north-1.amazonaws.com     | HTTPS    |

## Service quotas

| Name                                               | Default                    | Adjustable                                                                                                                                                                                             | Description                                                     |
| -------------------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | --------------------------------------------------------------- |
| Number of profiling groups per account and region. | Each supported Region: 500 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/codeguru-profiler/quotas/L-DA8D4E8D "https://console.aws.amazon.com/servicequotas/home/services/codeguru-profiler/quotas/L-DA8D4E8D") | The maximum number of profiling groups per account, per region. |
