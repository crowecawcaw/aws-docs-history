

# Connected Mobility Data Lake

Publication date: **January 1, 2023 ([Diagram history](diagram-history.md))**

This architecture enables you to create connected mobility data products and democratize data access with a serverless data mesh architecture.

## Connected Mobility Data Lake diagram
<a name="connected-mobility-data-lake-diagram1"></a>

![Reference architecture diagram showing how to create connected mobility data products and democratize data access with a serverless data mesh architecture](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/automotive/images/connected-mobility-data-lake.png)


1. Ingest vehicle data through a network provider to [AWS IoT Core](https://docs.aws.amazon.com/iot/latest/developerguide/). Ingest factory data through [Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/) and [Amazon Kinesis Data Streams](https://docs.aws.amazon.com/streams/latest/dev/). Sync a customer relationship management (CRM) database to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3) with [AWS DataSync](https://docs.aws.amazon.com/datasync/latest/userguide/).

1. Forward messages from AWS IoT Core based on rules and use [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) to process messages and ingest into [Amazon DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/) and Amazon S3. Use DynamoDB to store attributes and vehicle status.

1. Store raw data in Amazon S3 . 

1. An Amazon S3 event initiates AWS Lambda for data processing, which initiates an [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/) batch job for data preparation. 

1. Store datasets that you want to present as a product in an Amazon S3 bucket. Data producers are responsible for data quality and format. 

1. Create [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/) Data Catalog entities using an [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/) crawler job in a producer account. The Data Catalog is [replicated](https://aws.amazon.com/premiumsupport/knowledge-center/glue-data-catalog-cross-account-access/) in a central data governance account to make data discoverable.

1. Grant roles to a data producer to manage schema changes and permission data transformations (alter, delete, update) on the central Data Catalog when it changes at the source. Propagate automatic schema changes from a producer account.

1. Depending on data consumer requests and the need to make data [visible and accessible](https://docs.aws.amazon.com/lake-formation/latest/dg/viewing-shared-resources.html) , the data owner grants AWS Lake Formation permissions in the centralized account to a consumer account. These permissions are based on direct entity sharing or tag-based access controls, which can be used to administer access through controls like data classification, cost centers, or environment.

1. [Call center applications ](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/automotive-call-center-ra.pdf) can access data from various sources in different accounts to help customers.

1. Original equipment manufacturer (OEM) departments or their partners see available data and request access to create new use cases. Data queries are done using [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/), [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/) Data Wrangler, or [Amazon Redshift Spectrum](https://docs.aws.amazon.com/redshift/latest/dg/). 

1. OEMs can give end user applications and businesses access to data using [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/) and [monetize APIs](https://aws.amazon.com/blogs/awsmarketplace/monetize-your-custom-http-apis-via-aws-data-exchange/) . 

## Further reading
<a name="connected-mobility-data-lake-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 