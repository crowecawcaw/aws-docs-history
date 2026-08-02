# Amazon Managed Streaming for Apache Kafka endpoints and quotas

To connect programmatically to an AWS service, you use an endpoint. AWS services offer the following endpoint types
in some or all of the AWS Regions that the service supports: IPv4 endpoints, dual-stack endpoints, and FIPS endpoints.
Some services provide global endpoints. For more information, see [AWS service endpoints](rande.md "rande.md").

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.
For more information, see [AWS service quotas](aws_service_limits.md "aws_service_limits.md").

The following are the service endpoints and service quotas for this service.

## Service endpoints

| Region Name                | Region         | Endpoint                                                                                                                                           | Protocol                         |
| -------------------------- | -------------- | -------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------- |
| US East (Ohio)             | us-east-2      | kafka.us-east-2.amazonaws.com<br>kafka-api-fips.us-east-2.api.aws<br>kafka-fips.us-east-2.amazonaws.com<br>kafka-api.us-east-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US East (N. Virginia)      | us-east-1      | kafka.us-east-1.amazonaws.com<br>kafka-api-fips.us-east-1.api.aws<br>kafka-fips.us-east-1.amazonaws.com<br>kafka-api.us-east-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (N. California)    | us-west-1      | kafka.us-west-1.amazonaws.com<br>kafka-api-fips.us-west-1.api.aws<br>kafka-fips.us-west-1.amazonaws.com<br>kafka-api.us-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| US West (Oregon)           | us-west-2      | kafka.us-west-2.amazonaws.com<br>kafka-api-fips.us-west-2.api.aws<br>kafka-fips.us-west-2.amazonaws.com<br>kafka-api.us-west-2.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Africa (Cape Town)         | af-south-1     | kafka.af-south-1.amazonaws.com<br>kafka-api.af-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Hong Kong)   | ap-east-1      | kafka.ap-east-1.amazonaws.com<br>kafka-api.ap-east-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Hyderabad)   | ap-south-2     | kafka.ap-south-2.amazonaws.com<br>kafka-api.ap-south-2.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (Jakarta)     | ap-southeast-3 | kafka.ap-southeast-3.amazonaws.com<br>kafka-api.ap-southeast-3.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Malaysia)    | ap-southeast-5 | kafka.ap-southeast-5.amazonaws.com<br>kafka-api.ap-southeast-5.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Melbourne)   | ap-southeast-4 | kafka.ap-southeast-4.amazonaws.com<br>kafka-api.ap-southeast-4.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Mumbai)      | ap-south-1     | kafka.ap-south-1.amazonaws.com<br>kafka-api.ap-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Asia Pacific (New Zealand) | ap-southeast-6 | kafka.ap-southeast-6.amazonaws.com<br>kafka-api.ap-southeast-6.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Osaka)       | ap-northeast-3 | kafka.ap-northeast-3.amazonaws.com<br>kafka-api.ap-northeast-3.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Seoul)       | ap-northeast-2 | kafka.ap-northeast-2.amazonaws.com<br>kafka-api.ap-northeast-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Singapore)   | ap-southeast-1 | kafka.ap-southeast-1.amazonaws.com<br>kafka-api.ap-southeast-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Sydney)      | ap-southeast-2 | kafka.ap-southeast-2.amazonaws.com<br>kafka-api.ap-southeast-2.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Taipei)      | ap-east-2      | kafka.ap-east-2.amazonaws.com<br>kafka-api.ap-east-2.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Asia Pacific (Thailand)    | ap-southeast-7 | kafka.ap-southeast-7.amazonaws.com<br>kafka-api.ap-southeast-7.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Asia Pacific (Tokyo)       | ap-northeast-1 | kafka.ap-northeast-1.amazonaws.com<br>kafka-api.ap-northeast-1.api.aws                                                                             | HTTPS<br>HTTPS                   |
| Canada (Central)           | ca-central-1   | kafka.ca-central-1.amazonaws.com<br>kafka-api-fips.ca-central-1.api.aws<br>kafka-fips.ca-central-1.amazonaws.com<br>kafka-api.ca-central-1.api.aws | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Canada West (Calgary)      | ca-west-1      | kafka.ca-west-1.amazonaws.com<br>kafka-api-fips.ca-west-1.api.aws<br>kafka-fips.ca-west-1.amazonaws.com<br>kafka-api.ca-west-1.api.aws             | HTTPS<br>HTTPS<br>HTTPS<br>HTTPS |
| Europe (Frankfurt)         | eu-central-1   | kafka.eu-central-1.amazonaws.com<br>kafka-api.eu-central-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Europe (Ireland)           | eu-west-1      | kafka.eu-west-1.amazonaws.com<br>kafka-api.eu-west-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Europe (London)            | eu-west-2      | kafka.eu-west-2.amazonaws.com<br>kafka-api.eu-west-2.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Milan)             | eu-south-1     | kafka.eu-south-1.amazonaws.com<br>kafka-api.eu-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Paris)             | eu-west-3      | kafka.eu-west-3.amazonaws.com<br>kafka-api.eu-west-3.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| Europe (Spain)             | eu-south-2     | kafka.eu-south-2.amazonaws.com<br>kafka-api.eu-south-2.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Stockholm)         | eu-north-1     | kafka.eu-north-1.amazonaws.com<br>kafka-api.eu-north-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Europe (Zurich)            | eu-central-2   | kafka.eu-central-2.amazonaws.com<br>kafka-api.eu-central-2.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Israel (Tel Aviv)          | il-central-1   | kafka.il-central-1.amazonaws.com<br>kafka-api.il-central-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Mexico (Central)           | mx-central-1   | kafka.mx-central-1.amazonaws.com<br>kafka-api.mx-central-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| Middle East (Bahrain)      | me-south-1     | kafka.me-south-1.amazonaws.com<br>kafka-api.me-south-1.api.aws                                                                                     | HTTPS<br>HTTPS                   |
| Middle East (UAE)          | me-central-1   | kafka.me-central-1.amazonaws.com<br>kafka-api.me-central-1.api.aws                                                                                 | HTTPS<br>HTTPS                   |
| South America (São Paulo)  | sa-east-1      | kafka.sa-east-1.amazonaws.com<br>kafka-api.sa-east-1.api.aws                                                                                       | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-East)     | us-gov-east-1  | kafka.us-gov-east-1.amazonaws.com<br>kafka-api.us-gov-east-1.api.aws                                                                               | HTTPS<br>HTTPS                   |
| AWS GovCloud (US-West)     | us-gov-west-1  | kafka.us-gov-west-1.amazonaws.com<br>kafka-api.us-gov-west-1.api.aws                                                                               | HTTPS<br>HTTPS                   |

