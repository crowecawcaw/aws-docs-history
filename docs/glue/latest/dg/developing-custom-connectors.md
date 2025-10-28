# Developing custom connectors

You can write the code that reads data from or writes data to your data store and formats
the data for use with AWS Glue Studio jobs. You can create connectors for Spark, Athena, and JDBC data
stores. Sample code posted on GitHub provides an overview of the basic interfaces you need to
implement.

You will need a local development environment for creating your connector code. You can
use any IDE or even just a command line editor to write your connector. Examples of
development environments include:

- A local Scala environment with a local AWS Glue ETL Maven library, as described in [Developing Locally with Scala](aws-glue-programming-etl-libraries.md#develop-local-scala "aws-glue-programming-etl-libraries.md#develop-local-scala") in the
  _AWS Glue Developer Guide_.
- IntelliJ IDE, by downloading the IDE from [https://www.jetbrains.com/idea/](https://www.jetbrains.com/idea/ "https://www.jetbrains.com/idea/").

###### Topics

- [Developing Spark connectors](#code-spark-connector "#code-spark-connector")
- [Developing Athena connectors](#code-athena-connector "#code-athena-connector")
- [Developing JDBC connectors](#code-jdbc-connector "#code-jdbc-connector")
- [Examples of using custom connectors with
  AWS Glue Studio](#custom-connector-examples "#custom-connector-examples")
- [Developing AWS Glue connectors for AWS Marketplace](#code-marketplace-connector "#code-marketplace-connector")

## Developing Spark connectors

You can create a Spark connector with Spark DataSource API V2 (Spark 2.4) to read
data.

**To create a custom Spark connector**

Follow the steps in the AWS Glue GitHub sample library for developing Spark connectors,
which is located at [https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/Spark/README.md](https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/Spark/README.md "https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/Spark/README.md").

## Developing Athena connectors

You can create an Athena connector to be used by AWS Glue and AWS Glue Studio to query a custom data
source.

**To create a custom Athena connector**

Follow the steps in the AWS Glue GitHub sample library for developing Athena connectors,
which is located at [https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/Athena](https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/Athena "https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/Athena").

## Developing JDBC connectors

You can create a connector that uses JDBC to access your data stores.

###### To create a custom JDBC connector

1. Install the AWS Glue Spark runtime libraries in your local development environment.
   Refer to the instructions in the AWS Glue GitHub sample library at [https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/GlueSparkRuntime/README.md](https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/GlueSparkRuntime/README.md "https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/development/GlueSparkRuntime/README.md").
2. Implement the JDBC driver that is responsible for retrieving the data from the data
   source. Refer to the [Java
   Documentation](https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/ "https://docs.oracle.com/javase/8/docs/technotes/guides/jdbc/") for Java SE 8.

Create an entry point within your code that AWS Glue Studio uses to locate your connector.
The **Class name** field should be the full path of your JDBC
driver. 3. Use the `GlueContext` API to read data with the connector. Users can add
more input options in the AWS Glue Studio console to configure the connection to the data source,
if necessary. For a code example that shows how to read from and write to a JDBC
database with a custom JDBC connector, see [Custom and AWS Marketplace connectionType values](aws-glue-programming-etl-connect.md#aws-glue-programming-etl-connect-market "aws-glue-programming-etl-connect.md#aws-glue-programming-etl-connect-market").

## Examples of using custom connectors with

AWS Glue Studio

You can refer to the following blogs for examples of using custom connectors:

- [Developing, testing, and deploying custom connectors for your data stores with AWS Glue](https://aws.amazon.com/blogs/big-data/developing-testing-and-deploying-custom-connectors-for-your-data-stores-with-aws-glue/ "https://aws.amazon.com/blogs/big-data/developing-testing-and-deploying-custom-connectors-for-your-data-stores-with-aws-glue/")
- Apache Hudi: [Writing to Apache Hudi tables using AWS Glue Custom Connector](https://aws.amazon.com/blogs/big-data/writing-to-apache-hudi-tables-using-aws-glue-connector/ "https://aws.amazon.com/blogs/big-data/writing-to-apache-hudi-tables-using-aws-glue-connector/")
- Google BigQuery: [Migrating data from Google BigQuery to Amazon S3 using AWS Glue custom
  connectors](https://aws.amazon.com/blogs/big-data/migrating-data-from-google-bigquery-to-amazon-s3-using-aws-glue-custom-connectors/ "https://aws.amazon.com/blogs/big-data/migrating-data-from-google-bigquery-to-amazon-s3-using-aws-glue-custom-connectors/")
- Snowflake (JDBC): [Performing data transformations using Snowflake and AWS Glue](https://aws.amazon.com/blogs/big-data/performing-data-transformations-using-snowflake-and-aws-glue/ "https://aws.amazon.com/blogs/big-data/performing-data-transformations-using-snowflake-and-aws-glue/")
- SingleStore: [Building fast ETL using SingleStore and AWS Glue](https://aws.amazon.com/blogs/big-data/building-fast-etl-using-singlestore-and-aws-glue/ "https://aws.amazon.com/blogs/big-data/building-fast-etl-using-singlestore-and-aws-glue/")
- Salesforce: [Ingest Salesforce data into Amazon S3 using the CData JDBC custom connector
  with AWS Glue](https://aws.amazon.com/blogs/big-data/ingest-salesforce-data-into-amazon-s3-using-the-cdata-jdbc-custom-connector-with-aws-glue "https://aws.amazon.com/blogs/big-data/ingest-salesforce-data-into-amazon-s3-using-the-cdata-jdbc-custom-connector-with-aws-glue") -
- MongoDB: [Building AWS Glue Spark ETL jobs using Amazon DocumentDB (with MongoDB compatibility)
  and MongoDB](https://aws.amazon.com/blogs/big-data/building-aws-glue-spark-etl-jobs-using-amazon-documentdb-with-mongodb-compatibility-and-mongodb/ "https://aws.amazon.com/blogs/big-data/building-aws-glue-spark-etl-jobs-using-amazon-documentdb-with-mongodb-compatibility-and-mongodb/")
- Amazon Relational Database Service (Amazon RDS): [Building AWS Glue Spark ETL jobs by bringing your own JDBC drivers for Amazon RDS](https://aws.amazon.com/blogs/big-data/building-aws-glue-spark-etl-jobs-by-bringing-your-own-jdbc-drivers-for-amazon-rds/ "https://aws.amazon.com/blogs/big-data/building-aws-glue-spark-etl-jobs-by-bringing-your-own-jdbc-drivers-for-amazon-rds/")
- MySQL (JDBC):
  [https://github.com/aws-samples/aws-glue-samples/blob/master/GlueCustomConnectors/development/Spark/SparkConnectorMySQL.scala](https://github.com/aws-samples/aws-glue-samples/blob/master/GlueCustomConnectors/development/Spark/SparkConnectorMySQL.scala "https://github.com/aws-samples/aws-glue-samples/blob/master/GlueCustomConnectors/development/Spark/SparkConnectorMySQL.scala")

## Developing AWS Glue connectors for AWS Marketplace

As an AWS partner, you can create custom connectors and upload them to AWS Marketplace to sell to
AWS Glue customers.

The process for developing the connector code is the same as for custom connectors, but
the process of uploading and verifying the connector code is more detailed. Refer to the
instructions in [Creating Connectors for AWS Marketplace](https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/marketplace/publishGuide.pdf "https://github.com/aws-samples/aws-glue-samples/tree/master/GlueCustomConnectors/marketplace/publishGuide.pdf") on the GitHub website.
