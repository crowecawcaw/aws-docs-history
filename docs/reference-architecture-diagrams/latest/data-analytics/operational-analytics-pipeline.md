

# Operational analytics pipeline on AWS
<a name="operational-analytics-pipeline"></a>

Publication date: **January 1, 2021 ([Diagram history](diagram-history.md))**

With this architecture, you can perform operational analytics in batch and real time. You use log information from operational data sources such as [AWS CloudTrail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/) and Amazon VPC flow logs. You visualize operational insights in an OpenSearch dashboard and distribute alerts through [Amazon Simple Notification Service](https://docs.aws.amazon.com/sns/latest/dg/) (Amazon SNS).

## Operational analytics pipeline on AWS diagram
<a name="oap-diagram"></a>

![Architecture diagram for an operational analytics pipeline on AWS with CloudWatch, Firehose, OpenSearch Service, and Lambda.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/build-operational-analytics-pipeline-on-AWS-modern-data-architecture.png)


The following steps describe the architecture:

1. Logs stream to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/) from various data sources. Example sources include AWS CloudTrail and Amazon VPC flow logs.

1. [Amazon Managed Service for Apache Flink](https://docs.aws.amazon.com/managed-flink/latest/java/) receives logs intended for real-time analysis.

1. An [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket receives logs intended for batch processing. This bucket serves as a backup for storing the raw logs.

1. Amazon CloudWatch subscription filters stream log data to [Amazon Data Firehose](https://docs.aws.amazon.com/firehose/latest/dev/) for distribution.

1. Amazon Managed Service for Apache Flink derives metrics and sends them to a [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function for processing. The Lambda function transforms the metrics and ingests them into [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/). If a condition requires alerting, the Lambda function publishes a message to Amazon SNS for distribution.

1. [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) collects the logs from Amazon S3 and performs bulk processing, transformation, and analysis. AWS Glue uses the Amazon OpenSearch Service connector to ingest the results into Amazon OpenSearch Service.

1. An OpenSearch dashboard visualizes the metrics from Amazon OpenSearch Service.

1. Amazon SNS notifies consumers of alerts by publishing to email and SMS notification topics.

## Further reading
<a name="oap-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)