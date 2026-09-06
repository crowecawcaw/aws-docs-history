

# AWS implementation options
<a name="data-mesh-aws-options-section"></a>

AWS provides multiple approaches for implementing data mesh architectures. Use the capabilities of [analytics on AWS](https://aws.amazon.com/big-data/datalakes-and-analytics/) to build data mesh–based solutions for your organization. The analytics on AWS resource recommends several AWS services to build data mesh at low cost without compromising on performance.

Customers have adopted the following options for building a data mesh–based solution:
+ Implement data mesh by using Amazon DataZone
+ Implement data mesh by using open source frameworks on AWS such as data.all
+ Implement data mesh by using AWS Lake Formation

## Common AWS Services
<a name="common-aws-services"></a>

These three options use the following AWS services:
+  [Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) 
+  [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) 
+  [Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-what-is-emr.html) 
+  [AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/what-is-glue.html) (including AWS Glue Data Catalog and AWS Glue crawler)
+  [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) 
+  [AWS Key Management Service (AWS KMS)](https://docs.aws.amazon.com/kms/latest/developerguide/overview.html) 
+  [Amazon Kinesis](https://docs.aws.amazon.com/kinesis/) 
+  [AWS Lake Formation](https://docs.aws.amazon.com/lake-formation/latest/dg/what-is-lake-formation.html) 
+  [Amazon Managed Streaming for Apache Kafka (Amazon MSK)](https://docs.aws.amazon.com/msk/latest/developerguide/what-is-msk.html) 
+  [Amazon QuickSight](https://docs.aws.amazon.com/quicksight/latest/user/welcome.html) 
+  [Amazon Redshift](https://docs.aws.amazon.com/redshift/latest/mgmt/welcome.html) 
+  [AWS Resource Access Manager (AWS RAM)](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) 
+  [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) 
+  [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) 
+  [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) 

The Amazon DataZone option also uses [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).

The data.all and AWS Lake Formation options also use the following AWS services and resources:
+  [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) 
+  [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) 
+  [Amazon Cognito](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) 
+  [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) 
+  [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) 
+  [AWS WAF](https://docs.aws.amazon.com/waf/latest/developerguide/waf-chapter.html) 

The AWS services that you use in your implementation might differ, based on your organization’s requirements.

## Amazon DataZone
<a name="amazon-datazone"></a>

If you want to use a fully managed service, consider using Amazon DataZone to implement data mesh for your organization. Amazon DataZone is a data management service for cataloging, discovering, sharing, and governing data stored across AWS, on premises, and third-party sources. The following diagram shows a data mesh reference architecture based on Amazon DataZone.

![Multiple producer and consumer accounts with a central governance account and Amazon DataZone](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/datazone.png)


In the reference architecture, the member accounts belong to the data domains. They’re grouped into data producers and data consumers. The architecture diagram contains following components:

1. The data producers publish data products in the business catalog provided by the Amazon DataZone data portal. The data portal is hosted in the central governance account.

1. Data consumers (users) log in to the data portal by using their AWS credentials or single sign-on credentials. They can browse the catalog and search for the data products of their interest by using keywords. They can filter the search results.

1. After the data users belonging to the consumer teams find the data product of their interest, they can request access to the data. Amazon DataZone has a built-in access-management workflow that the data owner uses to review and approve the request.

1. The data consumer teams can consume the data to empower their artificial intelligence and machine learning (AI/ML), analytics and reporting, and extract, transform, and load (ETL) use cases.

## Data.all
<a name="data-all"></a>

If you understand open source and want to build and manage your own solution, consider using open source frameworks such as [data.all](https://awslabs.github.io/aws-dataall/). Data.all is a modern data marketplace that supports collaboration among diverse users. Data.all simplifies data discovery, sharing, and granular data access management while builders use the AWS portfolio of data and analytics services. The following diagram shows a data mesh reference architecture based on data.all.

![Multiple producer and consumer accounts with a central governance account and data.all](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/data-all.png)


The architecture diagram contains following components:

1. The data producers publish data products in the catalog provided by the data.all frontend. The frontend and backend of data.all are hosted in the central governance account.

1. Data consumers (users) log in to the data.all frontend by using their single sign-on or Amazon Cognito credentials. They can browse the catalog and search for the data products of their interest. They can filter the search results.

1. After the data users belonging to the consumer teams find the data product of their interest, they can request access the data. Data.all has a built-in access-management workflow that the data owner uses to review and approve access requests.

1. The consumer teams can consume the data to empower their AI/ML, analytics and reporting, and ETL use cases.

## AWS Lake Formation
<a name="aws-lake-formation"></a>

If you want to build a custom data mesh solution from the ground up and manage it, consider using AWS Lake Formation. Lake Formation helps you centrally govern, secure, and globally share data for analytics and machine learning. The following diagram shows a data mesh reference architecture based on Lake Formation.

![Multiple producer and consumer accounts with a central governance account and Lake Formation](http://docs.aws.amazon.com/guidance/latest/automotive-data-platform-on-aws/images/aws-lake-formation.png)


The architecture diagram contains following components:

1. The data producers publish data products in the AWS Glue Data Catalog of the central governance account. AWS Lake Formation manages access to the entities of the central Data Catalog.

1. After access is granted, the consumer teams can consume the data to empower their AI/ML, analytics and reporting, and ETL use-cases.

## This Implementation
<a name="this-implementation"></a>

This Automotive Data Platform uses **Amazon DataZone V2** as the primary catalog and governance surface for the following reasons:
+  **Rapid Deployment**: One foundation deploy (`make deploy STAGE=`) provisions the complete DataZone V2 domain and all 9 governed data products
+  **Integrated Governance**: DataZone V2 combines data catalog, producer/consumer project management, subscription workflows, and Lake Formation tag-based access control in a single managed service
+  **Managed Service**: Focus on data products, not infrastructure management
+  **AWS Native**: Seamless integration with S3 Iceberg lake, Glue, Athena, Lake Formation, Macie, CloudTrail, and IAM Identity Center
+  **Enterprise Ready**: Built-in governance, security, and compliance features; downstream consumers can subscribe via DataZone for BI or analytics workloads; predictive-maintenance reference consumers use SageMaker Studio notebooks

For organizations requiring more customization, the architecture can be adapted to use data.all or Lake Formation with minimal changes to the domain structure and data product definitions.