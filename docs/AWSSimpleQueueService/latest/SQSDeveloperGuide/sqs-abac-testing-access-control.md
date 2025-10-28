# Testing attribute-based access control in

Amazon SQS

The following examples show you how to test attribute-based access control in
Amazon SQS.

## Create a queue with the tag

key set to environment and the tag value set to prod

Run this AWS CLI command to test creating the queue with the tag key set
to environment and the tag value set to prod. If you don't have AWS CLI, you
can [download and configure](../../../cli/latest/userguide/getting-started-install.md "../../../cli/latest/userguide/getting-started-install.md") it for your machine.

```
aws sqs create-queue --queue-name prodQueue —region us-east-1 —tags "environment=prod"
```

You receive an `AccessDenied` error from the Amazon SQS endpoint:

```
An error occurred (AccessDenied) when calling the CreateQueue operation: Access to the resource <queueUrl> is denied.
```

This is because the tag value on the IAM user does not match the tag passed in the
[`CreateQueue`](../APIReference/API_CreateQueue.md "../APIReference/API_CreateQueue.md") API call. Remember that we applied a tag to the IAM
user with the key set to `environment` and the value set to
`beta`.

## Create a queue with the tag key

set to environment and the tag value set to beta

Run the this CLI command to test creating a queue with the tag key set to
`environment` and the tag value set to `beta`.

```
aws sqs create-queue --queue-name betaQueue —region us-east-1 —tags "environment=beta"
```

You receive a message confirming the successful creation of the queue, similar to the
one below.

```
{
"QueueUrl": "<queueUrl>“
}
```

## Sending a message to a

queue

Run this CLI command to test sending a message to a queue.

```
aws sqs send-message --queue-url <queueUrl> --message-body testMessage
```

The response shows a successful message delivery to the Amazon SQS queue. The IAM user
permission allows you to send a message to a queue that has a `beta` tag. The
response includes `MD5OfMessageBody` and `MessageId` containing the
message.

```
{
"MD5OfMessageBody": "<MD5OfMessageBody>",
"MessageId": "<MessageId>"
}

```
