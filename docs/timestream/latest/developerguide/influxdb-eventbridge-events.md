

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Amazon Timestream for InfluxDB event notifications with Amazon EventBridge
<a name="influxdb-eventbridge-events"></a>

Amazon Timestream for InfluxDB publishes events to Amazon EventBridge when database instances or clusters undergo state changes. You can create EventBridge rules to route these events to any supported target to build automation, receive alerts, and maintain audit trails.

## Overview
<a name="influxdb-eventbridge-overview"></a>

Amazon Timestream for InfluxDB generates events when operations such as instance creation, compute scaling, parameter group updates, maintenance, or deletion complete or fail. Events are published to the default EventBridge event bus in your account with source `aws.timestream-influxdb`, supporting content-based filtering and routing to any EventBridge target including AWS Lambda functions, AWS Step Functions, Amazon Simple Queue Service queues, Amazon Simple Notification Service topics, and cross-account event buses.

To receive and act on these events, you create EventBridge rules that match the events you care about and route them to the targets of your choice. For example, you can:
+ Route failure events to an Amazon SNS topic for on-call alerting via PagerDuty or email.
+ Trigger a Lambda function when a compute scaling operation completes.
+ Send all events to Amazon CloudWatch Logs for a compliance audit trail.
+ Start a Step Functions workflow when a new cluster finishes creation.

There is no additional Amazon Timestream for InfluxDB charge for publishing events. Standard Amazon EventBridge pricing applies for rule evaluation and target delivery.

## Event categories
<a name="influxdb-eventbridge-categories"></a>

Events are grouped into categories for use in EventBridge rule filtering:


| Category | Description | 
| --- | --- | 
| creation | Instance or cluster created successfully, or creation failed | 
| notification | Informational events for configuration changes, scaling, reboots, and other lifecycle operations | 
| maintenance | Scheduled maintenance window started or ended | 
| failure | All failure events across all operation types | 

**Note**  
An event can belong to multiple categories. For example, a failed compute scaling event belongs to both `notification` and `failure`.

## Source types
<a name="influxdb-eventbridge-source-types"></a>


| Source type | Description | 
| --- | --- | 
| DB\_INSTANCE | InfluxDB v2 standalone instances | 
| DB\_CLUSTER | InfluxDB v2 Read Replica clusters and InfluxDB v3 clusters | 

## Event schema
<a name="influxdb-eventbridge-schema"></a>

Events are published with the following structure:

```
{
  "version": "0",
  "id": "12345678-1234-1234-1234-123456789012",
  "detail-type": "Timestream InfluxDB DB Instance Event",
  "source": "aws.timestream-influxdb",
  "account": "123456789012",
  "time": "2026-06-15T14:30:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:timestream-influxdb:us-east-1:123456789012:db-instance/my-influxdb-instance"
  ],
  "detail": {
    "EventID": "TIDB-EVENT-12001",
    "SourceType": "DB_INSTANCE",
    "SourceIdentifier": "my-influxdb-instance",
    "SourceArn": "arn:aws:timestream-influxdb:us-east-1:123456789012:db-instance/my-influxdb-instance",
    "EventCategories": ["notification"],
    "Message": "InfluxDB v2 instance 'my-influxdb-instance' compute updated",
    "Date": "2026-06-15T14:30:00.000Z"
  }
}
```

The following example shows a failure event, which includes additional diagnostic fields:

```
{
  "version": "0",
  "id": "87654321-4321-4321-4321-210987654321",
  "detail-type": "Timestream InfluxDB DB Cluster Event",
  "source": "aws.timestream-influxdb",
  "account": "123456789012",
  "time": "2026-06-15T11:15:00Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:timestream-influxdb:us-east-1:123456789012:db-cluster/my-influxdb3-cluster"
  ],
  "detail": {
    "EventID": "TIDB-EVENT-21101",
    "SourceType": "DB_CLUSTER",
    "SourceIdentifier": "my-influxdb3-cluster",
    "SourceArn": "arn:aws:timestream-influxdb:us-east-1:123456789012:db-cluster/my-influxdb3-cluster",
    "EventCategories": ["creation", "failure"],
    "Message": "InfluxDB v3 cluster 'my-influxdb3-cluster' creation failed",
    "Date": "2026-06-15T11:15:00.000Z",
    "FailureCode": "INSUFFICIENT_EC2_CAPACITY",
    "FailureReason": "Insufficient capacity in requested Availability Zone",
    "RecommendedActions": "Retry the operation or try a different Availability Zone"
  }
}
```

