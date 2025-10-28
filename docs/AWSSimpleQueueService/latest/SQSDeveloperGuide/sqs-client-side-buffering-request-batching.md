# Enabling client-side

buffering and request batching with Amazon SQS

The [AWS SDK for Java](https://aws.amazon.com/sdkforjava/ "https://aws.amazon.com/sdkforjava/") includes
`AmazonSQSBufferedAsyncClient` which accesses Amazon SQS. This client allows
for simple request batching using client-side buffering. Calls made from the client are
first buffered and then sent as a batch request to Amazon SQS.

Client-side buffering allows up to 10 requests to be buffered and sent as a batch
request, decreasing your cost of using Amazon SQS and reducing the number of sent requests.
`AmazonSQSBufferedAsyncClient` buffers both synchronous and asynchronous
calls. Batched requests and support for [long
polling](sqs-short-and-long-polling.md "sqs-short-and-long-polling.md") can also help increase throughput. For more information, see [Increasing throughput
using horizontal scaling and action batching with Amazon SQS](sqs-throughput-horizontal-scaling-and-batching.md "sqs-throughput-horizontal-scaling-and-batching.md").

Because `AmazonSQSBufferedAsyncClient` implements the same interface as
`AmazonSQSAsyncClient`, migrating from `AmazonSQSAsyncClient`
to `AmazonSQSBufferedAsyncClient` typically requires only minimal changes to
your existing code.

###### Note

The Amazon SQS Buffered Asynchronous Client doesn't currently support FIFO queues.

## Using

AmazonSQSBufferedAsyncClient

Before you begin, complete the steps in [Setting up Amazon SQS](sqs-setting-up.md "sqs-setting-up.md").

### AWS SDK for Java

1.x

For AWS SDK for Java 1.x, you can create a new
`AmazonSQSBufferedAsyncClient` based on the following
example:

```
// Create the basic Amazon SQS async client
final AmazonSQSAsync sqsAsync = new AmazonSQSAsyncClient();

// Create the buffered client
final AmazonSQSAsync bufferedSqs = new AmazonSQSBufferedAsyncClient(sqsAsync);
```

After you create the new `AmazonSQSBufferedAsyncClient`, you can
use it to send multiple requests to Amazon SQS (just as you can with
`AmazonSQSAsyncClient`), for example:

```
final CreateQueueRequest createRequest = new CreateQueueRequest().withQueueName("MyQueue");

final CreateQueueResult res = bufferedSqs.createQueue(createRequest);

final SendMessageRequest request = new SendMessageRequest();
final String body = "Your message text" + System.currentTimeMillis();
request.setMessageBody( body );
request.setQueueUrl(res.getQueueUrl());

final Future<SendMessageResult> sendResult = bufferedSqs.sendMessageAsync(request);

final ReceiveMessageRequest receiveRq = new ReceiveMessageRequest()
    .withMaxNumberOfMessages(1)
    .withQueueUrl(queueUrl);
final ReceiveMessageResult rx = bufferedSqs.receiveMessage(receiveRq);
```

### Configuring

AmazonSQSBufferedAsyncClient

`AmazonSQSBufferedAsyncClient` is preconfigured with settings that
work for most use cases. You can further configure
`AmazonSQSBufferedAsyncClient`, for example:

1. Create an instance of the `QueueBufferConfig` class with
   the required configuration parameters.
2. Provide the instance to the `AmazonSQSBufferedAsyncClient`
   constructor.

```
// Create the basic Amazon SQS async client
final AmazonSQSAsync sqsAsync = new AmazonSQSAsyncClient();

final QueueBufferConfig config = new QueueBufferConfig()
    .withMaxInflightReceiveBatches(5)
    .withMaxDoneReceiveBatches(15);

// Create the buffered client
final AmazonSQSAsync bufferedSqs = new AmazonSQSBufferedAsyncClient(sqsAsync, config);
```

| QueueBufferConfig configuration parameters | Parameter             | Default value                                                                                                                                                                                                                                                                                                                                                                                                                                                        | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| ------------------------------------------ | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------- | ------------- | ----------- |
| `longPoll`                                 | `true`                | When `longPoll` is set to `true`, `AmazonSQSBufferedAsyncClient` attempts to use long polling when it consumes messages.                                                                                                                                                                                                                                                                                                                                             |
| `longPollWaitTimeoutSeconds`               | 20 s                  | The maximum amount of time (in seconds) which a `ReceiveMessage` call blocks off on the server, waiting for messages to appear in the queue before returning with an empty receive result. NoteWhen long polling is disabled, this setting has no effect.                                                                                                                                                                                                            |
| `maxBatchOpenMs`                           | 200 ms                | The maximum amount of time (in milliseconds) that an outgoing call waits for other calls with which it batches messages of the same type. The higher the setting, the fewer batches are required to perform the same amount of work (however, the first call in a batch has to spend a longer time waiting). When you set this parameter to `0`, submitted requests don't wait for other requests, effectively disabling batching.                                   |
| `maxBatchSize`                             | 10 requests per batch | The maximum number of messages that are batched together in a single request. The higher the setting, the fewer batches are required to carry out the same number of requests. Note10 requests per batch is the maximum allowed value for Amazon SQS.                                                                                                                                                                                                                |
| `maxBatchSizeBytes`                        | 1 MiB                 | The maximum size of a message batch, in bytes, that the client attempts to send to Amazon SQS. Note1 MiB is the maximum allowed value for Amazon SQS.                                                                                                                                                                                                                                                                                                                |
| `maxDoneReceiveBatches`                    | 10 batches            | The maximum number of receive batches that `AmazonSQSBufferedAsyncClient` prefetches and stores client-side. The higher the setting, the more receive requests can be satisfied without having to make a call to Amazon SQS (however, the more messages are prefetched, the longer they remain in the buffer, causing their own visibility timeout to expire). Note`0` indicates that all message pre-fetching is disabled and messages are consumed only on demand. |
| `maxInflightOutboundBatches`               | 5 batches             | The maximum number of active outbound batches that can be processed at the same time. The higher the setting, the faster outbound batches can be sent (subject to quotas such as CPU or bandwidth) and the more threads are consumed by `AmazonSQSBufferedAsyncClient`.                                                                                                                                                                                              |
| `maxInflightReceiveBatches`                | 10 batches            | The maximum number of active receive batches that can be processed at the same time. The higher the setting, the more messages can be received (subject to quotas such as CPU or bandwidth), and the more threads are consumed by `AmazonSQSBufferedAsyncClient`. Note`0` indicates that all message pre-fetching is disabled and messages are consumed only on demand.                                                                                              |
| `visibilityTimeoutSeconds`                 | -1                    | When this parameter is set to a positive, non-zero value, the visibility timeout set here overrides the visibility timeout set on the queue from which messages are consumed. Note`-1` indicates that the default setting is selected for the queue.You can't set visibility timeout to `0`.                                                                                                                                                                         | ### AWS SDK for Java 2.x For AWS SDK for Java 2.x, you can create a new `SqsAsyncBatchManager` based on the following example: `// Create the basic Sqs Async Client SqsAsyncClient sqs = SqsAsyncClient.builder() .region(Region.US_EAST_1) .build(); // Create the batch manager SqsAsyncBatchManager sqsAsyncBatchManager = sqs.batchManager();` After you create the new `SqsAsyncBatchManager`, you can use it to send multiple requests to Amazon SQS (just as you can with `SqsAsyncClient`), for example: `final String queueName = "MyAsyncBufferedQueue" + UUID.randomUUID(); final CreateQueueRequest request = CreateQueueRequest.builder().queueName(queueName).build(); final String queueUrl = sqs.createQueue(request).join().queueUrl(); System.out.println("Queue created: " + queueUrl); // Send messages CompletableFuture<SendMessageResponse> sendMessageFuture; for (int i = 0; i < 10; i++) { final int index = i; sendMessageFuture = sqsAsyncBatchManager.sendMessage( r -> r.messageBody("Message " + index).queueUrl(queueUrl)); SendMessageResponse response= sendMessageFuture.join(); System.out.println("Message " + response.messageId() + " sent!"); } // Receive messages with customized configurations CompletableFuture<ReceiveMessageResponse> receiveResponseFuture = customizedBatchManager.receiveMessage( r -> r.queueUrl(queueUrl) .waitTimeSeconds(10) .visibilityTimeout(20) .maxNumberOfMessages(10) ); System.out.println("You have received " + receiveResponseFuture.join().messages().size() + " messages in total."); // Delete messages DeleteQueueRequest deleteQueueRequest =  DeleteQueueRequest.builder().queueUrl(queueUrl).build(); int code = sqs.deleteQueue(deleteQueueRequest).join().sdkHttpResponse().statusCode(); System.out.println("Queue is deleted, with statusCode " + code);` ### Configuring SqsAsyncBatchManager `SqsAsyncBatchManager` is preconfigured with settings that work for most use cases. You can further configure `SqsAsyncBatchManager`, for example: Creating custom configuration via `SqsAsyncBatchManager.Builder`: `SqsAsyncBatchManager customizedBatchManager = SqsAsyncBatchManager.builder() .client(sqs) .scheduledExecutor(Executors.newScheduledThreadPool(5)) .overrideConfiguration(b -> b .maxBatchSize(10) .sendRequestFrequency(Duration.ofMillis(200)) .receiveMessageMinWaitDuration(Duration.ofSeconds(10)) .receiveMessageVisibilityTimeout(Duration.ofSeconds(20)) .receiveMessageAttributeNames(Collections.singletonList("*")) .receiveMessageSystemAttributeNames(Collections.singletonList(MessageSystemAttributeName.ALL))) .build();` `BatchOverrideConfiguration` parameters | Parameter | Default value | Description |
| ---                                        | ---                   | ---                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |
| `maxBatchSize`                             | 10 requests per batch | The maximum number of messages that are batched together in a single request. The higher the setting, the fewer batches are required to carry out the same number of requests. NoteThe maximum allowed value for Amazon SQS is 10 requests per batch.                                                                                                                                                                                                                |
| `sendRequestFrequency`                     | 200 ms                | The maximum amount of time (in milliseconds) that an outgoing call waits for other calls with which it batches messages of the same type. The higher the setting, the fewer batches are required to perform the same amount of work (however, the first call in a batch has to spend a longer time waiting). When you set this parameter to `0`, submitted requests don't wait for other requests, effectively disabling batching.                                   |
| `receiveMessageVisibilityTimeout`          | -1                    | When this parameter is set to a positive, non-zero value, the visibility timeout set here overrides the visibility timeout set on the queue from which messages are consumed. Note `1` indicates that the default setting is selected for the queue. You can't set visibility timeout to `0`.                                                                                                                                                                        |
| `receiveMessageMinWaitDuration`            | 50 ms                 | The minimal amount of time (in milliseconds) that a `receiveMessage` call waits for available messages to be fetched. The higher the setting, the fewer batches are required to carry out the same number of request.                                                                                                                                                                                                                                                |
