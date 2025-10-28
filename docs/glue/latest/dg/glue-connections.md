# Connecting to data

An AWS Glue
_connection_ is a Data Catalog object that stores login
credentials, URI strings, virtual private cloud (VPC) information, and more for a particular
data store. AWS Glue crawlers, jobs, and development endpoints use connections in order to
access certain types of data stores. You can use connections for both sources and targets,
and reuse the same connection across multiple crawler or extract, transform, and load (ETL)
jobs.

The latest version of the AWS Glue connections schema provides a unified way to manage data connections across AWS services and applications, such as AWS Glue, Amazon Athena, and Amazon SageMaker AI Unified Studio.

## Overview of using connectors and

connections

A _connection_ contains the properties that are required to connect to
a particular data store. When you create a connection, it is stored in the AWS Glue Data Catalog. You
choose a connector, and then create a connection based on that connector.

You can subscribe to connectors for non-natively supported data stores in AWS Marketplace, and then
use those connectors when you're creating connections. Developers can also create their own
connectors, and you can use them when creating connections.

###### Note

Connections created using custom or AWS Marketplace connectors in AWS Glue Studio appear in the AWS Glue console with type set to
`UNKNOWN`.

The following steps describe the overall process of using connectors in AWS Glue Studio:

1. Subscribe to a connector in AWS Marketplace, or develop your own connector and upload it to
   AWS Glue Studio. For more information, see [Adding connectors to AWS Glue Studio](creating-custom-connectors.md#creating-connectors "creating-custom-connectors.md#creating-connectors").
2. Review the connector usage information. You can find this information on the
   **Usage** tab on the connector product page. For example, if you click
   the **Usage** tab on this product page, [AWS Glue Connector for Google BigQuery](https://aws.amazon.com/marketplace/pp/prodview-w2ranrogj3xmm?ref_=beagle&applicationId=GlueStudio "https://aws.amazon.com/marketplace/pp/prodview-w2ranrogj3xmm?ref_=beagle&applicationId=GlueStudio"), you can see in the **Additional
   Resources** section a link to a blog about using this connector.
3. Create a connection. You choose which connector to use and provide additional information for the connection, such as login credentials, URI strings, and virtual private cloud (VPC) information. For more information, see [Creating connections for connectors](creating-connections.md "creating-connections.md").
4. Create an IAM role for your job. The job assumes the permissions of the IAM role that you
   specify when you create it. This IAM role must have the necessary permissions to
   authenticate with, extract data from, and write data to your data stores.
5. Create an ETL job and configure the data source properties for your ETL job. Provide
   the connection options and authentication information as instructed by the custom
   connector provider. For more information, see [Authoring jobs with custom
   connectors](job-authoring-custom-connectors.md "job-authoring-custom-connectors.md").
6. Customize your ETL job by adding transforms or additional data stores, as described in
   [Starting visual ETL jobs in AWS Glue Studio](edit-nodes-chapter.md "edit-nodes-chapter.md").
7. If using a connector for the data target, configure the data target properties for
   your ETL job. Provide the connection options and authentication information as instructed
   by the custom connector provider. For more information, see [Authoring jobs with custom
   connectors](job-authoring-custom-connectors.md "job-authoring-custom-connectors.md").
8. Customize the job run environment by configuring job properties, as described in [Modify the job properties](managing-jobs-chapter.md#edit-jobs-properties "managing-jobs-chapter.md#edit-jobs-properties").
9. Run the job.
