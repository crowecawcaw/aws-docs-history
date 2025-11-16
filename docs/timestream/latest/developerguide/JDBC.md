For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# Configuring the JDBC driver for Timestream for LiveAnalytics

Follow the steps below to configure the JDBC driver.

###### Topics

- [Timestream for LiveAnalytics JDBC driver JARs](#w24aab7c44c37b7b7 "#w24aab7c44c37b7b7")
- [Timestream for LiveAnalytics JDBC driver class and URL format](#w24aab7c44c37b7b9 "#w24aab7c44c37b7b9")
- [Sample application](#w24aab7c44c37b7c11 "#w24aab7c44c37b7c11")

## Timestream for LiveAnalytics JDBC driver JARs

You can obtain the Timestream for LiveAnalytics JDBC driver via direct download or by adding the driver as
a Maven dependency.

- _As a direct download:_. To directly download the Timestream for LiveAnalytics
  JDBC driver, complete the following steps:
  1.  Navigate to [https://github.com/awslabs/amazon-timestream-driver-jdbc/releases](https://github.com/awslabs/amazon-timestream-driver-jdbc/releases "https://github.com/awslabs/amazon-timestream-driver-jdbc/releases")
  2.  You can use
      `amazon-timestream-jdbc-1.0.1-shaded.jar`
      directly with your business intelligence tools and
      applications
  3.  Download
      `amazon-timestream-jdbc-1.0.1-javadoc.jar` to
      a directory of your choice.
  4.  In the directory where you have downloaded
      `amazon-timestream-jdbc-1.0.1-javadoc.jar`,
      run the following command to extract the Javadoc HTML files:

  ```
  jar -xvf amazon-timestream-jdbc-1.0.1-javadoc.jar
  ```

- _As a Maven dependency:_ To add the Timestream for LiveAnalytics JDBC driver as a
  Maven dependency, complete the following steps:
  1.  Navigate to and open your application's
      `pom.xml` file in an editor of your
      choice.
  2.  Add the JDBC driver as a dependency into your application's
      `pom.xml` file:

  ```
  <!-- https://mvnrepository.com/artifact/software.amazon.timestream/amazon-timestream-jdbc -->
  <dependency>
      <groupId>software.amazon.timestream</groupId>
      <artifactId>amazon-timestream-jdbc</artifactId>
      <version>1.0.1</version>
  </dependency>
  ```

## Timestream for LiveAnalytics JDBC driver class and URL format

The driver class for Timestream for LiveAnalytics JDBC driver is:

```
software.amazon.timestream.jdbc.TimestreamDriver
```

The Timestream JDBC driver requires the following JDBC URL format:

```
jdbc:timestream:
```

To specify database properties through the JDBC URL, use the following URL
format:

```
jdbc:timestream://
```

## Sample application

To help you get started with using Timestream for LiveAnalytics with JDBC, we've created a fully
functional sample application in GitHub.

1. Create a database with sample data following the instructions described
   [here](getting-started.md#getting-started.db-w-sample-data.using-console "getting-started.md#getting-started.db-w-sample-data.using-console").
2. Clone the GitHub repository for the [sample application for JDBC](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/jdbc "https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/jdbc") following the instructions from
   [GitHub](https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository "https://docs.github.com/en/free-pro-team@latest/github/creating-cloning-and-archiving-repositories/cloning-a-repository").
3. Follow the instructions in the [README](https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/jdbc/README.md "https://github.com/awslabs/amazon-timestream-tools/tree/mainline/integrations/jdbc/README.md") to get started with the sample application.
