# Using AWS Lambda with change streams

Amazon DocumentDB is integrated with AWS Lambda so you can use Lambda functions to process records in a change stream.
Lambda event source mapping is a resource that can be used to invoke Lambda functions in order to process Amazon DocumentDB events that don’t directly invoke Lambda.
With Amazon DocumentDB change stream as an event source, you can build event-driven applications that respond to changes in your data.
For example, you can use Lambda functions to process new documents, track updates to existing documents, or log deleted documents.

You can configure an event source mapping to send records from your Amazon DocumentDB change stream to a Lambda function.
Events can be sent one at a time or batched for improved efficiency and will processed in-order.
You can configure your event source mapping’s batching behavior based on a specific time window duration (0 - 300 sec) or batch record count (max limit of 10,000 records).
You can create multiple event source mappings to process the same data with multiple Lambda functions, or to process distinct items from multiple streams with a single function.

If your function returns an error, Lambda retries the batch until it processes successfully.
In case the events in the change stream have expired, Lambda will disable the event source mapping.
In this case, you can create a new event source mapping and configure it with a starting position of your choice.
Lambda event source mappings process events at least once due to the distributed nature of its pollers.
As a result, your Lambda function may receive duplicate events in rare situations.
Follow best practices for working with AWS Lambda functions and build idempotent functions to avoid issues related to duplicate events.
For more information see [Using AWS Lambda console with Amazon DocumentDB](../../../lambda/latest/dg/with-documentdb.md "../../../lambda/latest/dg/with-documentdb.md") in the _AWS Lambda Developer Guide_.

As performance best practices, the Lambda function needs to be short lived.
To avoid introducing unnecessary processing delays, it also should not execute complex logic.
For a high velocity stream in particular, it is better to trigger an asynchronous post-processing step function workflows than synchronous long running Lambdas.
For more information about AWS Lambda, see the [AWS Lambda Developer Guide](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md").

## Limitations

The following are limitations to consider when working with Amazon DocumentDB and AWS Lambda:

- AWS Lambda is currently supported only on Amazon DocumentDB 4.0 and 5.0.
- AWS Lambda is not currently supported on elastic clusters or global clusters.
- AWS Lambda payload sizes cannot exceed 6MB.
  For more information about Lambda batch sizes, see “Batching behavior” in [Lambda event source mappings](../../../lambda/latest/dg/invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching "../../../lambda/latest/dg/invocation-eventsourcemapping.md#invocation-eventsourcemapping-batching") section in the _AWS Lambda Developer Guide_.
