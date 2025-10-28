# Configuring an Amazon SQS queue to

trigger an AWS Lambda function

You can use a Lambda function to process messages from an Amazon SQS queue. Lambda polls the
queue and invokes your function synchronously, passing a batch of messages as an
event.

**Configuring visibility timeout**

Set the queue's visibility timeout to at least six times the [function timeout](../../../lambda/latest/dg/configuration-function-common.md#configuration-common-summary "../../../lambda/latest/dg/configuration-function-common.md#configuration-common-summary"). This ensures Lambda has enough time to retry if a
function is throttled while processing a previous batch.

**Using a dead-letter queue (DLQ)**

Specify a dead-letter queue to capture messages that the Lambda function fails
to process.

**Handling multiple queues and functions**

A Lambda function can process multiple queues by creating a separate event
source for each queue. You can also associate multiple Lambda functions with the
same queue.

**Permissions for encrypted queues**

If you associate an encrypted queue with a Lambda function but Lambda doesn't
poll for messages, add the `kms:Decrypt` permission to your Lambda
execution role.

**Restrictions**

The queue and Lambda function must be in the same AWS Region.

An [encrypted queue](sqs-server-side-encryption.md "sqs-server-side-encryption.md")
that uses the default key (AWS managed KMS key for Amazon SQS) cannot invoke a Lambda function in a different AWS account.

For implementation details, see [Using AWS Lambda
with Amazon SQS](../../../lambda/latest/dg/with-sqs.md "../../../lambda/latest/dg/with-sqs.md") in the _AWS Lambda Developer Guide_.

## Prerequisites

To configure Lambda function triggers, you must meet the following requirements:

- If you use a user, your Amazon SQS role must include the following
  permissions:
  - `lambda:CreateEventSourceMapping`
  - `lambda:ListEventSourceMappings`
  - `lambda:ListFunctions`

- The Lambda execution role must include the following permissions:
  - `sqs:DeleteMessage`
  - `sqs:GetQueueAttributes`
  - `sqs:ReceiveMessage`

- If you associate an encrypted queue with a Lambda function, add the
  `kms:Decrypt` permission to the Lambda execution role.

For more information, see [Overview of managing access in
Amazon SQS](sqs-overview-of-managing-access.md "sqs-overview-of-managing-access.md").

###### To configure a queue to trigger a Lambda function (console)

1. Open the Amazon SQS console at
   [https://console.aws.amazon.com/sqs/](https://console.aws.amazon.com/sqs/ "https://console.aws.amazon.com/sqs/").
2. In the navigation pane, choose **Queues**.
3. On the **Queues** page, choose the queue to configure.
4. On the queue's page, choose the **Lambda triggers** tab.
5. On the **Lambda triggers** page, choose a Lambda trigger.

If the list doesn't include the Lambda trigger that you need, choose
**Configure Lambda function trigger**. Enter the Amazon Resource
Name (ARN) of the Lambda function or choose an existing resource. Then choose
**Save**. 6. Choose **Save**. The console saves the configuration and displays
the **Details** page for the queue.

On the **Details** page, the **Lambda triggers**
tab displays the Lambda function and its status. It takes approximately 1 minute for
the Lambda function to become associated with your queue. 7. To verify the results of the configuration, [send
a message to your queue](creating-sqs-standard-queues.md#sqs-send-messages "creating-sqs-standard-queues.md#sqs-send-messages") and then view the triggered Lambda function in the
Lambda console.
