# Monitoring Amazon Quick using CloudWatch Logs

You can use [Amazon CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md") to deliver chat conversations, user feedback, agent hours usage, and index storage usage in Amazon Quick for you to analyze. These logs can be delivered to multiple destinations, such as CloudWatch, Amazon S3, or Amazon Data Firehose (standard rates apply).

###### Important

Set up vended log delivery shortly after enabling Amazon Quick AI features. Logs are not retroactive – you only receive events that occur after delivery is configured.

The following are examples of tasks you can complete with logs from Amazon Quick:

- Identify common user queries and pain points by reviewing the chat message content.
- Monitor the quality of responses by looking at metrics like `feedbackReason`.
- Understand user sentiment and satisfaction by analyzing the feedback data, including comments and usefulness ratings.
- Generate custom dashboards and reports to track key metrics and trends over time.
- Identify and analyze cases where the chat returned no answer or the user query was blocked.
- Monitor agent hours usage.
- Track index storage usage across knowledge bases and Spaces.
- Track knowledge base sync operations and identify document crawl or indexing failures.

###### Important

Logs from conversations might include sensitive or personally identifiable data passed in the chats. You can filter out this information from your logs when setting up logs subscription. Or you can mask this data on your logs using CloudWatch Logs masking policies. For more information, see [Help protect sensitive log data with masking](../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md "../../../AmazonCloudWatch/latest/logs/mask-sensitive-log-data.md").

## Supported log destinations

Amazon Quick can deliver logs to the following destinations:

- **Amazon CloudWatch Logs** – For real-time monitoring and analysis
- **Amazon S3** – For long-term storage and batch processing
- **Amazon Data Firehose** – For streaming analytics and data transformation

## Prerequisites

Before you can enable logging, make sure that you have the following:

- An active Amazon Quick instance with Enterprise or Professional subscriptions
- Appropriate IAM permissions to configure log delivery
- A destination configured for your logs (CloudWatch Logs, Amazon S3 bucket, or Firehose)

## Configure logging

To enable logging for Amazon Quick chat and feedback, configure IAM permissions, create a delivery source and destination, and verify log delivery.

###### Topics

- [Set up IAM permissions](#quicksuite-chat-feedback-setup-iam-permissions "#quicksuite-chat-feedback-setup-iam-permissions")
- [Configure log subscription](#quicksuite-chat-feedback-configure-log-subscription "#quicksuite-chat-feedback-configure-log-subscription")
- [Verify log delivery](#quicksuite-chat-feedback-verify-log-delivery "#quicksuite-chat-feedback-verify-log-delivery")

### Set up IAM permissions

To set up CloudWatch Logs for Amazon Quick, use the following IAM policy examples to grant the necessary permissions.

```
{
    "Version": "2012-10-17",
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
    "Effect": "Allow",
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

Create a delivery source with the [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") CloudWatch Logs API operation. Give the delivery source a name and for `resourceArn`, specify the ARN of your application. For `logType`, specify `CHAT_LOGS`, `AGENT_HOURS_LOGS`, `AGENT_METADATA_LOGS`, `FEEDBACK_LOGS`, `INDEX_USAGE_LOGS`, or `KB_FILE_SYNC_LOGS`.

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

```
{
    "logType": "AGENT_HOURS_LOGS",
    "name": "my-quick-suite-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```

```
{
    "logType": "INDEX_USAGE_LOGS",
    "name": "my-quick-index-usage-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```

```
{
    "logType": "KB_FILE_SYNC_LOGS",
    "name": "my-quick-kb-file-sync-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```

```
{
    "logType": "AGENT_METADATA_LOGS",
    "name": "my-quick-agent-metadata-delivery-source",
    "resourceArn": "arn:aws:quicksight:your-region:your-account-id:account/account-id"
}
```

To enable user conversation logging with the CloudWatch Logs API operations, you call the `PutDeliverySource`, `PutDeliveryDestination`, and `CreateDelivery` API operations.

###### Note

Vended-log delivery is per Region. Each delivery captures only the activity that occurs in the Region specified by the `resourceArn` in `PutDeliverySource`. To receive logs from multiple Regions, configure a separate delivery in each Region.

### Verify log delivery

After you configure log delivery, verify that logs are being delivered to your destination:

- **Verify the setup:** Verify the list of deliveries that have been created in the account by using the `DescribeDeliveries` API in CloudWatch Logs.
- **CloudWatch Logs**: Check the specified log group for new log streams.
- **Amazon S3**: Monitor your bucket for new log files.
- **Firehose**: Verify data is flowing through your delivery stream.

## Log schema and format

Amazon Quick logs follow a structured schema with common fields shared across all log types and specific fields for chat and feedback logs.

### Common fields

All log events include these common fields:

- `resource_arn` – Resource ARN of your Amazon Quick account (for example, `arn:aws:quicksight:us-east-1:111122223333:account/111122223333:`)
- `event_timestamp` – Unix epoch time in milliseconds (for example, `1763532110061`)
- `logType` – Type of log (for example, `CHAT_LOGS` or `FEEDBACK_LOGS`)
- `accountId` – AWS account ID (for example, `123456789012`)
- `user_arn` – Amazon Quick user ARN associated with the event (for example, `"arn:aws:quicksight:us-west-2:111122223333:user/default/user"`)

### Chat logs

Chat logs capture conversation interactions:

###### Note

Temporary conversations that are excluded from history and memory are still delivered to chat logs. Each record includes the `user_arn` and `user_type` of the user who initiated the conversation.

- `user_arn` – Amazon Quick user ARN associated with the event
- `user_type` – Amazon Quick user type associated with the event (for example, `ADMIN_PRO`)
- `status_code` – Status of the chat request (for example, `success`, `request_blocked`, `no_answer_found`)
- `conversation_id` – Unique ID for the user conversation
- `system_message_id` – System-generated message ID
- `message_scope` – Scope of the message (for example, `all_resources`, `specific_resources`, `no_resources`)
- `user_message_id` – Unique ID of the user message
- `user_message` – User message in the conversation
- `agent_id` – Unique ID of the chat agent, or `SYSTEM` for the default agent
- `flow_id` – Unique ID of the Amazon Quick Flow, or `-` if not a flow invocation
- `system_text_message` – System response in the conversation
- `user_selected_resources` – List of resources selected by user
- `action_connectors` – List of action connectors available in the conversation
- `cited_resource` – List of cited resources
- `file_attachment` – List of files attached by user
- `resource_arn` – Resource ARN of your Amazon Quick account
- `event_timestamp` – Timestamp of the event
- `logType` – `CHAT_LOGS`
- `accountId` – AWS account ID

The following is an example of chat logs:

```
{
    "user_arn": "arn:aws:quicksight:us-east-1:111122223333:user/default/johndoe",
    "user_type": "ADMIN_PRO",
    "status_code": "success",
    "conversation_id": "c11ba72c-ff18-4213-9686-1952bb547c19",
    "system_message_id": "42a37690-1804-442b-8368-3d34570dd2cd",
    "message_scope": "all_resources",
    "user_message_id": "5ec45e03-bf22-40c7-b32a-d69eb015f86b",
    "user_message": "What is in this document?",
    "agent_id": "SYSTEM",
    "flow_id": "-",
    "system_text_message": "Here is a summary of the attached document.",
    "user_selected_resources": [{"resourceId": "ALL", "resourceType": "space"}],
    "action_connectors": [{"actionConnectorId": "quicksuite-documentation"}, {"actionConnectorId": "quicksuite-websearch"}],
    "cited_resource": [{"citedResourceType": "document", "citedResourceId": null, "citedResourceName": "example-document.html"}],
    "file_attachment": [{"fileAttachmentType": "html", "fileAttachmentName": "example-document.html"}],
    "resource_arn": "arn:aws:quicksight:us-east-1:111122223333:account/111122223333",
    "event_timestamp": 1787185484508,
    "logType": "CHAT_LOGS",
    "accountId": "111122223333"
}
```

### Feedback logs

Feedback logs capture user feedback on chat responses:

- `user_arn` – Amazon Quick user ARN associated with the event
- `user_type` – Amazon Quick user type associated with the event (for example, `ADMIN_PRO`)
- `status_code` – Status of the event delivery
- `conversation_id` – Unique ID of the conversation
- `system_message_id` – System generated message ID
- `user_message_id` – Unique ID of user message
- `feedback_type` – Type of feedback (for example, `Not Useful`, `Useful`)
- `feedback_reason` – Feedback reason selected by the user
- `feedback_details` – (Optional) Additional details provided by the user
- `resource_arn` – Resource ARN of your Amazon Quick account
- `event_timestamp` – Timestamp of the event
- `logType` – `FEEDBACK_LOGS`
- `accountId` – AWS account ID

The following is an example of feedback logs:

```
{
    "user_arn": "arn:aws:quicksight:us-east-1:111122223333:user/default/johndoe",
    "user_type": "ADMIN_PRO",
    "status_code": "success",
    "conversation_id": "c11ba72c-ff18-4213-9686-1952bb547c19",
    "system_message_id": "42a37690-1804-442b-8368-3d34570dd2cd",
    "user_message_id": "5ec45e03-bf22-40c7-b32a-d69eb015f86b",
    "feedback_type": "Not Useful",
    "feedback_reason": "Too wordy",
    "feedback_details": "The answer included too much background information.",
    "resource_arn": "arn:aws:quicksight:us-east-1:111122223333:account/111122223333",
    "event_timestamp": 1787185500123,
    "logType": "FEEDBACK_LOGS",
    "accountId": "111122223333"
}
```

## Agent hours logs

This log type captures the usage logs for different agents within your Quick account used for pricing:

- `user_arn` – Amazon Quick user ARN associated with the event
- `subscription_type` – Subscription tier of the user. Values: `ENTERPRISE`, `PROFESSIONAL`.
- `reporting_service` – The Quick surface that consumed agent hours. Current values include `FLOW`, `AUTOMATION`, and `RESEARCH`. New values might appear as additional Quick features begin metering agent hours.
- `usage_group` – Whether the usage is covered by the subscription entitlement or billed as overage. Values:

  - `Included` – Usage within the daily entitlement grant for the subscription tier. No incremental charge.
  - `Extra` – Overage beyond the daily grant. Billed on consumption.

- `usage_hours` – Decimal value indicating the agent hours consumed for this record
- `service_resource_arn` – ARN of the resource that consumed the hours (for example, a flow, automation, or research session)
- `resource_arn` – Resource ARN of your Amazon Quick account
- `event_timestamp` – Timestamp of the event
- `logType` – `AGENT_HOURS_LOGS`
- `accountId` – AWS account ID

The following is an example of Agent Hours logs:

```
{
    "user_arn": "arn:aws:quicksight:us-east-1:111122223333:user/default/johndoe",
    "subscription_type": "ENTERPRISE",
    "reporting_service": "RESEARCH",
    "usage_group": "Included",
    "usage_hours": 0.0928,
    "service_resource_arn": "arn:aws:quicksight::111122223333:research/a11b2bbc-c123-3abc-a12b-12a34b5c678d",
    "resource_arn": "arn:aws:quicksight:us-east-1:111122223333:account/111122223333",
    "event_timestamp": 1787183715000,
    "logType": "AGENT_HOURS_LOGS",
    "accountId": "111122223333"
}
```

## Agent metadata logs

Agent metadata logs capture lifecycle events for chat agents, including
creation, updates, permission changes, and deletion. One record is emitted
per agent operation:

- `user_arn` – Amazon Quick user ARN associated with the event.
- `event_name` – The agent lifecycle operation. Values
  include `CreateAgent`, `UpdateAgent`,
  `DeleteAgent`, `UpdateAgentPermissions`,
  and others as new operations are added.
- `event_version` – Schema version of the log
  record.
- `agent_id` – UUID of the agent.
- `agent_arn` – Full ARN of the agent.
- `agent_name` – Display name of the agent.
- `agent_status` – Current status of the agent (for
  example, `ACTIVE`).
- `request_id` – Request identifier for the
  operation.
- `description` – Agent description text.
- `spaces` – JSON array of spaces attached to the
  agent.
- `permissions_granted` – Permissions added in this
  operation.
- `permissions_revoked` – Permissions removed in this
  operation.
- `permissions_state` – Current permissions after the operation.
- `update_action` – The update action performed.
- `version` – Agent version number.
- `icon_id` – Icon identifier for the agent.
- `magic_builder_query` – The natural language query used to create the agent via the builder.
- `instructions` – Agent instructions.
- `failed_to_add_spaces` – Spaces that could not be attached.
- `failed_to_remove_spaces` – Spaces that could not be detached.
- `draft_discarded` – Whether a draft was discarded.
- `custom_prompt_input` – Custom prompt input configured for the agent.
- `welcome_message` – Welcome message shown to users of the agent.
- `starter_prompts` – Starter prompts suggested to users of the agent.
- `resource_arn` – Resource ARN of your Amazon Quick account.
- `event_timestamp` – Timestamp of the event.
- `log_type` – `AGENT_METADATA_LOGS`.
- `account_id` – AWS account ID.

###### Note

The `custom_prompt_input`, `welcome_message`,
and `starter_prompts` fields contain sensitive content. When
you configure a customer managed AWS KMS key for delivery, these fields are
encrypted. Without a key, they are delivered in cleartext.

The following is an example of an agent metadata log for a
`CreateAgent` event:

```
{
    "user_arn": "arn:aws:quicksight:us-east-1:111122223333:user/default/johndoe",
    "event_version": "1.0",
    "event_name": "CreateAgent",
    "agent_id": "12345678-90ab-cdef-1234-567890abcdef",
    "request_id": "fedcba98-7654-3210-fedc-ba9876543210",
    "agent_arn": "arn:aws:quicksight:us-east-1:111122223333:agent/12345678-90ab-cdef-1234-567890abcdef",
    "agent_name": "Project Status Assistant",
    "agent_status": "ACTIVE",
    "description": "An agent that helps track project status and find relevant documentation.",
    "spaces": "[{\"Arn\": \"arn:aws:quicksight:us-east-1:111122223333:space/11112222-3333-4444-5555-666677778888\"}]",
    "resource_arn": "arn:aws:quicksight:us-east-1:111122223333:account/111122223333",
    "event_timestamp": 1787185396000,
    "log_type": "AGENT_METADATA_LOGS",
    "account_id": "111122223333"
}
```

## Index usage logs

Index usage logs capture per-source storage metrics for knowledge
bases and Spaces. Events are published whenever a change occurs
(created, updated, synced, or deleted):

- `user_arn` – Amazon Quick user ARN associated with the event
- `consumed_index_size` – Total size (in bytes)
  consumed by the entire index
- `source_type` – Type of source:
  `SPACE` or `KB`
- `source_name` – Display name of the Space or
  knowledge base
- `source_arn` – Full ARN of the source
- `consumed_source_size` – Size (in bytes)
  consumed by this individual source
- `consumed_source_doc_count` – Number of
  documents in this source
- `resource_arn` – Resource ARN of your Amazon Quick account
- `event_timestamp` – Timestamp of the event
- `log_type` – `INDEX_USAGE_LOGS`
- `account_id` – AWS account ID

The following is an example of index usage logs:

```
{
    "account_id": "111122223333",
    "event_timestamp": 1774911984257,
    "log_type": "INDEX_USAGE_LOGS",
    "user_arn": "arn:aws:quicksight::111122223333:user/default/user",
    "resource_arn": "arn:aws:quicksight:us-west-2:111122223333:account/111122223333",
    "consumed_index_size": 500000,
    "source_type": "SPACE",
    "source_name": "my-space",
    "source_arn": "arn:aws:quicksight:us-west-2:111122223333:space/2744af89-31b2-423b-93a2-69b0cd0d7fa1",
    "consumed_source_size": 244436,
    "consumed_source_doc_count": 2
}
```

###### Note

Events are published per source on change. Not all sources
emit events every day. To reconstruct the current state, use
the most recent event per `source_arn`.

For information about building dashboards and running queries
against index usage logs, see
[Monitor index storage usage](index-usage-monitoring.md "index-usage-monitoring.md").

## Knowledge base file sync logs

Knowledge base file sync logs capture per-document sync status
events. One log record is emitted per document per sync run:

- `document_id` – Original document identifier
  such as a URL or file path.
- `document_title` – Document title.
- `document_status` – Terminal document status.
  Values: `ADDED`, `MODIFIED`,
  `UNMODIFIED`, `DELETED`,
  `SKIPPED`, `FAILED`.
- `sync_result` – High-level availability
  result. Values: `AVAILABLE` or
  `UNAVAILABLE`.
- `sync_id` – Sync job execution ID.
- `data_source_id` – Identifier of the data
  source that the knowledge base is connected to.
- `source_uri` – Source URL of the
  document.
- `error_message` – Error description when
  status is `FAILED` or
  `SKIPPED`.
- `error_mitigation` – Actionable guidance for
  resolving the error.
- `error_type` – Error code when status is
  `FAILED` or `SKIPPED`.
- `knowledge_base_id` – UUID of the knowledge
  base that produced the log.

The following table describes the `document_status`
values and their corresponding `sync_result`.

| document\_status | sync\_result  | Meaning                                                             |
| ---------------- | ------------- | ------------------------------------------------------------------- |
| `ADDED`          | `AVAILABLE`   | New document successfully indexed                                   |
| `MODIFIED`       | `AVAILABLE`   | Existing document re-indexed with changes                           |
| `UNMODIFIED`     | `AVAILABLE`   | Document content unchanged, no re-indexing needed                   |
| `DELETED`        | `UNAVAILABLE` | Document removed from index                                         |
| `SKIPPED`        | `UNAVAILABLE` | Document filtered during crawl, such as by robots.txt or size limit |
| `FAILED`         | `UNAVAILABLE` | Document failed during crawl or indexing                            |

The following example shows a successful knowledge base file
sync log where a document was added to the knowledge base:

```
{
    "resource_arn": "arn:aws:quicksight:us-west-2:111122223333:account/111122223333",
    "event_timestamp": 1781296858575,
    "log_type": "KB_FILE_SYNC_LOGS",
    "account_id": "111122223333",
    "document_id": "https://docs.aws.amazon.com/quick/latest/userguide/monitoring-cloudwatch-logs.html",
    "document_title": "Monitoring Amazon QuickSight usage using CloudWatch Logs",
    "document_status": "ADDED",
    "sync_result": "AVAILABLE",
    "sync_id": "86a70a9a-cad9-4fc6-8881-e3909c8954d2",
    "data_source_id": "56225744-18bc-4373-a91f-861dd1c3d566",
    "source_uri": "https://docs.aws.amazon.com/quick/latest/userguide/monitoring-cloudwatch-logs.html",
    "knowledge_base_id": "b0bd0a47-8095-439d-9dff-c64bd5fe3fa3"
}
```

The following example shows a skipped document log where
crawling was skipped due to a validation error:

```
{
    "resource_arn": "arn:aws:quicksight:us-west-2:111122223333:account/111122223333",
    "event_timestamp": 1781296492951,
    "log_type": "KB_FILE_SYNC_LOGS",
    "account_id": "111122223333",
    "document_id": "https://docs.aws.amazon.com/quick/latest/userguide/blocked-page.html",
    "document_title": "Blocked Page",
    "document_status": "SKIPPED",
    "sync_result": "UNAVAILABLE",
    "sync_id": "86a70a9a-cad9-4fc6-8881-e3909c8954d2",
    "data_source_id": "56225744-18bc-4373-a91f-861dd1c3d566",
    "source_uri": "https://docs.aws.amazon.com/quick/latest/userguide/blocked-page.html",
    "error_message": "This URL wasn't crawled because crawling isn't allowed by its robots.txt file.",
    "error_mitigation": "Contact the website administrator for assistance.",
    "error_type": "VALIDATION_ERROR",
    "knowledge_base_id": "b0bd0a47-8095-439d-9dff-c64bd5fe3fa3"
}
```

## Security considerations

- **Encryption** – Use customer-managed AWS KMS keys for sensitive data.
- **Access control** – Implement least-privilege IAM policies.
- **Data retention** – Configure appropriate retention policies for your compliance requirements.
