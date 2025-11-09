# Cost

You are responsible for the cost of the AWS services used while running this Guidance. As of September 2024, the cost for running this Guidance with the default settings in the US East (N. Virginia) Region is approximately **$0.50-2.00 per hour** depending on fleet size and deployment phases.

The estimated monthly cost for running this guidance varies based on deployment phases and fleet size:

**Phase 1-2 (Basic Fleet Management)**: $200-400/month for 100-500 vehicles

**Phase 3-6 (Full Telemetry Pipeline)**: $500-2,000/month for 100-1,000 vehicles

We recommend creating a [budget](https://alpha-docs-aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-create.html "https://alpha-docs-aws.amazon.com/awsaccountbilling/latest/aboutv2/budgets-create.html") through [AWS Cost Explorer](http://aws.amazon.com/aws-cost-management/aws-cost-explorer/ "http://aws.amazon.com/aws-cost-management/aws-cost-explorer/") to help manage costs.

## Sample cost table

| AWS service                   | Dimensions                   | Cost [USD] |
| ----------------------------- | ---------------------------- | ---------- |
| Amazon MSK                    | 3 x kafka.m5.large brokers   | $350/month |
| Amazon Kinesis Data Analytics | 4 Flink apps, 8 KPUs         | $400/month |
| Amazon DynamoDB               | 1,000 RCU/WCU provisioned    | $150/month |
| AWS IoT Core                  | 1M messages/month            | $5/month   |
| Amazon S3                     | 100GB storage, 10GB transfer | $25/month  |
| Amazon CloudFront             | 100GB data transfer          | $15/month  |
