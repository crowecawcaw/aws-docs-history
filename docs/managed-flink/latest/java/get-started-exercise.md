

# Create and run a Managed Service for Apache Flink application
<a name="get-started-exercise"></a>

In this step, you create a Managed Service for Apache Flink application with Kinesis data streams as a source and a sink.

**Topics**
+ [Create dependent resources](#get-started-exercise-0)
+ [Set up your local development environment](#get-started-exercise-2)
+ [Download and examine the Apache Flink streaming Java code](#get-started-exercise-5)
+ [Write sample records to the input stream](#get-started-exercise-5-4)
+ [Run your application locally](#get-started-exercise-5-run)
+ [Observe input and output data in Kinesis streams](#get-started-exercise-input-output)
+ [Stop your application running locally](#get-started-exercise-stop)
+ [Compile and package your application code](#get-started-exercise-5-5)
+ [Upload the application code JAR file](#get-started-exercise-6)
+ [Create and configure the Managed Service for Apache Flink application](#get-started-exercise-7)
+ [Next step](#get-started-exercise-next-step-4)

## Create dependent resources
<a name="get-started-exercise-0"></a>

Before you create a Managed Service for Apache Flink application for this exercise, you create the following dependent resources: 
+ Two Kinesis data streams for input and output
+ An Amazon S3 bucket to store the application's code
**Note**  
This tutorial assumes that you are deploying your application in the us-east-1 US East (N. Virginia) Region. If you use another Region, adapt all steps accordingly.

### Create two Amazon Kinesis data streams
<a name="get-started-exercise-1"></a>

Before you create a Managed Service for Apache Flink application for this exercise, create two Kinesis data streams (`ExampleInputStream` and `ExampleOutputStream`). Your application uses these streams for the application source and destination streams.

You can create these streams using either the Amazon Kinesis console or the following AWS CLI command. For console instructions, see [Creating and Updating Data Streams](https://docs.aws.amazon.com/kinesis/latest/dev/amazon-kinesis-streams.html) in the *Amazon Kinesis Data Streams Developer Guide*. To create the streams using the AWS CLI, use the following commands, adjusting to the Region you use for your application.

**To create the data streams (AWS CLI)**

1. To create the first stream (`ExampleInputStream`), use the following Amazon Kinesis `create-stream` AWS CLI command:

   ```
   $ aws kinesis create-stream \
   --stream-name ExampleInputStream \
   --shard-count 1 \
   --region us-east-1 \
   ```

1. To create the second stream that the application uses to write output, run the same command, changing the stream name to `ExampleOutputStream`:

   ```
   $ aws kinesis create-stream \
   --stream-name ExampleOutputStream \
   --shard-count 1 \
   --region us-east-1 \
   ```

### Create an Amazon S3 bucket for the application code
<a name="get-started-exercise-1-5"></a>

You can create the Amazon S3 bucket using the console. To learn how to create an Amazon S3 bucket using the console, see [Creating a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/create-bucket-overview.html) in the [Amazon S3 User Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/). Name the Amazon S3 bucket using a globally unique name, for example by appending your login name.

**Note**  
 Make sure that you create the bucket in the Region you use for this tutorial (us-east-1).

### Other resources
<a name="get-started-exercise-1-6"></a>

When you create your application, Managed Service for Apache Flink automatically creates the following Amazon CloudWatch resources if they don't already exist:
+ A log group called `/AWS/KinesisAnalytics-java/<my-application>`
+ A log stream called `kinesis-analytics-log-stream`

## Set up your local development environment
<a name="get-started-exercise-2"></a>

For development and debugging, you can run the Apache Flink application on your machine directly from your IDE of choice. Any Apache Flink dependencies are handled like regular Java dependencies using Apache Maven. 

**Note**  
On your development machine, you must have Java JDK 11, Maven, and Git installed. We recommend that you use a development environment such as [Eclipse Java Neon](https://www.eclipse.org/downloads/packages/release/neon/3) or [IntelliJ IDEA](https://www.jetbrains.com/idea/). To verify that you meet all prerequisites, see [Fulfill the prerequisites for completing the exercises](getting-started.md#setting-up-prerequisites). You **do not** need to install an Apache Flink cluster on your machine. 

### Authenticate your AWS session
<a name="get-started-exercise-2-5"></a>

The application uses Kinesis data streams to publish data. When running locally, you must have a valid AWS authenticated session with permissions to write to the Kinesis data stream. Use the following steps to authenticate your session:

1. If you don't have the AWS CLI and a named profile with valid credential configured, see [Set up the AWS Command Line Interface (AWS CLI)](setup-awscli.md).

1. Verify that your AWS CLI is correctly configured and your users have permissions to write to the Kinesis data stream by publishing the following test record:

   ```
   $ aws kinesis put-record --stream-name ExampleOutputStream --data TEST --partition-key TEST
   ```

1. If your IDE has a plugin to integrate with AWS, you can use it to pass the credentials to the application running in the IDE. For more information, see [AWS Toolkit for IntelliJ IDEA](https://aws.amazon.com/intellij/) and [AWS Toolkit for Eclipse](https://docs.aws.amazon.com/toolkit-for-eclipse/v1/user-guide/welcome.html).

## Download and examine the Apache Flink streaming Java code
<a name="get-started-exercise-5"></a>

The Java application code for this example is available from GitHub. To download the application code, do the following:

1. Clone the remote repository using the following command:

   ```
   git clone https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples.git
   ```

1. Navigate to the `amazon-managed-service-for-apache-flink-examples/tree/main/java/GettingStarted` directory.

### Review application components
<a name="get-started-exercise-5-1"></a>

The application is entirely implemented in the `com.amazonaws.services.msf.BasicStreamingJob` class. The `main()` method defines the data flow to process the streaming data and to run it. 

**Note**  
For an optimized developer experience, the application is designed to run without any code changes both on Amazon Managed Service for Apache Flink and locally, for development in your IDE.
+ To read the runtime configuration so it will work when running in Amazon Managed Service for Apache Flink and in your IDE, the application automatically detects if it's running standalone locally in the IDE. In that case, the application loads the runtime configuration differently:

  1. When the application detects that it's running in standalone mode in your IDE, form the `application_properties.json` file included in the **resources** folder of the project. The content of the file follows.

  1. When the application runs in Amazon Managed Service for Apache Flink, the default behavior loads the application configuration from the runtime properties you will define in the Amazon Managed Service for Apache Flink application. See [Create and configure the Managed Service for Apache Flink application](#get-started-exercise-7).

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
+ The `main()` method defines the application data flow and runs it. 
  + Initializes the default streaming environments. In this example, we show how to create both the `StreamExecutionEnvironment` to be used with the DataSteam API and the `StreamTableEnvironment` to be used with SQL and the Table API. The two environment objects are two separate references to the same runtime environment, to use different APIs. 

    ```
    StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();
    ```
  + Load the application configuration parameters. This will automatically load them from the correct place, depending on where the application is running:

    ```
    Map<String, Properties> applicationParameters = loadApplicationProperties(env);
    ```
  + The application defines a source using the [Kinesis Consumer](https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/connectors/datastream/kinesis/#kinesis-consumer) connector to read data from the input stream. The configuration of the input stream is defined in the `PropertyGroupId`=`InputStream0`. The name and Region of the stream are in the properties named `stream.name` and `aws.region` respectively. For simplicity, this source reads the records as a string. 

    ```
    private static FlinkKinesisConsumer<String> createSource(Properties inputProperties) {
        String inputStreamName = inputProperties.getProperty("stream.name");
        return new FlinkKinesisConsumer<>(inputStreamName, new SimpleStringSchema(), inputProperties);
    }
    ...
    
    public static void main(String[] args) throws Exception { 
       ...
       SourceFunction<String> source = createSource(applicationParameters.get("InputStream0"));
       DataStream<String> input = env.addSource(source, "Kinesis Source");  
       ...
    }
    ```
  + The application then defines a sink using the [Kinesis Streams Sink](https://nightlies.apache.org/flink/flink-docs-release-1.18/docs/connectors/datastream/kinesis/#kinesis-streams-sink) connector to send data to the output stream. Output stream name and Region are defined in the `PropertyGroupId`=`OutputStream0`, similar to the input stream. The sink is connected directly to the internal `DataStream` that is getting data from the source. In a real application, you have some transformation between source and sink. 

    ```
    private static KinesisStreamsSink<String> createSink(Properties outputProperties) {
        String outputStreamName = outputProperties.getProperty("stream.name");
        return KinesisStreamsSink.<String>builder()
                .setKinesisClientProperties(outputProperties)
                .setSerializationSchema(new SimpleStringSchema())
                .setStreamName(outputStreamName)
                .setPartitionKeyGenerator(element -> String.valueOf(element.hashCode()))
                .build();
    }
    ...
    public static void main(String[] args) throws Exception { 
       ...
       Sink<String> sink = createSink(applicationParameters.get("OutputStream0"));
       input.sinkTo(sink);
       ...
    }
    ```
  + Finally, you run the data flow that you just defined. This must be the last instruction of the `main()` method, after you defined all the operators the data flow requires:

    ```
    env.execute("Flink streaming Java API skeleton");
    ```

### Use the pom.xml file
<a name="get-started-exercise-5-2"></a>

The pom.xml file defines all dependencies required by the application and sets up the Maven Shade plugin to build the fat-jar that contains all dependencies required by Flink. 
+ Some dependencies have `provided` scope. These dependencies are automatically available when the application runs in Amazon Managed Service for Apache Flink. They are required to compile the application, or to run the application locally in your IDE. For more information, see [Run your application locally](#get-started-exercise-5-run). Make sure that you are using the same Flink version as the runtime you will use in Amazon Managed Service for Apache Flink.

  ```
  <dependency>
      <groupId>org.apache.flink</groupId>
      <artifactId>flink-clients</artifactId>
      <version>${flink.version}</version>
      <scope>provided</scope>
  </dependency>
  <dependency>
      <groupId>org.apache.flink</groupId>
      <artifactId>flink-streaming-java</artifactId>
      <version>${flink.version}</version>
      <scope>provided</scope>
  </dependency>
  ```
+ You must add additional Apache Flink dependencies to the pom with the default scope, such as the [Kinesis connector](https://nightlies.apache.org/flink/flink-docs-master/docs/connectors/datastream/kinesis/) used by this application. For more information, see [Use Apache Flink connectors](how-flink-connectors.md). You can also add any additional Java dependencies required by your application. 

  ```
  <dependency>
      <groupId>org.apache.flink</groupId>
      <artifactId>flink-connector-kinesis</artifactId>
      <version>${aws.connector.version}</version>
  </dependency>
  ```
+ The Maven Java Compiler plugin makes sure that the code is compiled against Java 11, the JDK version currently supported by Apache Flink. 
+ The Maven Shade plugin packages the fat-jar, excluding some libraries that are provided by the runtime. It also specifies two transformers: `ServicesResourceTransformer` and `ManifestResourceTransformer`. The latter configures the class containing the `main` method to start the application. If you rename the main class, don't forget to update this transformer.
+ 

  ```
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

## Write sample records to the input stream
<a name="get-started-exercise-5-4"></a>

In this section, you will send sample records to the stream for the application to process. You have two options for generating sample data, either using a Python script or the [Kinesis Data Generator](https://github.com/awslabs/amazon-kinesis-data-generator).

### Generate sample data using a Python script
<a name="get-started-exercise-5-4-1"></a>

You can use a Python script to send sample records to the stream.

**Note**  
To run this Python script, you must use Python 3.x and have the [AWS SDK for Python (Boto)](https://aws.amazon.com/developer/language/python/) library installed.

**To start sending test data to the Kinesis input stream:**

1. Download the data generator `stock.py` Python script from the [Data generator GitHub repository](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/data-generator).

1. Run the `stock.py` script:

   ```
   $ python stock.py
   ```

Keep the script running while you complete the rest of the tutorial. You can now run your Apache Flink application.

### Generate sample data using Kinesis Data Generator
<a name="get-started-exercise-5-4-2"></a>

Alternatively to using the Python script, you can use [Kinesis Data Generator](https://github.com/awslabs/amazon-kinesis-data-generator), also available in a [hosted version](https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html), to send random sample data to the stream. Kinesis Data Generator runs in your browser, and you don't need to install anything on your machine. 

**To set up and run Kinesis Data Generator:**

1. Follow the instructions in the [Kinesis Data Generator documentation](https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html) to set up access to the tool. You will run an CloudFormation template that sets up a user and password. 

1. Access Kinesis Data Generator through the URL generated by the CloudFormation template. You can find the URL in the **Output** tab after the CloudFormation template is completed. 

1. Configure the data generator:
   + **Region:** Select the Region that you are using for this tutorial: us-east-1
   + **Stream/delivery stream:** Select the input stream that the application will use: `ExampleInputStream`
   + **Records per second:** 100
   + **Record template:** Copy and paste the following template:

     ```
     {
       "event_time" : "{{date.now("YYYY-MM-DDTkk:mm:ss.SSSSS")}},
       "ticker" : "{{random.arrayElement(
             ["AAPL", "AMZN", "MSFT", "INTC", "TBV"]
         )}}",
       "price" : {{random.number(100)}}          
     }
     ```

1. Test the template: Choose **Test template** and verify that the generated record is similar to the following:

   ```
   { "event_time" : "2024-06-12T15:08:32.04800, "ticker" : "INTC", "price" : 7 }
   ```

1. Start the data generator: Choose **Select Send Data**.

Kinesis Data Generator is now sending data to the `ExampleInputStream`. 

## Run your application locally
<a name="get-started-exercise-5-run"></a>

You can run and debug your Flink application locally in your IDE.

**Note**  
Before you continue, verify that the input and output streams are available. See [Create two Amazon Kinesis data streams](#get-started-exercise-1). Also, verify that you have permission to read and write from both streams. See [Authenticate your AWS session](#get-started-exercise-2-5).   
Setting up the local development environment requires Java 11 JDK, Apache Maven, and and IDE for Java development. Verify you meet the required prerequisites. See [Fulfill the prerequisites for completing the exercises](getting-started.md#setting-up-prerequisites).

### Import the Java project into your IDE
<a name="get-started-exercise-5-run-1"></a>

To start working on the application in your IDE, you must import it as a Java project. 

The repository you cloned contains multiple examples. Each example is a separate project. For this tutorial, import the content in the `./java/GettingStarted` subdirectory into your IDE. 

Insert the code as an existing Java project using Maven.

**Note**  
The exact process to import a new Java project varies depending on the IDE you are using.

### Check the local application configuration
<a name="get-started-exercise-5-run-2"></a>

When running locally, the application uses the configuration in the `application_properties.json` file in the resources folder of the project under `./src/main/resources`. You can edit this file to use different Kinesis stream names or Regions.

```
[
  {
    "PropertyGroupId": "InputStream0",
    "PropertyMap": {
      "stream.name": "ExampleInputStream",
      "flink.stream.initpos": "LATEST",
      "aws.region": "us-east-1"
    }
  },
  {
    "PropertyGroupId": "OutputStream0",
    "PropertyMap": {
      "stream.name": "ExampleOutputStream",
      "aws.region": "us-east-1"
    }
  }
]
```

### Set up your IDE run configuration
<a name="get-started-exercise-5-run-3"></a>

You can run and debug the Flink application from your IDE directly by running the main class `com.amazonaws.services.msf.BasicStreamingJob`, as you would run any Java application. Before running the application, you must set up the Run configuration. The setup depends on the IDE you are using. For example, see [Run/debug configurations](https://www.jetbrains.com/help/idea/run-debug-configuration.html) in the IntelliJ IDEA documentation. In particular, you must set up the following:

1. **Add the `provided` dependencies to the classpath**. This is required to make sure that the dependencies with `provided` scope are passed to the application when running locally. Without this set up, the application displays a `class not found` error immediately. 

1. **Pass the AWS credentials to access the Kinesis streams to the application**. The fastest way is to use [AWS Toolkit for IntelliJ IDEA](https://aws.amazon.com/intellij/). Using this IDE plugin in the Run configuration, you can select a specific AWS profile. AWS authentication happens using this profile. You don't need to pass AWS credentials directly. 

1. Verify that the IDE runs the application using **JDK 11**.

### Run the application in your IDE
<a name="get-started-exercise-5-run-4"></a>

After you set up the Run configuration for the `BasicStreamingJob`, you can run or debug it like a regular Java application. 

**Note**  
You can't run the fat-jar generated by Maven directly with `java -jar ...` from the command line. This jar does not contain the Flink core dependencies required to run the application standalone.

When the application starts successfully, it logs some information about the standalone minicluster and the initialization of the connectors. This is followed by a number of INFO and some WARN logs that Flink normally emits when the application starts.

```
13:43:31,405 INFO  com.amazonaws.services.msf.BasicStreamingJob                 [] - Loading application properties from 'flink-application-properties-dev.json'
13:43:31,549 INFO  org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer [] - Flink Kinesis Consumer is going to read the following streams: ExampleInputStream, 
13:43:31,676 INFO  org.apache.flink.runtime.taskexecutor.TaskExecutorResourceUtils [] - The configuration option taskmanager.cpu.cores required for local execution is not set, setting it to the maximal possible value.
13:43:31,676 INFO  org.apache.flink.runtime.taskexecutor.TaskExecutorResourceUtils [] - The configuration option taskmanager.memory.task.heap.size required for local execution is not set, setting it to the maximal possible value.
13:43:31,676 INFO  org.apache.flink.runtime.taskexecutor.TaskExecutorResourceUtils [] - The configuration option taskmanager.memory.task.off-heap.size required for local execution is not set, setting it to the maximal possible value.
13:43:31,676 INFO  org.apache.flink.runtime.taskexecutor.TaskExecutorResourceUtils [] - The configuration option taskmanager.memory.network.min required for local execution is not set, setting it to its default value 64 mb.
13:43:31,676 INFO  org.apache.flink.runtime.taskexecutor.TaskExecutorResourceUtils [] - The configuration option taskmanager.memory.network.max required for local execution is not set, setting it to its default value 64 mb.
13:43:31,676 INFO  org.apache.flink.runtime.taskexecutor.TaskExecutorResourceUtils [] - The configuration option taskmanager.memory.managed.size required for local execution is not set, setting it to its default value 128 mb.
13:43:31,677 INFO  org.apache.flink.runtime.minicluster.MiniCluster             [] - Starting Flink Mini Cluster
....
```

After the initialization is complete, the application doesn't emit any further log entries. **While data is flowing, no log is emitted.**

To verify if the application is correctly processing data, you can inspect the input and output Kinesis streams, as described in the following section.

**Note**  
 Not emitting logs about flowing data is the normal behavior for a Flink application. Emitting logs on every record might be convenient for debugging, but can add considerable overhead when running in production. 

## Observe input and output data in Kinesis streams
<a name="get-started-exercise-input-output"></a>

You can observe records sent to the input stream by the (generating sample Python) or the Kinesis Data Generator (link) by using the **Data Viewer** in the Amazon Kinesis console. 

**To observe records**

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. Verify that the Region is the same where you are running this tutorial, which is us-east-1 US East (N. Virginia) by default. Change the Region if it does not match. 

1. Choose **Data Streams**. 

1. Select the stream that you want to observe, either `ExampleInputStream` or `ExampleOutputStream.`

1. Choose the **Data viewer** tab. 

1. Choose any **Shard**, keep **Latest** as **Starting position**, and then choose **Get records**. You might see a "No record found for this request" error. If so, choose **Retry getting records**. The newest records published to the stream display. 

1. Choose the value in the Data column to inspect the content of the record in JSON format.

## Stop your application running locally
<a name="get-started-exercise-stop"></a>

Stop the application running in your IDE. The IDE usually provides a "stop" option. The exact location and method depends on the IDE you're using. 

## Compile and package your application code
<a name="get-started-exercise-5-5"></a>

In this section, you use Apache Maven to compile the Java code and package it into a JAR file. You can compile and package your code using the Maven command line tool or your IDE.

**To compile and package using the Maven command line:**

Move to the directory containing the Java GettingStarted project and run the following command:

```
$ mvn package
```

**To compile and package using your IDE:**

Run `mvn package` from your IDE Maven integration.

In both cases, the following JAR file is created: `target/amazon-msf-java-stream-app-1.0.jar`.

**Note**  
 Running a "build project" from your IDE might not create the JAR file.

## Upload the application code JAR file
<a name="get-started-exercise-6"></a>

In this section, you upload the JAR file you created in the previous section to the Amazon Simple Storage Service (Amazon S3) bucket you created at the beginning of this tutorial. If you have not completed this step, see (link).

**To upload the application code JAR file**

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/).

1. Choose the bucket you previously created for the application code.

1. Choose **Upload**.

1. Choose **Add files**.

1. Navigate to the JAR file generated in the previous step: `target/amazon-msf-java-stream-app-1.0.jar`. 

1. Choose **Upload** without changing any other settings.

**Warning**  
Make sure that you select the correct JAR file in `<repo-dir>/java/GettingStarted/target/amazon-msf-java-stream-app-1.0.jar`.   
The `target` directory also contains other JAR files that you don't need to upload.

## Create and configure the Managed Service for Apache Flink application
<a name="get-started-exercise-7"></a>

You can create and run a Managed Service for Apache Flink application using either the console or the AWS CLI. For this tutorial, you will use the console. 

**Note**  
When you create the application using the console, your AWS Identity and Access Management (IAM) and Amazon CloudWatch Logs resources are created for you. When you create the application using the AWS CLI, you create these resources separately.

**Topics**
+ [Create the application](#get-started-exercise-7-console-create)
+ [Edit the IAM policy](#get-started-exercise-7-console-iam)
+ [Configure the application](#get-started-exercise-7-console-configure)
+ [Run the application](#get-started-exercise-7-console-run)
+ [Observe the metrics of the running application](#get-started-exercise-7-console-stop)
+ [Observe output data in Kinesis streams](#get-started-exercise-7-console-output)
+ [Stop the application](#get-started-exercise-stop)

### Create the application
<a name="get-started-exercise-7-console-create"></a>

**To create the application**

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.

1. Verify that the correct Region is selected: us-east-1 US East (N. Virginia)

1. Open the menu on the right and choose **Apache Flink applications** and then **Create streaming application**. Alternatively, choose **Create streaming application** in the Get started container of the initial page. 

1. On the **Create streaming application** page:
   + **Choose a method to set up the stream processing application:** choose **Create from scratch**.
   + **Apache Flink configuration, Application Flink version:** choose **Apache Flink 1.20**.

1. Configure your application
   + **Application name:** enter **MyApplication**.
   + **Description:** enter **My java test app**.
   + **Access to application resources:** choose **Create / update IAM role `kinesis-analytics-MyApplication-us-east-1` with required policies**.

1. Configure your **Template for application settings**
   + **Templates:** choose **Development**.

1. Choose **Create streaming application** at the bottom of the page.

**Note**  
When you create a Managed Service for Apache Flink application using the console, you have the option of having an IAM role and policy created for your application. Your application uses this role and policy to access its dependent resources. These IAM resources are named using your application name and Region as follows:  
Policy: `kinesis-analytics-service-{{MyApplication}}-{{us-east-1}}`
Role: `kinesisanalytics-{{MyApplication}}-{{us-east-1}}`
Amazon Managed Service for Apache Flink was formerly known as Kinesis Data Analytics. The name of the resources that are automatically created is prefixeed with `kinesis-analytics-` for backward compatibility.

### Edit the IAM policy
<a name="get-started-exercise-7-console-iam"></a>

Edit the IAM policy to add permissions to access the Kinesis data streams.

**To edit the policy**

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

1. Choose **Policies**. Choose the **`kinesis-analytics-service-MyApplication-us-east-1`** policy that the console created for you in the previous section. 

1. Choose **Edit** and then choose the **JSON** tab.

1. Add the highlighted section of the following policy example to the policy. Replace the sample account IDs ({{012345678901}}) with your account ID.

------
#### [ JSON ]

****  

   ```
   {
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
                   "arn:aws:s3:::my-bucket/kinesis-analytics-placeholder-s3-object"
               ]
           },
           {
               "Sid": "ListCloudwatchLogGroups",
               "Effect": "Allow",
               "Action": [
                   "logs:DescribeLogGroups"
               ],
               "Resource": [
                   "arn:aws:logs:us-east-1:{{012345678901}}:log-group:*"
               ]
           },
           {
               "Sid": "ListCloudwatchLogStreams",
               "Effect": "Allow",
               "Action": [
                   "logs:DescribeLogStreams"
               ],
               "Resource": [
                   "arn:aws:logs:us-east-1:{{012345678901}}:log-group:/aws/kinesis-analytics/MyApplication:log-stream:*"
               ]
           },
           {
               "Sid": "PutCloudwatchLogs",
               "Effect": "Allow",
               "Action": [
                   "logs:PutLogEvents"
               ],
               "Resource": [
                   "arn:aws:logs:us-east-1:{{012345678901}}:log-group:/aws/kinesis-analytics/MyApplication:log-stream:kinesis-analytics-log-stream"
               ]
           }{{,
           {
               "Sid": "ReadInputStream",
               "Effect": "Allow",
               "Action": "kinesis:*",
               "Resource": "arn:aws:kinesis:us-east-1:{{012345678901}}:stream/ExampleInputStream"
           },
           {
               "Sid": "WriteOutputStream",
               "Effect": "Allow",
               "Action": "kinesis:*",
               "Resource": "arn:aws:kinesis:us-east-1:{{012345678901}}:stream/ExampleOutputStream"
           }}}
       ]
   }
   ```

------

1.  Choose **Next** at the bottom of the page and then choose **Save changes**.

### Configure the application
<a name="get-started-exercise-7-console-configure"></a>

Edit the application configuration to set the application code artifact.

**To edit the configuration**

1. On the **MyApplication** page, choose **Configure**.

1. In the **Application code location** section:
   + For **Amazon S3 bucket**, select the bucket you previously created for the application code. Choose **Browse** and select the correct bucket, and then select **Choose**. Do not click on the bucket name.
   + For **Path to Amazon S3 object**, enter **amazon-msf-java-stream-app-1.0.jar**.

1. For **Access permissions**, choose **Create / update IAM role `kinesis-analytics-MyApplication-us-east-1` with required policies**.

1. In the **Runtime properties** section, add the following properties.

1. Choose **Add new item** and add each of the following parameters:    
[See the AWS documentation website for more details](http://docs.aws.amazon.com/managed-flink/latest/java/get-started-exercise.html)

1. Do not modify any of the other sections.

1. Choose **Save changes**.

**Note**  
When you choose to enable Amazon CloudWatch logging, Managed Service for Apache Flink creates a log group and log stream for you. The names of these resources are as follows:   
Log group: `/aws/kinesis-analytics/MyApplication`
Log stream: `kinesis-analytics-log-stream`

### Run the application
<a name="get-started-exercise-7-console-run"></a>

The application is now configured and ready to run.

**To run the application**

1. On the console for Amazon Managed Service for Apache Flink, choose **My Application** and choose **Run**.

1. On the next page, the Application restore configuration page, choose **Run with latest snapshot** and then choose **Run**. 

   The **Status** in **Application details** transitions from `Ready` to `Starting` and then to `Running` when the application has started.

When the application is in the `Running` status, you can now open the Flink dashboard. 

**To open the dashboard**

1. Choose **Open Apache Flink dashboard**. The dashboard opens on a new page.

1. In the **Runing jobs** list, choose the single job that you can see. 
**Note**  
If you set the Runtime properties or edited the IAM policies incorrectly, the application status might turn into `Running`, but the Flink dashboard shows that the job is continuously restarting. This is a common failure scenario if the application is misconfigured or lacks permissions to access the external resources.   
When this happens, check the **Exceptions** tab in the Flink dashboard to see the cause of the problem.

### Observe the metrics of the running application
<a name="get-started-exercise-7-console-stop"></a>

On the **MyApplication** page, in the **Amazon CloudWatch metrics** section, you can see some of the fundamental metrics from the running application. 

**To view the metrics**

1. Next to the **Refresh** button, select **10 seconds** from the dropdown list.

1. When the application is running and healthy, you can see the **uptime** metric continuously increasing.

1. The **fullrestarts** metric should be zero. If it is increasing, the configuration might have issues. To investigate the issue, review the **Exceptions** tab on the Flink dashboard.

1. The **Number of failed checkpoints** metric should be zero in a healthy application. 
**Note**  
This dashboard displays a fixed set of metrics with a granularity of 5 minutes. You can create a custom application dashboard with any metrics in the CloudWatch dashboard.

### Observe output data in Kinesis streams
<a name="get-started-exercise-7-console-output"></a>

Make sure you are still publishing data to the input, either using the Python script or the Kinesis Data Generator. 

You can now observe the output of the application running on Managed Service for Apache Flink by using the Data Viewer in the [https://console.aws.amazon.com/kinesis/](https://console.aws.amazon.com/kinesis/), similarly to what you already did earlier. 

**To view the output**

1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis).

1. Verify that the Region is the same as the one you are using to run this tutorial. By default, it is us-east-1US East (N. Virginia). Change the Region if necessary.

1. Choose **Data Streams**. 

1. Select the stream that you want to observe. For this tutorial, use `ExampleOutputStream`. 

1.  Choose the **Data viewer** tab. 

1. Select any **Shard**, keep **Latest** as **Starting position**, and then choose **Get records**. You might see a "no record found for this request" error. If so, choose **Retry getting records**. The newest records published to the stream display.

1. Select the value in the Data column to inspect the content of the record in JSON format.

### Stop the application
<a name="get-started-exercise-stop"></a>

To stop the applicatio, go to the console page of the Managed Service for Apache Flink application named `MyApplication`.

**To stop the application**

1. From the **Action** dropdown list, choose **Stop**.

1. The **Status** in **Application details** transitions from `Running` to `Stopping`, and then to `Ready` when the application is completely stopped. 
**Note**  
Don't forget to also stop sending data to the input stream from the Python script or the Kinesis Data Generator.

## Next step
<a name="get-started-exercise-next-step-4"></a>

[Clean up AWS resources](getting-started-cleanup.md)