

# Account and Security Strategy for the Serverless Data Platform
<a name="account-security-data-platform"></a>

Publication date: **December 21, 2020 ([Diagram history](#account-security-history))**

A multi-account strategy is a best practice for resource and security isolation. An analytics architecture demands data governance with high security standards. You must grant correct access levels to users across multiple accounts.

This architecture shows how to organize AWS accounts for a serverless data platform. It addresses security, governance, and access control across environments.

## Account and security strategy diagram
<a name="account-security-diagram"></a>

![Multi-account security architecture for a serverless data platform on AWS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/account-security-data-platform/images/travel-hospitality-account-security-ra.png)


The following steps describe the architecture:

1. The root account is the most critical account in AWS. Apply restrictive access policies to protect this account.

1. The security account maintains the overall security posture. Use it to scan for vulnerabilities across all accounts.

1. Centralized network connections from on-premises are shared with other accounts. Control communication between accounts with [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/).

1. Users interact with data and develop machine learning (ML) models with correct security and data access. Publish final models with [SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/).

1. Centralized logs monitor all accounts to audit activities. Use [CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/) for unified logging.

1. Use any tools your customers need to present data. These include third-party tools or AWS services such as [Quick](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html).

1. DevOps flows deploy code as a service and artifacts on ingestion and analytics accounts.

1. Users who need development and test analytics models work with correct security and data governance.

1. Centralized data services provide governance and API management. Run queries against petabytes of data in [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) through [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) Spectrum. Transform data with [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/). Secure repositories with [Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/).

1. Control batch or streaming ingestion that feeds the data lake. Use [Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) for real-time data streaming.

1. Common services shared with other accounts include golden AMIs and DNS management.

## Further reading
<a name="account-security-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="account-security-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#account-security-history) | Reference architecture diagram first published. | December 21, 2020 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.