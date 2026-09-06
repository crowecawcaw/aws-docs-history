

# AWS Health Planned lifecycle events
<a name="batch-planned-lifecycle-events"></a>

AWS Health provides advance notification when upcoming changes affect your AWS Batch resources. These notifications, called *planned lifecycle events*, alert you to changes such as AMI deprecations, operating system end-of-support dates, and infrastructure updates that require action. AWS Batch leverages AWS Health to give you early visibility into these changes so that you can plan migrations and avoid disruption to your batch processing workloads.

For general information about AWS Health, see [What is AWS Health?](https://docs.aws.amazon.com/health/latest/ug/what-is-aws-health.html) in the *AWS Health User Guide*.

## What are planned lifecycle events for AWS Batch?
<a name="batch-ple-overview"></a>

AWS Health sends planned lifecycle event notifications when upcoming changes affect your AWS Batch resources, such as AMI end-of-support dates and other infrastructure changes that require you to take action.

Planned lifecycle events have the following characteristics:
+ **Type category** – `scheduledChange`
+ **Event type code** – Follows the pattern `AWS_BATCH_PLANNED_LIFECYCLE_EVENT`
+ **Lead time** – A minimum of 180 days for major changes and 90 days for minor changes, where possible.
+ **Event start time** – The earliest date at which your resources can be affected by the change.
+ **Dynamic resource tracking** – Affected resources are listed with a `PENDING` status. After you complete the required action or delete the resource, the status updates to `RESOLVED`.
+ **Scope** – You receive a single event ARN for each planned lifecycle event, grouped by AWS Region where you have affected resources.

**Note**  
Resource status updates are asynchronous and can take up to 72 hours to reflect the current state. If you resolve all affected resources before the end-of-support date, the AWS Health event status changes to `Closed`.

## Example: Amazon ECS Amazon Linux 2 AMI deprecation
<a name="batch-ple-example-al2"></a>

The Amazon ECS Amazon Linux 2 AMI deprecation is an example of a planned lifecycle event for AWS Batch. AWS announced that Amazon Linux 2 reaches end of support, and starting in January 2026, AWS Batch changes the default AMI for new Amazon ECS compute environments from Amazon Linux 2 to Amazon Linux 2023.

Customers received AWS Health planned lifecycle event notifications that identified their affected compute environments. Each affected compute environment was listed with a `PENDING` status. After a compute environment was migrated to Amazon Linux 2023, the status updated to `RESOLVED`. This allowed teams to track migration progress across their fleet of compute environments.

For more information about this deprecation, see [Amazon ECS Amazon Linux 2 AMI deprecation](ecs-al2-ami-deprecation.md). For migration steps, see [How to migrate from ECS AL2 to ECS AL2023](ecs-migration-2023.md).

## Viewing planned lifecycle events
<a name="batch-ple-viewing"></a>

You can view planned lifecycle events for AWS Batch in the AWS Health Dashboard.

**To view planned lifecycle events**

1. Open the AWS Health Dashboard at [https://health.aws.amazon.com/health/home](https://health.aws.amazon.com/health/home).

1. In the navigation pane, choose **Scheduled changes**.

1. Find the **Batch planned lifecycle event**. You can filter by service or use the calendar view to see events on a monthly timeline.

1. Choose the event to view the **Details** and **Affected resources** tabs.

The **Affected resources** tab lists each affected resource with its current status:
+ **Pending** – The resource requires action.
+ **Resolved** – The required action is complete or the resource was deleted.
+ **Unknown** – The status can't be determined.

You can download the list of affected resources in CSV or JSON format. If your account is part of an AWS organization, the organization view shows affected resources across all member accounts.

The calendar view projects scheduled changes up to 3 months in the past and 1 year into the future, so you can plan maintenance windows accordingly.

## Monitoring planned lifecycle events with Amazon EventBridge
<a name="batch-ple-eventbridge"></a>

You can create Amazon EventBridge rules to automatically detect and respond to AWS Health planned lifecycle events for AWS Batch. AWS Health delivers events to EventBridge, and you can create rules that match these events and route them to targets such as AWS Lambda functions, Amazon Simple Notification Service topics, and Amazon Simple Queue Service queues.

The following is an example event pattern that matches AWS Health planned lifecycle events for AWS Batch:

```
{
  "source": ["aws.health"],
  "detail-type": ["AWS Health Event"],
  "detail": {
    "service": ["BATCH"],
    "eventTypeCategory": ["scheduledChange"]
  }
}
```

Common use cases for EventBridge rules with planned lifecycle events include:
+ Sending notifications to team chat channels through Amazon Simple Notification Service.
+ Creating operational tickets automatically when new events are detected.
+ Invoking AWS Lambda functions to assess affected resources and begin migration workflows.

For more information about configuring EventBridge rules for AWS Health, see [Monitoring AWS Health events with Amazon EventBridge](https://docs.aws.amazon.com/health/latest/ug/cloudwatch-events-health.html) in the *AWS Health User Guide*. For sample automation, see the [AWS Health Tools](https://github.com/aws/aws-health-tools) repository on GitHub.