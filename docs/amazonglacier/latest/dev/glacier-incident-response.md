**This page is only for existing customers of the Amazon Glacier service using Vaults and the original REST API from 2012.**

If you're looking for archival storage solutions, we recommend using the Amazon Glacier storage classes in Amazon S3, S3 Glacier Instant Retrieval, S3 Glacier Flexible Retrieval, and S3 Glacier Deep Archive. To learn more about these storage options, see [Amazon Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/").

Amazon Glacier (original standalone vault-based service) will no longer accept new customers starting December 15, 2025, with no impact to existing customers. Amazon Glacier is a standalone service with its own APIs that stores data in vaults and is distinct from Amazon S3 and the Amazon S3 Glacier storage classes. Your existing data will remain secure and accessible in Amazon Glacier indefinitely. No migration is required. For low-cost, long-term archival storage, AWS recommends the [Amazon S3 Glacier storage classes](https://aws.amazon.com/s3/storage-classes/glacier/ "https://aws.amazon.com/s3/storage-classes/glacier/"), which deliver a superior customer experience with S3 bucket-based APIs, full AWS Region availability, lower costs, and AWS service integration. If you want enhanced capabilities, consider migrating to Amazon S3 Glacier storage classes by using our [AWS Solutions Guidance for transferring data from Amazon Glacier vaults to Amazon S3 Glacier storage classes](https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/ "https://aws.amazon.com/solutions/guidance/data-transfer-from-amazon-s3-glacier-vaults-to-amazon-s3/").

# Logging and Monitoring in Amazon Glacier

Monitoring is an important part of maintaining the reliability, availability, and
performance of Amazon Glacier (Amazon Glacier) and your AWS solutions. You should collect monitoring data
from all of the parts of your AWS solution so that you can more easily identify and debug the source of a failure if one occurs. AWS provides the following tools for monitoring your Amazon Glacier resources
and responding to potential incidents:

**Amazon CloudWatch Alarms**
When using Amazon Glacier via Amazon S3, you can use Amazon CloudWatch alarms to watch a single metric over a time period that you specify. If the
metric exceeds a given threshold, a notification is sent to an Amazon SNS topic or
AWS Auto Scaling policy. CloudWatch alarms do not invoke actions because they are in a
particular state. Rather the state must have changed and been maintained for a
specified number of periods. For more information, see [Monitoring Metrics with Amazon CloudWatch](../../../AmazonS3/latest/dev/cloudwatch-monitoring.md "../../../AmazonS3/latest/dev/cloudwatch-monitoring.md").

**AWS CloudTrail Logs**
CloudTrail provides a record of actions taken by a user, role, or an AWS service in Amazon Glacier. CloudTrail captures all API calls for Amazon Glacier as events,
including calls from the Amazon Glacier console and from code calls to the Amazon Glacier APIs. For more information, see [Logging Amazon Glacier API Calls with AWS CloudTrail](audit-logging.md "audit-logging.md").

**AWS Trusted Advisor**
Trusted Advisor draws upon best practices learned from serving hundreds of thousands of AWS customers. Trusted Advisor inspects your AWS environment and then makes recommendations when opportunities exist to save money, improve system availability and performance, or help close security gaps. All AWS customers have access to five Trusted Advisor checks. Customers with a Business or Enterprise support plan can view all Trusted Advisor checks.

For more information, see [AWS Trusted Advisor](../../../awssupport/latest/user/getting-started.md#trusted-advisor "../../../awssupport/latest/user/getting-started.md#trusted-advisor") in the _Support User Guide_.
