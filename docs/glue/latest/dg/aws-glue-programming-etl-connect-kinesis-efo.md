

# Using enhanced fan-out in Kinesis streaming jobs
<a name="aws-glue-programming-etl-connect-kinesis-efo"></a>

An enhanced fan-out consumer is able to recieve records from a Kinesis stream with dedicated throughput that can be greater than typical consumers. This is done by optimizing the transfer protocol used to provide data to a Kinesis consumer, such as your job. For more information about Kinesis Enhanced Fan-Out, see [the Kinesis documentation](https://docs.aws.amazon.com/streams/latest/dev/enhanced-consumers.html).

In enhanced fan-out mode, the `maxRecordPerRead` and `idleTimeBetweenReadsInMs` connection options no longer apply, as those parameters are not configurable when using enhanced fan-out. The configuration options for retries perform as described.

Use the following procedures to enable and disable enhanced fan-out for your streaming job. You should register a stream consumer for each job that will consume data from your stream.

**To enable enhanced fan-out consumption on your job:**

1. Register a stream consumer for your job using the Kinesis API. Follow the instructions to *register a consumer with enhanced fan-out using the Kinesis Data Streams API* in the [Kinesis documentation](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-api). You will only need to follow the first step - calling [RegisterStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_RegisterStreamConsumer.html). Your request should return an ARN, {{consumerARN}}. 

1. Set the connection option `fanoutConsumerARN` to {{consumerARN}} in your connection method arguments.

1. Restart your job.

**To disable enhanced fan-out consumption on your job:**

1. Remove the `fanoutConsumerARN` connection option from your method call.

1. Restart your job.

1. Follow the instructions to *deregister a consumer* in the [Kinesis documentation](https://docs.aws.amazon.com/streams/latest/dev/building-enhanced-consumers-console.html). These instructions apply to the console, but can also be achieved through the Kinesis API. For more information about stream consumer deregistration through the Kinesis API, consult [DeregisterStreamConsumer](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_DeregisterStreamConsumer.html) in the Kinesis documentation.