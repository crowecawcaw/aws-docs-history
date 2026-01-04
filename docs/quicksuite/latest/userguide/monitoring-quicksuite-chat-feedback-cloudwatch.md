# Monitoring Amazon Quick Suite chat and feedback using CloudWatch Logs

You can use [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") to deliver user conversations and response feedback in Amazon Quick Suite for you to analyze. These logs can be delivered to multiple destinations, such as CloudWatch, Amazon S3, or (standard rates apply). We recommend that you set up conversation and feedback logging shortly after creating your Amazon Quick Suite chat agent.

The following are examples of tasks you can complete with logs from conversations and response feedback in Amazon Quick Suite:

- Identify common user queries and pain points by reviewing the chat message content.
- Monitor the quality of responses by looking at metrics like `feedbackReason`.
- Understand user sentiment and satisfaction by analyzing the feedback data, including comments and usefulness ratings.
- Generate custom dashboards and reports to track key metrics and trends over time.

###### Important

Logs from conversations might include sensitive or personally identifiable data passed in the chats. You can filter out this information from your logs when setting up logs subscription. Or you can mask this data on your logs using CloudWatch Logs masking policies. For more information, see [Help protect sensitive log data with masking](../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md "../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md").

## Supported log destinations

Amazon Quick Suite can deliver logs to the following destinations:

- **Amazon CloudWatch Logs** - For real-time monitoring and analysis
- **Amazon S3** - For long-term storage and batch processing
- **Amazon Data Firehose** - For streaming analytics and data transformation

## Prerequisites

Before you can enable logging, ensure you have:

- An active Amazon Quick Suite instance with Enterprise or Professional subscriptions
- Appropriate IAM permissions to configure log delivery
- A destination configured for your logs (CloudWatch Logs, Amazon S3 bucket, or Firehose)

## Configure logging

To enable logging for Amazon Quick Suite chat and feedback, you need to configure IAM permissions, create a delivery source and destination, and verify that logs are being delivered successfully.

###### Topics

- [Set up IAM permissions](#quicksuite-chat-feedback-setup-iam-permissions "#quicksuite-chat-feedback-setup-iam-permissions")
- [Configure log subscription](#quicksuite-chat-feedback-configure-log-subscription "#quicksuite-chat-feedback-configure-log-subscription")
- [Verify log delivery](#quicksuite-chat-feedback-verify-log-delivery "#quicksuite-chat-feedback-verify-log-delivery")

### Set up IAM permissions

To set up CloudWatch Logs for Amazon Quick Suite, use the following IAM policy examples to grant the necessary permissions.

```
{
    "Version": "2012-10-17"		 	 	 ,
    "Statement": [{
        "Sid": "QuicksightLogDeliveryPermissions",
        "Effect": "Allow",
        "Action": "quicksight:AllowVendedLogDeliveryForResource",
        "Resource": "arn:aws:quicksight:region:account-id:account/account-id"
    }]
}
```

You must also allow the `delivery.logs.amazonaws.com` service principal in your customer managed AWS KMS key policy.

```
{
    "Effect": "Allow"		 	 	 ,
    "Principal": {
        "Service": "delivery.logs.amazonaws.com"
    },
    "Action": [
        "kms:GenerateDataKey",
        "kms:Decrypt"
    ],
    "Resource": "*",
    "Condition": {
        "StringEquals": {
            "kms:EncryptionContext:SourceArn": "arn:partition:logs:region:account-id:*"
        }
    }
}
```

### Configure log subscription

For example IAM policies with all the required permissions for your specific logging destination, see [Enable logging from AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") in the _Amazon CloudWatch Logs User Guide_.

Create a delivery source with the [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") CloudWatch Logs API operation. Give the delivery source a name and for `resourceArn`, specify the ARN of your application. For `logType`, specify `CHAT_LOGS` or `FEEDBACK_LOGS`

```
{
    "logType": "CHAT_LOGS",
    "name": "my-quick-suite-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```

```
{
    "logType": "FEEDBACK_LOGS",
    "name": "my-quick-suite-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```

To enable user conversation logging with the CloudWatch Logs API operations, you call the `PutDeliverySource`, `PutDeliveryDestination`, and `CreateDelivery` API operations.

###### Note

Logs would be available for the region mentioned in resource ARN in `PutDeliverySource` input.

### Verify log delivery

Once configured, verify that logs are being delivered to your destination:

- **Verify the setup:** Verify the list of deliveries that have been created in the account by using the `DescribeDeliveries` API in CloudWatch Logs.
- **CloudWatch Logs**: Check the specified log group for new log streams.
- **Amazon S3**: Monitor your bucket for new log files.
- **Firehose**: Verify data is flowing through your delivery stream.

## Log schema and format

Amazon Quick Suite logs follow a structured schema with common fields shared across all log types and specific fields for chat and feedback logs.

### Common fields

All log events include these common fields:

- `resourceArn` - Resource ARN of your Amazon Quick Suite account (for example, `arn:aws:quicksight:us-east-1:111122223333:account/111122223333:`)
- `eventTimestamp` - ISO 8601 timestamp of the event (for example, `1763532110061`)
- `logType` - Type of log (for example, `Chat` or `Feedback`)
- `accountId` - AWS account ID (for example, `123456789012`)
- `userArn` - Amazon Quick Suite user ARN associated with the event (for example, `"arn:aws:quicksight:us-west-2:111122223333:user/default/user"`)
- `userType` - Amazon Quick Suite user type associated with the event (for example, `ADMIN_PRO`)
- `nameSpace` - Amazon Quick Suite namespace for the event (for example, `default`)
- `statusCode` - Status of the event delivery (for example, `Success`, `request_blocked`, `no_answer_found`)

### Chat logs

Chat logs capture conversation interactions and contains below fields:

- `conversationId` - Unique ID for the user conversation
- `systemMessageId` - System-generated message ID
- `latency` - Chat message latency in milliseconds
- `timeToFirstToken` - Time in milliseconds of first response token
- `messageScope` - Scope of the message
- `userMessageId` - Unique ID of the user message
- `userMessage` - user message in the conversation
- `agentId` - Unique ID of the chat agent
- `flowId` - Unique ID of the Amazon Quick Suite Flow
- `systemTextMessage` - Text message in the conversation
- `surfaceType` - Application being used for the conversation
- `webSearch` - Web search required or not
- `userSelectedResources`- List of resources selected by user
- `actionConnectors` - List of action connectors
- `citedResource` - List of cited resources
- `fileAttachment` - List of files attached by user

The following is an example of chat logs:

```
{
    "conversationId": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "systemMessageId": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "latency": "10000",
    "timeToFirstToken": "10000",
    "messageScope": "General Knowledge, ALL etc",
    "userMessageId": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "userMessage": "What is the status of my project?",
    "agentId": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "flowId": "a11b2bbc-c123-3abc-a12b-12a34b5c678d?",
    "systemTextMessage": "What is the status of my project?",
    "surfaceType": "Slack, WebApp etc.",
    "webSearch": "TRUE"
    "userSelectedResources": [{"resource_type": "Dashboard","resource_id": "146abs-1222-534894"},{"resource_type": "Space","resource_id": "123abs-1234-534894"}],
    "actionConnectors": [{"action_connector_id": "quicksight-website"},{"action_connector_id": "123abs-1234-534894"}]
    "citedResource": [{"cited_resource_name": "Dashboard","cited_resource_id": "146abs-1222-534894","cited_resource_name": "ds1"},{"cited_resource_name": "Space","cited_resource_id": "123abs-1234-534894","cited_resource_name": "space1"}],
    "fileAttachment": [{"file_attachmet_type": "pdf","file_attachment_name": "file1.pdf"},{"file_attachmet_type": "txt","file_attachment_name": "file2.txt"}]
}
```

### Feedback logs

Feedback logs capture user feedback on chat and contains below fields:

- `conversationId` - Unique ID of the conversation
- `researchId` - Unique ID of the research
- `systemMessageId` - System generated message ID
- `userMessageId` - Unique ID of user message
- `feedback_type` - Type of feedback
- `feedback_reason` - Reason for the feedback
- `feedback_details` - Text message in the feedback
- `rating` - Rating provided by the user

The following is an example of feedback logs:

```
Chat Feedback:
    "conversationId": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "researchId": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "systemMessageId": "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "userMessageId" : "a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "feedback_type" :"thumbsUp,thumbsDown,ease_of_use etc."
    "feedback_reason" : "Too wordy,Issue with sources,Other etc."
    "feedback_details" : "additional text shared by user"
    "rating" : "thumbsUp,thumbsDown,ease_of_use etc."
```

## Security considerations

- **Encryption**: Use customer-managed AWS KMS keys for sensitive data
- **Access control**: Implement least-privilege IAM policies
- **Data retention**: Configure appropriate retention policies for your compliance requirements
