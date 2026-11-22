

# Delete a stream

You can delete a stream with the Kinesis Data Streams console, or programmatically. To delete a stream programmatically, use `DeleteStreamRequest`, as shown in the following code.

```java
DeleteStreamRequest deleteStreamRequest = new DeleteStreamRequest();
deleteStreamRequest.setStreamName(myStreamName);
client.deleteStream(deleteStreamRequest);
```

Shut down any applications that are operating on the stream before you delete it. If an application attempts to operate on a deleted stream, it receives `ResourceNotFound` exceptions. Also, if you subsequently create a new stream that has the same name as your previous stream, and applications that were operating on the previous stream are still running, these applications might try to interact with the new stream as though it were the previous stream—with unpredictable results.

Delete every queue on a stream before you delete the stream. `DeleteStream` fails with `ResourceInUseException` while a queue is attached, and `EnforceConsumerDeletion` deletes enhanced fan-out consumers but has no effect on queues. For more information, see [Consume records from a stream with queues](consuming-with-queues.md).