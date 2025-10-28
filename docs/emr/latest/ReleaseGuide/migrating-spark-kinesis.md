# Migrating Spark Kinesis connector to SDK

2.x for Amazon EMR 7.0

The AWS SDK provides a rich set of APIs and libraries to interact with AWS
cloud computing services, such as managing credentials, connecting to S3 and Kinesis
services. The Spark Kinesis connector is used to consume data from Kinesis Data Streams, and the
received data is transformed and processed in Spark’s execution engine. Currently
this connector is built on top of 1.x of AWS SDK and Kinesis-client-library (KCL).

As part of the AWS SDK 2.x migration, the Spark Kinesis connector is also
updated accordingly to run with the SDK 2.x. In the Amazon EMR 7.0 release, Spark
contains the SDK 2.x upgrade that is not yet available in the community version of
Apache Spark. If you use the Spark Kinesis connector from a release that's lower
than 7.0, you must migrate your application codes to run on SDK 2.x before you can
migrate to Amazon EMR 7.0.

## Migration

guides

This section describes the steps to migrate an application to the upgraded
Spark Kinesis connector. It includes guides to migrate to the Kinesis Client
Library (KCL) 2.x, AWS credential providers, and AWS service clients in
AWS SDK 2.x. For reference, it also includes a sample [WordCount](https://github.com/apache/spark/blob/v3.5.0/connector/kinesis-asl/src/main/scala/org/apache/spark/examples/streaming/KinesisWordCountASL.scala "https://github.com/apache/spark/blob/v3.5.0/connector/kinesis-asl/src/main/scala/org/apache/spark/examples/streaming/KinesisWordCountASL.scala") program that uses the Kinesis connector.

###### Topics

- [Migrating KCL
  from 1.x to 2.x](#migrating-spark-kinesis-KCL-from-1.x-to-2.x "#migrating-spark-kinesis-KCL-from-1.x-to-2.x")
- [Migrating
  AWS credentials providers from AWS SDK 1.x to 2.x](#migrating-spark-kinesis-creds-from-1.x-to-2.x "#migrating-spark-kinesis-creds-from-1.x-to-2.x")
- [Migrating
  AWS service clients from AWS SDK 1.x to 2.x](#migrating-spark-kinesis-service-from-1.x-to-2.x "#migrating-spark-kinesis-service-from-1.x-to-2.x")
- [Code examples
  for streaming applications](#migrating-spark-kinesis-streaming-examples "#migrating-spark-kinesis-streaming-examples")
- [Considerations when
  using the upgraded Spark Kinesis connector](#migrating-spark-kinesis-considerations "#migrating-spark-kinesis-considerations")

### Migrating KCL

from 1.x to 2.x

- **Metrics level and dimensions in
  `KinesisInputDStream`**

When you instantiate a `KinesisInputDStream`, you can
control the metrics level and dimensions for the stream. The
following example demonstrates how you might customize these
parameters with KCL 1.x:

```
import com.amazonaws.services.kinesis.clientlibrary.lib.worker.KinesisClientLibConfiguration
import com.amazonaws.services.kinesis.metrics.interfaces.MetricsLevel

val kinesisStream = KinesisInputDStream.builder
  .streamingContext(ssc)
  .streamName(streamName)
  .endpointUrl(endpointUrl)
  .regionName(regionName)
  .initialPosition(new Latest())
  .checkpointAppName(appName)
  .checkpointInterval(kinesisCheckpointInterval)
  .storageLevel(StorageLevel.MEMORY_AND_DISK_2)
  .metricsLevel(MetricsLevel.DETAILED)
  .metricsEnabledDimensions(KinesisClientLibConfiguration.DEFAULT_METRICS_ENABLED_DIMENSIONS.asScala.toSet)
  .build()
```

In KCL 2.x, these config settings have different package names. To
migrate to 2.x:

    1. Change the import statements for
     `com.amazonaws.services.kinesis.clientlibrary.lib.worker.KinesisClientLibConfiguration`
     and
     `com.amazonaws.services.kinesis.metrics.interfaces.MetricsLevel`
     to `software.amazon.kinesis.metrics.MetricsLevel`
     and `software.amazon.kinesis.metrics.MetricsUtil`
     respectively.



    ```
    // import com.amazonaws.services.kinesis.metrics.interfaces.MetricsLevel
    import software.amazon.kinesis.metrics.MetricsLevel

    // import com.amazonaws.services.kinesis.clientlibrary.lib.worker.KinesisClientLibConfiguration
    import software.amazon.kinesis.metrics.MetricsUtil
    ```
    2. Replace the line
     `metricsEnabledDimensionsKinesisClientLibConfiguration.DEFAULT_METRICS_ENABLED_DIMENSIONS.asScala.toSet`
     with
     `metricsEnabledDimensionsSet(MetricsUtil.OPERATION_DIMENSION_NAME,
     MetricsUtil.SHARD_ID_DIMENSION_NAME)`

Following is an updated version of the
`KinesisInputDStream` with customized metrics level
and metrics dimensions:

```
import software.amazon.kinesis.metrics.MetricsLevel
import software.amazon.kinesis.metrics.MetricsUtil

val kinesisStream = KinesisInputDStream.builder
  .streamingContext(ssc)
  .streamName(streamName)
  .endpointUrl(endpointUrl)
  .regionName(regionName)
  .initialPosition(new Latest())
  .checkpointAppName(appName)
  .checkpointInterval(kinesisCheckpointInterval)
  .storageLevel(StorageLevel.MEMORY_AND_DISK_2)
  .metricsLevel(MetricsLevel.DETAILED)
  .metricsEnabledDimensions(Set(MetricsUtil.OPERATION_DIMENSION_NAME, MetricsUtil.SHARD_ID_DIMENSION_NAME))
  .build()
```

- Message handler function in
  `KinesisInputDStream`

When instantiating a `KinesisInputDStream`, you may
also provide a “message handler function” that takes a Kinesis
Record and returns a generic object T, in case you would like to use
other data included in a Record such as partition key.

In KCL 1.x, the message handler function signature is:
`Record => T`, where Record is
`com.amazonaws.services.kinesis.model.Record`. In KCL
2.x, the handler’s signature is changed to:
`KinesisClientRecord => T`, where KinesisClientRecord
is
`software.amazon.kinesis.retrieval.KinesisClientRecord`.

Following is an example of providing a message handler in KCL
1.x:

```
import com.amazonaws.services.kinesis.model.Record


def addFive(r: Record): Int = JavaUtils.bytesToString(r.getData).toInt + 5
val stream = KinesisInputDStream.builder
  .streamingContext(ssc)
  .streamName(streamName)
  .endpointUrl(endpointUrl)
  .regionName(regionName)
  .initialPosition(new Latest())
  .checkpointAppName(appName)
  .checkpointInterval(Seconds(10))
  .storageLevel(StorageLevel.MEMORY_ONLY)
  .buildWithMessageHandler(addFive)
```

To migrate the message handler:

    1. Change the import statement for
     `com.amazonaws.services.kinesis.model.Record`
     to
     `software.amazon.kinesis.retrieval.KinesisClientRecord`.



    ```
    // import com.amazonaws.services.kinesis.model.Record
    import software.amazon.kinesis.retrieval.KinesisClientRecord
    ```
    2. Update the the method signature of the message
     handler.



    ```
    //def addFive(r: Record): Int = JavaUtils.bytesToString(r.getData).toInt + 5
    def addFive = (r: KinesisClientRecord) => JavaUtils.bytesToString(r.data()).toInt + 5
    ```

Following is an updated example of providing the message handler
in KCL 2.x:

```
import software.amazon.kinesis.retrieval.KinesisClientRecord


def addFive = (r: KinesisClientRecord) => JavaUtils.bytesToString(r.data()).toInt + 5
val stream = KinesisInputDStream.builder
  .streamingContext(ssc)
  .streamName(streamName)
  .endpointUrl(endpointUrl)
  .regionName(regionName)
  .initialPosition(new Latest())
  .checkpointAppName(appName)
  .checkpointInterval(Seconds(10))
  .storageLevel(StorageLevel.MEMORY_ONLY)
  .buildWithMessageHandler(addFive)
```

For more information about migrating from KCL 1.x to 2.x, see
[Migrating Consumers
from KCL 1.x to KCL 2.x](../../../streams/latest/dev/kcl-migration.md "../../../streams/latest/dev/kcl-migration.md").

### Migrating

AWS credentials providers from AWS SDK 1.x to 2.x

Credentials providers are used to obtain AWS credentials for
interactions with AWS. There are several interface and class changes
related to the credentials providers in SDK 2.x, which can be found [here](https://github.com/aws/aws-sdk-java-v2/blob/master/docs/LaunchChangelog.md#122-client-credentials "https://github.com/aws/aws-sdk-java-v2/blob/master/docs/LaunchChangelog.md#122-client-credentials"). Spark Kinesis connector has defined an interface
(`org.apache.spark.streaming.kinesis.SparkAWSCredentials`)
and implementation classes that returns 1.x version of AWS credential
providers. These credentials providers are needed when initializing Kinesis
clients. For instance, if you are using the method
`SparkAWSCredentials.provider` in the applications, you would
need to update codes to consume 2.x version of AWS credential
providers.

Following is an example of using the credential providers in AWS SDK
1.x:

```
import org.apache.spark.streaming.kinesis.SparkAWSCredentials
import com.amazonaws.auth.AWSCredentialsProvider

val basicSparkCredentials = SparkAWSCredentials.builder
    .basicCredentials("accessKey", "secretKey")
    .build()

val credentialProvider = basicSparkCredentials.provider
assert(credentialProvider.isInstanceOf[AWSCredentialsProvider], "Type should be AWSCredentialsProvider")
```

###### To migrate to SDK 2.x:

1. Change the import statement for
   `com.amazonaws.auth.AWSCredentialsProvider` to
   `software.amazon.awssdk.auth.credentials.AwsCredentialsProvider`

```
//import com.amazonaws.auth.AWSCredentialsProvider
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider
```

2. Update the remaining codes that use this class.

```
import org.apache.spark.streaming.kinesis.SparkAWSCredentials
import software.amazon.awssdk.auth.credentials.AwsCredentialsProvider

val basicSparkCredentials = SparkAWSCredentials.builder
    .basicCredentials("accessKey", "secretKey")
    .build()

val credentialProvider = basicSparkCredentials.provider
assert (credentialProvider.isInstanceOf[AwsCredentialsProvider], "Type should be AwsCredentialsProvider")
```

### Migrating

AWS service clients from AWS SDK 1.x to 2.x

AWS service clients have different package names in 2.x (i.e.
`software.amazon.awssdk`). whereas the SDK 1.x uses
`com.amazonaws`. For more information about the client
changes, see [here](../../../sdk-for-java/latest/developer-guide/migration-whats-different.md "../../../sdk-for-java/latest/developer-guide/migration-whats-different.md"). If you are using these service clients in the codes, you
would need to migrate the clients accordingly.

Following is an example of creating a client in SDK 1.x:

```
import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient
import com.amazonaws.services.dynamodbv2.document.DynamoDB

AmazonDynamoDB ddbClient = AmazonDynamoDBClientBuilder.defaultClient();
AmazonDynamoDBClient ddbClient = new AmazonDynamoDBClient();
```

###### To migrate to 2.x:

1. Change the import statements for service clients. Take DynamoDB
   clients as an example. You would need to change
   `com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient`
   or `com.amazonaws.services.dynamodbv2.document.DynamoDB`
   to
   `software.amazon.awssdk.services.dynamodb.DynamoDbClient`.

```
// import com.amazonaws.services.dynamodbv2.AmazonDynamoDBClient
// import com.amazonaws.services.dynamodbv2.document.DynamoDB
import software.amazon.awssdk.services.dynamodb.DynamoDbClient
```

2. Update the codes that initialize the clients

```
// AmazonDynamoDB ddbClient = AmazonDynamoDBClientBuilder.defaultClient();
// AmazonDynamoDBClient ddbClient = new AmazonDynamoDBClient();

DynamoDbClient ddbClient = DynamoDbClient.create();
DynamoDbClient ddbClient = DynamoDbClient.builder().build();
```

For more information about migrating AWS SDK from 1.x to 2.x,
see [What's different between the AWS SDK for Java 1.x and
2.x](../../../sdk-for-java/latest/developer-guide/migration-whats-different.md "../../../sdk-for-java/latest/developer-guide/migration-whats-different.md")

### Code examples

for streaming applications

```
import java.net.URI
import software.amazon.awssdk.auth.credentials.DefaultCredentialsProvider
import software.amazon.awssdk.http.apache.ApacheHttpClient
import software.amazon.awssdk.services.kinesis.KinesisClient
import software.amazon.awssdk.services.kinesis.model.DescribeStreamRequest
import software.amazon.awssdk.regions.Region
import software.amazon.kinesis.metrics.{MetricsLevel, MetricsUtil}

import org.apache.spark.SparkConf
import org.apache.spark.storage.StorageLevel
import org.apache.spark.streaming.{Milliseconds, StreamingContext}
import org.apache.spark.streaming.dstream.DStream.toPairDStreamFunctions
import org.apache.spark.streaming.kinesis.KinesisInitialPositions.Latest
import org.apache.spark.streaming.kinesis.KinesisInputDStream


object KinesisWordCountASLSDKV2 {

  def main(args: Array[String]): Unit = {
    val appName = "demo-app"
    val streamName = "demo-kinesis-test"
    val endpointUrl = "https://kinesis.us-west-2.amazonaws.com"
    val regionName = "us-west-2"

    // Determine the number of shards from the stream using the low-level Kinesis Client
    // from the AWS Java SDK.
    val credentialsProvider = DefaultCredentialsProvider.create
    require(credentialsProvider.resolveCredentials() != null,
      "No AWS credentials found. Please specify credentials using one of the methods specified " +
        "in https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/credentials.html")
    val kinesisClient = KinesisClient.builder()
      .credentialsProvider(credentialsProvider)
      .region(Region.US_WEST_2)
      .endpointOverride(URI.create(endpointUrl))
      .httpClientBuilder(ApacheHttpClient.builder())
      .build()
    val describeStreamRequest = DescribeStreamRequest.builder()
      .streamName(streamName)
      .build()
    val numShards = kinesisClient.describeStream(describeStreamRequest)
      .streamDescription
      .shards
      .size


    // In this example, we are going to create 1 Kinesis Receiver/input DStream for each shard.
    // This is not a necessity; if there are less receivers/DStreams than the number of shards,
    // then the shards will be automatically distributed among the receivers and each receiver
    // will receive data from multiple shards.
    val numStreams = numShards

    // Spark Streaming batch interval
    val batchInterval = Milliseconds(2000)

    // Kinesis checkpoint interval is the interval at which the DynamoDB is updated with information
    // on sequence number of records that have been received. Same as batchInterval for this
    // example.
    val kinesisCheckpointInterval = batchInterval

    // Setup the SparkConfig and StreamingContext
    val sparkConfig = new SparkConf().setAppName("KinesisWordCountASLSDKV2")
    val ssc = new StreamingContext(sparkConfig, batchInterval)

    // Create the Kinesis DStreams
    val kinesisStreams = (0 until numStreams).map { i =>
      KinesisInputDStream.builder
        .streamingContext(ssc)
        .streamName(streamName)
        .endpointUrl(endpointUrl)
        .regionName(regionName)
        .initialPosition(new Latest())
        .checkpointAppName(appName)
        .checkpointInterval(kinesisCheckpointInterval)
        .storageLevel(StorageLevel.MEMORY_AND_DISK_2)
        .metricsLevel(MetricsLevel.DETAILED)
        .metricsEnabledDimensions(Set(MetricsUtil.OPERATION_DIMENSION_NAME, MetricsUtil.SHARD_ID_DIMENSION_NAME))
        .build()
    }

    // Union all the streams
    val unionStreams = ssc.union(kinesisStreams)

    // Convert each line of Array[Byte] to String, and split into words
    val words = unionStreams.flatMap(byteArray => new String(byteArray).split(" "))

    // Map each word to a (word, 1) tuple so we can reduce by key to count the words
    val wordCounts = words.map(word => (word, 1)).reduceByKey(_ + _)

    // Print the first 10 wordCounts
    wordCounts.print()

    // Start the streaming context and await termination
    ssc.start()
    ssc.awaitTermination()
  }
}
```

### Considerations when

using the upgraded Spark Kinesis connector

- If your applications uses the
  `Kinesis-producer-library` with JDK version lower
  than 11, you may run into exceptions like
  `java.lang.NoClassDefFoundError:
javax/xml/bind/DatatypeConverter`. This happens because
  EMR 7.0 comes with JDK 17 by default and J2EE modules have been
  removed from the standard libraries since Java 11+. This could be
  fixed by adding the following dependency in the pom file. Replace
  the library version with one as you see fit.

```
<dependency>
      <groupId>javax.xml.bind</groupId>
      <artifactId>jaxb-api</artifactId>
      <version>${jaxb-api.version}</version>
    </dependency>
```

- The Spark Kinesis connector jar can be found under this path after
  an EMR cluster is created:
  `/usr/lib/spark/connector/lib/`
