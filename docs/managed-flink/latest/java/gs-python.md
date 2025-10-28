Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Get started with Amazon Managed Service for Apache Flink for Python

This section introduces you to the fundamental concepts of a Managed Service for Apache Flink using Python and the Table API.
It describes the available options for creating and testing your applications. It also
provides instructions for installing the necessary tools to complete the tutorials in this
guide and to create your first application.

###### Topics

- [Review the components of a Managed Service for Apache Flink
  application](#gs-python-table-components "#gs-python-table-components")
- [Fulfill the prerequisites](#gs-python-prerequisites "#gs-python-prerequisites")
- [Create and run a Managed Service for Apache Flink for Python
  application](gs-python-createapp.md "gs-python-createapp.md")
- [Clean up AWS resources](gs-python-cleanup.md "gs-python-cleanup.md")

## Review the components of a Managed Service for Apache Flink

application

###### Note

Amazon Managed Service for Apache Flink supports all [Apache Flink APIs](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/overview/#flinks-apis "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/overview/#flinks-apis"). Depending on the API you choose, the structure of
the application is slightly different. One popular approach when developing an
Apache Flink application in Python is to define the application flow using SQL
embedded in Python code. This is the approach that we follow in the following
Gettgin Started tutorial.

To process data, your Managed Service for Apache Flink application uses a Python script to define the data
flow that processes input and produces output using the Apache Flink runtime.

A typical Managed Service for Apache Flink application has the following components:

- **Runtime properties:** You can use
  _runtime properties_ to configure your application
  without recompiling your application code.
- **Sources:** The application consumes data from
  one or more _sources_. A source uses a [connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/") to read data from an external system such as a Kinesis data
  stream, or an Amazon MSK topic. You can also use special connectors to generate data
  from within the application. When you use SQL, the application defines sources
  as _source tables_.
- **Transformations:** The application processes
  data by using one or more _transformations_
  that can filter, enrich, or aggregate data. When you use SQL, the application
  defines transformations as SQL queries.
- **Sinks:** The application sends data to external
  sources through _sinks_. A sink uses a [connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/overview/") to send data to an external system such as a Kinesis data
  stream, an Amazon MSK topic, an Amazon S3 bucket, or a relational database. You can also
  use a special connector to print the output for development purposes. When you
  use SQL, the application defines sinks as _sink tables_ into
  which you insert results. For more information, see [Write data using sinks in Managed Service for Apache Flink](how-sinks.md "how-sinks.md").

Your Python application might also require external dependencies, such as additional
Python libraries or any Flink connector your application uses. When you package your
application, you must include every dependency that your application requires. This
tutorial demonstrates how to include connector dependencies and how to package the
application for deployment on Amazon Managed Service for Apache Flink.

## Fulfill the prerequisites

To complete this tutorial, you must have the following:

- **Python 3.11**, preferably using a standalone
  environment like [VirtualEnv (venv)](https://docs.python.org/3.11/library/venv.html "https://docs.python.org/3.11/library/venv.html"), [Conda](https://docs.conda.io/en/latest/ "https://docs.conda.io/en/latest/"), or [Miniconda](https://docs.anaconda.com/miniconda/ "https://docs.anaconda.com/miniconda/").
- [Git
  client](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "https://git-scm.com/book/en/v2/Getting-Started-Installing-Git") - install the Git client if you have not already.
- [Java
  Development Kit (JDK) version 11](https://www.oracle.com/java/technologies/downloads/#java11 "https://www.oracle.com/java/technologies/downloads/#java11") - install a Java JDK 11 and set the
  `JAVA_HOME` environment variable to point to your install
  location. If you don't have a JDK 11, you can use [Amazon Corretto](../../../corretto.md "../../../corretto.md") or any standard
  JDK of our choice.
  - To verify that you have the JDK correctly installed, run the following
    command. The output will be different if you are using a JDK other than
    Amazon Corretto 11. Make sure that the version is 11.x.

  ```
  $ java --version

  openjdk 11.0.23 2024-04-16 LTS
  OpenJDK Runtime Environment Corretto-11.0.23.9.1 (build 11.0.23+9-LTS)
  OpenJDK 64-Bit Server VM Corretto-11.0.23.9.1 (build 11.0.23+9-LTS, mixed mode)
  ```

- [Apache Maven](https://maven.apache.org/ "https://maven.apache.org/") - install Apache
  Maven if you have not done so already. For more information, see [Installing Apache
  Maven](https://maven.apache.org/install.html "https://maven.apache.org/install.html").
  - To test your Apache Maven installation, use the following
    command:

  ```
  $ mvn -version
  ```

###### Note

Although your application is written in Python, Apache Flink runs in the Java
Virtual Machine (JVM). It distributes most of the dependencies, such as the Kinesis
connector, as JAR files. To manage these dependencies and to package the application
in a ZIP file, use [Apache Maven](https://maven.apache.org/ "https://maven.apache.org/"). This
tutorial explains how to do so.

###### Warning

We recommend that you use Python 3.11 for local development. This is the same
Python version used by Amazon Managed Service for Apache Flink with the Flink runtime 1.19.

Installing the Python Flink library 1.19 on Python 3.12 might fail.

If you have another Python version installed by default on your machine, we
recommend that you create a standalone environment such as VirtualEnv using Python
3.11.

**IDE for local development**

We recommend that you use a development environment such as [PyCharm](https://www.jetbrains.com/pycharm/ "https://www.jetbrains.com/pycharm/") or [Visual Studio Code](https://code.visualstudio.com/ "https://code.visualstudio.com/") to develop and
compile your application.

Then, complete the first two steps of the [Get started with Amazon Managed Service for Apache Flink (DataStream API)](getting-started.md "getting-started.md"):

- [Set up an AWS account and create an
  administrator user](setting-up.md "setting-up.md")
- [Set up the AWS Command Line Interface (AWS CLI)](setup-awscli.md "setup-awscli.md")

To get started, see [Create an application](gs-python-createapp.md "gs-python-createapp.md").
