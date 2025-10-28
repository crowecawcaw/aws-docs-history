# Ground Truth streaming labeling jobs

If you want to perpetually send new data objects to Amazon SageMaker Ground Truth to be labeled, use a
streaming labeling job. Streaming labeling jobs allow you to:

- Send new dataset objects to workers in real time using a perpetually running
  labeling job. Workers continuously receive new data objects to label as long as the
  labeling job is active and new objects are being sent to it.
- Gain visibility into the number of objects that have been queued and are waiting
  to be labeled. Use this information to control the flow of data objects sent to your
  labeling job.
- Receive label data for individual data objects in real time as workers finish
  labeling them.
  Ground Truth streaming labeling jobs remain active until they are manually stopped or have been
  idle for more than 10 days. You can intermittently send new data objects to workers while
  the labeling job is active.

If you are a new user of Ground Truth streaming labeling jobs, it is recommended that you review
[How it works](#sms-streaming-how-it-works "#sms-streaming-how-it-works").

Use [Create a streaming labeling job](sms-streaming-create-job.md "sms-streaming-create-job.md") to
learn how to create a streaming labeling job.

###### Note

Ground Truth streaming labeling jobs are only supported through the SageMaker API.

## How it works

When you create a Ground Truth streaming labeling job, the job remains active
until it is manually stopped, remains idle for more than 10 days, or is unable
to access input data sources. You can intermittently send new data objects to
workers while it is active. A worker can continue to receive new data objects in
real time as long as the total number of tasks currently available to the worker
is less than the value in [`MaxConcurrentTaskCount`](../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-MaxConcurrentTaskCount "../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-MaxConcurrentTaskCount"). Otherwise, the data object
is sent to a queue that Ground Truth creates on your behalf in [Amazon Simple Queue Service](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md") (Amazon SQS) for later processing. These tasks are sent to
workers as soon as the total number of tasks currently available to a worker
falls below `MaxConcurrentTaskCount`. If a data object is not sent to
a worker after 14 days, it expires. You can view the number of tasks pending in
the queue and adjust the number of objects you send to the labeling job. For
example, you may decrease the speed at which you send objects to the labeling
job if the backlog of pending objects moves above a threshold.

###### Topics

- [Send data to a streaming labeling job](sms-streaming-how-it-works-send-data.md "sms-streaming-how-it-works-send-data.md")
- [Manage labeling requests with an Amazon SQS queue](sms-streaming-how-it-works-sqs.md "sms-streaming-how-it-works-sqs.md")
- [Receive output data from a streaming
  labeling job](sms-streaming-how-it-works-output-data.md "sms-streaming-how-it-works-output-data.md")
- [Duplicate message handling](sms-streaming-impotency.md "sms-streaming-impotency.md")
