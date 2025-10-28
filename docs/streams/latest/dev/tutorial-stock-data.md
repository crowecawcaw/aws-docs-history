# Tutorial: Analyze real-time stock data using

Amazon Managed Service for Apache Flink

The scenario for this tutorial involves ingesting stock trades into a data stream and
writing a simple [Amazon Managed Service for Apache Flink](../../../kinesisanalytics/latest/java/what-is.md "../../../kinesisanalytics/latest/java/what-is.md") application that performs calculations on the stream. You will
learn how to send a stream of records to Kinesis Data Streams and implement an application that consumes
and processes the records in near real time.

With Amazon Managed Service for Apache Flink, you can use Java or Scala to process and analyze streaming data. The
service lets you author and run Java or Scala code against streaming sources to perform
time-series analytics, feed real-time dashboards, and create real-time metrics.

You can build Flink applications in Managed Service for Apache Flink using open-source libraries based on [Apache Flink](https://flink.apache.org/ "https://flink.apache.org/"). Apache Flink is a popular framework and engine for processing data streams.

###### Important

After you create two data streams and an application, your account incurs nominal
charges for Kinesis Data Streams and Managed Service for Apache Flink usage because they are not eligible for the AWS Free Tier.
When you are finished with this application, delete your AWS resources to stop incurring
charges.

The code does not access actual stock market data, but instead simulates the stream of
stock trades. It does so by using a random stock trade generator. If you have access to a
real-time stream of stock trades, you might be interested in deriving useful, timely
statistics from that stream. For example, you might want to perform a sliding window
analysis where you determine the most popular stock purchased in the last 5 minutes. Or you
might want a notification whenever there is a sell order that is too large (that is, it has
too many shares). You can extend the code in this series to provide such
functionality.

The examples shown use the US West (Oregon) Region, but they work on any of the [AWS Regions that support Managed Service for Apache Flink](../../../general/latest/gr/rande.md#ka_region "../../../general/latest/gr/rande.md#ka_region").

###### Tasks

- [Prerequisites for completing the
  exercises](#setting-up-prerequisites "#setting-up-prerequisites")
- [Set up an AWS account and create an administrator
  user](setting-up.md "setting-up.md")
- [Set up the AWS Command Line Interface (AWS CLI)](setup-awscli.md "setup-awscli.md")
- [Create and run a Managed Service for Apache Flink application](get-started-exercise.md "get-started-exercise.md")

## Prerequisites for completing the

exercises

To complete the steps in this guide, you must have the following:

- [Java Development Kit](http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html "http://www.oracle.com/technetwork/java/javase/downloads/jdk8-downloads-2133151.html") (JDK) version 8. Set the
  `JAVA_HOME` environment variable to point to your JDK install
  location.
- We recommend that you use a development environment (such as [Eclipse Java
  Neon](http://www.eclipse.org/downloads/packages/release/neon/3 "http://www.eclipse.org/downloads/packages/release/neon/3") or [IntelliJ
  Idea](https://www.jetbrains.com/idea/ "https://www.jetbrains.com/idea/")) to develop and compile your application.
- [Git
  Client.](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "https://git-scm.com/book/en/v2/Getting-Started-Installing-Git") Install the Git client if you haven't already.
- [Apache
  Maven Compiler Plugin](https://maven.apache.org/plugins/maven-compiler-plugin/ "https://maven.apache.org/plugins/maven-compiler-plugin/"). Maven must be in your working path. To test
  your Apache Maven installation, enter the following:

```
$ mvn -version
```

To get started, go to [Set up an AWS account and create an administrator
user](setting-up.md "setting-up.md").