## Service quotas

| Name                                  | Default                    | Adjustable                                                                                                                                                                     | Description                                                                  |
| ------------------------------------- | -------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ---------------------------------------------------------------------------- |
| Number of brokers per KRaft cluster   | Each supported Region: 60  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-03FD6822 "https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-03FD6822") | The maximum number of brokers that a KRaft cluster can contain.              |
| Number of brokers per account         | Each supported Region: 90  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-EDD31C36 "https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-EDD31C36") | The maximum number of brokers that can be created per account.               |
| Number of brokers per cluster         | Each supported Region: 30  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-FAB9E493 "https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-FAB9E493") | The maximum number of brokers that a cluster can contain.                    |
| Number of configurations per account  | Each supported Region: 100 | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-B2FDE22A "https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-B2FDE22A") | The maximum number of custom configurations that can be created per account. |
| Number of data channels per cluster   | Each supported Region: 50  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-9B45E609 "https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-9B45E609") | The maximum number of data channels that can be created per cluster.         |
| Number of replicators per account     | Each supported Region: 15  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-8F940D28 "https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-8F940D28") | The maximum number of replicators that can be created per account.           |
| Number of revisions per configuration | Each supported Region: 50  | [Yes](https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-36D29E8C "https://console.aws.amazon.com/servicequotas/home/services/kafka/quotas/L-36D29E8C") | The maximum number of revisions that can be made to a custom configuration.  |
