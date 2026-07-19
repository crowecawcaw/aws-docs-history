# Cost

As of March 2026, the cost for running this Guidance with the default settings in the US East (N. Virginia) Region is approximately **$400.00 per month** for processing 1,000 vehicles with moderate usage.

###### Note

The primary cost drivers are:

- Amazon MSK cluster (~49% of total cost)
- Amazon Managed Service for Apache Flink (~27% of total cost)
- VPC and NAT Gateway (~15% of total cost)
  The following table provides a sample cost breakdown for deploying this Guidance with the default parameters in the US East (N. Virginia) Region for one month.

| AWS Service                             | Dimensions                                      | Cost [USD]   |
| --------------------------------------- | ----------------------------------------------- | ------------ |
| Amazon MSK                              | 3 kafka.m5.large brokers, 100 GB storage each   | $194.00      |
| Amazon Managed Service for Apache Flink | 10 KPUs (1 per Flink application)               | $108.00      |
| Amazon VPC                              | NAT Gateway (2 AZs), data transfer              | $45.00       |
| AWS Lambda                              | 10M invocations, 512 MB memory                  | $20.00       |
| Amazon ElastiCache for Redis            | cache.t3.micro node                             | $12.00       |
| Amazon CloudFront                       | 100 GB data transfer                            | $8.50        |
| Amazon Location Service                 | 100K map tile requests, 10K geocoding requests  | $8.00        |
| AWS IoT Core                            | 108M messages (1,000 vehicles × 3,600 msgs/day) | $3.24        |
| Amazon DynamoDB                         | On-demand, 10 GB storage                        | $3.50        |
| Amazon API Gateway                      | 1M REST API calls per month                     | $3.50        |
| Amazon S3                               | 50 GB storage, 1M requests                      | $1.50        |
| Amazon Cognito                          | 1,000 active users (free tier)                  | $0.00        |
| **Total**                               |                                                 | **~$400.00** |

###### Note

Prices are subject to change. For full details, refer to the pricing webpage for each AWS service used in this Guidance.

**Cost Optimization Strategies**

- Use DynamoDB on-demand billing to avoid over-provisioning
- Implement S3 lifecycle policies to archive old telemetry data to S3 Glacier
- Right-size MSK broker instances based on actual throughput requirements
- Use appropriate ElastiCache node types for development vs. production environments
- Enable CloudWatch Logs retention policies to manage log storage costs
- Monitor and optimize Flink application parallelism based on workload

**Cost Scaling**

Costs scale primarily with:

- Number of vehicles and message volume (IoT Core, MSK, Flink)
- Data storage requirements (DynamoDB, S3)
- API request volume (API Gateway, Lambda)
- Map tile requests and geocoding operations (Location Service)
- Data transfer and CloudFront usage
  For 100 vehicles: ~$250/month
For 1,000 vehicles: ~$400/month
  For 10,000 vehicles: ~$1,200/month

We recommend creating a [Budget](../../../cost-management/latest/userguide/budgets-managing-costs.md "../../../cost-management/latest/userguide/budgets-managing-costs.md") through [AWS Cost Explorer](https://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "https://aws.amazon.com/aws-cost-management/aws-cost-explorer/") to help manage costs.
