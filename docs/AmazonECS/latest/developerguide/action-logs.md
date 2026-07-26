# Monitor Amazon ECS operations with Action Logs

## Amazon ECS Action Logs overview

With Amazon ECS Action Logs, you can monitor all actions that Amazon ECS performs on
your behalf during container lifecycle operations. Action Logs capture timestamped
records of every resource operation, state transition, and service-initiated API
call within your clusters.

Action Logs record previously invisible operations such as container image downloads,
load balancer registrations, and security group configurations. Without Action Logs,
you can only observe the start and end states of your resources. With Action Logs, you
can see every intermediate step that Amazon ECS takes between those states.

When you enable Action Logs, Amazon Q in the AWS Management Console can access
these logs to help you debug deployment failures and daemon issues directly from the
console.

## Benefits of Action Logs

Action Logs provide the following benefits for managing your Amazon ECS workloads:

- **Visibility into service actions** – View
  previously invisible actions that Amazon ECS performs between state transitions,
  including infrastructure provisioning, network configuration, and resource
  registration.
- **Improved troubleshooting** – Diagnose
  deployment failures and infrastructure problems without
  contacting AWS Support. Action Logs support a growing set of failure
  reasons.
- **Extended failure metadata** – Retain
  metadata about failed tasks beyond the standard 1-hour retention period. You
  can review detailed failure information at your own pace.
- **Self-service debugging** – Investigate
  and resolve issues independently by reviewing the complete sequence of actions
  that led to a failure.

## What gets logged

Action Logs capture actions for the following Amazon ECS operations:

- **Service deployments** – State
  transitions, rollbacks, and lifecycle hook execution.
- **Managed Daemon lifecycle** – Create,
  update, delete, and instance drain operations for Managed Daemons.

## How Action Logs work

You opt in to Action Logs at the cluster level. You can enable Action Logs
through the Amazon ECS console or by using the Amazon CloudWatch APIs
(`PutDeliverySource`,
`PutDeliveryDestination`, and `CreateDelivery`).

After you enable Action Logs, Amazon ECS emits structured JSON logs through the CloudWatch
Ingestion Hub. Amazon ECS delivers logs to your chosen destination: CloudWatch Logs, Amazon S3, or
Amazon Data Firehose.

Action Logs use fire-and-forget publishing. Log publishing never blocks or degrades
Amazon ECS resource operations. If a transient delivery failure occurs, Amazon ECS continues
processing your workloads without interruption.

## Log schema overview

Each Action Log entry contains the following fields:

- `timestamp` – Unix milliseconds when the event
  occurred.
- `logLevel` – The severity level: `INFO`,
  `WARN`, or `ERROR`.
- `account` – The AWS account ID.
- `region` – The AWS Region where the event
  occurred.
- `resourceArn` – The cluster ARN that
  represents the opt-in scope.
- `actionSourceId` – The sub-resource identifier, such as a
  service ARN or daemon ARN.
- `eventName` – The action identifier, for example
  `DAEMON_DEPLOYMENT_IN_PROGRESS`.
- `detail` – An event-specific JSON payload with additional
  context about the action.

## Log destinations and organization

You can deliver Action Logs to the following destinations:

- **CloudWatch Logs** – CloudWatch Logs stores logs in a log
  group named `/aws/vendedlogs/ecs/action-logs/{resourceId}`. Amazon ECS creates a
  separate log stream for each sub-resource, using the
  `{actionSourceId}` as the log stream name.
- **Amazon S3** – Amazon S3 partitions logs by
  account, Region, and 5-minute time windows. Amazon S3 compresses the files
  using gzip for efficient storage.
- **Amazon Data Firehose** – Amazon Data
  Firehose delivers logs as newline-delimited JSON records in near
  real-time.

## Pricing

Action Logs is a paid feature that uses standard CloudWatch vended logs pricing. You pay
for log ingestion and storage based on the volume of logs that your clusters generate.
You can configure retention through your destination settings. When you enable Action
Logs through the Amazon ECS console, CloudWatch Logs uses a default retention of 7 days.

###### Topics

- [Getting started with Amazon ECS Action Logs](action-logs-getting-started.md "action-logs-getting-started.md")
- [Troubleshooting with Amazon ECS Action Logs](action-logs-troubleshooting.md "action-logs-troubleshooting.md")
