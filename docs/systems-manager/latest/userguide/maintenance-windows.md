# AWS Systems Manager Maintenance Windows

Maintenance Windows, a tool in AWS Systems Manager, helps you define a schedule for when to perform potentially
disruptive actions on your nodes such as patching an operating system, updating drivers, or
installing software or patches.

###### Note

State Manager and Maintenance Windows can perform some similar types of updates on your managed nodes.
Which one you choose depends on whether you need to automate system compliance or perform
high-priority, time-sensitive tasks during periods you specify.

For more information, see [Choosing between State Manager and
Maintenance Windows](state-manager-vs-maintenance-windows.md "state-manager-vs-maintenance-windows.md").

With Maintenance Windows, you can schedule actions on numerous other AWS resource types, such as
Amazon Simple Storage Service (Amazon S3) buckets, Amazon Simple Queue Service (Amazon SQS) queues, AWS Key Management Service (AWS KMS) keys, and many more.

For a full list of supported resource types that you can include in a maintenance window
target, see [Resources you can use with AWS Resource Groups and Tag Editor](../../../ARG/latest/userguide/supported-resources.md#supported-resources-console "../../../ARG/latest/userguide/supported-resources.md#supported-resources-console") in the _AWS Resource Groups
User Guide_. To get started with Maintenance Windows, open the [Systems Manager console](https://console.aws.amazon.com/systems-manager/maintenance-windows "https://console.aws.amazon.com/systems-manager/maintenance-windows"). In the navigation
pane, choose **Maintenance Windows**.

Each maintenance window has a schedule, a maximum duration, a set of registered targets
(the managed nodes or other AWS resources that are acted upon), and a set of registered
tasks. You can add tags to your maintenance windows when you create or update them. (Tags
are keys that help identify and sort your resources within your organization.) You can also
specify dates that a maintenance window shouldn't run before or after, and you can specify
the international time zone on which to base the maintenance window schedule.

For an explanation of how the various schedule-related options for maintenance windows
relate to one another, see [Maintenance window scheduling and
active period options](maintenance-windows-schedule-options.md "maintenance-windows-schedule-options.md").

For more information about working with the `--schedule` option, see [Reference: Cron and rate expressions
for Systems Manager](reference-cron-and-rate-expressions.md "reference-cron-and-rate-expressions.md").

###### Supported task types

With maintenance windows, you can run four types of tasks:

- Commands in Run Command, a tool in Systems Manager

For more information about Run Command, see [AWS Systems Manager Run Command](run-command.md "run-command.md").

- Workflows in Automation, a tool in Systems Manager

For more information about Automation workflows, see [AWS Systems Manager Automation](systems-manager-automation.md "systems-manager-automation.md").

- Functions in AWS Lambda

For more information about Lambda functions, see [Getting started with Lambda](../../../lambda/latest/dg/getting-started.md "../../../lambda/latest/dg/getting-started.md")
in the _AWS Lambda Developer Guide_.

- Tasks in AWS Step Functions

###### Note

Maintenance window tasks support Step Functions Standard state machine workflows only.
They don't support Express state machine workflows. For information about state
machine workflow types, see [Standard
vs. Express Workflows](../../../step-functions/latest/dg/concepts-standard-vs-express.md "../../../step-functions/latest/dg/concepts-standard-vs-express.md") in the
_AWS Step Functions Developer Guide_.

For more information about Step Functions, see the _[AWS Step Functions Developer Guide](../../../step-functions/latest/dg.md "../../../step-functions/latest/dg.md")_.
This means you can use maintenance windows to perform tasks such as the following on your
selected targets.

- Install or update applications.
- Apply patches.
- Install or update SSM Agent.
- Run PowerShell commands and Linux shell scripts by using a Systems Manager Run Command
  task.
- Build Amazon Machine Images (AMIs), boot-strap software, and configure nodes by using a
  Systems Manager Automation task.
- Run AWS Lambda functions that invokes additional actions, such as scanning your
  nodes for patch updates.
- Run AWS Step Functions state machines to perform tasks such as removing a node from an
  Elastic Load Balancing environment, patching the node, and then adding the node back to the Elastic Load Balancing
  environment.
- Target nodes that are offline by specifying an AWS resource group as the
  target.

###### Note

One or more targets must be specified for maintenance window Run Command-type tasks.
Depending on the task, targets are optional for other maintenance window task types
(Automation, AWS Lambda, and AWS Step Functions). For more information about running tasks that
don't specify targets, see [Registering maintenance window
tasks without targets](maintenance-windows-targetless-tasks.md "maintenance-windows-targetless-tasks.md").

###### EventBridge support

This Systems Manager tool is supported as an _event_ type in Amazon EventBridge rules.
For information, see [Monitoring Systems Manager events with
Amazon EventBridge](monitoring-eventbridge-events.md "monitoring-eventbridge-events.md") and [Reference: Amazon EventBridge event patterns and types
for Systems Manager](reference-eventbridge-events.md "reference-eventbridge-events.md").

###### Contents

- [Setting up Maintenance Windows](setting-up-maintenance-windows.md "setting-up-maintenance-windows.md")
- [Create and manage maintenance windows using
  the console](sysman-maintenance-working.md "sysman-maintenance-working.md")
- [Tutorials](maintenance-windows-tutorials.md "maintenance-windows-tutorials.md")
- [Using pseudo parameters
  when registering maintenance window tasks](maintenance-window-tasks-pseudo-parameters.md "maintenance-window-tasks-pseudo-parameters.md")
- [Maintenance window scheduling and
  active period options](maintenance-windows-schedule-options.md "maintenance-windows-schedule-options.md")
- [Registering maintenance window
  tasks without targets](maintenance-windows-targetless-tasks.md "maintenance-windows-targetless-tasks.md")
- [Troubleshooting maintenance
  windows](troubleshooting-maintenance-windows.md "troubleshooting-maintenance-windows.md")
