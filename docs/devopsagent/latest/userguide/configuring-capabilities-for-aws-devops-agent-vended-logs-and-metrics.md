# Vended Logs and Metrics

You can monitor your agent spaces and service operations by using vended Amazon CloudWatch metrics and logs. This topic describes the CloudWatch metrics that the AWS DevOps Agent automatically publishes to your account and the vended logs that you can configure for delivery to your preferred destinations.

## Vended CloudWatch metrics

AWS DevOps Agent automatically publishes metrics to Amazon CloudWatch in your account. These metrics are available without any configuration. You can use them to monitor usage, track operational activity, and create alarms.

## Prerequisites

In order to have CloudWatch metrics published in your account from AWS DevOps Agent, you will need to setup a [service-linked role](../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md "../../../IAM/latest/UserGuide/id_roles_create-service-linked-role.md").

### Namespace

All metrics are published under the `AWS/AIDevOps` namespace.

### Dimensions

All metrics include the following dimension.

A B 1Dimension Description 2`AgentSpaceUUID` The unique identifier of the agent space. To aggregate metrics across all agent spaces in your account, use CloudWatch math expressions or omit the dimension filter.

### Metrics reference

A B C D E 1Metric name Description Unit Publishing frequency Useful statistics 2ConsumedChatRequests The number of chat requests that an agent space consumed. To get the total count for your account, use the `SUM` statistic across all `AgentSpaceUUID` dimensions. Count Every 5 minutes Sum, Average 3ConsumedInvestigationTime The time spent running investigations in an agent space. Seconds Every 5 minutes Sum, Average, Maximum 4ConsumedEvaluationTime The time spent running evaluations in an agent space. Seconds Every 5 minutes Sum, Average, Maximum 5TopologyCompletionCount The number of topology processing completions. AWS DevOps Agent emits this metric when a topology finishes processing, whether from initial creation during onboarding, a manual update, or a scheduled daily refresh. Count Event-driven (emitted on each completion) Sum, SampleCount

### Viewing metrics in the CloudWatch console

1. Open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/").
2. In the navigation pane, choose **Metrics**, and then choose **All metrics**.
3. Choose the **AWS/AIDevOps** namespace.
4. Choose **By AgentSpace** to view metrics for your agent spaces.

**Tip:** You can create CloudWatch alarms on these metrics to receive notifications when usage exceeds a threshold. For example, create an alarm on `ConsumedChatRequests` to monitor chat request consumption.

## Prerequisites

Before you configure log delivery, make sure that you have the following:

- An active AWS account with access to the AWS DevOps Agent console
- An IAM principal with permissions for CloudWatch Logs delivery APIs
- (Optional) An Amazon S3 bucket or Amazon Data Firehose delivery stream, if you plan to use those as log destinations

## Vended logs

AWS DevOps Agent supports vended logs that provide visibility into events that your agent spaces and service registrations process. Vended logs use the Amazon CloudWatch Logs infrastructure to deliver logs to your preferred destination.

To use vended logs, you must configure a delivery destination. The following destinations are supported:

- **Amazon CloudWatch Logs** – A log group in your account
- **Amazon S3** – An S3 bucket in your account
- **Amazon Data Firehose** – A Firehose delivery stream in your account

### Supported log types

A single log type is supported: `APPLICATION_LOGS`. This log type covers all operational events that the service emits.

### Log event types

The following table summarizes the events that AWS DevOps Agent logs.

A B C 1Event Description Log level 2Agent inbound event received An agent is triggered by an integrated source and receives an inbound event (for example, a PagerDuty incident event). INFO 3Agent inbound event dropped An inbound event was dropped before the agent processed it. The log includes the reason (for example, malformed data). TBD 4Agent outbound communication failure An outbound communication to a third-party integration failed. The log includes the task ID and destination identifier (for example, an authentication error). TBD 5Topology creation queued A topology creation job was queued for processing. INFO 6Topology creation started A topology creation job began processing. INFO 7Topology creation finished A topology creation job completed processing. This event applies to initial creation, updates, and daily refreshes. INFO 8Resource discovery failed Resource discovery during topology creation encountered a failure. ERROR

### Permissions

