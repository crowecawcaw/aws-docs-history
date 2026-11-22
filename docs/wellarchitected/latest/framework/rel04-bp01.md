

# REL04-BP01 Identify the kind of distributed systems you depend on

 Distributed systems communicate in one of three styles: synchronous, asynchronous, or batch. Each style carries different failure characteristics, latency behavior, and coupling. When you know which style each dependency uses, you can choose error handling, timeouts, and retry strategies that match how that dependency behaves. Misidentifying the style leads to brittle chains, indefinite waits, and duplicate processing. 

 **Desired outcome:** 
+  You have classified each dependency your workload calls as synchronous, asynchronous, or batch. 
+  Your workload tolerates disruption in any dependency because its error handling matches the communication style. 
+  Your synchronous calls have defined timeouts and fail fast instead of waiting indefinitely. 
+  Your asynchronous consumers handle duplicate messages without producing duplicate side effects. 
+  Your batch jobs run on a controlled schedule that prevents concurrent runs of the same job. 

 **Common anti-patterns:** 
+  A workload waits indefinitely for a dependency response, so clients time out without knowing whether the request was received. 
+  Teams chain synchronous dependencies that each call the next, so every system in the path must be available for a single request to succeed. 
+  Teams communicate asynchronously but assume exactly-once delivery, even though duplicate messages still arrive after retries or network failures. 
+  Teams run batch jobs without a scheduler, which allows concurrent runs of the same job to corrupt output. 

 **Benefits of establishing this best practice:** 
