Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Get started with Amazon Managed Service for Apache Flink (Table API)

This section introduces you to the fundamental concepts of Managed Service for Apache Flink and implementing an
application in Java using the Table API and SQL. It demonstrates how to switch between
different APIs within the same application, and it describes the available options for
creating and testing your applications. It also provides instructions for installing the
necessary tools to complete the tutorials in this guide and to create your first
application.

###### Topics

- [Review the components of the Managed Service for Apache Flink
  application](#gs-table-components "#gs-table-components")
- [Complete the required prerequisites](#gs-table-prerequisites "#gs-table-prerequisites")
- [Create and run a Managed Service for Apache Flink application](gs-table-create.md "gs-table-create.md")
- [Next step](#gs-table-next-step-4 "#gs-table-next-step-4")
- [Clean up AWS resources](gs-table-cleanup.md "gs-table-cleanup.md")
- [Explore additional resources](gs-table-next-steps.md "gs-table-next-steps.md")

## Review the components of the Managed Service for Apache Flink

application

###### Note

Managed Service for Apache Flink supports all [Apache Flink APIs](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/overview/#flinks-apis "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/overview/#flinks-apis") and potentially all JVM languages. Depending on the
API you choose, the structure of the application and the implementation is slightly
different. This tutorial covers the implementation of applications using the Table
API and SQL, and the integration with the DataStream API, implemented in Java.

To process data, your Managed Service for Apache Flink application uses a Java application that processes
input and produces output using the Apache Flink runtime.

A typical Apache Flink application has the following components:

- **Runtime properties:** You can use
  _runtime properties_ to pass configuration parameters to
  your application without modifying and republishing the code.
- **Sources:** The application consumes data from
  one or more _sources_. A source uses a [connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/") to read data from and external system, such as a Kinesis
  data stream or an Amazon MSK topic. For development or testing, you can also have
  sources random[ly generate test data. For more information, see [Add streaming data sources to Managed Service for Apache Flink](how-sources.md "how-sources.md"). With SQL or Table API,
  sources are defined as _source tables_.
- **Transformations:** The application processes
  data through one or more transformations that can filter, enrich, or aggregate
  data. When using SQL or Table API, transformations are defined as _queries over tables_ or _views_.
- **Sinks:** The application sends data to external
  systems through _sinks_. A sink uses a [connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/") to send data to an external system, such as a Kinesis data
  stream, an Amazon MSK topic, an Amazon S3 bucket, or a relational database. You can also
  use a special connector to print the output for development purposes only. When
  using SQL or Table API, sinks are defined as _sink
  tables_ where you will insert results. For more information, see
  [Write data using sinks in Managed Service for Apache Flink](how-sinks.md "how-sinks.md").

Your application requires some **external dependencies**,
such as Flink connectors your application uses, or potentially a Java library. To run in
Amazon Managed Service for Apache Flink, you must package the application along with dependencies in a _fat-JAR_ and upload it to an Amazon S3 bucket. You
then create a Managed Service for Apache Flink application. You pass the code package location, along with other runtime
configuration parameters. This tutorial demonstrates how to use Apache Maven to package
the application and how to run the application locally in the IDE of your choice.

## Complete the required prerequisites

Before starting this tutorial, complete the first two steps of the [Get started with Amazon Managed Service for Apache Flink (DataStream API)](getting-started.md "getting-started.md"):

- [Fulfill the prerequisites for completing the
  exercises](getting-started.md#setting-up-prerequisites "getting-started.md#setting-up-prerequisites")
- [Set up the AWS Command Line Interface (AWS CLI)](setup-awscli.md "setup-awscli.md")

To get started, see [Create an application](gs-table-create.md "gs-table-create.md").

## Next step

[Clean up AWS resources](gs-table-cleanup.md "gs-table-cleanup.md")
