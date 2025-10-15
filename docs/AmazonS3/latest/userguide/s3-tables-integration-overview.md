# Amazon S3 Tables integration with AWS analytics
 services overview

To make tables in your account accessible by AWS analytics services, you integrate your Amazon S3
 table buckets with Amazon SageMaker Lakehouse. This integration allows AWS analytics services to
 automatically discover and access your table data. You can use this integration to work with your tables
 in these services:


* [Amazon Athena](s3-tables-integrating-athena.md "s3-tables-integrating-athena.md")
* [Amazon Redshift](s3-tables-integrating-redshift.md "s3-tables-integrating-redshift.md")
* [Amazon EMR](s3-tables-integrating-emr.md "s3-tables-integrating-emr.md")
* [QuickSight](s3-tables-integrating-quicksight.md "s3-tables-integrating-quicksight.md")
* [Amazon Data Firehose](s3-tables-integrating-firehose.md "s3-tables-integrating-firehose.md")
###### Note

This integration uses the AWS Glue and AWS Lake Formation services and might incur AWS Glue request and storage costs. For more information,
 see [AWS Glue Pricing.](https://aws.amazon.com/glue/pricing/ "https://aws.amazon.com/glue/pricing/")

Additional pricing applies for running queries on your S3 tables. For more information, see
 pricing information for the query engine that you're using.


## How the integration works


When you create a table bucket in the console, Amazon S3 initiates the following actions to integrate table buckets in the Region that you have selected with AWS analytics services: 



1. Creates a new AWS Identity and Access Management (IAM) [service
 role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html "https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-service.html") that gives Lake Formation access to all your table
 buckets.
2. Using the service role, Lake Formation registers table buckets in the current Region. This allows Lake Formation to manage access, permissions, and governance for all current and future table buckets in that Region.
3. Adds the `s3tablescatalog` catalog to the AWS Glue Data Catalog in the current Region.
 Adding the `s3tablescatalog` catalog allows all your table buckets, namespaces, and
 tables to be populated in the Data Catalog.

###### Note

These actions are automated through the Amazon S3 console. If you perform this integration programmatically,
 you must manually take all of these actions.


You integrate your table buckets once per AWS Region. After the integration is completed, all
 current and future table buckets, namespaces, and tables are added to the AWS Glue Data Catalog in that
 Region.


The following illustration shows how the `s3tablescatalog` catalog automatically
 populates table buckets, namespaces, and tables in the current Region as corresponding objects in the
 Data Catalog. Table buckets are populated as subcatalogs. Namespaces within a table bucket are populated as
 databases within their respective subcatalogs. Tables are populated as tables in their respective
 databases.



![The ways that table resources are represented in AWS Glue Data Catalog.](../../../images/AmazonS3/latest/userguide/images/S3Tables-glue-catalog.png)

###### How permissions work


We recommend integrating your table buckets with AWS analytics services so that you can work
 with your table data across services that use the AWS Glue Data Catalog as a metadata store. The integration
 enables fine-grained access control through AWS Lake Formation. This security approach means that, in addition
 to AWS Identity and Access Management (IAM) permissions, you must grant your IAM principal Lake Formation permissions on your tables
 before you can work with them. 


There are two main types of permissions in AWS Lake Formation: 



* Metadata access permissions control the ability to create, read, update, and delete metadata
 databases and tables in the Data Catalog.
* Underlying data access permissions control the ability to read and write data to the underlying
 Amazon S3 locations that the Data Catalog resources point to.

Lake Formation uses a combination of its own permissions model and the IAM permissions model to control
 access to Data Catalog resources and underlying data:



* For a request to access Data Catalog resources or underlying data to succeed, the request must pass
 permission checks by both IAM and Lake Formation.
* IAM permissions control access to the Lake Formation and AWS Glue APIs and resources, whereas Lake Formation
 permissions control access to the Data Catalog resources, Amazon S3 locations, and the underlying data.

Lake Formation permissions apply only in the Region in which they were granted, and a principal must be
 authorized by a data lake administrator or another principal with the necessary permissions in order to
 be granted Lake Formation permissions. 


For more information, see [Overview of
 Lake Formation permissions](https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-overview.html "https://docs.aws.amazon.com/lake-formation/latest/dg/lf-permissions-overview.html") in the *AWS Lake Formation Developer Guide*. 


Make sure that you follow the steps in [Integrating S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md") so that you have the appropriate permissions to access the
 AWS Glue Data Catalog and your table resources, and to work with AWS analytics services.


## Next steps



* [Integrating S3 Tables with AWS analytics services](s3-tables-integrating-aws.md "s3-tables-integrating-aws.md")
* [Create a namespace](s3-tables-namespace-create.md "s3-tables-namespace-create.md")
* [Create a table](s3-tables-create.md "s3-tables-create.md")
