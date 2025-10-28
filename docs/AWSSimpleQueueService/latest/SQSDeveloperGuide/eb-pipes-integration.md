# Accessing Amazon EventBridge Pipes through the Amazon SQS

console

Amazon EventBridge Pipes connect sources to targets. Pipes are intended for point-to-point
integrations between supported sources and targets, with support for advanced
transformations and enrichment. EventBridge Pipes provide a highly scalable way to connect your
Amazon SQS queue to AWS services such as Step Functions, Amazon SQS, and API Gateway, as well as third-party
software as a service (SaaS) applications like Salesforce.

To set up a pipe, you choose the source, add optional filtering, define optional
enrichment, and choose the target for the event data.

On the details page for an Amazon SQS queue, you can view the pipes that use that
queue as their source. From there, you can also:

- Launch the EventBridge console to view pipe details.
- Launch the EventBridge console to create a new pipe with the queue as its
  source.
  For more information on configuring an Amazon SQS queue as a pipe source, see
  [Amazon SQS
  queue as a source](../../../eventbridge/latest/userguide/eb-pipes-sqs.md "../../../eventbridge/latest/userguide/eb-pipes-sqs.md") in the _Amazon EventBridge User Guide_. For more
  information about EventBridge Pipes in general, see [EventBridge Pipes](../../../eventbridge/latest/userguide/eb-pipes.md "../../../eventbridge/latest/userguide/eb-pipes.md").

###### To access EventBridge pipes for a given Amazon SQS queue

1. Open the [Queues
   page](https://console.aws.amazon.com/sqs/#/queues "https://console.aws.amazon.com/sqs/#/queues") of the Amazon SQS console.
2. Select a queue.
3. On the queue detail page, choose the **EventBridge Pipes**
   tab.

The **EventBridge Pipes** tab includes a list of any pipes currently
configured to use the selected queue as a source, including:

    * pipe name
    * current status
    * pipe target
    * when the pipe was last modified

4. View more pipe details or create a new pipe, if desired:
   - **To access more details about a pipe:**

   Choose the pipe name.

   This launches the **Pipe details** page of the EventBridge
   console.
   - **To create a new pipe:**

   Choose **Connect Amazon SQS queue to pipe**.

   This launches the **Create pipe** page of the EventBridge
   console, with the Amazon SQS queue specified as the pipe source. For more
   information, see [Creating an EventBridge
   pipe](../../../eventbridge/latest/userguide/eb-pipes-create.md "../../../eventbridge/latest/userguide/eb-pipes-create.md") in the _Amazon EventBridge User Guide_.

   ###### Important

   A message on an Amazon SQS queue is read by a single pipe and then deleted from the queue after being processed,
   _whether or not the message matches the filter you can configured for that pipe_. Proceed with caution when configuring multiple pipes
   to use the same queue as their source.
