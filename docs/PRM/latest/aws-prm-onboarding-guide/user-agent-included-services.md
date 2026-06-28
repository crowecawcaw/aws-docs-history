# Included AWS Services

The following AWS services are supported for User Agent string implementation. User Agent strings must be included in all regular AWS API/CLI calls to ensure proper revenue attribution.

For detailed information including specific API actions and regions supported for each service, download the [User Agent Included Services and API Actions (CSV)](samples/user-agent-included-services.zip.md "samples/user-agent-included-services.zip.md").

User Agent String Included Services| Service Name | Product Service Code | Notes |
| --- | --- | --- |
| AWS Certificate Manager | AWSCertificateManager | None |
| Amazon CloudFront | AmazonCloudFront | None |
| Amazon CloudWatch | AmazonCloudWatch | Alarms and Logs |
| AWS CodeBuild | CodeBuild | None |
| AWS Direct Connect | AWSDirectConnect | None |
| AWS Directory Service | AWSDirectoryService | None |
| Amazon DynamoDB Accelerator (DAX) | AmazonDAX | None |
| Amazon EC2 | AmazonEC2 | None |
| Amazon ECS | AmazonECS | None |
| Amazon ElastiCache | AmazonElastiCache | None |
| Elastic Load Balancing (ELB) | AWSELB | None |
| Amazon EMR | ElasticMapReduce | None |
| Amazon EventBridge | AmazonEventBridge | None |
| Amazon Kinesis | AmazonKinesis | Data Streams and Data Firehose |
| AWS License Manager | AWSLicenseManager | None |
| Amazon Lightsail | AmazonLightsail | None |
| Amazon MemoryDB for Redis | AmazonMemoryDB | None |
| Amazon OpenSearch Service | AmazonES | None |
| Amazon RDS | AmazonRDS | None |
| Amazon Route 53 | AmazonRoute53 | None |
| Amazon S3 | AmazonS3 | None |
| AWS Shield | AWSShield | None |
| AWS WAF | awswaf | None |
| Amazon WorkSpaces | AmazonWorkSpaces | None |

###### Note

Monthly API operations on resources are required for attribution to occur.

###### Note

Partner Revenue Measurement intends to support all AWS services. We recommend that you instrument PRM on all AWS services and resources that your partner solution interacts with to avoid on-going operational changes as service coverage expands. At this time, revenue attribution data is surfaced for the services listed above. Any partial spend captured on services not listed above is aggregated as "Other".
