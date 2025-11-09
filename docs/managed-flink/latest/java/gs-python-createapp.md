Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Create and run a Managed Service for Apache Flink for Python

application

In this section, you create a Managed Service for Apache Flink application for Python application with a Kinesis stream as a
source and a sink.

###### This section contains the following steps.

- [Create dependent resources](#gs-python-resources "#gs-python-resources")
- [Set up your local development
  environment](#gs-python-set-up "#gs-python-set-up")
- [Download and examine the Apache Flink streaming
  Python code](#gs-python-download "#gs-python-download")
- [Manage JAR dependencies](#gs-python-jar-dependencies "#gs-python-jar-dependencies")
- [Write sample records to the input stream](#gs-python-sample-records "#gs-python-sample-records")
- [Run your application locally](#gs-python-run-locally "#gs-python-run-locally")
- [Observe input and output data in Kinesis streams](#gs-python-observe-input-output "#gs-python-observe-input-output")
- [Stop your application running locally](#gs-python-stop "#gs-python-stop")
- [Package your application code](#gs-python-package-code "#gs-python-package-code")
- [Upload the application package to an Amazon S3
  bucket](#gs-python-upload-bucket "#gs-python-upload-bucket")
- [Create and configure the Managed Service for Apache Flink
  application](#gs-python-7 "#gs-python-7")
- [Next step](#gs-python-next-step-4 "#gs-python-next-step-4")

## Create dependent resources

Before you create a Managed Service for Apache Flink for this exercise, you create the following
dependent resources:

- Two Kinesis streams for input and output.
- An Amazon S3 bucket to store the application's code.

###### Note

This tutorial assumes that you are deploying your application in the
us-east-1 Region. If you use another Region, you must adapt all steps
accordingly.

### Create two Kinesis streams

Before you create a Managed Service for Apache Flink application for this exercise, create two Kinesis data streams
(`ExampleInputStream` and `ExampleOutputStream`) in
the same Region you will use to deploy your application (us-east-1 in
this example). Your application uses these streams for the application source
and destination streams.

You can create these streams using either the Amazon Kinesis console or the following
AWS CLI command. For console instructions, see [Creating and Updating Data
Streams](../../../kinesis/latest/dev/amazon-kinesis-streams.md "../../../kinesis/latest/dev/amazon-kinesis-streams.md") in the _Amazon Kinesis Data Streams Developer Guide_.

###### To create the data streams (AWS CLI)

1. To create the first stream (`ExampleInputStream`), use the
   following Amazon Kinesis `create-stream` AWS CLI command.

```
$ aws kinesis create-stream \
--stream-name ExampleInputStream \
--shard-count 1 \
--region us-east-1
```

2. To create the second stream that the application uses to write output, run
   the same command, changing the stream name to
   `ExampleOutputStream`.

```
$ aws kinesis create-stream \
--stream-name ExampleOutputStream \
--shard-count 1 \
--region us-east-1
```

### Create an Amazon S3 bucket

You can create the Amazon S3 bucket using the console. For instructions for
creating this resource, see the following topics:

- [How Do I Create an S3
  Bucket?](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md") in the _Amazon Simple Storage Service User Guide_. Give the
  Amazon S3 bucket a globally unique name, for example by appending your login
  name.

###### Note

Make sure that you create the S3 bucket in the Region you use for
this tutorial (us-east-1).

### Other resources

When you create your application, Managed Service for Apache Flink creates the following Amazon CloudWatch resources if they don't already
exist:

- A log group called
  `/AWS/KinesisAnalytics-java/<my-application>`.
- A log stream called `kinesis-analytics-log-stream`.

## Set up your local development

environment

For development and debugging, you can run the Python Flink application on your
machine. You can start the application from the command line with `python
 main.py` or in a Python IDE of your choice.

###### Note

On your development machine, you must have Python 3.10 or 3.11, Java 11,
Apache Maven, and Git installed. We recommend that you use an IDE such as [PyCharm](https://www.jetbrains.com/pycharm/ "https://www.jetbrains.com/pycharm/") or [Visual Studio Code](https://code.visualstudio.com/ "https://code.visualstudio.com/"). To verify
that you meet all prerequisites, see [Fulfill the prerequisites for completing the
exercises](gs-python.md#gs-python-prerequisites "gs-python.md#gs-python-prerequisites") before you proceed.

### Install the PyFlink library

To develop your application and run it locally, you must install the Flink
Python library.

1. Create a standalone Python environment using VirtualEnv, Conda, or any
   similar Python tool.
2. Install the PyFlink library in that environment. Use the same Apache
   Flink runtime version that you will use in Amazon Managed Service for Apache Flink. Currently, the
   recommended runtime is 1.19.1.

```
$ pip install apache-flink==1.19.1
```

3. Make sure that the environment is active when you run your
   application. If you run the application in the IDE, make sure that the
   IDE is using the environment as runtime. The process depends on the IDE
   that you are using.

###### Note

You only need to install the PyFlink library. You **do not** need to install an Apache Flink
cluster on your machine.

### Authenticate your AWS

session

The application uses Kinesis data streams to publish data. When running locally,
you must have a valid AWS authenticated session with permissions to write to
the Kinesis data stream. Use the following steps to authenticate your
session:

1. If you don't have the AWS CLI and a named profile with valid credential
   configured, see [Set up the AWS Command Line Interface (AWS CLI)](setup-awscli.md "setup-awscli.md").
2. Verify that your AWS CLI is correctly configured and your users have
   permissions to write to the Kinesis data stream by publishing the following
   test record:

```
$ aws kinesis put-record --stream-name ExampleOutputStream --data TEST --partition-key TEST
```

3. If your IDE has a plugin to integrate with AWS, you can use it to
   pass the credentials to the application running in the IDE. For more
   information, see [AWS
   Toolkit for PyCharm](https://aws.amazon.com/pycharm/ "https://aws.amazon.com/pycharm/"), [AWS Toolkit for
   Visual Studio Code](https://aws.amazon.com/visualstudiocode/ "https://aws.amazon.com/visualstudiocode/"), and [AWS Toolkit for IntelliJ
   IDEA](https://aws.amazon.com/intellij/ "https://aws.amazon.com/intellij/").

## Download and examine the Apache Flink streaming

Python code

The Python application code for this example is available from GitHub. To download
the application code, do the following:

1. Clone the remote repository using the following command:

```
git clone https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples.git
```

2. Navigate to the `./python/GettingStarted` directory.

### Review application components

The application code is located in `main.py`. We use SQL embedded
in Python to define the flow of the application.

###### Note

For an optimized developer experience, the application is designed to run
without any code changes both on Amazon Managed Service for Apache Flink and locally, for development on
your machine. The application uses the environment variable `IS_LOCAL =
 true` to detect when it is running locally. You must set the
environment variable `IS_LOCAL = true` either on your shell or in
the run configuration of your IDE.

- The application sets up the execution environment and reads the
  runtime configuration. To work both on Amazon Managed Service for Apache Flink and locally, the
  application checks the `IS_LOCAL` variable.
  - The following is the default behavior when the application
    runs in Amazon Managed Service for Apache Flink:
    1. Load dependencies packaged with the application. For
       more information, see (link)
    2. Load the configuration from the Runtime properties you
       define in the Amazon Managed Service for Apache Flink application. For more
       information, see (link)

  - When the application detects `IS_LOCAL = true` when
    you run your application locally:
    1. Loads external dependencies from the project.
    2. Loads the configuration from the
       `application_properties.json` file
       included in the project.

    ```
    ...
    APPLICATION_PROPERTIES_FILE_PATH = "/etc/flink/application_properties.json"
    ...
    is_local = (
        True if os.environ.get("IS_LOCAL") else False
    )
    ...
    if is_local:
        APPLICATION_PROPERTIES_FILE_PATH = "application_properties.json"
        CURRENT_DIR = os.path.dirname(os.path.realpath(__file__))
        table_env.get_config().get_configuration().set_string(
            "pipeline.jars",
            "file:///" + CURRENT_DIR + "/target/pyflink-dependencies.jar",
        )
    ```

- The application defines a source table with a `CREATE
TABLE` statement, using the [Kinesis Connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/kinesis/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/kinesis/"). This table reads data from the input
  Kinesis stream. The application takes the name of the stream, the Region,
  and initial position from the runtime configuration.

```
table_env.execute_sql(f"""
        CREATE TABLE prices (
                ticker VARCHAR(6),
                price DOUBLE,
                event_time TIMESTAMP(3),
                WATERMARK FOR event_time AS event_time - INTERVAL '5' SECOND
              )
              PARTITIONED BY (ticker)
              WITH (
                'connector' = 'kinesis',
                'stream' = '{input_stream_name}',
                'aws.region' = '{input_stream_region}',
                'format' = 'json',
                'json.timestamp-format.standard' = 'ISO-8601'
              ) """)
```

- The application also defines a sink table using the [Kinesis Connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/kinesis/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/kinesis/") in this example. This tale sends data to
  the output Kinesis stream.

```
table_env.execute_sql(f"""
            CREATE TABLE output (
                ticker VARCHAR(6),
                price DOUBLE,
                event_time TIMESTAMP(3)
              )
              PARTITIONED BY (ticker)
              WITH (
                'connector' = 'kinesis',
                'stream' = '{output_stream_name}',
                'aws.region' = '{output_stream_region}',
                'sink.partitioner-field-delimiter' = ';',
                'sink.batch.max-size' = '100',
                'format' = 'json',
                'json.timestamp-format.standard' = 'ISO-8601'
              )""")
```

- Finally, the application executes a SQL that `INSERT
INTO...` the sink table from the source table. In a more
  complex application, you likely have additional steps transforming data
  before writing to the sink.

```
table_result = table_env.execute_sql("""INSERT INTO output
        SELECT ticker, price, event_time FROM prices""")
```

- You must add another step at the end of the `main()`
  function to run the application locally:

```
if is_local:
    table_result.wait()
```

Without this statement, the application terminates immediately when
you run it locally. You must not execute this statement when you run
your application in Amazon Managed Service for Apache Flink.

## Manage JAR dependencies

A PyFlink application usually requires one or more connectors. The application in
this tutorial uses the [Kinesis Connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/kinesis/ "https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/table/kinesis/"). Because Apache Flink runs in the Java JVM,
connectors are distributed as JAR files, regardless if you implement your
application in Python. You must package these dependencies with the application when
you deploy it on Amazon Managed Service for Apache Flink.

In this example, we show how to use Apache Maven to fetch the dependencies and
package the application to run on Managed Service for Apache Flink.

###### Note

There are alternative ways to fetch and package dependencies. This example
demonstrates a method that works correctly with one or more connectors. It also
lets you run the application locally, for development, and on Managed Service for Apache Flink without code
changes.

### Use the pom.xml file

Apache Maven uses the `pom.xml` file to control dependencies and
application packaging.

Any JAR dependencies are specified in the `pom.xml` file in the
`<dependencies>...</dependencies>` block.

```
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>
    ...
    <dependencies>
        <dependency>
            <groupId>org.apache.flink</groupId>
            <artifactId>flink-connector-kinesis</artifactId>
            <version>4.3.0-1.19</version>
        </dependency>
    </dependencies>
    ...
```

To find the correct artifact and version of connector to use, see [Use Apache Flink connectors with Managed Service for Apache Flink](how-flink-connectors.md "how-flink-connectors.md"). Make sure
that you refer to the version of Apache Flink you are using. For this example, we
use the Kinesis connector. For Apache Flink 1.19, the connector version is
`4.3.0-1.19`.

###### Note

If you are using Apache Flink 1.19, there is no connector version released
specifically for this version. Use the connectors released for 1.18.

### Download and package

dependencies

Use Maven to download the dependencies defined in the `pom.xml`
file and package them for the Python Flink application.

1. Navigate to the directory that contains the Python Getting Started
   project called `python/GettingStarted`.
2. Run the following command:

```
$ mvn package
```

Maven creates a new file called
`./target/pyflink-dependencies.jar`. When you are developing locally
on your machine, the Python application looks for this file.

###### Note

If you forget to run this command, when you try to run your application,
it will fail with the error: **Could not find any factory for
identifier "kinesis**.

## Write sample records to the input stream

In this section, you will send sample records to the stream for the application to
process. You have two options for generating sample data, either using a Python
script or the [Kinesis Data Generator](https://github.com/awslabs/amazon-kinesis-data-generator "https://github.com/awslabs/amazon-kinesis-data-generator").

### Generate sample data using a Python

script

You can use a Python script to send sample records to the stream.

###### Note

To run this Python script, you must use Python 3.x and have the [AWS SDK for
Python (Boto)](https://aws.amazon.com/developer/language/python/ "https://aws.amazon.com/developer/language/python/") library installed.

**To start sending test data to the Kinesis input stream:**

1. Download the data generator `stock.py` Python script from
   the [Data generator GitHub repository](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/data-generator "https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/python/data-generator").
2. Run the `stock.py` script:

```
$ python stock.py
```

Keep the script running while you complete the rest of the
tutorial. You can now run your Apache Flink application.

### Generate sample data using Kinesis

Data Generator

Alternatively to using the Python script, you can use [Kinesis Data
Generator](https://github.com/awslabs/amazon-kinesis-data-generator "https://github.com/awslabs/amazon-kinesis-data-generator"), also available in a [hosted version](https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html "https://awslabs.github.io/amazon-kinesis-data-generator/web/producer.html"), to send random sample data to the stream. Kinesis Data
Generator runs in your browser, and you don't need to install anything on your
machine.

**To set up and run Kinesis Data Generator:**

1. Follow the instructions in the [Kinesis Data Generator documentation](https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html "https://awslabs.github.io/amazon-kinesis-data-generator/web/help.html") to set up access to
   the tool. You will run an AWS CloudFormation template that sets up a user and
   password.
2. Access Kinesis Data Generator through the URL generated by the CloudFormation
   template. You can find the URL in the **Output** tab
   after the CloudFormation template is completed.
3. Configure the data generator:
   - **Region:** Select the Region
     that you are using for this tutorial:
     us-east-1
   - **Stream/delivery stream:**
     Select the input stream that the application will use:
     `ExampleInputStream`
   - **Records per second:**
     100
   - **Record template:** Copy and
     paste the following template:

   ```
   {
     "event_time" : "{{date.now("YYYY-MM-DDTkk:mm:ss.SSSSS")}},
     "ticker" : "{{random.arrayElement(
           ["AAPL", "AMZN", "MSFT", "INTC", "TBV"]
       )}}",
     "price" : {{random.number(100)}}
   }
   ```

4. Test the template: Choose **Test template** and
   verify that the generated record is similar to the following:

```
{ "event_time" : "2024-06-12T15:08:32.04800, "ticker" : "INTC", "price" : 7 }
```

5. Start the data generator: Choose **Select Send
   Data**.

Kinesis Data Generator is now sending data to the
`ExampleInputStream`.

## Run your application locally

You can test the application locally, running from the command line with
`python main.py` or from your IDE.

To run your application locally, you must have the correct version of the PyFlink
library installed as described in the previous section. For more information, see
(link)

###### Note

Before you continue, verify that the input and output streams are available.
See [Create two Amazon Kinesis data streams](get-started-exercise.md#get-started-exercise-1 "get-started-exercise.md#get-started-exercise-1"). Also, verify that you have permission to read
and write from both streams. See [Authenticate your AWS
session](get-started-exercise.md#get-started-exercise-2-5 "get-started-exercise.md#get-started-exercise-2-5").

### Import the Python project into your

IDE

To start working on the application in your IDE, you must import it as a
Python project.

The repository you cloned contains multiple examples. Each example is a
separate project. For this tutorial, import the content in the
`./python/GettingStarted` subdirectory into your IDE.

Import the code as an existing Python project.

###### Note

The exact process to import a new Python project varies depending on the
IDE you are using.

### Check the local application configuration

When running locally, the application uses the configuration in the
`application_properties.json` file in the resources folder of the
project under `./src/main/resources`. You can edit this file to use
different Kinesis stream names or Regions.

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

### Run your Python application

locally

You can run your application locally, either from the command line as a
regular Python script, or from the IDE.

###### To run your application from the command line

1. Make sure that the standalone Python environment such as Conda or
   VirtualEnv where you installed the Python Flink library is currently
   active.
2. Make sure that you ran `mvn package` at least one time.
3. Set the `IS_LOCAL = true` environment variable:

```
$ export IS_LOCAL=true
```

4. Run the application as a regular Python script.

```
$python main.py
```

###### To run the application from within the IDE

1. Configure your IDE to run the `main.py` script with the
   following configuration:
   1. Use the standalone Python environment such as Conda or
      VirtualEnv where you installed the PyFlink library.
   2. Use the AWS credentials to access the input and output Kinesis
      data streams.
   3. Set `IS_LOCAL = true`.

2. The exact process to set the run configuration depends on your IDE and
   varies.
3. When you have set up your IDE, run the Python script and use the
   tooling provided by your IDE while the application is running.

### Inspect application logs locally

When running locally, the application does not show any log in the console,
aside from a few lines printed and displayed when the application starts.
PyFlink writes logs to a file in the directory where the Python Flink library is
installed. The application prints the location of the logs when it starts. You
can also run the following command to find the logs:

```
$ python -c "import pyflink;import os;print(os.path.dirname(os.path.abspath(pyflink.__file__))+'/log')"
```

1. List the files in the logging directory. You usually find a single
   `.log` file.
2. Tail the file while the application is running: `tail -f
<log-path>/<log-file>.log`.

## Observe input and output data in Kinesis streams

You can observe records sent to the input stream by the (generating sample Python)
or the Kinesis Data Generator (link) by using the **Data Viewer** in
the Amazon Kinesis console.

**To observe records:**

## Stop your application running locally

Stop the application running in your IDE. The IDE usually provides a "stop"
option. The exact location and method depends on the IDE.

## Package your application code

In this section, you use Apache Maven to package the application code and all
required dependencies in a .zip file.

Run the Maven package command again:

```
$ mvn package
```

This command generates the file
`target/managed-flink-pyflink-getting-started-1.0.0.zip`.

## Upload the application package to an Amazon S3

bucket

In this section, you upload the .zip file you created in the previous section to
the Amazon Simple Storage Service (Amazon S3) bucket you created at the beginning of this tutorial. If you
have not completed this step, see (link).

###### To upload the application code JAR file

1. Open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose the bucket you previously created for the application code.
3. Choose **Upload**.
4. Choose **Add files**.
5. Navigate to the .zip file generated in the previous step:
   `target/managed-flink-pyflink-getting-started-1.0.0.zip`.
6. Choose **Upload** without changing any other
   settings.

## Create and configure the Managed Service for Apache Flink

application

You can create and configure a Managed Service for Apache Flink application using either the
console or the AWS CLI. For this tutorial, we will use the console.

### Create the application

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
2. Verify that the correct Region is selected:
   US East (N. Virginia)us-east-1.
3. Open the right-side menu and choose **Apache Flink
   applications** and then **Create streaming
   application**. Alternatively, choose **Create
   streaming application** from the **Get
   started** section of the initial page.
4. On the **Create streaming applications**
   page:
   - For **Chose a method to set up the stream
     processing application**, choose **Create
     from scratch**.
   - For **Apache Flink configuration, Application
     Flink version**, choose **Apache Flink
     1.19**.
   - For **Application configuration**:
     - For **Application name**, enter
       `MyApplication`.
     - For **Description**, enter
       `My Python test app`.
     - In **Access to application
       resources**, choose **Create /
       update IAM role
       kinesis-analytics-MyApplication-us-east-1 with
       required policies**.

   - For **Template for applications
     settings**:
     - For **Templates**, choose
       **Development**.

   - Choose **Create streaming
     application**.

###### Note

When you create a Managed Service for Apache Flink application using the console, you have the option of
having an IAM role and policy created for your application. Your
application uses this role and policy to access its dependent resources.
These IAM resources are named using your application name and Region
as follows:

- Policy:
  `kinesis-analytics-service-`MyApplication`-`us-west-2``
- Role:
  `kinesisanalytics-`MyApplication`-`us-west-2``Amazon Managed Service for Apache Flink was formerly known as *Kinesis Data Analytics*. The name
 of the resources that are generated automatically is prefixed with
`kinesis-analytics` for backward compatibility.

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
   policy. Replace the sample account IDs
   (`012345678901`) with your account
   ID.

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
 "arn:aws:logs:us-east-1:`012345678901`:log-group:*"
 ]
 },
 {
 "Sid": "ListCloudwatchLogStreams",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogStreams"
 ],
 "Resource": [
 "arn:aws:logs:us-east-1:`012345678901`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:*"
 ]
 },
 {
 "Sid": "PutCloudwatchLogs",
 "Effect": "Allow",
 "Action": [
 "logs:PutLogEvents"
 ],
 "Resource": [
 "arn:aws:logs:us-east-1:`012345678901`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:kinesis-analytics-log-stream"
 ]
 }`,
 {
 "Sid": "ReadInputStream",
 "Effect": "Allow",
 "Action": "kinesis:*",
 "Resource": "arn:aws:kinesis:us-east-1:`012345678901`:stream/ExampleInputStream"
 },
 {
 "Sid": "WriteOutputStream",
 "Effect": "Allow",
 "Action": "kinesis:*",
 "Resource": "arn:aws:kinesis:us-east-1:`012345678901`:stream/ExampleOutputStream"
 }`
 ]
}`

```

5. Choose **Next** and then choose **Save
   changes**.

### Configure the

application

Edit the application configuration to set the application code artifact.

###### To configure the application

1. On the **MyApplication** page, choose
   **Configure**.
2. In the **Application code location**
   section:
   - For **Amazon S3 bucket**, select the bucket
     you previously created for the application code. Choose
     **Browse** and select the correct bucket,
     then choose **Choose**. Don't select on the
     bucket name.
   - For **Path to Amazon S3 object**, enter
     `managed-flink-pyflink-getting-started-1.0.0.zip`.

3. For **Access permissions**, choose
   **Create / update IAM role
   `kinesis-analytics-MyApplication-us-east-1` with
   required policies**.
4. Move to **Runtime properties** and keep the
   default values for all other settings.
5. Choose **Add new item** and add each of the
   following parameters:

| Group ID                              | Key                    | Value                          |
| ------------------------------------- | ---------------------- | ------------------------------ |
| `InputStream0`                        | `stream.name`          | `ExampleInputStream`           |
| `InputStream0`                        | `flink.stream.initpos` | `LATEST`                       |
| `InputStream0`                        | `aws.region`           | `us-east-1`                    |
| `OutputStream0`                       | `stream.name`          | `ExampleOutputStream`          |
| `OutputStream0`                       | `aws.region`           | `us-east-1`                    |
| `kinesis.analytics.flink.run.options` | `python`               | `main.py`                      |
| `kinesis.analytics.flink.run.options` | `jarfile`              | `lib/pyflink-dependencies.jar` |

6. Do not modify any of the other sections and choose **Save
   changes**.

###### Note

When you choose to enable Amazon CloudWatch logging, Managed Service for Apache Flink creates a log group
and log stream for you. The names of these resources are as follows:

- Log group:
  `/aws/kinesis-analytics/MyApplication`
- Log stream: `kinesis-analytics-log-stream`

### Run the application

The application is now configured and ready to run.

###### To run the application

1. On the console for Amazon Managed Service for Apache Flink, choose **My
   Application** and choose **Run**.
2. On the next page, the Application restore configuration page, choose
   **Run with latest snapshot** and then choose
   **Run**.

The **Status** in **Application
details** transitions from `Ready` to
`Starting` and then to `Running` when the
application has started.

When the application is in the `Running` status, you can now open
the Flink dashboard.

###### To open the dashboard

1. Choose **Open Apache Flink dashboard**. The dashboard
   opens on a new page.
2. In the **Runing jobs** list, choose the single job
   that you can see.

###### Note

If you set the Runtime properties or edited the IAM policies
incorrectly, the application status might turn into
`Running`, but the Flink dashboard shows that the job
is continuously restarting. This is a common failure scenario if the
application is misconfigured or lacks permissions to access the
external resources.

When this happens, check the **Exceptions** tab
in the Flink dashboard to see the cause of the problem.

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
   increasing, the configuration might have issues. To investigate the
   issue, review the **Exceptions** tab on the Flink
   dashboard.
4. The **Number of failed checkpoints** metric should be
   zero in a healthy application.

###### Note

This dashboard displays a fixed set of metrics with a granularity
of 5 minutes. You can create a custom application dashboard with any
metrics in the CloudWatch dashboard.

### Observe output data in

Kinesis streams

Make sure you are still publishing data to the input, either using the Python
script or the Kinesis Data Generator.

You can now observe the output of the application running on Managed Service for Apache Flink by
using the Data Viewer in the [https://console.aws.amazon.com/kinesis/](https://console.aws.amazon.com/kinesis/ "https://console.aws.amazon.com/kinesis/"), similarly to what you
already did earlier.

###### To view the output

1. Open the Kinesis console at
   [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis").
2. Verify that the Region is the same as the one you are using to run
   this tutorial. By default, it is us-east-1US East (N. Virginia).
   Change the Region if necessary.
3. Choose **Data Streams**.
4. Select the stream that you want to observe. For this tutorial, use
   `ExampleOutputStream`.
5. Choose the **Data viewer** tab.
6. Select any **Shard**, keep
   **Latest** as **Starting
   position**, and then choose **Get
   records**. You might see a "no record found for this
   request" error. If so, choose **Retry getting
   records**. The newest records published to the stream
   display.
7. Select the value in the Data column to inspect the content of the
   record in JSON format.

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

## Next step

[Clean up AWS resources](gs-python-cleanup.md "gs-python-cleanup.md")
