Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Get started (Scala)

###### Note

Starting from version 1.15, Flink is Scala free. Applications can now use the Java API from
any Scala version. Flink still uses Scala in a few key components internally, but
doesn't expose Scala into the user code classloader. Because of that, you must add Scala
dependencies into your JAR-archives.

For more information about Scala changes in Flink 1.15, see [Scala Free in One Fifteen](https://flink.apache.org/2022/02/22/scala-free.html "https://flink.apache.org/2022/02/22/scala-free.html").

In this exercise, you create a Managed Service for Apache Flink application for Scala with a Kinesis stream as a source and a
sink.

###### This topic contains the following sections:

- [Create dependent resources](#examples-gs-scala-resources "#examples-gs-scala-resources")
- [Write sample records to the input stream](#examples-gs-scala-write "#examples-gs-scala-write")
- [Download and examine the application code](#examples-gs-scala-download "#examples-gs-scala-download")
- [Compile and upload the application code](#examples-gs-scala-upload "#examples-gs-scala-upload")
- [Create and run the application (console)](gs-scala-7.md "gs-scala-7.md")
- [Create and run the application (CLI)](examples-gs-scala-create-run-cli.md "examples-gs-scala-create-run-cli.md")
- [Clean up AWS resources](examples-gs-scala-cleanup.md "examples-gs-scala-cleanup.md")

## Create dependent resources

Before you create a Managed Service for Apache Flink application for this exercise, you create the following dependent resources:

- Two Kinesis streams for input and output.
- An Amazon S3 bucket to store the application's code (`ka-app-code-`<username>``)

You can create the Kinesis streams and Amazon S3 bucket using the console. For instructions for
creating these resources, see the following topics:

- [Creating and Updating Data
  Streams](../../../kinesis/latest/dev/amazon-kinesis-streams.md "../../../kinesis/latest/dev/amazon-kinesis-streams.md") in the _Amazon Kinesis Data Streams Developer Guide_. Name your data
  streams `ExampleInputStream` and `ExampleOutputStream`.

To create the data streams (AWS CLI)

    + To create the first stream (`ExampleInputStream`), use the following Amazon Kinesis create-stream AWS CLI command.



    ```
    aws kinesis create-stream \
        --stream-name ExampleInputStream \
        --shard-count 1 \
        --region us-west-2 \
        --profile adminuser
    ```
    + To create the second stream that the application uses to write output, run the same command, changing the stream name to `ExampleOutputStream`.



    ```
    aws kinesis create-stream \
        --stream-name ExampleOutputStream \
        --shard-count 1 \
        --region us-west-2 \
        --profile adminuser
    ```

- [How Do I Create an S3 Bucket?](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md") in the
  _Amazon Simple Storage Service User Guide_. Give the Amazon S3 bucket a globally unique name by appending your
  login name, such as `ka-app-code-`<username>``.

**Other resources**

When you create your application, Managed Service for Apache Flink creates the following Amazon CloudWatch resources if they don't already exist:

- A log group called `/AWS/KinesisAnalytics-java/MyApplication`
- A log stream called `kinesis-analytics-log-stream`

## Write sample records to the input stream

In this section, you use a Python script to write sample records to the stream for
the application to process.

###### Note

This section requires the [AWS SDK for Python (Boto)](https://aws.amazon.com/developers/getting-started/python/ "https://aws.amazon.com/developers/getting-started/python/").

###### Note

The Python script in this section uses the AWS CLI. You must configure your AWS CLI to use
your account credentials and default region. To configure your AWS CLI, enter the following:

```
aws configure
```

1. Create a file named `stock.py` with the following
   contents:

```
import datetime
import json
import random
import boto3

STREAM_NAME = "ExampleInputStream"


def get_data():
    return {
        'event_time': datetime.datetime.now().isoformat(),
        'ticker': random.choice(['AAPL', 'AMZN', 'MSFT', 'INTC', 'TBV']),
        'price': round(random.random() * 100, 2)}


def generate(stream_name, kinesis_client):
    while True:
        data = get_data()
        print(data)
        kinesis_client.put_record(
            StreamName=stream_name,
            Data=json.dumps(data),
            PartitionKey="partitionkey")


if __name__ == '__main__':
    generate(STREAM_NAME, boto3.client('kinesis', region_name='us-west-2'))
```

2. Run the `stock.py` script:

```
$ python stock.py
```

Keep the script running while completing the rest of the tutorial.

## Download and examine the application code

The Python application code for this example is available from GitHub. To download
the application code, do the following:

1. Install the Git client if you haven't already. For more information, see [Installing
   Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "https://git-scm.com/book/en/v2/Getting-Started-Installing-Git").
2. Clone the remote repository with the following command:

```
git clone https://github.com/aws-samples/amazon-kinesis-data-analytics-examples.git
```

3. Navigate to the `amazon-kinesis-data-analytics-java-examples/scala/GettingStarted` directory.

Note the following
about the application code:

- A `build.sbt` file contains information about the application's configuration and dependencies, including the Managed Service for Apache Flink libraries.
- The `BasicStreamingJob.scala` file contains the main method that defines the application's functionality.
- The application uses a Kinesis source to read from the source stream. The following snippet creates the Kinesis source:

```
private def createSource: FlinkKinesisConsumer[String] = {
  val applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties
  val inputProperties = applicationProperties.get("ConsumerConfigProperties")

  new FlinkKinesisConsumer[String](inputProperties.getProperty(streamNameKey, defaultInputStreamName),
    new SimpleStringSchema, inputProperties)
}
```

The application also uses a Kinesis sink to write into the result stream. The following snippet creates the Kinesis sink:

```
private def createSink: KinesisStreamsSink[String] = {
  val applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties
  val outputProperties = applicationProperties.get("ProducerConfigProperties")

  KinesisStreamsSink.builder[String]
    .setKinesisClientProperties(outputProperties)
    .setSerializationSchema(new SimpleStringSchema)
    .setStreamName(outputProperties.getProperty(streamNameKey, defaultOutputStreamName))
    .setPartitionKeyGenerator((element: String) => String.valueOf(element.hashCode))
    .build
}

```

- The application creates source and sink connectors to access external resources using a StreamExecutionEnvironment object.
- The application creates source and sink connectors using dynamic application properties.
  Runtime application's properties are read to configure the connectors. For more information about
  runtime properties, see [Runtime Properties](how-properties.md "how-properties.md").

## Compile and upload the application code

In this section, you
compile and upload your application code to the Amazon S3 bucket you created in the [Create dependent resources](#examples-gs-scala-resources "#examples-gs-scala-resources") section.

###### Compile the Application Code

In this section, you use the [SBT](https://www.scala-sbt.org/ "https://www.scala-sbt.org/") build tool to build the Scala code for the
application. To install SBT, see [Install sbt with cs setup](https://www.scala-sbt.org/download.html "https://www.scala-sbt.org/download.html").
You also need to install the Java Development Kit (JDK). See [Prerequisites for Completing the Exercises](getting-started.md#setting-up-prerequisites "getting-started.md#setting-up-prerequisites").

1. To use your application code, you compile and package it into a JAR file. You can compile and package your code with SBT:

```
sbt assembly
```

2. If the application compiles successfully, the following file is created:

```
target/scala-3.2.0/getting-started-scala-1.0.jar
```

###### Upload the Apache Flink Streaming Scala Code

In this section, you create an Amazon S3 bucket and upload your application code.

1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Choose **Create bucket**
3. Enter `ka-app-code-<username>` in the **Bucket name** field.
   Add a suffix to the bucket name, such as your user name, to make it globally unique. Choose **Next**.
4. In **Configure options**, keep the settings as they are, and choose **Next**.
5. In **Set permissions**, keep the settings as they are, and choose **Next**.
6. Choose **Create bucket**.
7. Choose the `ka-app-code-<username>` bucket, and then choose **Upload**.
8. In the **Select files** step, choose **Add
   files**. Navigate to the
   `getting-started-scala-1.0.jar` file that you created
   in the previous step.
9. You don't need to change any of the settings for the object, so choose **Upload**.

Your application code is now stored in an Amazon S3 bucket where your application can
access it.
