# Create a stream using the

APIs

Use the following steps to create your Kinesis data stream.

## Build the Kinesis Data Streams

client

Before you can work with Kinesis data streams, you must build a client object. The
following Java code instantiates a client builder and uses it to set the Region,
credentials, and the client configuration. It then builds a client object.

```
AmazonKinesisClientBuilder clientBuilder = AmazonKinesisClientBuilder.standard();

clientBuilder.setRegion(regionName);
clientBuilder.setCredentials(credentialsProvider);
clientBuilder.setClientConfiguration(config);

AmazonKinesis client = clientBuilder.build();
```

For more information, see [Kinesis Data Streams Regions
and Endpoints](../../../general/latest/gr/rande.md#ak_region "../../../general/latest/gr/rande.md#ak_region") in the _AWS General Reference_.

## Create the stream

Now that you have created your Kinesis Data Streams client, you can create a stream using the
console or programmatically. To create a stream programmatically, instantiate a
`CreateStreamRequest` object and specify a name for the stream. If
you want to use provisioned mode, specify the number of shards for the stream to
use.

- **On-demand**:

```
CreateStreamRequest createStreamRequest = new CreateStreamRequest();
createStreamRequest.setStreamName( myStreamName );
```

- **Provisioned**:

```
CreateStreamRequest createStreamRequest = new CreateStreamRequest();
createStreamRequest.setStreamName( myStreamName );
createStreamRequest.setShardCount( myStreamSize );
```

The stream name identifies the stream. The name is scoped to the AWS account
used by the application. It is also scoped by Region. That is, two streams in two
different AWS accounts can have the same name, and two streams in the same AWS
account but in two different Regions can have the same name, but not two streams on
the same account and in the same Region.

The throughput of the stream is a function of the number of shards. For greater
provisioned throughput, you require more shards. More shards also increase the cost
that AWS charges for the stream. For more information about calculating an
appropriate number of shards for your application, see [Choose the data stream capacity mode](how-do-i-size-a-stream.md "how-do-i-size-a-stream.md").

After you have configured the `createStreamRequest` object, create a
stream by calling the `createStream` method on the client. After calling
`createStream`, wait for the stream to reach the `ACTIVE`
state before performing any operations on the stream. To check the state of the
stream, call the `describeStream` method. However,
`describeStream` throws an exception if the stream does not exist.
Therefore, enclose the `describeStream` call in a `try/catch`
block.

```
client.createStream( createStreamRequest );
DescribeStreamRequest describeStreamRequest = new DescribeStreamRequest();
describeStreamRequest.setStreamName( myStreamName );

long startTime = System.currentTimeMillis();
long endTime = startTime + ( 10 * 60 * 1000 );
while ( System.currentTimeMillis() < endTime ) {
  try {
    Thread.sleep(20 * 1000);
  }
  catch ( Exception e ) {}

  try {
    DescribeStreamResult describeStreamResponse = client.describeStream( describeStreamRequest );
    String streamStatus = describeStreamResponse.getStreamDescription().getStreamStatus();
    if ( streamStatus.equals( "ACTIVE" ) ) {
      break;
    }
    //
    // sleep for one second
    //
    try {
      Thread.sleep( 1000 );
    }
    catch ( Exception e ) {}
  }
  catch ( ResourceNotFoundException e ) {}
}
if ( System.currentTimeMillis() >= endTime ) {
  throw new RuntimeException( "Stream " + myStreamName + " never went active" );
}
```