AWS DevOps Agent uses [CloudWatch vended logs (V2 permissions)](../../../AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions-V2.md "../../../AmazonCloudWatch/latest/logs/AWS-vended-logs-permissions-V2.md") to deliver logs. To set up log delivery, the IAM role that configures the delivery must have the following permissions:

- `aidevops:AllowVendedLogDeliveryForResource` – Required to allow log delivery for the agent space resource.
- Permissions for the CloudWatch Logs delivery APIs (`logs:PutDeliverySource`, `logs:PutDeliveryDestination`, `logs:CreateDelivery`, and related operations).
- Permissions specific to your chosen delivery destination.

For the full IAM policy that is required for each destination type, see the following topics in the _Amazon CloudWatch Logs User Guide_:

- [Logs sent to CloudWatch Logs](../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-CloudWatchLogs.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-CloudWatchLogs.md")
- [Logs sent to Amazon S3](../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-S3.md")
- [Logs sent to Firehose](../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-Firehose.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-infrastructure-V2-Firehose.md")

### Configure log delivery (console)

AWS DevOps Agent provides two locations in the AWS Management Console to configure log delivery:

- **Service Registration settings page** – Configure log delivery for service-level events. These logs use the service ARN (`arn:aws:aidevops:<region>:<account-id>:service`) as the resource.
- **Agent Space page** – Configure log delivery for events that are specific to an individual agent space. These logs use the agent space ARN (`arn:aws:aidevops:<region>:<account-id>:agent-space/<agent-space-id>`) as the resource.

#### To configure log delivery for a service registration

1. Open the AWS DevOps Agent console in the AWS Management Console.
2. In the navigation pane, choose **Settings**.
3. In the **Capability Providers\*\***>\***\*Logs** tab, choose **Configure**.
4. For **Destination type**, choose one of the following:
5. **CloudWatch Logs** – Select or create a log group.
6. **Amazon S3** – Enter the S3 bucket ARN.
7. **Amazon Data Firehose** – Select or create a Firehose delivery stream.
8. For **Additional settings – \*optional** \*, you can specify the following options:
   1. For **Field selection**, select the log field names that you want to deliver to your destination. You can select [access log fields](../../../AmazonCloudFront/latest/DeveloperGuide/standard-logs-reference.md#BasicDistributionFileFormat "../../../AmazonCloudFront/latest/DeveloperGuide/standard-logs-reference.md#BasicDistributionFileFormat") and a subset of [real-time access log fields](../../../AmazonCloudFront/latest/DeveloperGuide/standard-logging.md#standard-logging-real-time-log-selection "../../../AmazonCloudFront/latest/DeveloperGuide/standard-logging.md#standard-logging-real-time-log-selection").
   2. (Amazon S3 only) For **Partitioning**, specify the path to partition your log file data.
   3. (Amazon S3 only) For **Hive-compatible file format**, you can select the checkbox to use Hive-compatible S3 paths. This helps simplify loading new data into your Hive-compatible tools.
   4. For **Output format**, specify your preferred format.
   5. For **Field delimiter**, specify how to separate log fields.

9. Choose **Save**.
10. Verify that the delivery status shows **Active**.

#### To configure log delivery for an agent space

1. Open the AWS DevOps Agent console in the AWS Management Console.
2. Choose the agent space that you want to configure.
3. In the **Configuration** tab, choose **Configure**.
4. For **Destination type**, choose one of the following:
5. **CloudWatch Logs** – Select or create a log group.
6. **Amazon S3** – Enter the S3 bucket ARN.
7. **Amazon Data Firehose** – Select or create a Firehose delivery stream.
8. For **Additional settings – \*optional** \*, you can specify the following options:
   1. For **Field selection**, select the log field names that you want to deliver to your destination. You can select [access log fields](../../../AmazonCloudFront/latest/DeveloperGuide/standard-logs-reference.md#BasicDistributionFileFormat "../../../AmazonCloudFront/latest/DeveloperGuide/standard-logs-reference.md#BasicDistributionFileFormat") and a subset of [real-time access log fields](../../../AmazonCloudFront/latest/DeveloperGuide/standard-logging.md#standard-logging-real-time-log-selection "../../../AmazonCloudFront/latest/DeveloperGuide/standard-logging.md#standard-logging-real-time-log-selection").
   2. (Amazon S3 only) For **Partitioning**, specify the path to partition your log file data.
   3. (Amazon S3 only) For **Hive-compatible file format**, you can select the checkbox to use Hive-compatible S3 paths. This helps simplify loading new data into your Hive-compatible tools.
   4. For **Output format**, specify your preferred format.
   5. For **Field delimiter**, specify how to separate log fields.

9. Choose **Save**.
10. Verify that the delivery status shows **Active**.

### Configure log delivery (CloudWatch API)

You can also use the CloudWatch Logs API to configure log delivery programmatically. A working log delivery consists of three elements:

- A **DeliverySource** – Represents the AWS DevOps Agent space resource that generates the logs.
- A **DeliveryDestination** – Represents the destination where logs are written.
- A **Delivery** – Connects a delivery source to a delivery destination.

#### Step 1: Create a delivery source

Use the [PutDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliverySource.md") operation to create a delivery source. Pass the ARN of your AWS DevOps Agent space resource and specify `APPLICATION_LOGS` as the log type.

The following example creates a delivery source for an agent space:

```
{
    "name": "my-agent-space-delivery-source",
    "resourceArn": "arn:aws:aidevops:us-east-1:123456789012:agentspace/my-agent-space-id",
    "logType": "APPLICATION_LOGS"
}
```

The following example creates a delivery source for the service:

```
{
    "name": "my-service-delivery-source",
    "resourceArn": "arn:aws:aidevops:us-east-1:123456789012:service",
    "logType": "APPLICATION_LOGS"
}
```

#### Step 2: Create a delivery destination

Use the [PutDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestination.md") operation to configure where logs are stored. You can choose Amazon CloudWatch Logs, Amazon S3, or Amazon Data Firehose.

The following example creates a CloudWatch Logs destination:

```
{
    "name": "my-cwl-destination",
    "deliveryDestinationConfiguration": {
        "destinationResourceArn": "arn:aws:logs:us-east-1:123456789012:log-group:/aws/aidevops/my-agent-space"
    },
    "outputFormat": "json"
}
```

The following example creates an Amazon S3 destination:

```
{
    "name": "my-s3-destination",
    "deliveryDestinationConfiguration": {
        "destinationResourceArn": "arn:aws:s3:::my-aidevops-logs-bucket"
    },
    "outputFormat": "json"
}
```

The following example creates an Amazon Data Firehose destination:

```
{
    "name": "my-firehose-destination",
    "deliveryDestinationConfiguration": {
        "destinationResourceArn": "arn:aws:firehose:us-east-1:123456789012:deliverystream/my-aidevops-log-stream"
    },
    "outputFormat": "json"
}
```

**Note:** If you deliver logs cross-account, you must use [PutDeliveryDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDeliveryDestinationPolicy.md") in the destination account to authorize the delivery.

**Note:** If you want to use CloudFormation, you can use the following:

- [Delivery](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md")
- [DeliveryDestination](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md")
- [DeliverySource](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md")

The `ResourceArn` is the `AgentSpaceArn`, and `LogType` must be `APPLICATION_LOGS` as the supported log type.

#### Step 3: Create a delivery

Use the [CreateDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateDelivery.md") operation to link the delivery source to the delivery destination.

```
{
    "deliverySourceName": "my-agent-space-delivery-source",
    "deliveryDestinationArn": "arn:aws:logs:us-east-1:123456789012:delivery-destination:my-cwl-destination"
}
```

#### AWS CloudFormation

You can also configure log delivery by using AWS CloudFormation with the following resources:

- [AWS::Logs::DeliverySource](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverysource.md")
- [AWS::Logs::DeliveryDestination](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-deliverydestination.md")
- [AWS::Logs::Delivery](../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-logs-delivery.md")

Set `ResourceArn` to the AWS DevOps Agent agent space or service ARN, and set `LogType` to `APPLICATION_LOGS`.

### Log schema reference

AWS DevOps Agent uses a shared log schema across all event types. Not every log event uses every field.

The following table describes the fields in the log schema.A B C 1Field Type Description 2event_timestamp Long Unix timestamp of when the event occurred 3resource_arn String ARN of the resource that generated the event 4account_id String AWS account ID associated with the log. 5level String Log level: `INFO`, `WARN`, `ERROR` 6agent_space_id String Identifier of the agent space. 7association_id String Association identifier for the log. 8status String Status of the topology operation. 9webhook_id String Webhook identifier. 10mcp_endpoint_url String MCP server endpoint URL 11service_type String Type of the Service: `DYNATRACE`, `DATADOG`, `GITHUB`, `SLACK`, `SERVICENOW`. 12service_endpoint_url String Endpoint URL for third-party integrations. 13service_id String Identifier of the source. 14request_id String Request identifier for correlating with AWS CloudTrail or support tickets. 15operation String Name of the operation that was performed. 16task_type String Agent backlog task type: `INVESTIGATION` or `EVALUATION` 17task_id String Agent Backlog Task IDAgent backlog task identifier. 18reference String Reference from an agent task (for example, a Jira ticket). 19error_type String Error type 20error_message String (JSON) Error description when an operation fails. 21details String (JSON) Service-specific event payload that contains operation parameters and results.

### Manage and disable log delivery

You can modify or remove log delivery at any time from the AWS DevOps Agent console in the AWS Management Console or by using the CloudWatch Logs API.

#### Manage log delivery (console)

1. Open the AWS DevOps Agent console in the AWS Management Console.
2. Navigate to the **Settings** page (for service-level logs) or the specific **Agent Space** page (for Agent Space-level logs).
3. In the **Configuration** tab (for Agent Space-level logs) or **Capability Providers\*\***>\***\*Logs** tab (for service-level logs), choose the delivery to modify.
4. Update the configuration as needed and choose **Save**.

###### Note

You can't change the destination type of an existing delivery. To change the destination type, delete the current delivery and create a new one.

#### Disable log delivery (console)

1. Open the AWS DevOps Agent console in the AWS Management Console.
2. Navigate to the **Settings** page (for service-level logs) or the specific **Agent Space** page (for Agent Space-level logs).
3. In the **Configuration** tab (for Agent Space-level logs) or **Capability Providers\*\***>\***\*Logs** tab (for service-level logs),, select the delivery to remove.
4. Choose **Delete** and confirm.

#### Disable log delivery (API)

To remove a log delivery by using the API, delete the resources in the following order:

1. Delete the delivery by using [DeleteDelivery](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDelivery.md").
2. Delete the delivery source by using [DeleteDeliverySource](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliverySource.md").
3. (Optional) If the delivery destination is no longer needed, delete it by using [DeleteDeliveryDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliveryDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_DeleteDeliveryDestination.md").

###### Important

You are responsible for removing log delivery resources after you delete the agent space resource that generates the logs (for example, after you delete an agent space). If you don't remove these resources, orphaned delivery configurations might remain.

### Example log entries

The following examples show the log output for each event type.

#### Event received

```
{
    "event_timestamp": 1739918400000,
    "resource_arn": "arn:aws:aidevops:us-east-1:123456789012:agent-space/abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "account_id": "123456789012",
    "level": "INFO",
    "agent_space_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "request_id": "req-a1b2c3d4-e5f6-7890-abcd-ef1234567890",
    "operation": "ProcessInboundEvent",
    "webhook_id": "wh-98765",
    "service_type": "PAGERDUTY",
    "service_id": "my-pagerduty-integration",
    "details": "{\"event_id\":\"evt-00112233\",\"event_type\":\"incident.triggered\"}"
}
```

#### Event dropped

```
{
    "event_timestamp": 1739918460000,
    "resource_arn": "arn:aws:aidevops:us-east-1:123456789012:agent-space/abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "account_id": "123456789012",
    "level": "WARN",
    "agent_space_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "request_id": "req-b2c3d4e5-f6a7-8901-bcde-f12345678901",
    "operation": "ProcessInboundEvent",
    "webhook_id": "wh-98765",
    "service_type": "DATADOG",
    "service_id": "my-datadog-integration",
    "error_type": "VALIDATION_ERROR",
    "error_message": "{\"reason\":\"Malformed event payload: missing required field 'severity'\"}"
}
```

#### Outbound communication failure

```
{
    "event_timestamp": 1739918520000,
    "resource_arn": "arn:aws:aidevops:us-east-1:123456789012:agent-space/abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "account_id": "123456789012",
    "level": "ERROR",
    "agent_space_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "request_id": "req-c3d4e5f6-a7b8-9012-cdef-123456789012",
    "operation": "SendOutboundCommunication",
    "service_type": "SLACK",
    "service_id": "my-slack-workspace",
    "service_endpoint_url": "https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXX",
    "task_type": "INVESTIGATION",
    "task_id": "task-d4e5f6a7-b8c9-0123-defg-456789012345",
    "reference": "JIRA-1234",
    "error_type": "AUTH_ERROR",
    "error_message": "{\"reason\":\"OAuth token expired for destination workspace\"}",
    "details": "{\"http_status\":401,\"retry_attempt\":3}"
}
```

#### Topology creation queued

```
{
    "event_timestamp": 1739918580000,
    "resource_arn": "arn:aws:aidevops:us-east-1:123456789012:agent-space/abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "account_id": "123456789012",
    "level": "INFO",
    "agent_space_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "request_id": "req-e5f6a7b8-c9d0-1234-efgh-567890123456",
    "operation": "CreateTopology",
    "association_id": "assoc-f6a7b8c9-d0e1-2345-fghi-678901234567",
    "status": "QUEUED"
}
```

#### Topology creation started

```
{
    "event_timestamp": 1739918640000,
    "resource_arn": "arn:aws:aidevops:us-east-1:123456789012:agent-space/abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "account_id": "123456789012",
    "level": "INFO",
    "agent_space_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "request_id": "req-e5f6a7b8-c9d0-1234-efgh-567890123456",
    "operation": "CreateTopology",
    "association_id": "assoc-f6a7b8c9-d0e1-2345-fghi-678901234567",
    "status": "PROCESSING"
}
```

#### Topology creation finished

```
{
    "event_timestamp": 1739918700000,
    "resource_arn": "arn:aws:aidevops:us-east-1:123456789012:agent-space/abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "account_id": "123456789012",
    "level": "INFO",
    "agent_space_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "request_id": "req-e5f6a7b8-c9d0-1234-efgh-567890123456",
    "operation": "CreateTopology",
    "association_id": "assoc-f6a7b8c9-d0e1-2345-fghi-678901234567",
    "status": "COMPLETED",
    "details": "{\"resources_discovered\":142,\"duration_seconds\":120}"
}
```

#### Resource discovery failed during topology creation

```
{
    "event_timestamp": 1739918760000,
    "resource_arn": "arn:aws:aidevops:us-east-1:123456789012:agent-space/abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "account_id": "123456789012",
    "level": "ERROR",
    "agent_space_id": "abcd1234-5678-90ef-ghij-klmnopqrstuv",
    "request_id": "req-a7b8c9d0-e1f2-3456-ghij-789012345678",
    "operation": "DiscoverResources",
    "association_id": "assoc-f6a7b8c9-d0e1-2345-fghi-678901234567",
    "status": "FAILED",
    "mcp_endpoint_url": "https://mcp.example.com/v1/resources",
    "error_type": "RESOURCE_DISCOVERY_ERROR",
    "error_message": "{\"reason\":\"Timed out while discovering resources from MCP endpoint\"}",
    "details": "{\"resources_discovered_before_failure\":87,\"timeout_seconds\":300}"
}
```

## Pricing

The AWS DevOps Agent does not charge for enabling vended logs. However, you can incur charges for the delivery, ingestion, storage or access, depending on the log delivery destination that you select. For pricing details, see **Vended Logs** on the **Logs** tab at [Amazon CloudWatch Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/").

For destination-specific pricing, see the following:

- [Amazon CloudWatch Logs Pricing](https://aws.amazon.com/cloudwatch/pricing/ "https://aws.amazon.com/cloudwatch/pricing/")
- [Amazon S3 Pricing](https://aws.amazon.com/s3/pricing/ "https://aws.amazon.com/s3/pricing/")
- [Amazon Data Firehose Pricing](https://aws.amazon.com/kinesis/data-firehose/pricing/ "https://aws.amazon.com/kinesis/data-firehose/pricing/")
