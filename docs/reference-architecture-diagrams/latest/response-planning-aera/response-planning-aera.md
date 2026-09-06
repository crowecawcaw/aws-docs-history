

# Response Planning on AWS using Aera
<a name="response-planning-aera"></a>

Publication date: **November 4, 2022 ([Diagram history](#aera-history))**

With this architecture, you can explore options for ingesting data and using AWS services in an Aera Response Planning solution. You can connect SaaS apps, an enterprise resource planning (ERP) or customer relationship management (CRM) system, and file shares to the Aera platform.

## Architecture diagram
<a name="aera-diagram"></a>

![Data flowing from various sources through AWS services into the Aera SaaS solution and an AWS data lake for analytics and ML.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/response-planning-aera/images/response-planning-on-aws-using-aera-ra.png)


The following steps describe the architecture:

1. Various sources feed data into the Aera Response Planning solution, including SaaS apps, an ERP or CRM system, and file shares.

1. You can ingest data into the response planning SaaS solution by using native Aera APIs and SSH File Transfer Protocol (SFTP).

1. You can also ingest data into your AWS account. Service selection depends on the source. Use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) for SQL and NoSQL. Use [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/) for a transportation management system (TMS), order management system (OMS), yard management system (YMS), or SaaS. Use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/) or [AWS Transfer Family](https://docs.aws.amazon.com/transfer/latest/userguide/) for a file share.

1. Store ingested data in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) in your AWS account.

1. You can batch-ingest AWS customer account data in Amazon S3 into the Aera SaaS solution by using the AWS SDK or [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) and [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/).

1. Alternatively, Aera crawlers can batch-ingest Amazon S3 data into the Aera SaaS solution.

1. Collect outbound data from the Aera SaaS solution in Amazon S3 by using Aera Write Back (Actions), standard Amazon S3 APIs, or AWS Lambda and Amazon API Gateway.

1. Integrate Aera SaaS data into an AWS data lake built with Amazon S3, [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/), IAM for permissions, and [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/).

1. Integrate outbound data in Amazon S3 for analytics by using [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) and [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/).

1. Integrate outbound data in Amazon S3 for machine learning by using [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) and [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/).

## Further reading
<a name="aera-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="aera-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#aera-history) | Reference architecture diagram first published. | November 4, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.