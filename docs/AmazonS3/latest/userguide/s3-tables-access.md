# Accessing table data

There are multiple ways to access tables in Amazon S3 table buckets, you can integrate tables with AWS analytics services using Amazon SageMaker Lakehouse, or access tables directly using the Amazon S3 Tables Iceberg REST endpoint or the Amazon S3 Tables Catalog for Apache Iceberg. The access method you use will depend on your catalog setup, governance model, and access control needs. The following is an overview of these access methods.



**Amazon SageMaker Lakehouse integration**
This is the recommended access method for working with tables in S3 table buckets. The integration gives you unified table management, centralized governance, and fine-grained access control across multiple AWS analytics services. After integration, you can query tables in services such as Athena and Amazon Redshift.


**Direct access**
Use this method if you need to work with AWS Partner Network (APN) catalog implementations, custom catalog implementations, or if you only need to perform basic read/write operations on tables within a single table bucket.


###### Note

To access tables the IAM identity you use needs access to your table resources and S3 Tables actions. For more information, see [Access management for S3 Tables](s3-tables-setting-up.md "s3-tables-setting-up.md").


## Accessing tables through the Amazon SageMaker Lakehouse integration


You can integrate S3 table buckets with Amazon SageMaker Lakehouse to access tables from AWS analytics services, such as Amazon Athena, Amazon Redshift, and QuickSight. Amazon SageMaker Lakehouse unifies your data across Amazon S3 data lakes and Amazon Redshift data warehouses, so you can build analytics, machine learning (ML), and generative AI applications on a single copy of data. The integration populates the AWS Glue Data Catalog with your table resources, and federates access to these resources with AWS Lake Formation. For more information on integrating, see [Integrating Amazon S3 Tables with AWS analytics
 services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md").


The integration enables fine-grained access control through AWS Lake Formation to provide additional security. Lake Formation uses a combination of its own permissions model and the IAM permissions model to control access to table resources and underlying data. This means that a request to access your table must pass permission checks by both IAM and Lake Formation. For more information, see [Lake Formation permissions overview](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-overview.html "https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-overview.html") in the *AWS Lake Formation Developer Guide*.


The following AWS analytics services can access tables through this integration:



* [Amazon Athena](s3-tables-integrating-athena.md "s3-tables-integrating-athena.md")
* [Amazon Redshift](s3-tables-integrating-redshift.md "s3-tables-integrating-redshift.md")
* [Amazon EMR](s3-tables-integrating-emr.md "s3-tables-integrating-emr.md")
* [QuickSight](s3-tables-integrating-quicksight.md "s3-tables-integrating-quicksight.md")
* [Amazon Data Firehose](s3-tables-integrating-firehose.md "s3-tables-integrating-firehose.md")
* [AWS Glue
 ETL](s3-tables-integrating-glue.md "s3-tables-integrating-glue.md")

### Accessing tables using the AWS Glue Iceberg REST endpoint


Once your S3 table buckets are integrated with Amazon SageMaker Lakehouse, you can also use the AWS Glue Iceberg REST endpoint to connect to S3 tables from third-party query engines that support Iceberg. For more information, see [Accessing Amazon S3 tables using the AWS Glue Iceberg REST endpoint](s3-tables-integrating-glue-endpoint.md "s3-tables-integrating-glue-endpoint.md").


We recommend using the AWS Glue Iceberg REST endpoint when you want to access tables from Spark, PyIceberg, or other Iceberg-compatible clients.



The following clients can access tables directly through the AWS Glue Iceberg REST endpoint:


* Any Iceberg client, including Spark, PyIceberg, and more.

## Accessing tables directly



 You can access tables directly from open source query engines through methods that bridge S3 Tables management operations to your Apache Iceberg analytics applications. There are two direct access methods: the Amazon S3 Tables Iceberg REST endpoint or the Amazon S3 Tables Catalog for Apache Iceberg. The REST endpoint is recommended. 


We recommend direct access if you access tables in self-managed catalog implementations, or only need to perform basic read/write operations on tables in a single table bucket. For other access scenarios, we recommend the Amazon SageMaker Lakehouse integration.


Direct access to tables is managed through either IAM identity-based policies or resource-based policies attached to tables and table buckets. You do not need to manage Lake Formation permissions for tables when you access them directly. 


### Accessing tables through the Amazon S3 Tables Iceberg REST endpoint


You can use the Amazon S3 Tables Iceberg REST endpoint to access your tables directly from any Iceberg REST compatible clients through HTTP endpoints, for more information, see [Accessing tables using the Amazon S3 Tables Iceberg REST endpoint](s3-tables-integrating-open-source.md "s3-tables-integrating-open-source.md").
 


The following AWS analytics services and query engines can access tables directly using the Amazon S3 Tables Iceberg REST endpoint:



###### Supported query engines


* Any Iceberg client, including Spark, PyIceberg, and more.
* [Amazon EMR](s3-tables-integrating-emr.md "s3-tables-integrating-emr.md")
* [AWS Glue
 ETL](s3-tables-integrating-glue.md "s3-tables-integrating-glue.md")

### Accessing tables directly through the Amazon S3 Tables Catalog for Apache Iceberg


You can also access tables directly from query engines like Apache Spark by using the S3 Tables client catalog, for more information, see [Accessing Amazon S3 tables with
 the Amazon S3 Tables Catalog for Apache Iceberg](s3-tables-client-catalog.md "s3-tables-client-catalog.md"). However, S3 recommends using the Amazon S3 Tables Iceberg REST endpoint for direct access because it supports more applications, without requiring language or engine-specific code.



The following query engines can access tables directly using the client catalog:


* [Apache Spark](s3-tables-client-catalog.md#s3-tables-integrating-open-source-spark "s3-tables-client-catalog.md#s3-tables-integrating-open-source-spark")
