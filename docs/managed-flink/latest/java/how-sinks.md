

# Write data using sinks in Managed Service for Apache Flink
<a name="how-sinks"></a>

In your application code, you can use any [Apache Flink sink](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/overview/) connector to write into external systems, including AWS services, such as Kinesis Data Streams and DynamoDB.

Apache Flink also provides sinks for files and sockets, and you can implement custom sinks. Among the several supported sinks, the following are frequently used:

## Use Kinesis data streams
<a name="sinks-streams"></a>

Apache Flink provides information about the [Kinesis Data Streams Connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/kinesis/) in the Apache Flink documentation.

For an example of an application that uses a Kinesis data stream for input and output, see [Tutorial: Get started using the DataStream API in Managed Service for Apache Flink](getting-started.md).

## Use Apache Kafka and Amazon Managed Streaming for Apache Kafka (MSK)
<a name="sinks-MSK"></a>

The [Apache Flink Kafka connector](https://nightlies.apache.org/flink/flink-docs-release-1.19/docs/connectors/datastream/kafka/#kafka-sink) provides extensive support for publishing data to Apache Kafka and Amazon MSK, including exactly once guarantees. To learn how to write to Kafka, see [Kafka Connectors examples](https://github.com/aws-samples/amazon-managed-service-for-apache-flink-examples/tree/main/java/KafkaConnectors) in the Apache Flink documentation.

## Use Amazon S3
<a name="sinks-s3"></a>

You can use the Apache Flink `StreamingFileSink` to write objects to an Amazon S3 bucket.

For an example about how to write objects to S3, see [Example: Writing to an Amazon S3 bucket](earlier.md#examples-s3). 

## Use Firehose
<a name="sinks-firehose"></a>

The `FlinkKinesisFirehoseProducer` is a reliable, scalable Apache Flink sink for storing application output using the [Firehose](https://docs.aws.amazon.com/firehose/latest/dev/) service. This section describes how to set up a Maven project to create and use a `FlinkKinesisFirehoseProducer`.

**Topics**
+ [Create a `FlinkKinesisFirehoseProducer`](#sinks-firehose-create)
+ [`FlinkKinesisFirehoseProducer` Code Example](#sinks-firehose-sample)

### Create a `FlinkKinesisFirehoseProducer`
<a name="sinks-firehose-create"></a>

The following code example demonstrates creating a `FlinkKinesisFirehoseProducer`:

```
Properties outputProperties = new Properties();
outputProperties.setProperty(ConsumerConfigConstants.AWS_REGION, region);

FlinkKinesisFirehoseProducer<String> sink = new FlinkKinesisFirehoseProducer<>(outputStreamName, new SimpleStringSchema(), outputProperties);
```

### `FlinkKinesisFirehoseProducer` Code Example
<a name="sinks-firehose-sample"></a>

The following code example demonstrates how to create and configure a `FlinkKinesisFirehoseProducer` and send data from an Apache Flink data stream to the Firehose service.

```
 
package com.amazonaws.services.kinesisanalytics;

import com.amazonaws.services.kinesisanalytics.flink.connectors.config.ProducerConfigConstants;
import com.amazonaws.services.kinesisanalytics.flink.connectors.producer.FlinkKinesisFirehoseProducer;
import com.amazonaws.services.kinesisanalytics.runtime.KinesisAnalyticsRuntime;
import org.apache.flink.api.common.serialization.SimpleStringSchema;
import org.apache.flink.streaming.api.datastream.DataStream;
import org.apache.flink.streaming.api.environment.StreamExecutionEnvironment;
import org.apache.flink.streaming.connectors.kinesis.FlinkKinesisConsumer;
import org.apache.flink.streaming.connectors.kinesis.FlinkKinesisProducer;

import org.apache.flink.streaming.connectors.kinesis.config.ConsumerConfigConstants;

import java.io.IOException;
import java.util.Map;
import java.util.Properties;

public class StreamingJob {

	private static final String region = "us-east-1";
	private static final String inputStreamName = "ExampleInputStream";
	private static final String outputStreamName = "ExampleOutputStream";

	private static DataStream<String> createSourceFromStaticConfig(StreamExecutionEnvironment env) {
		Properties inputProperties = new Properties();
		inputProperties.setProperty(ConsumerConfigConstants.AWS_REGION, region);
		inputProperties.setProperty(ConsumerConfigConstants.STREAM_INITIAL_POSITION, "LATEST");

		return env.addSource(new FlinkKinesisConsumer<>(inputStreamName, new SimpleStringSchema(), inputProperties));
	}

	private static DataStream<String> createSourceFromApplicationProperties(StreamExecutionEnvironment env)
			throws IOException {
		Map<String, Properties> applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();
		return env.addSource(new FlinkKinesisConsumer<>(inputStreamName, new SimpleStringSchema(),
				applicationProperties.get("ConsumerConfigProperties")));
	}

	private static FlinkKinesisFirehoseProducer<String> createFirehoseSinkFromStaticConfig() {
		/*
		 * com.amazonaws.services.kinesisanalytics.flink.connectors.config.
		 * ProducerConfigConstants
		 * lists of all of the properties that firehose sink can be configured with.
		 */

		Properties outputProperties = new Properties();
		outputProperties.setProperty(ConsumerConfigConstants.AWS_REGION, region);

		FlinkKinesisFirehoseProducer<String> sink = new FlinkKinesisFirehoseProducer<>(outputStreamName,
				new SimpleStringSchema(), outputProperties);
		ProducerConfigConstants config = new ProducerConfigConstants();
		return sink;
	}

	private static FlinkKinesisFirehoseProducer<String> createFirehoseSinkFromApplicationProperties() throws IOException {
		/*
		 * com.amazonaws.services.kinesisanalytics.flink.connectors.config.
		 * ProducerConfigConstants
		 * lists of all of the properties that firehose sink can be configured with.
		 */

		Map<String, Properties> applicationProperties = KinesisAnalyticsRuntime.getApplicationProperties();
		FlinkKinesisFirehoseProducer<String> sink = new FlinkKinesisFirehoseProducer<>(outputStreamName,
				new SimpleStringSchema(),
				applicationProperties.get("ProducerConfigProperties"));
		return sink;
	}

	public static void main(String[] args) throws Exception {
		// set up the streaming execution environment
		final StreamExecutionEnvironment env = StreamExecutionEnvironment.getExecutionEnvironment();

		/*
		 * if you would like to use runtime configuration properties, uncomment the
		 * lines below
		 * DataStream<String> input = createSourceFromApplicationProperties(env);
		 */

		DataStream<String> input = createSourceFromStaticConfig(env);

		// Kinesis Firehose sink
		input.addSink(createFirehoseSinkFromStaticConfig());

		// If you would like to use runtime configuration properties, uncomment the
		// lines below
		// input.addSink(createFirehoseSinkFromApplicationProperties());

		env.execute("Flink Streaming Java API Skeleton");
	}
}
```

For a complete tutorial about how to use the Firehose sink, see [Example: Writing to Firehose](earlier.md#get-started-exercise-fh).