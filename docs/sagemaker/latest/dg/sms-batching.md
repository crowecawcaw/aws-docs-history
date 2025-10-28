# Control the flow of data objects sent to workers

Depending on the type of labeling job you create, Amazon SageMaker Ground Truth sends data objects to workers in batches or in a streaming fashion. You can control the flow of data objects to workers in the following ways:

- For both types of labeling jobs, you can use
  `MaxConcurrentTaskCount` to control the total number of data
  objects available to all workers at a given point in time when the labeling job
  is running.
- For streaming labeling jobs, you can control the flow of data objects to
  workers by monitoring and controlling the number of data objects sent to the
  Amazon SQS associated with your labeling job.
  Use the following sections to learn more about these options.

###### Topics

- [Use MaxConcurrentTaskCount to control the flow
  of data objects](#sms-batching-maxconcurrenttaskcount "#sms-batching-maxconcurrenttaskcount")
- [Use Amazon SQS to control the flow of data objects to
  streaming labeling jobs](#sms-batching-streaming-sqs "#sms-batching-streaming-sqs")

## Use MaxConcurrentTaskCount to control the flow

of data objects

[`MaxConcurrentTaskCount`](../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-MaxConcurrentTaskCount "../APIReference/API_HumanTaskConfig.md#sagemaker-Type-HumanTaskConfig-MaxConcurrentTaskCount") defines the maximum number of data objects available at one time in the worker-portal task queue. If you use the console, this parameter is set to 1,000. If you use `CreateLabelingJob`, you can set this parameter to any integer between 1 and 5,000, inclusive.

Use the following example to better understand how the number of entries in your manifest file, the `NumberOfHumanWorkersPerDataObject`, and the `MaxConcurrentTaskCount` define what tasks workers see in their task queue in the worker-portal UI.

1. You have an input manifest files with 600 entries.
2. For each entry in your input manifest file, you can use `NumberOfHumanWorkersPerDataObject` to define the number of human workers that will label an entry from your input manifest file. In this example, you set `NumberOfHumanWorkersPerDataObject` equal to 3. This will create 3 different tasks for each entry in your input manifest file. Also, to be marked as successfully labeled, at least 3 different workers must label the object. This creates a total of 1,800 tasks (600 x 3) to be completed by workers.
3. You want workers to only see 100 tasks at a time in their queue in the worker portal UI. To do this, you set `MaxConcurrentTaskCount` equal to 100. Ground Truth will then fill the worker-portal task queue with 100 tasks per worker.
4. What happens next depends on the type of labeling job you are creating, and if it is a streaming labeling job.
   - **Streaming labeling job**: As long as the total number of objects available to workers is equal to
     `MaxConcurrentTaskCount`, all remaining dataset objects in your input manifest file and that you send in real time using Amazon SNS are placed on an Amazon SQS queue. When the total number of objects available to workers falls below `MaxConcurrentTaskCount` minus
     `NumberOfHumanWorkersPerDataObject`, a new data object from the queue is used to create`NumberOfHumanWorkersPerDataObject`-tasks, which are sent to workers in real time.
   - **Non-streaming labeling job**: As workers finish labeling one set of objects, up to `MaxConcurrentTaskCount` times `NumberOfHumanWorkersPerDataObject` number of new tasks will be sent to workers. This process is repeated until all data objects in the input manifest file are labeled.

## Use Amazon SQS to control the flow of data objects to

streaming labeling jobs

When you create a streaming labeling job, an Amazon SQS queue is automatically created
in your account. Data objects are only added to the Amazon SQS queue when the total
number of objects sent to workers is above `MaxConcurrentTaskCount`.
Otherwise, objects are sent directly to workers.

You can use this queue to manage the flow of data objects to your labeling job. To
learn more, see [Manage labeling requests with an Amazon SQS queue](sms-streaming-how-it-works-sqs.md "sms-streaming-how-it-works-sqs.md").
