# DevOps Guru coverage

DevOps Guru addresses and creates insights for a number of different AWS services. For each service that DevOps Guru creates insights for,
DevOps Guru displays a variety of analyzed metrics and generated insights.

Example use case for reactive insights:

| Service Name | Use Case                                                                                                                                                                                                      | Examples                                                                                                                                                                                                                                                                                                                                                                           | Metrics               |
| ------------ | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------- |
| AWS Lambda   | Detect latency or duration anomalies for Lambda functions caused by various root causes like cold starts, increased requests, downstream throttling, or code deployments. Recommend ways to quickly mitigate. | Code deployment: Amazon API Gateway latency is affected by an increase in Lambda latency after a recent Lambda code deployment.<br>Downstream throttling: the operator reduced capacity on read units for DynamoDB, causing increased retries. This results in throttling.<br>Cold start: the Lambda function is under-provisioned, so Lambda takes longer when requests are made. | Duration<br>Throttles |

Example use case for proactive insights:

| Service Name    | Use Case                                                                                                                                                                                                                                                                                                                                                                                          | Metrics                   |
| --------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------- |
| Amazon DynamoDB | \*_The DynamoDB table read consumed capacity is at risk of reaching table limit._<br>• Recommended action: if you are using provisioned capacity mode, use auto scaling to actively manage throughput capacity for tables or purchase reserved capacity in advance for tables. Switch to on-demand capacity mode to pay per read request, paying only for what is used.<br>Detection time: 6 days | ConsumedReadCapacityUnits |

## Service coverage list

For some services, DevOps Guru creates reactive insights. A reactive insight identifies anomalous behavior as it
occurs. It contains anomalies with recommendations, related metrics, and events to help
you understand and address the issues now.

For some services, DevOps Guru creates proactive insights. A proactive insight lets you know about anomalous behavior
before it occurs. It contains anomalies with recommendations to help you address the
issues before they are predicted to happen.

###### DevOps Guru creates reactive insights for services such as the following:

- Amazon API Gateway
- Amazon CloudFront
- Amazon DynamoDB
- Amazon EC2

###### Note

DevOps Guru monitoring is at an Auto Scaling group level,
and not at a single instance level.

- Amazon ECS
- Amazon EKS
- AWS Elastic Beanstalk
- Elastic Load Balancing
- Amazon Kinesis
- AWS Lambda
- Amazon OpenSearch Service
- Amazon RDS
- Amazon Redshift
- Amazon Route 53
- Amazon S3
- Amazon SageMaker AI
- AWS Step Functions
- Amazon SNS
- Amazon SQS
- Amazon SWF
- Amazon VPC

###### DevOps Guru creates proactive insights for services such as the following:

- Amazon DynamoDB
- Amazon Kinesis
- AWS Lambda
- Amazon RDS
- Amazon SQS
