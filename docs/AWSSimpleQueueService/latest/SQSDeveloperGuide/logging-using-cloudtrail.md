# Logging Amazon Simple Queue Service API calls using

AWS CloudTrail

CloudTrail allows you to log and monitor Amazon SQS operations using two event types: data events and
management events. This makes it easy to track and audit Amazon SQS activity in your account.

## Amazon SQS data events in CloudTrail

[Data events](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events") provide information about the resource operations performed on or in a
resource (for example, sending messages to an Amazon SQS object). These are also known as data
plane operations. Data events are often high-volume activities. By default, CloudTrail doesn’t log
data events. The CloudTrail **Event history** doesn't record data events.

Additional charges apply for data events. For more information about CloudTrail pricing, see
[AWS CloudTrail Pricing](https://aws.amazon.com/cloudtrail/pricing/ "https://aws.amazon.com/cloudtrail/pricing/").

You can log data events for the Amazon SQS resource types by using the CloudTrail console, AWS CLI,
or CloudTrail API operations. For more information about how to log data events, see [Logging data events with the AWS Management Console](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#logging-data-events-console") and [Logging data events with the AWS Command Line Interface](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md#creating-data-event-selectors-with-the-AWS-CLI") in the
_AWS CloudTrail User Guide_.

To log Amazon SQS data events with CloudTrail, you must use advanced event selectors to configure the
specific Amazon SQS resources or actions you want to log. Include the resource type [`AWS::SQS::Queue`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.md") to capture queue-related actions. You can refine
your logging preferences even further with using filters like `eventName` (such as
[`SendMessage`](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md") events). For more information, see [AdvancedEventSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedEventSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedEventSelector.md") in the _CloudTrail API
Reference_.

| Data event type (console) | resources.type value                                                                                                                                               | Data APIs logged to CloudTrail                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Amazon SQS queue**      | [`AWS::SQS::Queue`](../../../AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-sqs-queue.md") | • [ChangeMessageVisibility](../APIReference/API_ChangeMessageVisibility.md "../APIReference/API_ChangeMessageVisibility.md")<br>• [ChangeMessageVisibilityBatch](../APIReference/API_ChangeMessageVisibilityBatch.md "../APIReference/API_ChangeMessageVisibilityBatch.md")<br>• [DeleteMessage](../APIReference/API_DeleteMessage.md "../APIReference/API_DeleteMessage.md")<br>• [DeleteMessageBatch](../APIReference/API_DeleteMessageBatch.md "../APIReference/API_DeleteMessageBatch.md")<br>• [GetQueueAttributes](../APIReference/API_GetQueueAttributes.md "../APIReference/API_GetQueueAttributes.md")<br>• [GetQueueUrl](../APIReference/API_GetQueueUrl.md "../APIReference/API_GetQueueUrl.md")<br>• [ListDeadLetterSourceQueues](../APIReference/API_ListDeadLetterSourceQueues.md "../APIReference/API_ListDeadLetterSourceQueues.md")<br>• [ListQueues](../APIReference/API_ListQueues.md "../APIReference/API_ListQueues.md")<br>• [ListQueueTags](../APIReference/API_ListQueueTags.md "../APIReference/API_ListQueueTags.md")<br>• [ReceiveMessage](../APIReference/API_ReceiveMessage.md "../APIReference/API_ReceiveMessage.md")<br>• [SendMessage](../APIReference/API_SendMessage.md "../APIReference/API_SendMessage.md")<br>• [SendMessageBatch](../APIReference/API_SendMessageBatch.md "../APIReference/API_SendMessageBatch.md") |

Use advanced event selectors to filter fields and log only important events. For more
information about these fields, see [AdvancedFieldSelector](../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md "../../../awscloudtrail/latest/APIReference/API_AdvancedFieldSelector.md") in the
_AWS CloudTrail API Reference_.

## Amazon SQS management events in CloudTrail

[Management events](../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events "../../../awscloudtrail/latest/userguide/logging-management-events-with-cloudtrail.md#logging-management-events") provide information about management operations that are performed on resources in your AWS account. These are also known as control plane operations. By default, CloudTrail logs management events.

Amazon SQS logs the following control plane operations to CloudTrail as _management
events_.

- [AddPermission](../APIReference/API_AddPermission.md "../APIReference/API_AddPermission.md")
- [CancelMessageMoveTask](../APIReference/API_CancelMessageMoveTask.md "../APIReference/API_CancelMessageMoveTask.md")
- [CreateQueue](../APIReference/API_CreateQueue.md "../APIReference/API_CreateQueue.md")
- [DeleteQueue](../APIReference/API_DeleteQueue.md "../APIReference/API_DeleteQueue.md")
- [ListMessageMoveTasks](../APIReference/API_ListMessageMoveTasks.md "../APIReference/API_ListMessageMoveTasks.md")
- [PurgeQueue](../APIReference/API_PurgeQueue.md "../APIReference/API_PurgeQueue.md")
- [RemovePermission](../APIReference/API_RemovePermission.md "../APIReference/API_RemovePermission.md")
- [SetQueueAttributes](../APIReference/API_SetQueueAttributes.md "../APIReference/API_SetQueueAttributes.md")
- [StartMessageMoveTask](../APIReference/API_StartlMessageMoveTask.md "../APIReference/API_StartlMessageMoveTask.md")
- [TagQueue](../APIReference/API_TagQueue.md "../APIReference/API_TagQueue.md")
- [UntagQueue](../APIReference/API_UntagQueue.md "../APIReference/API_UntagQueue.md")

## Amazon SQS event example

An event represents a single request from any source and includes information about the requested API operation, the date and time of the operation, request parameters, and so on. CloudTrail log files aren't an ordered stack trace of the public API calls, so events don't appear in any specific order.

The following example shows a CloudTrail event that demonstrates the `SendMessage`
operation.

```
{
  "eventVersion": "1.09",
  "userIdentity": {
    "type": "AssumedRole",
    "principalId": "EXAMPLE_PRINCIPAL_ID",
    "arn": "arn:aws:sts::123456789012:assumed-role/RoleToBeAssumed/SessionName",
    "accountId": "123456789012",
    "accessKeyId": "ACCESS_KEY_ID",
    "sessionContext": {
      "sessionIssuer": {
        "type": "Role",
        "principalId": "AKIAI44QH8DHBEXAMPLE",
        "arn": "arn:aws:sts::123456789012:assumed-role/RoleToBeAssumed",
        "accountId": "123456789012",
        "userName": "RoleToBeAssumed"
      },
      "attributes": {
        "creationDate": "2023-11-07T22:13:06Z",
        "mfaAuthenticated": "false"
      }
    }
  },
  "eventTime": "2023-11-07T23:59:11Z",
  "eventSource": "sqs.amazonaws.com",
  "eventName": "SendMessage",
  "awsRegion": "ap-southeast-4",
  "sourceIPAddress": "10.0.118.80",
  "userAgent": "aws-cli/1.29.16 md/Botocore#1.31.16 ua/2.0 os/linux#5.4.250-173.369.amzn2int.x86_64 md/arch#x86_64 lang/python#3.8.17 md/pyimpl#CPython cfg/retry-mode#legacy botocore/1.31.16",
  "requestParameters": {
    "queueUrl": "https://sqs.ap-southeast-4.amazonaws.com/123456789012/MyQueue",
    "messageBody": "HIDDEN_DUE_TO_SECURITY_REASONS",
    "messageDeduplicationId": "MsgDedupIdSdk1ae1958f2-bbe8-4442-83e7-4916e3b035aa",
    "messageGroupId": "MsgGroupIdSdk16"
  },
  "responseElements": {
    "mD5OfMessageBody": "9a4e3f7a614d9dd9f8722092dbda17a2",
    "mD5OfMessageSystemAttributes": "f88f0587f951b7f5551f18ae699c3a9d",
    "messageId": "93bb6e2d-1090-416c-81b0-31eb1faa8cd8",
    "sequenceNumber": "18881790870905840128"
  },
  "requestID": "c4584600-fe8a-5aa3-a5ba-1bc42f055fae",
  "eventID": "98c735d8-70e0-4644-9432-b6ced4d791b1",
  "readOnly": false,
  "resources": [
    {
      "accountId": "123456789012",
      "type": "AWS::SQS::Queue",
      "ARN": "arn:aws:sqs:ap-southeast-4:123456789012:MyQueue"
    }
  ],
  "eventType": "AwsApiCall",
  "managementEvent": false,
  "recipientAccountId": "123456789012",
  "eventCategory": "Data",
  "tlsDetails": {
    "tlsVersion": "TLSv1.2",
    "cipherSuite": "ECDHE-RSA-AES128-GCM-SHA256",
    "clientProvidedHostHeader": "sqs.ap-southeast-4.amazonaws.com"
  }
```

###### Note

The `ListQueues` operation is a unique case because it doesn’t act on a
specific resource. As a result, the ARN field doesn’t include a queue name and uses a
wildcard (\*) instead.

For information about CloudTrail record contents, see [CloudTrail
record contents](../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md "../../../awscloudtrail/latest/userguide/cloudtrail-event-reference-record-contents.md") in the _AWS CloudTrail User Guide_.
