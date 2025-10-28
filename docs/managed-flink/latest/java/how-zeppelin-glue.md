Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Work with AWS Glue

Your Studio notebook stores and gets information about its data sources and sinks from AWS Glue. When you create
your Studio notebook, you specify the AWS Glue database that contains your connection information. When you
access your data sources and sinks, you specify AWS Glue tables contained in the database. Your AWS Glue tables
provide access to the AWS Glue connections
that define the locations, schemas, and parameters of your data sources and destinations.

Studio notebooks use table properties to store application-specific data. For more information, see
[Table properties](how-zeppelin-glue-properties.md "how-zeppelin-glue-properties.md").

For an example of how to set up a AWS Glue connection, database, and table for use with Studio notebooks, see
[Create an AWS Glue database](example-notebook.md#example-notebook-glue "example-notebook.md#example-notebook-glue") in the
[Tutorial: Create a Studio notebook in
Managed Service for Apache Flink](example-notebook.md "example-notebook.md") tutorial.
