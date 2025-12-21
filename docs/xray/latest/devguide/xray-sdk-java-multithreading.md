# Passing segment context between threads in a

multithreaded application

###### Note

X-Ray SDK/Daemon Maintenance Notice – On February 25th, 2026, the AWS X-Ray SDKs/Daemon will enter maintenance mode, where AWS will limit X-Ray SDK and Daemon releases to address security issues only. For more information on the support timeline, see
[X-Ray SDK and Daemon Support timeline](xray-sdk-daemon-timeline.md "xray-sdk-daemon-timeline.md"). We recommend to migrate to OpenTelemetry. For more information on migrating to OpenTelemetry, see [Migrating from X-Ray instrumentation to OpenTelemetry instrumentation](xray-sdk-migration.md "xray-sdk-migration.md") .

When you create a new thread in your application, the `AWSXRayRecorder` doesn't
maintain a reference to the current segment or subsegment [Entity](../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/entities/Entity.md "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/entities/Entity.md"). If you use an
instrumented client in the new thread, the SDK tries to write to a segment that doesn't exist,
causing a [SegmentNotFoundException](../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/exceptions/SegmentNotFoundException.md "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/exceptions/SegmentNotFoundException.md").

To avoid throwing exceptions during development, you can configure the recorder with a
[ContextMissingStrategy](../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/strategy/ContextMissingStrategy.md "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/strategy/ContextMissingStrategy.md") that tells it to log an error instead. You can configure the
strategy in code with [SetContextMissingStrategy](<../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#setContextMissingStrategy(com.amazonaws.xray.strategy.ContextMissingStrategy)> "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#setContextMissingStrategy(com.amazonaws.xray.strategy.ContextMissingStrategy)"), or configure equivalent options with an [environment variable](xray-sdk-java-configuration.md#xray-sdk-java-configuration-envvars "xray-sdk-java-configuration.md#xray-sdk-java-configuration-envvars") or [system property](xray-sdk-java-configuration.md#xray-sdk-java-configuration-sysprops "xray-sdk-java-configuration.md#xray-sdk-java-configuration-sysprops").

One way to address the error is to use a new segment by calling [beginSegment](<../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#beginSegment(java.lang.String)> "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#beginSegment(java.lang.String)") when you start the thread and [endSegment](../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#endSegment-- "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/AWSXRayRecorder.md#endSegment--") when you close it. This works if you are instrumenting code that doesn't
run in response to an HTTP request, like code that runs when your application starts.

If you use multiple threads to handle incoming requests, you can pass the current segment or subsegment to the
new thread and provide it to the global recorder. This ensures that the information recorded within the new thread
is associated with the same segment as the rest of the information recorded about that request. Once the segment is
available in the new thread, you can execute any runnable with access to that segment's context using the
`segment.run(() -> { ... })` method.

See [Using instrumented clients in worker threads](scorekeep-workerthreads.md "scorekeep-workerthreads.md") for an
example.

## Using X-Ray with Asynchronous Programming

The X-Ray SDK for Java can be used in asynchronous Java programs with
[SegmentContextExecutors](../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/contexts/SegmentContextExecutors.md "../../../xray-sdk-for-java/latest/javadoc/com/amazonaws/xray/contexts/SegmentContextExecutors.md").
The SegmentContextExecutor implements the Executor interface, which means it can be passed into all asynchronous operations of a
[CompletableFuture](https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html "https://docs.oracle.com/javase/8/docs/api/java/util/concurrent/CompletableFuture.html").
This ensures that any asynchronous operations will be executed with the correct segment in its context.

###### Example App.java: Passing SegmentContextExecutor to CompletableFuture

```
DynamoDbAsyncClient client = DynamoDbAsyncClient.create();

AWSXRay.beginSegment();

// ...

client.getItem(request).thenComposeAsync(response -> {
    // If we did not provide the segment context executor, this request would not be traced correctly.
    return client.getItem(request2);
}, SegmentContextExecutors.newSegmentContextExecutor());
```
