

# Lambda parameters for Amazon SQS event source mappings

All Lambda event source types share the same [CreateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_CreateEventSourceMapping.html) and [UpdateEventSourceMapping](https://docs.aws.amazon.com/lambda/latest/api/API_UpdateEventSourceMapping.html) API operations. However, only some of the parameters apply to Amazon SQS.


| Parameter | Required | Default | Notes | 
| --- | --- | --- | --- | 
| BatchSize | N | 10 | For standard queues, the maximum is 10,000. For FIFO queues, the maximum is 10, or 10,000 if the event source mapping uses [provisioned mode](with-sqs.md#sqs-provisioned-mode). For a batch size over 10, you must also set `MaximumBatchingWindowInSeconds` to at least 1 second. | 
| Enabled | N | true | none  | 
| EventSourceArn | Y | N/A | The ARN of the data stream or a stream consumer | 
| FunctionName | Y | N/A  | none  | 
| FilterCriteria | N | N/A  | [Control which events Lambda sends to your Event Function](invocation-eventfiltering.md) | 
| FunctionResponseTypes | N | N/A  | To let your Event Function report specific failures in a batch, include the value `ReportBatchItemFailures` in `FunctionResponseTypes`. For more information, see [Implementing partial batch responses](services-sqs-errorhandling.md#services-sqs-batchfailurereporting). | 
| MaximumBatchingWindowInSeconds | N | 0 | 0 to 300 seconds. For FIFO queues, you can set a batching window only on event source mappings that use provisioned mode. | 
| ProvisionedPollerConfig | N | N/A | Configures the minimum (2-200) and maximum (2-2000) number of dedicated event pollers for the SQS event source mapping. Each poller can handle up to 1 MB/sec of throughput and 10 concurrent invokes. | 
| ScalingConfig | N | N/A  | [Configuring maximum concurrency for Amazon SQS event sources](services-sqs-scaling.md#events-sqs-max-concurrency) | 