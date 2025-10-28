Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Managed Service for Apache Flink: How it works

Managed Service for Apache Flink is a fully managed Amazon service that lets you use an Apache Flink
application to process streaming data. First, you program your Apache Flink application, and
then you create your Managed Service for Apache Flink application.

## Program your Apache Flink application

An Apache Flink application is a Java or Scala application that is created with the
Apache Flink framework. You author and build your Apache Flink application locally.

Applications primarily use either the [DataStream API](https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/datastream_api.html "https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/datastream_api.html") or the
[Table API](https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/table/ "https://nightlies.apache.org/flink/flink-docs-release-1.15/dev/table/"). The other Apache Flink APIs are also
available for you to use, but they are less commonly used in building streaming
applications.

The features of the two APIs are as follows:

### DataStream API

The Apache Flink DataStream API programming model is based on two components:

- **Data stream:** The structured representation of
  a continuous flow of data records.
- **Transformation operator:** Takes one or more
  data streams as input, and produces one or more data streams as output.

Applications created
with the DataStream API do the following:

- Read data from a Data Source (such as a Kinesis stream or Amazon MSK topic).
- Apply transformations to the data, such as filtering, aggregation, or enrichment.
- Write the transformed data to a Data Sink.

Applications that use the DataStream API can be written in Java or Scala, and can
read from a Kinesis data stream, a Amazon MSK topic, or a custom source.

Your application processes data by using a _connector_. Apache
Flink uses the following types of connectors:

- **Source**: A connector used to read external
  data.
- **Sink**: A connector used to write to external
  locations.
- **Operator**: A connector used to process data
  within the application.

A typical application consists of at least one data stream with a source, a data
stream with one or more operators, and at least one data sink.

For more information about using the DataStream API, see
[Review DataStream API components](how-datastream.md "how-datastream.md").

### Table API

The Apache Flink Table API programming model is based on the following components:

- **Table Environment:** An interface to
  underlying data that you use to create and host one or more tables.
- **Table:** An object providing access to a
  SQL table or view.
- **Table Source:** Used to read data from an external
  source, such as an Amazon MSK topic.
- **Table Function:** A SQL query or API call used to
  transform data.
- **Table Sink:** Used to write data to an external location,
  such as an Amazon S3 bucket.

Applications created
with the Table API do the following:

- Create a `TableEnvironment` by connecting to a `Table Source`.
- Create a table in the `TableEnvironment` using either SQL queries or
  Table API functions.
- Run a query on the table using either Table API or SQL
- Apply transformations on the results of the query using Table Functions or SQL queries.
- Write the query or function results to a `Table Sink`.

Applications that use the Table API can be written in Java or Scala, and can query data using
either API calls or SQL queries.

For more information about using the Table API, see
[Review Table API components](how-table.md "how-table.md").

## Create your Managed Service for Apache Flink application

Managed Service for Apache Flink is an AWS service that creates an environment for hosting your Apache Flink application and provides it with the following settings::

- **[Use runtime properties](how-properties.md "how-properties.md"):** Parameters that you
  can provide to your application. You can change these parameters without
  recompiling your application code.
- **[Implement fault tolerance](how-fault.md "how-fault.md")**: How your application
  recovers from interrupts and restarts.
- **[Logging and monitoring in Amazon Managed Service for Apache Flink](monitoring-overview.md "monitoring-overview.md")**: How your
  application logs events to CloudWatch Logs.
- **[Implement application scaling](how-scaling.md "how-scaling.md")**: How your application
  provisions computing resources.

You create your Managed Service for Apache Flink application using either the console or the AWS CLI. To get started
creating a Managed Service for Apache Flink application, see [Tutorial: Get started using the DataStream API
in Managed Service for Apache Flink](getting-started.md "getting-started.md").
