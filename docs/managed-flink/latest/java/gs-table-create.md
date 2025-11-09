Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Create and run a Managed Service for Apache Flink application

In this exercise, you create a Managed Service for Apache Flink application with Kinesis data streams as a source and
sink.

###### This section contains the following steps.

- [Create dependent resources](#gs-table-resources "#gs-table-resources")
- [Set up your local development environment](#gs-table-2 "#gs-table-2")
- [Download and examine the Apache Flink streaming Java
  code](#gs-table-5 "#gs-table-5")
- [Run your application locally](#gs-table-run-locally "#gs-table-run-locally")
- [Observe the application writing data to an S3
  bucket](#gs-table-input-output "#gs-table-input-output")
- [Stop your application running locally](#gs-table-stop "#gs-table-stop")
- [Compile and package your application code](#gs-table-5.5 "#gs-table-5.5")
- [Upload the application code JAR file](#gs-table-6 "#gs-table-6")
- [Create and configure the Managed Service for Apache Flink
  application](#gs-table-7 "#gs-table-7")

## Create dependent resources

Before you create a Managed Service for Apache Flink for this exercise, you create the following
dependent resources:

- An Amazon S3 bucket to store the application's code and to write the
  application output.

###### Note

This tutorial assumes that you are deploying your application in the
us-east-1 Region. If you use another Region, you must adapt
all steps accordingly.

### Create an Amazon S3 bucket

You can create the Amazon S3 bucket using the console. For instructions for
creating this resource, see the following topics:

- [How Do I Create an S3
  Bucket?](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md") in the _Amazon Simple Storage Service User Guide_. Give the
  Amazon S3 bucket a globally unique name by appending your login name.

###### Note

Make sure that you create the bucket in the Region you use for
this tutorial. The default for the tutorial is
us-east-1.

### Other resources

When you create your application, Managed Service for Apache Flink creates the following Amazon CloudWatch resources if they don't already
exist:

- A log group called
  `/AWS/KinesisAnalytics-java/<my-application>`.
- A log stream called `kinesis-analytics-log-stream`.

## Set up your local development environment

For development and debugging, you can run the Apache Flink application on your
machine, directly from your IDE of choice. Any Apache Flink dependencies are handled
as normal Java dependencies using Maven.

###### Note

On your development machine, you must have Java JDK 11, Maven, and Git
installed. We recommend that you use a development environment such as [Eclipse Java
Neon](https://www.eclipse.org/downloads/packages/release/neon/3 "https://www.eclipse.org/downloads/packages/release/neon/3") or [IntelliJ
IDEA](https://www.jetbrains.com/idea/ "https://www.jetbrains.com/idea/"). To verify that you meet all prerequisites, see [Fulfill the prerequisites for completing the
exercises](getting-started.md#setting-up-prerequisites "getting-started.md#setting-up-prerequisites"). You **do not** need to install an Apache Flink
cluster on your machine.

### Authenticate your AWS

session

The application uses Kinesis data streams to publish data. When running locally,
you must have a valid AWS authenticated session with permissions to write to
the Kinesis data stream. Use the following steps to authenticate your
session:

1. If you don't have the AWS CLI and a named profile with valid credential
   configured, see [Set up the AWS Command Line Interface (AWS CLI)](setup-awscli.md "setup-awscli.md").
2. If your IDE has a plugin to integrate with AWS, you can use it to
   pass the credentials to the application running in the IDE. For more
   information, see [AWS
   Toolkit for IntelliJ IDEA](https://aws.amazon.com/intellij/ "https://aws.amazon.com/intellij/") and [AWS Toolkit for compiling the application or running
   Eclipse](../../../toolkit-for-eclipse/v1/user-guide/welcome.md "../../../toolkit-for-eclipse/v1/user-guide/welcome.md").

## Download and examine the Apache Flink streaming Java

code

The application code for this example is available from GitHub.

###### To download the Java application code

1. Clone the remote repository using the following command:

```
git clone https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples.git
```

2. Navigate to the `./java/GettingStartedTable` directory.

### Review application components

The application is entirely implemented in the
`com.amazonaws.services.msf.BasicTableJob` class. The
`main()` method defines sources, transformations, and sinks. The
execution is initiated by an execution statement at the end of this
method.

###### Note

For an optimal developer experience, the application is designed to run
without any code changes both on Amazon Managed Service for Apache Flink and locally, for development in
your IDE.

- To read the runtime configuration so that it will work when running in
  Amazon Managed Service for Apache Flink and in your IDE, the application automatically detects if it's
  running standalone locally in the IDE. In that case, the application
  loads the runtime configuration differently:
  1.  When the application detects that it's running in standalone
      mode in your IDE, form the
      `application_properties.json` file included in
      the **resources** folder of the project. The
      content of the file follows.
  2.  When the application runs in Amazon Managed Service for Apache Flink, the default behavior
      loads the application configuration from the runtime properties
      you will define in the Amazon Managed Service for Apache Flink application. See [Create and configure the Managed Service for Apache Flink
      application](get-started-exercise.md#get-started-exercise-7 "get-started-exercise.md#get-started-exercise-7").

  ```
  private static Map<String, Properties> loadApplicationProperties(StreamExecutionEnvironment env) throws IOException {
      if (env instanceof LocalStreamEnvironment) {
          LOGGER.info("Loading application properties from '{}'", LOCAL_APPLICATION_PROPERTIES_RESOURCE);
          return KinesisAnalyticsRuntime.getApplicationProperties(
                  BasicStreamingJob.class.getClassLoader()
                          .getResource(LOCAL_APPLICATION_PROPERTIES_RESOURCE).getPath());
      } else {
          LOGGER.info("Loading application properties from Amazon Managed Service for Apache Flink");
          return KinesisAnalyticsRuntime.getApplicationProperties();
      }
  }
  ```

- The `main()` method defines the application data flow and
  runs it.
  - Initializes the default streaming environments. In this
    example, we show how to create both the
    `StreamExecutionEnvironment` to use with the
    DataStream API, and the `StreamTableEnvironment` to
    use with SQL and the Table API. The two environment objects are
    two separate references to the same runtime environment, to use
    different APIs.

  ```
  StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
  StreamTableEnvironment tableEnv = StreamTableEnvironment.create(env, EnvironmentSettings.newInstance().build());
  ```

  - Load the application configuration parameters. This will
    automatically load them from the correct place, depending on
    where the application is running:

  ```
  Map<String, Properties> applicationParameters = loadApplicationProperties(env);
  ```

  - The [FileSystem sink connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/filesystem/#streaming-sink "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/filesystem/#streaming-sink") that the application uses
    to write results to Amazon S3 output files when Flink
    completes a [checkpoint](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/stateful-stream-processing/#checkpointing "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/stateful-stream-processing/#checkpointing"). You must enable checkpoints to write
    files to the destination. When the application is running in
    Amazon Managed Service for Apache Flink, the application configuration controls the checkpoint
    and enables it by default. Conversely, when running locally,
    checkpoints are disabled by default. The application detects
    that it runs locally and configures checkpointing every 5,000
    ms.

  ```
   if (env instanceof LocalStreamEnvironment) {
      env.enableCheckpointing(5000);
   }
  ```

  - This application does not receive data from an actual external
    source. It generates random data to process through the [DataGen connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/datagen/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/datagen/"). This connector is available for
    DataStream API, SQL, and Table API. To demonstrate the
    integration between APIs, the application uses the DataStram API
    version because it provides more flexibility. Each record is
    generated by a generator function called
    `StockPriceGeneratorFunction` in this case, where
    you can put custom logic.

  ```
  DataGeneratorSource<StockPrice> source = new DataGeneratorSource<>(
          new StockPriceGeneratorFunction(),
          Long.MAX_VALUE,
          RateLimiterStrategy.perSecond(recordPerSecond),
          TypeInformation.of(StockPrice.class));
  ```

  - In the DataStream API, records can have custom classes.
    Classes must follow specific rules so that Flink can use them as
    record. For more information, see [Supported Data Types](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/fault-tolerance/serialization/types_serialization/#supported-data-types "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/fault-tolerance/serialization/types_serialization/#supported-data-types"). In this example, the
    `StockPrice` class is a [POJO](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/fault-tolerance/serialization/types_serialization/#pojos "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/dev/datastream/fault-tolerance/serialization/types_serialization/#pojos").
  - The source is then attached to the execution environment,
    generating a `DataStream` of `StockPrice`.
    This application doesn't use [event-time semantics](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/time/#notions-of-time-event-time-and-processing-time "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/concepts/time/#notions-of-time-event-time-and-processing-time") and doesn't generate a
    watermark. Run the DataGenerator source with a parallelism of 1,
    independent of the parallelism of the rest of the
    application.

  ```
  DataStream<StockPrice> stockPrices = env.fromSource(
          source,
          WatermarkStrategy.noWatermarks(),
          "data-generator"
      ).setParallelism(1);
  ```

  - What follows in the data processing flow is defined using the
    Table API and SQL. To do so, we convert the DataStream of
    StockPrices into a table. The schema of the table is
    automatically inferred from the `StockPrice` class.

  ```
  Table stockPricesTable = tableEnv.fromDataStream(stockPrices);
  ```

  - The following snippet of code shows how to define a view and a
    query using the programmatic Table API:

  ```
  Table filteredStockPricesTable = stockPricesTable.
          select(
                  $("eventTime").as("event_time"),
                  $("ticker"),
                  $("price"),
                  dateFormat($("eventTime"), "yyyy-MM-dd").as("dt"),
                  dateFormat($("eventTime"), "HH").as("hr")
          ).where($("price").isGreater(50));

  tableEnv.createTemporaryView("filtered_stock_prices", filteredStockPricesTable);
  ```

  - A sink table is defined to write the results to an
    Amazon S3 bucket as JSON files. To illustrate the
    difference with defining a view programmatically, with the Table
    API the sink table is defined using SQL.

  ```
  tableEnv.executeSql("CREATE TABLE s3_sink (" +
              "eventTime TIMESTAMP(3)," +
              "ticker STRING," +
              "price DOUBLE," +
              "dt STRING," +
              "hr STRING" +
          ") PARTITIONED BY ( dt, hr ) WITH (" +
          "'connector' = 'filesystem'," +
          "'fmat' = 'json'," +
          "'path' = 's3a://"  + s3Path + "'" +
          ")");
  ```

  - The last step of the is an `executeInsert()` that
    inserts the filtered stock prices view into the sink table. This
    method initiates the execution of the data flow we have defined
    so far.

  ```
  filteredStockPricesTable.executeInsert("s3_sink");
  ```

### Use the pom.xml file

The pom.xml file defines all dependencies required by the application and sets
up the Maven Shade plugin to build the fat-jar that contains all dependencies
required by Flink.

- Some dependencies have `provided` scope. These dependencies
  are automatically available when the application runs in Amazon Managed Service for Apache Flink. They
  are required for application or to the application locally in your
  IDE. For more information, see (update to TableAPI) [Run your application locally](get-started-exercise.md#get-started-exercise-5-run "get-started-exercise.md#get-started-exercise-5-run"). Make sure that you are
  using the same Flink version as the runtime you will use in Amazon Managed Service for Apache Flink.
  To use the TableAPI and SQL, you must include the
  `flink-table-planner-loader` and
  `flink-table-runtime-dependencies`, both with
  `provided` scope.

```
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-streaming-java</artifactId>
    <version>${flink.version}</version>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-clients</artifactId>
    <version>${flink.version}</version>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-table-planner-loader</artifactId>
    <version>${flink.version}</version>
    <scope>provided</scope>
</dependency>
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-table-runtime</artifactId>
    <version>${flink.version}</version>
    <scope>provided</scope>
</dependency>
```

- You must add additional Apache Flink dependencies to the pom with the
  default scope. For example, the [DataGen connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/datagen/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/datagen/"), the [FileSystem SQL connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/filesystem/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/filesystem/"), and the [JSON format](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/formats/json/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/formats/json/").

```
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-datagen</artifactId>
    <version>${flink.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-connector-files</artifactId>
    <version>${flink.version}</version>
</dependency>
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-json</artifactId>
    <version>${flink.version}</version>
</dependency>
```

- To write to Amazon S3 when running locally, the S3 Hadoop File
  System is also included wit `provided` scope.

```
<dependency>
    <groupId>org.apache.flink</groupId>
    <artifactId>flink-s3-fs-hadoop</artifactId>
    <version>${flink.version}</version>
    <scope>provided</scope>
</dependency>
```

- The Maven Java Compiler plugin makes sure that the code is compiled
  against Java 11, the JDK version currently supported by Apache Flink.
- The Maven Shade plugin packages the fat-jar, excluding some libraries that
  are provided by the runtime. It also specifies two transformers:
  `ServicesResourceTransformer` and
  `ManifestResourceTransformer`. The latter configures the
  class containing the `main` method to start the application. If
  you rename the main class, don't forget update this transformer.
- ```
  <plugin>
      <groupId>org.apache.maven.plugins</groupId>
      <artifactId>maven-shade-plugin</artifactId>
      ...
          <transformer implementation="org.apache.maven.plugins.shade.resource.ManifestResourceTransformer">
              <mainClass>com.amazonaws.services.msf.BasicStreamingJob</mainClass>
          </transformer>
      ...
  </plugin>
  ```

```

## Run your application locally


You can run and debug your Flink application locally in your IDE.


###### Note

Before you continue, verify that the input and output streams are available.
 See [Create two Amazon Kinesis data streams](get-started-exercise.md#get-started-exercise-1 "get-started-exercise.md#get-started-exercise-1"). Also, verify that you have permission to read
 and write from both streams. See [Authenticate your AWS
 session](get-started-exercise.md#get-started-exercise-2-5 "get-started-exercise.md#get-started-exercise-2-5").

Setting up the local development environment requires Java 11 JDK, Apache Maven,
 and an IDE for Java development. Verify you meet the required prerequisites. See
 [Fulfill the prerequisites for completing the
 exercises](getting-started.md#setting-up-prerequisites "getting-started.md#setting-up-prerequisites").


### Import the Java project into your IDE


To start working on the application in your IDE, you must import it as a Java
 project.


The repository you cloned contains multiple examples. Each example is a
 separate project. For this tutorial, import the content in the
 `./jave/GettingStartedTable` subdirectory into your IDE .


Insert the code as an existing Java project using Maven.


###### Note

The exact process to import a new Java project varies depending on the IDE
 you are using.


### Modify the local application configuration


When running locally, the application uses the configuration in the
 `application_properties.json` file in the resources folder of the
 project under `./src/main/resources`. For this tutorial application, the
 configuration parameters are the name of the bucket and the path where the data will
 be written.


Edit the configuration and modify the name of the Amazon S3 bucket to
 match the bucket that you created at the beginning of this tutorial.



```

[
{
"PropertyGroupId": "bucket",
"PropertyMap": {
"name": "`<bucket-name>`",
"path": "output"
}
}
]

```

###### Note

The configuration property `name` must contain only the bucket name,
 for example `my-bucket-name`. Don't include any prefix such as
 `s3://` or a trailing slash.

If you modify the path, omit any leading or trailing slashes.


### Set up your IDE run configuration


You can run and debug the Flink application from your IDE directly by running the
 main class `com.amazonaws.services.msf.BasicTableJob`, as you would run
 any Java application. Before running the application, you must set up the Run
 configuration. The setup depends on the IDE that you are using. For example, see
 [Run/debug configurations](https://www.jetbrains.com/help/idea/run-debug-configuration.html "https://www.jetbrains.com/help/idea/run-debug-configuration.html") in the IntelliJ IDEA documentation. In
 particular, you must set up the following:



1. **Add the `provided` dependencies to
 the classpath**. This is required to make sure that the
 dependencies with `provided` scope are passed to the
 application when running locally. Without this set up, the application
 displays a `class not found` error immediately.
2. **Pass the AWS credentials to access the Kinesis
 streams to the application**. The fastest way is to use
 [AWS Toolkit for
 IntelliJ IDEA](https://aws.amazon.com/intellij/ "https://aws.amazon.com/intellij/"). Using this IDE plugin in the Run
 configuration, you can select a specific AWS profile. AWS
 authentication happens using this profile. You don't need to pass AWS
 credentials directly.
3. Verify that the IDE runs the application using **JDK 11**.

### Run the application in your IDE


After you set up the Run configuration for the `BasicTableJob`, you can
 run or debug it like a regular Java application.


###### Note

You can't run the fat-jar generated by Maven directly with `java -jar
 ...` from the command line. This jar does not contain the Flink
 core dependencies required to run the application standalone.


When the application starts successfully, it logs some information about the
 standalone minicluster and the initialization of the connectors. This is
 followed by a number of INFO and some WARN logs that Flink normally emits when
 the application starts.



```

21:28:34,982 INFO com.amazonaws.services.msf.BasicTableJob  
 [] - Loading application properties from 'flink-application-properties-dev.json'
21:28:35,149 INFO com.amazonaws.services.msf.BasicTableJob  
[] - s3Path is ExampleBucket/my-output-bucket
...

```

After the initialization is complete, the application doesn't emit any further
 log entries. **While data is flowing, no log is
 emitted.**


To verify if the application is correctly processing data, you can inspect the
 content of the output bucket, as described in the following section.


###### Note

 Not emitting logs about flowing data is the normal behavior for a Flink
 application. Emitting logs on every record might be convenient for
 debugging, but can add considerable overhead when running in production.


## Observe the application writing data to an S3
 bucket


This example application generates random data internally and writes this data to the
 destination S3 bucket you configured. Unless you modified the default configuration
 path, the data will be written to the `output` path followed by data and hour
 partitioning, in the format `./output/<yyyy-MM-dd>/<HH>`.


The  [FileSystem sink connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/filesystem/#streaming-sink "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/filesystem/#streaming-sink") creates new files on the Flink checkpoint. When
 running locally, the application runs a checkpoint every 5 seconds (5,000 milliseconds),
 as specified in the code.



```

if (env instanceof LocalStreamEnvironment) {
env.enableCheckpointing(5000);
}

```

###### To browse the S3 bucket and observe the file written by the
 application

1. 1. Open the Amazon S3 console at
	 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket you previously created.
3. Navigate to the `output` path, and then to the date and hour
 folders that correspond to the current time in the UTC time zone.
4. Periodically refresh to observe new files appearing every 5
 seconds.
5. Select and download one file to observe the content.


###### Note

By default, the files have no extensions. The content is
 formatted as JSON. You can open the files with any text editor
 to inspect the content.

## Stop your application running locally


Stop the application running in your IDE. The IDE usually provides a "stop"
 option. The exact location and method depends on the IDE.


## Compile and package your application code


In this section, you use Apache Maven to compile the Java code and package it into
 a JAR file. You can compile and package your code using the Maven command line tool or
 your IDE.


**To compile and package using the Maven command
 line**


Move to the directory that contains the Jave GettingStarted project and run the
 following command:



```

$ mvn package

```

**To compile and package using your IDE**


Run `mvn package` from your IDE Maven integration.


In both cases, the JAR file `target/amazon-msf-java-table-app-1.0.jar` is
 created.


###### Note

Running a *build project* from your IDE might not create the
 JAR file.


## Upload the application code JAR file


In this section, you upload the JAR file you created in the previous section to
 the Amazon S3 bucket you created at the beginning of this tutorial. If you have done it yet,
 complete [Create an Amazon S3 bucket](#gs-table-resources-s3 "#gs-table-resources-s3").


###### To upload the application code

1. Open the Amazon S3 console at
 [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket you previously created for the application code.
3. Choose **Upload** field.
4. Choose **Add files**.
5. Navigate to the JAR file generated in the previous section:
 `target/amazon-msf-java-table-app-1.0.jar`.
6. Choose **Upload** without changing any other settings.


###### Warning

 Make sure that you select the correct JAR file in
 `<repo-dir>/java/GettingStarted/target/**amazon/msf-java-table-app-1.0.jar**`.

The target directory also contains other JAR files that you don't need to
 upload.

## Create and configure the Managed Service for Apache Flink
 application


You can create and configure a Managed Service for Apache Flink application using either the
 console or the AWS CLI. For this tutorial, you will use the console.


###### Note

When you create the application using the console, your AWS Identity and Access Management (IAM) and
 Amazon CloudWatch Logs resources are created for you. When you create the application using the
 AWS CLI, you must create these resources separately.


### Create the application


1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
2. Verify that the correct Region is selected: US East (N. Virginia)
 us-east-1.
3. On the right menu, choose **Apache Flink
 applications** and then choose **Create streaming
 application**. Alternatively, choose **Create streaming
 application** in the **Get started** section
 of the initial page.
4. On the **Create streaming application** page,
 complete the following:




	* For **Choose a method to set up the stream
	 processing application**, choose **Create from
	 scratch**.
	* For **Apache Flink configuration, Application
	 Flink version**, choose **Apache Flink
	 1.19**.
	* In the **Application configuration**
	 section, complete the following:




		+ For **Application name**, enter
		 `MyApplication`.
		+ For **Description**, enter `My
		 Java Table API test app`.
		+ For **Access to application resources**,
		 choose **Create / update IAM role
		 kinesis-analytics-MyApplication-us-east-1 with required
		 policies**.
	* In **Template for application settings**,
	 complete the following:




		+ For **Templates**, choose
		 **Develoment**.
5. Choose **Create streaming application**.

###### Note

When you create a Managed Service for Apache Flink application using the console, you have the option of
 having an IAM role and policy created for your application. Your
 application uses this role and policy to access its dependent resources.
 These IAM resources are named using your application name and Region
 as follows:


* Policy:
 `kinesis-analytics-service-`MyApplication`-`us-east-1``
* Role:
 `kinesisanalytics-`MyApplication`-`us-east-1``

### Edit the IAM policy


Edit the IAM policy to add permissions to access the Amazon S3 bucket.


###### To edit the IAM policy to add S3 bucket permissions

1. Open the IAM console at
 [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Policies**. Choose the
 **`kinesis-analytics-service-MyApplication-us-east-1`**
 policy that the console created for you in the previous section.
3. Choose **Edit** and then choose the
 **JSON** tab.
4. Add the highlighted section of the following policy example to the
 policy. Replace the sample account ID
 (`012345678901`) with your account ID and
 `<bucket-name>` with the name of the S3
 bucket that you created.



JSON





```

`{
 "Version":"2012-10-17", 
 "Statement": [
 {
 "Sid": "ReadCode",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:s3:::`amzn-s3-demo-bucket`/kinesis-analytics-placeholder-s3-object"
 ]
 },
 {
 "Sid": "ListCloudwatchLogGroups",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:*"
 ]
 },
 {
 "Sid": "ListCloudwatchLogStreams",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:*"
 ]
 },
 {
 "Sid": "PutCloudwatchLogs",
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:`us-east-1`:`123456789012`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:kinesis-analytics-log-stream"
 ]
 }`,
{
"Sid": "WriteOutputBucket",
"Effect": "Allow",
"Action": "s3:\*",
"Resource": [
"arn:aws:s3:::`amzn-s3-demo-bucket2`"
]
}`
 ]
}`

```
5. Choose **Next** and then choose **Save
 changes**.

### Configure the
 application


Edit the application to set the application code artifact.


###### To configure the application

1. On the **MyApplication** page, choose
 **Configure**.
2. In the **Aplication code location** section,
 choose **Configure**.




	* For **Amazon S3 bucket**, select the bucket
	 you previously created for the application code. Choose
	 **Browse** and select the correct bucket, and
	 then choose **Choose**. Don't click on the bucket
	 name.
	* For **Path to Amazon S3 object**, enter
	 `amazon-msf-java-table-app-1.0.jar`.
3. For **Access permissions**, choose
 **Create / update IAM role
 `kinesis-analytics-MyApplication-us-east-1`**.
4. In the **Runtime properties** section, add the
 following properties.
5. Choose **Add new item** and add each of the
 following parameters:




| Group ID | Key | Value |
| --- | --- | --- |
| `bucket` | `name` | `your-bucket-name` |
| `bucket` | `path` | `output` |
6. Don't modify any other setting.
7. Choose **Save changes**.

###### Note

When you choose to enable Amazon CloudWatch logging, Managed Service for Apache Flink creates a log group
 and log stream for you. The names of these resources are as follows:


* Log group:
 `/aws/kinesis-analytics/MyApplication`
* Log stream: `kinesis-analytics-log-stream`

### Run the application


The application is now configured and ready to run.


###### To run the application

1. Return to the console page in Amazon Managed Service for Apache Flink and choose
 **MyApplication**.
2. Choose **Run** to start the application.
3. On the **Application restore configuration**, choose
 **Run with latest snapshot**.
4. Choose **Run**.
5. The **Status** in **Application details** transitions from
 `Ready` to `Starting` and then to
 `Running` after the application has started.

When the application is in `Running` status, you can open the Flink
 dashboard.


###### To open the dashboard and view the job

1. Choose **Open Apache Flink dashbard**. The
 dashboard opens in a new page.
2. In the **Running Jobs** list, choose the single
 job you can see.


###### Note

If you set the runtime properties or edited the IAM policies
 incorrectly, the application status might change to
 `Running`, but the Flink dashboard shows the job continuously
 restarting. This is a common failure scenario when the application is
 misconfigured or lacks the permissions to access the external resources.

When this happens, check the **Exceptions** tab in
 the Flink dashboard to investigate the cause of the problem.

### Observe the metrics of
 the running application


On the **MyApplication** page, in the **Amazon
 CloudWatch metrics** section, you can see some of the fundamental metrics
 from the running application.


###### To view the metrics

1. Next to the **Refresh** button, select **10
 seconds** from the dropdown list.
2. When the application is running and healthy, you can see the
 **uptime** metric continuously increasing.
3. The **fullrestarts** metric should be zero. If it is
 increasing, the configuration might have issues. Review the
 **Exceptions** tab on the Flink dashboard to
 investigate the issue.
4. The **Number of failed checkpoints** metric should be
 zero in a healthy application.


###### Note

This dashboard displays a fixed set of metrics with a granularity
 of 5 minutes. You can create a custom application dashboard with any
 metrics in the CloudWatch dashboard.

### Observe the application writing data to the
 destination bucket


You can now observe the application running in Amazon Managed Service for Apache Flink writing files to
 Amazon S3.


To observe the files, follow the same process you used to check the files
 being written when the application was running locally. See [Observe the application writing data to an S3
 bucket](#gs-table-input-output "#gs-table-input-output").


Remember that the application writes new files on the Flink checkpoint. When
 running on Amazon Managed Service for Apache Flink, checkpoints are enabled by default and run every 60 seconds.
 The application creates new files approximately every 1 minute.


### Stop the application


To stop the applicatio, go to the console page of the Managed Service for Apache Flink application
 named `MyApplication`.


###### To stop the application

1. From the **Action** dropdown list, choose
 **Stop**.
2. The **Status** in **Application
 details** transitions from `Running` to
 `Stopping`, and then to `Ready` when the
 application is completely stopped.


###### Note

Don't forget to also stop sending data to the input stream from
 the Python script or the Kinesis Data Generator.
```
