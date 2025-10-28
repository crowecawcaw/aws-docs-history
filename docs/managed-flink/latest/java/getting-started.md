Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Get started with Amazon Managed Service for Apache Flink (DataStream API)

This section introduces you to the fundamental concepts of Managed Service for Apache Flink and implementing an
application in Java using the DataStream API. It describes the available options for
creating and testing your applications. It also provides instructions for installing the
necessary tools to complete the tutorials in this guide and to create your first
application.

###### Topics

- [Review the components of the Managed Service for Apache Flink
  application](#getting-started-components "#getting-started-components")
- [Fulfill the prerequisites for completing the
  exercises](#setting-up-prerequisites "#setting-up-prerequisites")
- [Set up an AWS account and create an
  administrator user](setting-up.md "setting-up.md")
- [Set up the AWS Command Line Interface (AWS CLI)](setup-awscli.md "setup-awscli.md")
- [Create and run a Managed Service for Apache Flink application](get-started-exercise.md "get-started-exercise.md")
- [Clean up AWS resources](getting-started-cleanup.md "getting-started-cleanup.md")
- [Explore additional resources](getting-started-next-steps.md "getting-started-next-steps.md")

## Review the components of the Managed Service for Apache Flink

application

###### Note

Amazon Managed Service for Apache Flink supports all Apache Flink APIs and potentially all JVM languages.
For more information, see [Flink's APIs](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/overview/#flinks-apis "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/concepts/overview/#flinks-apis").

Depending on the API you choose, the structure of the application and the
implementation is slightly different. This Getting Started tutorial covers the
implementation of the applications using the DataStream API in Java.

To process data, your Managed Service for Apache Flink application uses a Java application that processes
input and produces output using the Apache Flink runtime.

A typical Managed Service for Apache Flink application has the following components:

- **Runtime properties:** You can use
  _runtime properties_ to pass configuration parameters to
  your application to change them without modifying and republishing the code.
- **Sources:** The application consumes data from
  one or more _sources_. A source uses a [connector](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/overview/") to read data from an external system, such as a Kinesis data
  stream, or a Kafka bucket. For more information, see [Add streaming data sources](how-sources.md "how-sources.md").
- **Operators:** The application processes data by
  using one or more _operators_. An operator can transform,
  enrich, or aggregate data. For more information, see [Operators](how-operators.md "how-operators.md").
- **Sinks:** The application sends data to external
  sources through _sinks_. A sink uses a [connector](https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.20/docs/connectors/table/overview/")v to send data to a Kinesis data stream, a Kafka topic, Amazon S3,
  or a relational database. You can also use a special connector to print the
  output for development purposes only. For more information, see [Write data using sinks](how-sinks.md "how-sinks.md").

Your application requires some _external dependencies_, such as the
Flink connectors that your application uses, or potentially a Java library. To run in
Amazon Managed Service for Apache Flink, the application must be packaged along with dependencies in a
_fat-jar_ and uploaded to an Amazon S3 bucket. You then create a
Managed Service for Apache Flink application. You pass the location of the code package, along with any other runtime
configuration parameter.

This tutorial demonstrates how to use Apache Maven to package the application, and how
to run the application locally in the IDE of your choice.

## Fulfill the prerequisites for completing the

exercises

To complete the steps in this guide, you must have the following:

- [Git
  client](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "https://git-scm.com/book/en/v2/Getting-Started-Installing-Git"). Install the Git client, if you haven't already.
- [Java
  Development Kit (JDK) version 11](https://www.oracle.com/java/technologies/downloads/#java11 "https://www.oracle.com/java/technologies/downloads/#java11") . Install a Java JDK 11 and set the
  `JAVA_HOME` environment variable to point to your JDK install
  location. If you don't have a JDK 11, you can use [Amazon Coretto 11](../../../corretto/latest/corretto-11-ug/what-is-corretto-11.md "../../../corretto/latest/corretto-11-ug/what-is-corretto-11.md") or any other standard JDK of your choice.
  - To verify that you have the JDK installed correctly, run the following
    command. The output will be different if you are using a JDK other than
    Amazon Corretto. Make sure that the version is 11.x.

  ```
  $ java --version

  openjdk 11.0.23 2024-04-16 LTS
  OpenJDK Runtime Environment Corretto-11.0.23.9.1 (build 11.0.23+9-LTS)
  OpenJDK 64-Bit Server VM Corretto-11.0.23.9.1 (build 11.0.23+9-LTS, mixed mode)
  ```

- [Apache Maven](https://maven.apache.org/ "https://maven.apache.org/"). Install Apache
  Maven if you haven't already. To learn how to install it, see [Installing Apache Maven](https://maven.apache.org/install.html "https://maven.apache.org/install.html").
  - To test your Apache Maven installation, enter the following:

```
$ mvn -version
```

- IDE for local development. We recommend that you use a development environment
  such as [Eclipse Java Neon](https://www.eclipse.org/downloads/packages/release/neon/3 "https://www.eclipse.org/downloads/packages/release/neon/3") or [IntelliJ IDEA](https://www.jetbrains.com/idea/ "https://www.jetbrains.com/idea/") to develop and compile your application.
  - To test your Apache Maven installation, enter the following:

```
$ mvn -version
```

To get started, go to [Set up an AWS account and create an
administrator user](setting-up.md "setting-up.md").
