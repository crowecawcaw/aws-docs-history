# Use Amazon Athena Federated Query

If you have data in sources other than Amazon S3, you can use Athena Federated Query to query the data in
place or build pipelines that extract data from multiple data sources and store them in
Amazon S3. With Athena Federated Query, you can run SQL queries across data stored in relational,
non-relational, object, and custom data sources.

Athena uses _data source connectors_ that run on AWS Lambda to run
federated queries. A data source connector is a piece of code that can translate between
your target data source and Athena. You can think of a connector as an extension of Athena's
query engine. Prebuilt Athena data source connectors exist for data sources like Amazon CloudWatch
Logs, Amazon DynamoDB, Amazon DocumentDB, and Amazon RDS, and JDBC-compliant relational data sources such MySQL,
and PostgreSQL under the Apache 2.0 license. You can also use the Athena Query Federation SDK to write
custom connectors. To choose, configure, and deploy a data source connector to your account,
you can use the Athena and Lambda consoles or the AWS Serverless Application Repository. After you deploy data source
connectors, the connector is associated with a catalog that you can specify in SQL queries.
You can combine SQL statements from multiple catalogs and span multiple data sources with a
single query.

When a query is submitted against a data source, Athena invokes the corresponding connector
to identify parts of the tables that need to be read, manages parallelism, and pushes down
filter predicates. Based on the user submitting the query, connectors can provide or
restrict access to specific data elements. Connectors use Apache Arrow as the format for
returning data requested in a query, which enables connectors to be implemented in languages
such as C, C++, Java, Python, and Rust. Since connectors are processed in Lambda, they can be
used to access data from any data source on the cloud or on-premises that is accessible from
Lambda.

To write your own data source connector, you can use the Athena Query Federation SDK to customize one of
the prebuilt connectors that Amazon Athena provides and maintains. You can modify a copy of the
source code from the [GitHub repository](https://github.com/awslabs/aws-athena-query-federation/wiki/Available-Connectors "https://github.com/awslabs/aws-athena-query-federation/wiki/Available-Connectors") and then use the [Connector publish tool](https://github.com/awslabs/aws-athena-query-federation/wiki/Connector_Publish_Tool "https://github.com/awslabs/aws-athena-query-federation/wiki/Connector_Publish_Tool") to create your own AWS Serverless Application Repository package.

###### Note

Third party developers may have used the Athena Query Federation SDK to write data source connectors.
For support or licensing issues with these data source connectors, please work with your
connector provider. These connectors are not tested or supported by AWS.

For a list of data source connectors written and tested by Athena, see [Available data source connectors](connectors-available.md "connectors-available.md").

For information about writing your own data source connector, see [Example Athena connector](https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-example "https://github.com/awslabs/aws-athena-query-federation/tree/master/athena-example") on GitHub.

## Considerations and limitations

- Engine versions – Athena Federated Query is supported
  only on Athena engine version 2 and later. For information about Athena engine versions, see
  [Athena engine versioning](engine-versions.md "engine-versions.md").
- Views – You can create and query views
  on federated data sources. Federated views are stored in AWS Glue, not the
  underlying data source. For more information, see [Query federated views](running-federated-queries.md#running-federated-queries-federated-views "running-federated-queries.md#running-federated-queries-federated-views").
- Delimited identifiers – Delimited
  identifiers (also known as quoted identifiers) begin and end with double
  quotation marks ("). Currently, delimited identifiers are not supported for
  federated queries in Athena.
- Write operations – Write operations like
  [INSERT INTO](insert-into.md "insert-into.md") are not supported.
  Attempting to do so may result in the error message **`This operation is
currently not supported for external catalogs`**.
- Pricing – For pricing information, see
  [Amazon Athena
  pricing](https://aws.amazon.com/athena/pricing/ "https://aws.amazon.com/athena/pricing/").
- JDBC driver – To use the JDBC driver
  with federated queries or an [external Hive metastore](connect-to-data-source-hive.md "connect-to-data-source-hive.md"),
  include `MetadataRetrievalMethod=ProxyAPI` in your JDBC connection
  string. For information about the JDBC driver, see [Connect to Amazon Athena with JDBC](connect-with-jdbc.md "connect-with-jdbc.md").
- Secrets Manager – To use the Athena Federated Query feature with
  AWS Secrets Manager, you must configure an Amazon VPC private endpoint for Secrets Manager. For more
  information, see [Create a Secrets Manager VPC private endpoint](../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md#vpc-endpoint-create "../../../secretsmanager/latest/userguide/vpc-endpoint-overview.md#vpc-endpoint-create") in the _AWS Secrets Manager User Guide_.

## Permissions required

Data source connectors might require access to the following resources to function
correctly. If you use a prebuilt connector, check the information for the connector to
ensure that you have configured your VPC correctly. Also, ensure that IAM principals
running queries and creating connectors have privileges to required actions. For more
information, see [Allow access to Athena Federated Query: Example policies](federated-query-iam-access.md "federated-query-iam-access.md").

- Amazon S3 – In addition to writing query
  results to the Athena query results location in Amazon S3, data connectors also write
  to a spill bucket in Amazon S3. Connectivity and permissions to this Amazon S3 location
  are required. We recommend using spill to disk encryption for each connector and
  [S3 lifecycle
  configuration](../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md "../../../AmazonS3/latest/userguide/object-lifecycle-mgmt.md") to expire spilled data that is no longer
  needed.
- Athena – Data sources need connectivity
  to Athena and vice versa for checking query status and preventing
  overscan.
- AWS Glue Data Catalog – Connectivity and
  permissions are required if your connector uses Data Catalog for supplemental or
  primary metadata.
- Amazon ECR – Data source connector Lambda
  functions use an Amazon ECR image from an Amazon ECR repository. The user that deploys the
  connector must have the permissions `ecr:BatchGetImage` and
  `ecr:GetDownloadUrlForLayer`. For more information, see [Amazon ECR permissions](../../../lambda/latest/dg/images-create.md#gettingstarted-images-permissions "../../../lambda/latest/dg/images-create.md#gettingstarted-images-permissions") in the
  _AWS Lambda Developer Guide_.

## Videos

Watch the following videos to learn more about using Athena Federated Query.

###### Video: Analyze Results of Federated Query in Amazon Athena in Quick

The following video demonstrates how to analyze results of an Athena federated
query in Quick.

###### Video: Game Analytics Pipeline

The following video shows how to deploy a scalable serverless data pipeline to
ingest, store, and analyze telemetry data from games and services using Amazon Athena
federated queries.