+  Workloads absorb dependency disruptions because each interaction style is handled on its own terms. 
+  Synchronous request paths stay responsive because timeouts and fail-fast behavior prevent cascading waits. 
+  Asynchronous processing stays correct under retries because consumers expect and handle duplicates. 
+  Batch processing produces reliable output because scheduling controls prevent overlapping runs. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Synchronous communication blocks the caller until the dependency responds. This creates *temporal coupling*: the workload and its dependency must be available at the same moment. Chaining several synchronous dependencies multiplies that cost. Combined availability is the product of each link's availability, so a request that crosses four dependencies at 99.9% each cannot exceed roughly 99.6% overall. A single unhealthy link in the chain fails the whole request. 

 Before you take a dependency, compare the reliability and latency it offers against what your workload requires. Distributed systems [introduce challenges](https://builder.aws.com/content/3F08f7GPFiZMCgXD8gny6OjxR0Z/challenges-with-distributed-systems) that raise architectural complexity, operational burden, and cost, including latency, network partitions, partial failure, data loss, and replication lag. A dependency's service-level objectives limit what your workload can promise. 

 Asynchronous communication removes temporal coupling by placing a durable intermediary between the producer and the consumer. Messaging through a broker can prioritize messages, track consumption for consumers, and delete a message after it is processed. Event streaming treats all messages equally, requires each consumer to track its own read position, preserves the order in which data was produced, and retains messages until a retention period expires, which makes replay possible. Choose messaging when you need per-message priority or consumption tracking. Choose event streaming when you need strict ordering or replay. 

 Asynchronous services redeliver a message after a network failure or a missing acknowledgement, so duplicate delivery is normal. A consumer that assumes each message arrives once will double-process. Design consumers to be idempotent so that a repeated message produces no additional effect. For more detail, see [REL04-BP04 Make mutating operations idempotent](rel04-bp04.md). 

 Batch dependencies accept a large input, run unattended jobs, and produce output, sometimes over minutes and sometimes over days. You define a schedule window, choose input and output storage that scales to the data volume, orchestrate jobs that depend on each other, and detect jobs that run longer than expected or that overlap. A batch system without these controls produces stale or duplicated output. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Inventory and classify your dependencies:** List every system your workload calls, then label each one as synchronous, asynchronous, or batch. Record the reliability and latency each dependency provides so you can confirm it meets your workload's requirements. 

1.  **Validate dependency service levels:** Monitor response times and error rates for each dependency using [AWS observability services](https://aws.amazon.com/cloudops/monitoring-and-observability) to confirm it performs at the level your workload needs. Add error handling and [logging](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) so you can troubleshoot when a dependency degrades. 

1.  **Harden synchronous calls:** Set an explicit timeout on every call so the workload does not wait indefinitely, and see [Tuning AWS Java SDK HTTP request settings](https://aws.amazon.com/blogs/database/tuning-aws-java-sdk-http-request-settings-for-latency-aware-amazon-dynamodb-applications/) for latency-aware configuration. Avoid chaining multiple synchronous dependencies for one function, minimize chatty back-and-forth calls, and fail fast rather than block. For retry handling on function invocations, see the [AWS Lambda retry guidance](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html). 

1.  **Design asynchronous communication:** Decide between [messaging](https://aws.amazon.com/messaging/) and [event streaming](https://aws.amazon.com/what-is/streaming-data/) based on your ordering, priority, and replay needs. Define how the workload learns that processing completed, for example through an [asynchronous invocation destination](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-destinations). Make consumers idempotent to absorb duplicate delivery, and limit retries to protect workload resources, following the [asynchronous error handling guidance](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html#invocation-async-errors). 

1.  **Control batch dependencies:** Define the recurrence window for each job, and choose scalable input and output storage such as [Amazon S3](https://aws.amazon.com/s3/), [Amazon EFS](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html), or [Amazon FSx for Lustre](https://docs.aws.amazon.com/fsx/latest/LustreGuide/what-is.html). Orchestrate dependent jobs with [AWS Step Functions](https://aws.amazon.com/step-functions/) and [AWS Batch](https://aws.amazon.com/batch/), and prevent concurrent runs of the same job. 

1.  **Instrument observability and tracing:** Monitor [Amazon SQS metrics](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-available-cloudwatch-metrics.html) and [event streaming metrics](https://docs.aws.amazon.com/streams/latest/dev/monitoring-with-cloudwatch.html) in [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/), and monitor batch jobs with [CloudWatch Container Insights](https://docs.aws.amazon.com/batch/latest/userguide/cloudwatch-container-insights.html). Instrument request paths with [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/xray-concepts.html) to trace failures across dependencies. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL04-BP02 Implement loosely coupled dependencies](rel04-bp02.md) 
+  [REL04-BP04 Make mutating operations idempotent](rel04-bp04.md) 
+  [REL05-BP03 Control and limit retry calls](rel05-bp03.md) 
+  [REL05-BP05 Set client timeouts](rel05-bp05.md) 
+  [REL11-BP05 Use static stability to prevent bimodal behavior](rel11-bp05.md) 

 **Related documents:** 
+  [The Amazon Builders' Library: Challenges with distributed systems](https://builder.aws.com/content/3F08f7GPFiZMCgXD8gny6OjxR0Z/challenges-with-distributed-systems) 
+  [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html) 
+  [Understanding retry behavior in Lambda](https://docs.aws.amazon.com/lambda/latest/dg/invocation-retries.html) 
+  [Invoking a Lambda function asynchronously](https://docs.aws.amazon.com/lambda/latest/dg/invocation-async.html) 
+  [Handle duplicate records](https://docs.aws.amazon.com/streams/latest/dev/kinesis-record-processor-duplicates.html) 
+  [Amazon SQS FIFO queues](https://aws.amazon.com/sqs/faqs/#FIFO_queues) 
+  [Tuning AWS Java SDK HTTP request settings for latency-aware Amazon DynamoDB applications](https://aws.amazon.com/blogs/database/tuning-aws-java-sdk-http-request-settings-for-latency-aware-amazon-dynamodb-applications/) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Capital One: Achieving resiliency to run mission-critical applications (FSI314)](https://www.youtube.com/watch?v=hgIqWCRKA2k) 

 **Related examples:** 
+  [GitHub - aws-samples/aws-stepfunction-complex-orchestrator-app](https://github.com/aws-samples/aws-stepfunction-complex-orchestrator-app) 

 **Related services:** 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon Simple Queue Service (Amazon SQS)](https://aws.amazon.com/sqs/) 
+  [Amazon Kinesis](https://aws.amazon.com/kinesis/) 
+  [Application Observability (APM)](https://aws.amazon.com/cloudwatch/features/application-observability-apm/) 