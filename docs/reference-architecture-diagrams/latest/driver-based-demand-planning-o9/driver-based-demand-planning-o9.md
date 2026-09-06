

# Guidance for Driver-based Demand Planning with o9
<a name="driver-based-demand-planning-o9"></a>

Publication date: **April 25, 2022 ([Diagram history](#o9-driver-history))**

With this architecture, you can review options for ingesting data and using AWS services in an [o9](https://o9solutions.com/) solution. You can connect SQL and NoSQL systems, enterprise resource planning (ERP) or customer relationship management (CRM) systems, SaaS applications, file shares, and streaming sources.

## Architecture diagram
<a name="o9-driver-diagram"></a>

![Data flowing from various sources through AWS ingestion services into Amazon S3 and the o9 SaaS solution for demand planning.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/driver-based-demand-planning-o9/images/guidance-for-driver-based-demand-planning-with-o9.png)


The following steps describe the architecture:

1. Various sources feed data into demand planning software, such as SQL and NoSQL systems, ERP or CRM systems, other SaaS applications, file shares, and streaming sources like social media, smart devices, and logs.

1. You can ingest data into the o9 SaaS solution by using native o9 APIs and SSH File Transfer Protocol (SFTP).

1. You can also ingest data into your AWS account. Service selection depends on the source. Use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) for SQL and NoSQL. Use [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/) for ERP, CRM, or SaaS. Use [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/) for a file share. Use [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/), [Amazon MSK](https://docs.aws.amazon.com/msk/latest/developerguide/), and [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/) for streaming feeds.

1. Store ingested data in [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) in your AWS account.

1. Streaming data can feed the o9 SaaS solution by using o9 REST APIs. Alternatively, store it in Amazon S3 through Amazon Kinesis Data Streams by using the AWS SDK or [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/).

1. You can subscribe to and use third-party data (such as TransUnion, IMDb, or Reuters) in the AWS Cloud with AWS Data Exchange.

1. You can batch-ingest AWS customer account data in Amazon S3 into the o9 SaaS solution by using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) through the AWS SDK or AWS Lambda.

1. Data within the o9 SaaS solution and the AWS customer account can be shared by using o9 APIs and optional AWS Lambda.

1. Collect outbound data from the o9 SaaS solution in Amazon S3 by using standard Amazon S3 APIs or AWS Lambda for analytics and AI/ML workloads.

1. Use [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) to build, train, and deploy ML models that complement the o9 SaaS solution.

1. Use [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/) and [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/dg/) for big data processing and warehousing.

1. Integrate o9 SaaS data into a data lake built with Amazon S3, AWS Glue, IAM, and [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/).

## Further reading
<a name="o9-driver-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="o9-driver-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#o9-driver-history) | Reference architecture diagram first published. | April 25, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.