# Quotas

Service quotas, also referred to as limits, are the maximum number of service resources or operations for your AWS account.

## Quotas for AWS services in this Guidance

Make sure you have sufficient quota for each of the services implemented in this guidance. For more information, see [AWS service quotas](../../../general/latest/gr/aws_service_limits.md "../../../general/latest/gr/aws_service_limits.md").

Consider the following service quotas when planning your deployment:

| Service                         | Quota                    | Adjustable |
| ------------------------------- | ------------------------ | ---------- |
| IoT Core concurrent connections | 500,000 per region       | Yes        |
| MSK cluster brokers             | 30 per cluster           | Yes        |
| Flink applications              | 50 per region            | Yes        |
| DynamoDB read/write capacity    | 40,000 RCU/WCU per table | Yes        |
