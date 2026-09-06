

# Real-time and async
<a name="bb-realtime-async"></a>

This section covers Blocks for real-time communication and background processing.

## Choosing a real-time or async Block
<a name="_choosing_a_real_time_or_async_block"></a>


| Block | Best for | Avoid when | 
| --- | --- | --- | 
|  `Realtime`  | Live updates, chat, notifications, collaborative features via WebSocket | Your use case is request/response only (no persistent connections needed) | 
|  `AsyncJob`  | Long-running background tasks, event-driven processing, queue-based workloads | The task completes in under a few seconds (handle it synchronously) | 
|  `CronJob`  | Scheduled recurring tasks, periodic cleanup, report generation | You need immediate execution triggered by an event (use AsyncJob) | 

## Realtime
<a name="bb-realtime"></a>

Typed WebSocket pub/sub channels. Define namespaces with Zod schemas for type-safe message broadcasting. Publish messages from the server and subscribe from the client. Each namespace can have multiple channels for topic-based routing.

Locally, Realtime uses an in-process EventEmitter with a local WebSocket server. On AWS, it provisions API Gateway WebSocket APIs with DynamoDB for connection management. Best for live updates, chat, notifications, and collaborative features.

For more information, see [bb-realtime on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-realtime).

## AsyncJob
<a name="bb-async-job"></a>

Background job processing. Submit work that runs asynchronously outside the request lifecycle. Define a handler function that processes each job payload. Jobs are fire-and-forget from the caller’s perspective with automatic retries on failure.

Locally, AsyncJob executes handlers in-process. On AWS, it provisions an SQS queue with a Lambda consumer. Best for tasks that don’t need an immediate response: sending emails, processing uploads, generating reports.

For more information, see [bb-async-job on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-async-job).

## CronJob
<a name="bb-cron-job"></a>

Scheduled task execution. Define a handler function and a cron expression or rate schedule. The handler runs automatically at the specified interval.

Locally, CronJob executes on schedule using Node.js timers. On AWS, it provisions an EventBridge rule that triggers a Lambda function. Best for periodic maintenance, batch processing, cleanup jobs, and report generation.

For more information, see [bb-cron-job on GitHub](https://github.com/aws-devtools-labs/aws-blocks/tree/main/packages/bb-cron-job).