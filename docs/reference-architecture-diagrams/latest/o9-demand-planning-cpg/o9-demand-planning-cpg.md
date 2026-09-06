

# o9 Demand Planning for CPG
<a name="o9-demand-planning-cpg"></a>

Publication date: **July 8, 2022 ([Diagram history](#o9-history))**

With this architecture, you can review options for ingesting data and using AWS services in an o9 demand planning solution. Consumer packaged goods (CPG) companies ingest data from SQL and NoSQL systems, enterprise resource planning (ERP) or customer relationship management (CRM) systems, SaaS applications, and streaming sources.

## o9 demand planning diagram
<a name="o9-diagram"></a>

![Data flowing from SQL, ERP, CRM, and streaming sources through AWS ingestion services into Amazon Simple Storage Service, with feeds to the o9 SaaS solution and AWS ML services.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/o9-demand-planning-cpg/images/o9-demand-planning-cpg.png)


The following steps describe the architecture:

1. SQL and NoSQL systems, ERP or CRM systems, SaaS applications, file shares, and streaming sources feed data into demand planning. An Amazon.com Selling Partner API provides access to vendor sales orders and product catalogs.

1. Data can be ingested into the o9 SaaS solution by using native o9 APIs and SSH File Transfer Protocol (SFTP). Alternatively, data can be ingested into an AWS account. You use [AWS Database Migration Service](https://docs.aws.amazon.com/dms/latest/userguide/) for SQL and NoSQL, [Amazon AppFlow](https://docs.aws.amazon.com/appflow/latest/userguide/) for ERP, CRM, or SaaS, or [Kinesis](https://docs.aws.amazon.com/kinesis/latest/dev/) for streaming data.

1. [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) stores the ingested data.

1. Streaming data can also be fed to the o9 SaaS solution by using native REST APIs. Alternatively, store it in Amazon S3 by using Kinesis Data Streams through an AWS SDK or Lambda.

1. Third-party data from providers such as TransUnion or Reuters can be imported by using AWS Data Exchange.

1. AWS customer account data in Amazon S3 can be batch-ingested into the o9 SaaS solution by using [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) through an AWS SDK or Lambda.

1. Data within the o9 SaaS solution and AWS customer account are shared by using native o9 APIs and optionally Lambda.

1. Outbound data is collected from the o9 SaaS solution in Amazon S3. You use this data for analytics and artificial intelligence and machine learning (AI/ML) workloads.

1. AWS AI/ML services such as [Amazon Forecast](https://docs.aws.amazon.com/forecast/latest/dg/) and [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) build, train, and deploy ML models. These complement o9 SaaS solution ML capabilities.

1. AWS analytics services such as Amazon EMR and Amazon Redshift provide big data processing and warehousing.

1. You can integrate data from the o9 SaaS solution to an AWS data lake. [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) provides governance with Amazon S3, AWS Glue Data Catalog, and IAM for permissions.

## Further reading
<a name="o9-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture/)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="o9-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#o9-history) | Reference architecture diagram first published. | July 8, 2022 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.