Key fields:
+ **source** — Always `aws.timestream-influxdb`
+ **detail-type** — Either `Timestream InfluxDB DB Instance Event` or `Timestream InfluxDB DB Cluster Event`
+ **detail.SourceType** — Either `DB_INSTANCE` or `DB_CLUSTER`
+ **detail.EventCategories** — Array of categories this event belongs to (an event can belong to multiple categories)
+ **detail.SourceIdentifier** — The name of the database instance or cluster
+ **detail.Message** — Human-readable description including the InfluxDB engine version and resource name
+ **detail.FailureCode** — (Failure events only) Machine-readable error code. Values include `INSUFFICIENT_EC2_CAPACITY`, `INSUFFICIENT_FREE_ADDRESSES_IN_SUBNET`, `INVALID_SUBNET_ID`, and `INTERNAL_ERROR`.
+ **detail.FailureReason** — (Failure events only) Detailed description of the failure
+ **detail.RecommendedActions** — (Failure events only) Suggested remediation steps as a string

## Setting up event notifications
<a name="influxdb-eventbridge-setup"></a>

### Step 1: Create an EventBridge rule
<a name="influxdb-eventbridge-setup-rule"></a>

1. Open the [Amazon EventBridge console](https://console.aws.amazon.com/events/).

1. Choose **Rules**, then **Create rule**.

1. Enter a rule name (for example, `timestream-influxdb-failures`).

1. For **Event bus**, keep **default**.

1. For **Rule type**, choose **Rule with an event pattern**.

1. Choose **Next**.

### Step 2: Define the event pattern
<a name="influxdb-eventbridge-setup-pattern"></a>

Choose **Custom pattern** and enter a pattern that matches the events you want.

**Match all Amazon Timestream for InfluxDB events:**

```
{
    "source": ["aws.timestream-influxdb"],
    "detail-type": ["Timestream InfluxDB DB Instance Event", "Timestream InfluxDB DB Cluster Event"]
}
```

**Note**  
Filtering by `detail-type` is recommended. Using only `"source": ["aws.timestream-influxdb"]` will also match CloudTrail events for the service, which can be noisy. The pattern above matches only Amazon Timestream for InfluxDB lifecycle events.

**Match only failure events:**

```
{
  "source": ["aws.timestream-influxdb"],
  "detail": {
    "EventCategories": ["failure"]
  }
}
```

**Match events for a specific production cluster:**

```
{
  "source": ["aws.timestream-influxdb"],
  "detail": {
    "SourceIdentifier": ["my-production-cluster"]
  }
}
```

**Match maintenance and failure events for a specific resource:**

```
{
  "source": ["aws.timestream-influxdb"],
  "detail": {
    "SourceIdentifier": ["my-production-cluster"],
    "EventCategories": ["maintenance", "failure"]
  }
}
```

### Step 3: Select a target
<a name="influxdb-eventbridge-setup-target"></a>

Choose a target for matched events:
+ **Amazon Simple Notification Service topic** — For email, SMS, or webhook notifications
+ **AWS Lambda function** — For custom processing or remediation
+ **Amazon Simple Queue Service queue** — For decoupled processing
+ **AWS Step Functions** — For multi-step automation workflows
+ **Amazon CloudWatch Logs** — For audit trail persistence

**Important**  
Ensure your target's resource policy allows `events.amazonaws.com` to invoke it. For example, Amazon SNS topics must grant publish permission, Lambda functions must grant invoke permission, and Amazon SQS queues must grant send-message permission to `events.amazonaws.com`.

### Step 4: Create the rule
<a name="influxdb-eventbridge-setup-create"></a>

Review and choose **Create rule**. Events matching your pattern will be routed to the target.

## Common patterns
<a name="influxdb-eventbridge-common-patterns"></a>

### Email alerts on failures
<a name="influxdb-eventbridge-pattern-email-alerts"></a>

1. Create an Amazon SNS topic (for example, `timestream-influxdb-alerts`) and subscribe your email address.

1. In the EventBridge console, create a rule matching `"EventCategories": ["failure"]`.

1. Set the Amazon SNS topic as the rule target.

1. Confirm the email subscription when you receive the confirmation message.

### CI/CD pipeline integration
<a name="influxdb-eventbridge-pattern-cicd"></a>

Create an EventBridge rule that triggers a Step Functions state machine when a specific operation completes:

```
{
  "source": ["aws.timestream-influxdb"],
  "detail": {
    "SourceIdentifier": ["my-staging-cluster"],
    "EventID": ["TIDB-EVENT-22001"]
  }
}
```

The state machine can then run integration tests, update DNS, and notify your deployment channel.

### Maintenance window suppression
<a name="influxdb-eventbridge-pattern-maintenance"></a>

Create two EventBridge rules:

1. Rule matching `"EventID": ["TIDB-EVENT-24001"]` (maintenance started) → Lambda that sets a maintenance flag in your monitoring system.

1. Rule matching `"EventID": ["TIDB-EVENT-24002"]` (maintenance ended) → Lambda that clears the flag.

This prevents false-positive alerts during planned maintenance.

### Audit trail with Amazon CloudWatch Logs
<a name="influxdb-eventbridge-pattern-audit"></a>

Create an EventBridge rule matching all events (`"source": ["aws.timestream-influxdb"]`) with a Amazon CloudWatch Logs log group as the target. Set the log group retention to your compliance requirement (for example, 1 year). All database lifecycle events are preserved for the retention period.

## Instance event reference
<a name="influxdb-eventbridge-instance-events"></a>


| Event ID | Operation | Category | Message | 
| --- | --- | --- | --- | 
| TIDB-EVENT-11001 | DB\_INSTANCE\_CREATED | creation | InfluxDB {{version}} instance '{{name}}' created | 
| TIDB-EVENT-11101 | DB\_INSTANCE\_CREATE\_FAILED | creation, failure | InfluxDB {{version}} instance '{{name}}' creation failed | 
| TIDB-EVENT-13001 | DB\_INSTANCE\_DELETED | notification | InfluxDB {{version}} instance '{{name}}' deleted | 
| TIDB-EVENT-13101 | DB\_INSTANCE\_DELETE\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' deletion failed | 
| TIDB-EVENT-16001 | DB\_INSTANCE\_REBOOTED | notification | InfluxDB {{version}} instance '{{name}}' rebooted | 
| TIDB-EVENT-16101 | DB\_INSTANCE\_REBOOT\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' reboot failed | 
| TIDB-EVENT-12001 | DB\_INSTANCE\_COMPUTE\_UPDATED | notification | InfluxDB {{version}} instance '{{name}}' compute updated | 
| TIDB-EVENT-12101 | DB\_INSTANCE\_COMPUTE\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' compute update failed | 
| TIDB-EVENT-12002 | DB\_INSTANCE\_STORAGE\_UPDATED | notification | InfluxDB {{version}} instance '{{name}}' storage updated | 
| TIDB-EVENT-12102 | DB\_INSTANCE\_STORAGE\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' storage update failed | 
| TIDB-EVENT-12003 | DB\_INSTANCE\_PORT\_UPDATED | notification | InfluxDB {{version}} instance '{{name}}' port updated | 
| TIDB-EVENT-12103 | DB\_INSTANCE\_PORT\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' port update failed | 
| TIDB-EVENT-12004 | DB\_INSTANCE\_PARAMETER\_GROUP\_UPDATED | notification | InfluxDB {{version}} instance '{{name}}' parameter group updated | 
| TIDB-EVENT-12104 | DB\_INSTANCE\_PARAMETER\_GROUP\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' parameter group update failed | 
| TIDB-EVENT-12005 | DB\_INSTANCE\_LOG\_DELIVERY\_UPDATED | notification | InfluxDB {{version}} instance '{{name}}' log delivery updated | 
| TIDB-EVENT-12105 | DB\_INSTANCE\_LOG\_DELIVERY\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' log delivery update failed | 
| TIDB-EVENT-12006 | DB\_INSTANCE\_MAINTENANCE\_WINDOW\_UPDATED | notification | InfluxDB {{version}} instance '{{name}}' maintenance window updated | 
| TIDB-EVENT-12106 | DB\_INSTANCE\_MAINTENANCE\_WINDOW\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' maintenance window update failed | 
| TIDB-EVENT-12009 | DB\_INSTANCE\_UPDATED\_TO\_MAZ | notification | InfluxDB {{version}} instance '{{name}}' updated to Multi-AZ | 
| TIDB-EVENT-12109 | DB\_INSTANCE\_UPDATE\_TO\_MAZ\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' Multi-AZ update failed | 
| TIDB-EVENT-12010 | DB\_INSTANCE\_UPDATED\_TO\_SAZ | notification | InfluxDB {{version}} instance '{{name}}' updated to Single-AZ | 
| TIDB-EVENT-12110 | DB\_INSTANCE\_UPDATE\_TO\_SAZ\_FAILED | notification, failure | InfluxDB {{version}} instance '{{name}}' Single-AZ update failed | 
| TIDB-EVENT-14001 | DB\_INSTANCE\_MAINTENANCE\_WINDOW\_STARTED | maintenance | InfluxDB {{version}} instance '{{name}}' maintenance started | 
| TIDB-EVENT-14002 | DB\_INSTANCE\_MAINTENANCE\_WINDOW\_ENDED | maintenance | InfluxDB {{version}} instance '{{name}}' maintenance ended | 

## Cluster event reference
<a name="influxdb-eventbridge-cluster-events"></a>


| Event ID | Operation | Category | Message | 
| --- | --- | --- | --- | 
| TIDB-EVENT-21001 | DB\_CLUSTER\_CREATED | creation | InfluxDB {{version}} cluster '{{name}}' created | 
| TIDB-EVENT-21101 | DB\_CLUSTER\_CREATE\_FAILED | creation, failure | InfluxDB {{version}} cluster '{{name}}' creation failed | 
| TIDB-EVENT-23001 | DB\_CLUSTER\_DELETED | notification | InfluxDB {{version}} cluster '{{name}}' deleted | 
| TIDB-EVENT-23101 | DB\_CLUSTER\_DELETE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' deletion failed | 
| TIDB-EVENT-26001 | DB\_CLUSTER\_REBOOTED | notification | InfluxDB {{version}} cluster '{{name}}' rebooted | 
| TIDB-EVENT-26101 | DB\_CLUSTER\_REBOOT\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' reboot failed | 
| TIDB-EVENT-22001 | DB\_CLUSTER\_COMPUTE\_UPDATED | notification | InfluxDB {{version}} cluster '{{name}}' compute updated | 
| TIDB-EVENT-22101 | DB\_CLUSTER\_COMPUTE\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' compute update failed | 
| TIDB-EVENT-22002 | DB\_CLUSTER\_STORAGE\_UPDATED | notification | InfluxDB {{version}} cluster '{{name}}' storage updated | 
| TIDB-EVENT-22102 | DB\_CLUSTER\_STORAGE\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' storage update failed | 
| TIDB-EVENT-22003 | DB\_CLUSTER\_PORT\_UPDATED | notification | InfluxDB {{version}} cluster '{{name}}' port updated | 
| TIDB-EVENT-22103 | DB\_CLUSTER\_PORT\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' port update failed | 
| TIDB-EVENT-22004 | DB\_CLUSTER\_PARAMETER\_GROUP\_UPDATED | notification | InfluxDB {{version}} cluster '{{name}}' parameter group updated | 
| TIDB-EVENT-22104 | DB\_CLUSTER\_PARAMETER\_GROUP\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' parameter group update failed | 
| TIDB-EVENT-22005 | DB\_CLUSTER\_LOG\_DELIVERY\_UPDATED | notification | InfluxDB {{version}} cluster '{{name}}' log delivery updated | 
| TIDB-EVENT-22105 | DB\_CLUSTER\_LOG\_DELIVERY\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' log delivery update failed | 
| TIDB-EVENT-22006 | DB\_CLUSTER\_MAINTENANCE\_WINDOW\_UPDATED | notification | InfluxDB {{version}} cluster '{{name}}' maintenance window updated | 
| TIDB-EVENT-22106 | DB\_CLUSTER\_MAINTENANCE\_WINDOW\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' maintenance window update failed | 
| TIDB-EVENT-22008 | DB\_CLUSTER\_INSTANCE\_MODES\_UPDATED | notification | InfluxDB {{version}} cluster '{{name}}' instance modes updated | 
| TIDB-EVENT-22108 | DB\_CLUSTER\_INSTANCE\_MODES\_UPDATE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' instance modes update failed | 
| TIDB-EVENT-22009 | DB\_CLUSTER\_ENGINE\_TYPE\_CONVERTED | notification | InfluxDB {{version}} cluster '{{name}}' engine type converted | 
| TIDB-EVENT-22109 | DB\_CLUSTER\_ENGINE\_TYPE\_CONVERSION\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' engine type conversion failed | 
| TIDB-EVENT-22011 | DB\_CLUSTER\_INSTANCES\_ADDED | notification | InfluxDB {{version}} cluster '{{name}}' instances added | 
| TIDB-EVENT-22111 | DB\_CLUSTER\_INSTANCE\_ADD\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' instance addition failed | 
| TIDB-EVENT-22012 | DB\_CLUSTER\_INSTANCES\_REMOVED | notification | InfluxDB {{version}} cluster '{{name}}' instances removed | 
| TIDB-EVENT-22112 | DB\_CLUSTER\_INSTANCE\_REMOVE\_FAILED | notification, failure | InfluxDB {{version}} cluster '{{name}}' instance removal failed | 
| TIDB-EVENT-24001 | DB\_CLUSTER\_MAINTENANCE\_WINDOW\_STARTED | maintenance | InfluxDB {{version}} cluster '{{name}}' maintenance started | 
| TIDB-EVENT-24002 | DB\_CLUSTER\_MAINTENANCE\_WINDOW\_ENDED | maintenance | InfluxDB {{version}} cluster '{{name}}' maintenance ended | 

## Troubleshooting
<a name="influxdb-eventbridge-troubleshooting"></a>

Events not appearing in EventBridge  
Verify the operation has completed. Events are emitted only when a workflow reaches a terminal state (success or failure), not when it starts. Check your EventBridge rule pattern matches the event structure using the EventBridge console **Test event pattern** feature. Ensure you are looking at the correct Region—events are published in the same Region as the database resource.

Target not receiving events  
Confirm your EventBridge rule is enabled and the target is correctly configured. Verify the target's resource policy allows `events.amazonaws.com` to invoke it. For Amazon SNS targets, ensure the topic policy grants publish permission and that your subscription is confirmed. Check CloudWatch metrics for the rule: `TriggeredRules`, `Invocations`, and `FailedInvocations`.

Events delayed  
Amazon EventBridge provides at-least-once delivery with a 24-hour retry window. Under normal conditions, events are delivered shortly after operation completion. If your target is throttled or misconfigured, EventBridge retries delivery for up to 24 hours. Check CloudWatch metrics for the rule and verify your target is healthy.

## Limitations
<a name="influxdb-eventbridge-limitations"></a>
+ Events are published to Amazon EventBridge only. There is no Amazon Timestream for InfluxDB-specific event subscription API or console page—use EventBridge rules to filter and route events.
+ EventBridge does not retain events. To persist event history, route events to Amazon CloudWatch Logs, Amazon S3, or another durable store using an EventBridge rule. Historical events that occurred before a rule was created or modified will not be delivered—rules only match events from the point they are created or updated onwards.
+ Events are emitted only for operations initiated through the Amazon Timestream for InfluxDB APIs (console, CLI, SDK, CloudFormation). Internal service operations do not generate customer-visible events.
+ Events are regional—they are published in the same Region as the database resource.

## Pricing
<a name="influxdb-eventbridge-pricing"></a>

There is no additional Amazon Timestream for InfluxDB charge for publishing events. Standard pricing applies for downstream processing:
+ [Amazon EventBridge pricing](https://aws.amazon.com/eventbridge/pricing/) — for rule evaluation and event delivery to targets
+ Target service pricing applies based on which targets you configure (Lambda invocations, Amazon SQS messages, Amazon SNS deliveries, etc.)