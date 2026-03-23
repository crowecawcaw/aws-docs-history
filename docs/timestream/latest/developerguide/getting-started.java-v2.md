For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Java v2

To get started with the [Java 2.0 SDK](https://aws.amazon.com/sdk-for-java/ "https://aws.amazon.com/sdk-for-java/") and Amazon Timestream,
complete the prerequisites, described below.

Once you've completed the necessary prerequisites for the Java 2.0 SDK, you can get started with the [Code samples](code-samples.md "code-samples.md").

## Prerequisites

Before you get started with Java, you must do the
following:

1. Follow the AWS setup instructions in [Accessing Timestream for LiveAnalytics](accessing.md "accessing.md").
2. You can configure the AWS SDK as a Maven dependency as described
   in
   [Using the SDK with Apache Maven](../../../sdk-for-java/v2/developer-guide/welcome.md "../../../sdk-for-java/v2/developer-guide/welcome.md").
3. Set up a Java development environment by downloading and installing the
   following:
   - Java SE Development Kit 8 (such as [Amazon Corretto 8](../../../corretto/latest/corretto-8-ug/downloads-list.md "../../../corretto/latest/corretto-8-ug/downloads-list.md")).
   - Java IDE (such as [Eclipse](http://www.eclipse.org "http://www.eclipse.org") or [IntelliJ](https://www.jetbrains.com/idea/ "https://www.jetbrains.com/idea/")).

   For more information, see [Getting Started with the AWS SDK for Java](../../../sdk-for-java/latest/developer-guide/get-started.md "../../../sdk-for-java/latest/developer-guide/get-started.md")

## Using Apache Maven

You can use [Apache Maven](https://maven.apache.org/ "https://maven.apache.org/")
to configure and build AWS SDK for Java projects.

###### Note

To use Apache Maven, ensure your Java SDK and runtime are 1.8 or higher.

You can configure the AWS SDK as a Maven dependency as described
in
[Using the SDK with Apache Maven](../../../sdk-for-java/v2/developer-guide/welcome.md "../../../sdk-for-java/v2/developer-guide/welcome.md"). The changes required to the pom.xml file are described
[here](../../../sdk-for-java/v2/migration-guide/whats-different.md#adding-v2 "../../../sdk-for-java/v2/migration-guide/whats-different.md#adding-v2").

You can run compile and run your source code with the following command:

```
mvn clean compile
mvn exec:java -Dexec.mainClass=<your source code Main class>

```

###### Note

`<your source code Main class>`
is the path to your Java source code's main class.
