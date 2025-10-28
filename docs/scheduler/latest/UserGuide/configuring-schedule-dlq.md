# Configuring a schedule's dead-letter queue in EventBridge Scheduler

Amazon EventBridge Scheduler supports dead-letter queues (DLQ) using Amazon Simple Queue Service. When a schedule fails to invoke its target, EventBridge Scheduler delivers a JSON payload containing invocation details and any response recieved from the target to an Amazon SQS standard queue
that you specify.

The following topic refers to this JSON as a _dead-letter event_. A dead-letter event lets you troubleshoot issues with your schedule or targets.
If you configure a retry policy for your schedule, EventBridge Scheduler delivers the dead-letter event it has exhausting the maximum number of retries you set.

The following topics describe how you can configure an Amazon SQS queue as a DLQ for your schedule, set up the permissions EventBridge Scheduler needs to deliver messages to Amazon SQS,
and receive dead-letter events from the DLQ.

###### Topics

- [Create an Amazon SQS queue](#configuring-schedule-dlq-create-queue "#configuring-schedule-dlq-create-queue")
- [Set up execution role permissions](#configuring-schedule-dlq-permissions "#configuring-schedule-dlq-permissions")
- [Specify a dead-letter queue](#configuring-schedule-dlq-console "#configuring-schedule-dlq-console")
- [Retrieve the dead-letter event](#configuring-schedule-dlq-dead-letter-event "#configuring-schedule-dlq-dead-letter-event")

## Create an Amazon SQS queue

Before you configure a DLQ for your schedule, you must create a standard Amazon SQS queue. For instructions on creating a queue using the Amazon SQS console, see
[Creating an Amazon SQS queue](../../../SQSDeveloperGuide/sqs-configure-create-queue.md "../../../SQSDeveloperGuide/sqs-configure-create-queue.md") in the _Amazon Simple Queue Service Developer Guide_.

###### Note

EventBridge Scheduler does not support using a FIFO queue as your schedule's DLQ.

Use the following AWS CLI command to create a standard queue.

```
`$` `aws sqs create-queue --queue-name `queue-name``
```

If successful, you'll see the `QueueURL` in the output.

```
{
    "QueueUrl": "https://sqs.us-west-2.amazonaws.com/123456789012/scheduler-dlq-test"
}
```

After you've created the queue, note the queue ARN. You'll need the ARN when you specify a DLQ for your EventBridge Scheduler schedule. You can find your queue ARN in the Amazon SQS console,
or by using the [`get-queue-attributes`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html#get-queue-attributes "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/get-queue-attributes.html#get-queue-attributes") AWS CLI command.

```
`$` `aws sqs get-queue-attributes --queue-url `your-dlq-url` --attribute-names QueueArn`
```

If successful, you will see the queue ARN in the output.

```
{
    "Attributes": {
        "QueueArn": "arn:aws:sqs:us-west-2:123456789012:scheduler-dlq-test"
    }
}
```

In the next section, you will add the required permissions to your schedule execution role to allow EventBridge Scheduler to deliver dead-letter events to Amazon SQS.

## Set up execution role permissions

To let EventBridge Scheduler to deliver dead-letter events to Amazon SQS, your schedule execution role needs the following permission policy. For more information on attaching a new permission policy to your schedule execution role,
see [Setting up the execution role](setting-up.md#setting-up-execution-role "setting-up.md#setting-up-execution-role").

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Action": [
 "sqs:SendMessage"
 ],
 "Effect": "Allow",
 "Resource": "*"
 }
 ]
}`

```

###### Note

Your schedule execution role might already have the required permissions attached if you use EventBridge Scheduler to invoke an Amazon SQS API target.

In the next section, you'll use the EventBridge Scheduler console and specify a DLQ for your schedule.

## Specify a dead-letter queue

To specify a DLQ, use the EventBridge Scheduler console or the AWS CLI to update an existing schedule, or create a new one.

Console

###### To specify a DLQ using the console

1. Sign in to the AWS Management Console, then choose the following link to open the EventBridge Scheduler section of the EventBridge conosle:
   [https://console.aws.amazon.com/scheduler/home](https://console.aws.amazon.com/scheduler/home "https://console.aws.amazon.com/scheduler/home")
2. On the EventBridge Scheduler console, create a new schedule, or choose an existing schedule from your list of schedules to edit.
3. On the **Settings** page, for **Dead-letter queue (DLQ)**, do one of the following:
   - Choose **Select an Amazon SQS queue in my AWS account as a DLQ**, then choose the queue ARN for your DLQ from the dropdown list.
   - Choose **Specify an Amazon SQS queue in other AWS accounts as a DLQ**, then enter the queue ARN for your DLQ. If you choose a queue in another
     AWS account, the EventBridge Scheduler console will not be able to display the queue ARNs in a dropdown list.

4. Review your selections, then choose **Create schedule** or **Save schedule** to finish configuring a DLQ.
5. (Optional) To view a schedule's DLQ details, choose the name of the schedule from the list, then choose
   the **Dead-letter queue** tab on the **Schedule detail** page.

AWS CLI

###### To update an existing schedule using the AWS CLI

- Use the [`update-schedule`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/update-schedule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/update-schedule.html")
  command to update your schedule. Specify the Amazon SQS queue you created previously as the DLQ. Specify the IAM role ARN
  to which you attached the required Amazon SQS permissions as the execution role. Replace all other placeholder values with your
  information.

```
`$` `aws scheduler update-schedule --name `existing-schedule` \
 --schedule-expression '`rate(5 minutes)`' \
 --target '{**"DeadLetterConfig": {"Arn": "`DLQ_ARN`"}**, "RoleArn": "`ROLE_ARN`", "Arn":"`QUEUE_ARN`", "Input": "Hello world!" }' \
 --flexible-time-window '{ "Mode": "OFF"}'`
```

###### To create a new schedule with a DLQ using the AWS CLI

- Use the [`create-schedule`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/create-schedule.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/scheduler/create-schedule.html")
  command to create a schedule. Replace all placeholder values with your information.

```
`$` `aws scheduler create-schedule --name `new-schedule` \
 --schedule-expression '`rate(5 minutes)`' \
 --target '{**"DeadLetterConfig": {"Arn": "`DLQ_ARN`"}**, "RoleArn": "`ROLE_ARN`", "Arn":"`QUEUE_ARN`", "Input": "Hello world!" }' \
 --flexible-time-window '{ "Mode": "OFF"}'`
```

In the next section, you'll use the AWS CLI to recieve a dead-letter event from the DLQ.

## Retrieve the dead-letter event

Use the [`receive-message`](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/sqs/receive-message.html") command,
as shown in the following, to retrieve a dead-letter event from the DLQ. You can set the number of messages to retrieve using the
`--max-number-of-messages` attribute.

```
`$` `aws sqs receive-message --queue-url `your-dlq-url` --attribute-names All --message-attribute-names All --max-number-of-messages 1`
```

If successful, you will see output similar to the following.

```
{
    "Messages": [
        {
            "MessageId": "2aeg3510-fe3a-4f5a-ab6a-6906560eaf7e",
            "ReceiptHandle": "AQEBkNKTdOMrWgHKPoITRBwrPoK3eCSZIcZwVqCY0BZ+FfTcORFpopJbtCqj36VbBTlHreM8+qM/m5jcwqSlAlGmIJO/hYmMgn/+dwIty9izE7HnpvRhhEyHxbeTZ5V05RbeasYaBdNyi9WLcnAHviDh6MebLXXNWoFyYNsxdwJuG0f/w3htX6r3dxpXvvFNPGoQb8ihY37+u0gtsbuIwhLtUSmE8rbldEEwiUfi3IJ1zEZpUS77n/k1GWrMrnYg0Gx/BuaLzOrFi2F738XI/Hnh45uv3ca6OYwS1ojPQ1LtX2URg1haV5884FYlaRvY8jRlpCZabTkYRTZKSXG5KNgYZnHpmsspii6JNkjitYVFKPo0H91w5zkHlSx3REAuWk7m3r7PmOMvTNPMhctbD3CkTw==",
            "MD5OfBody": "07adc3fc889d6107d8bb8fda42fe0573",
            "Body": "{\"MessageBody\":\"Hello, world!",\"QueueUrl\":\"https://sqs.us-west-2.amazonaws.com/123456789012/does-not-exist\"}",
            "Attributes": {
                "SenderId": "AROA2DZE3W4CTL5ZR7EIN:ff00212d8c453aaaae644bc6846d4723",
                "ApproximateFirstReceiveTimestamp": "1652499058144",
                "ApproximateReceiveCount": "2",
                "SentTimestamp": "1652490733042"
            },
            "MD5OfMessageAttributes": "f72c1d78100860e00403d849831d4895",
            "MessageAttributes": {
                "ERROR_CODE": {
                    "StringValue": "AWS.SimpleQueueService.NonExistentQueue",
                    "DataType": "String"
                },
                "ERROR_MESSAGE": {
                    "StringValue": "The specified queue does not exist for this wsdl version.",
                    "DataType": "String"
                },
                "EXECUTION_ID": {
                    "StringValue": "ad06616e51cdf74a",
                    "DataType": "String"
                },
                "EXHAUSTED_RETRY_CONDITION": {
                    "StringValue": "MaximumEventAgeInSeconds",
                    "DataType": "String"
                }
                "IS_PAYLOAD_TRUNCATED": {
                    "StringValue": "false",
                    "DataType": "String"
                },
                "RETRY_ATTEMPTS": {
                    "StringValue": "0",
                    "DataType": "String"
                },
                "SCHEDULED_TIME": {
                    "StringValue": "2022-05-14T01:12:00Z",
                    "DataType": "String"
                },
                "SCHEDULE_ARN": {
                    "StringValue": "arn:aws:scheduler:us-west-2:123456789012:schedule/DLQ-test",
                    "DataType": "String"
                },
                "TARGET_ARN": {
                    "StringValue": "arn:aws:scheduler:::aws-sdk:sqs:sendMessage",
                    "DataType": "String"
                }
            }
        }
    ]
}
```

Note the following attributes in the dead-letter event to help you identify and troubleshoot possible reasons why target inovcation has failed.

- **`ERROR_CODE`** – Contains the error code that EventBridge Scheduler receives from the target's service API. In the preceding example,
  the error code returned by Amazon SQS is `AWS.SimpleQueueService.NonExistentQueue`. If the schedule fails to invoke a target due to an issue with EventBridge Scheduler, you'll
  see the following error code instead: `AWS.Scheduler.InternalServerError`.
- **`ERROR_MESSAGE`** – Contains the error message that EventBridge Scheduler receives from the target's service API. In the preceding example,
  the error message returned by Amazon SQS is `The specified queue does not exist for this wsdl version`. If the schedule fails due to an issue with EventBridge Scheduler, you'll
  see the following error message instead: `Unexpected error occurred while processing the request`.
- **`TARGET_ARN`** – The ARN of the target that your schedule invokes, in the following service ARN format:
  `arn:aws:scheduler:::aws-sdk:`service`:`apiAction``.
- **`EXHAUSTED_RETRY_CONDITION`** – Indicates why the event was delivered to the DLQ. This attribute will be present if the error from
  the target API is a retryable error, and not a permanent error. The attribute can contain the values `MaximumRetryAttempts` if EventBridge Scheduler sent it to the
  DLQ after it exceeded the maximum retry attempts you configured for the schedule, or `MaximumEventAgeInSeconds`, if the event is older than the maximum age
  you configured on the schedule and is still failing to deliver.

In the preceding example, we can determine, based on the error code, and the error message, that the target queue we specified for the schedule does not exist.
