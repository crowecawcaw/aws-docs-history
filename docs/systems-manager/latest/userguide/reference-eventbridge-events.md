

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see [Amazon CloudWatch Dashboard documentation](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.html). 

# Reference: Amazon EventBridge event patterns and types for Systems Manager
<a name="reference-eventbridge-events"></a>


|  | 
| --- |
| Amazon EventBridge is the preferred way to manage your events. CloudWatch Events and EventBridge are the same underlying service and API, but EventBridge provides more features. Changes you make in either CloudWatch or EventBridge are reflected in each console. For more information, see the [*Amazon EventBridge User Guide*](https://docs.aws.amazon.com/eventbridge/). | 

Using Amazon EventBridge, you can create *rules* that match incoming *events* and route them to *targets* for processing. 

An event indicates a change in an environment in your own applications, software as a service (SaaS) applications, or an AWS service. Events are produced on a best effort basis. After an event type that is specified in a rule is detected, EventBridge routes it to a specified target for processing. Targets can include Amazon Elastic Compute Cloud (Amazon EC2) instances, AWS Lambda functions, Amazon Kinesis streams, Amazon Elastic Container Service (Amazon ECS) tasks, AWS Step Functions state machines, Amazon Simple Notification Service (Amazon SNS) topics, Amazon Simple Queue Service (Amazon SQS) queues, built-in targets and many more.

For information about creating EventBridge rules, see the following topics:
+ [Monitoring Systems Manager events with Amazon EventBridge](monitoring-eventbridge-events.md)
+ [Amazon EventBridge event examples for Systems Manager](monitoring-systems-manager-event-examples.md)
+ [Getting started with Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html) in the *Amazon EventBridge User Guide*

The remainder of this topic describes the types of Systems Manager events that you can include in your EventBridge rules.

 

## Event type: Automation
<a name="event-type-automation"></a>



| Event type name  | Description of events you can add to a rule | 
| --- | --- | 
| EC2 Automation Execution Status-change Notification | The overall status of an Automation workflow changes. You can add one or more of the following status changes to an event rule:+  Approved <br />+  Canceled <br />+  Failed <br />+  PendingApproval <br />+  PendingChangeCalendarOverride <br />+  Rejected <br />+  Scheduled <br />+  Success <br />+  TimedOut  | 
| EC2 Automation Step Status-change Notification | The status of a specific step in an Automation workflow changes. You can add one or more of the following status changes to an event rule:+  Canceled <br />+  Failed <br />+  Success <br />+  TimedOut  | 

## Event type: Change Calendar
<a name="event-type-change-calendar"></a>



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| Calendar State Change | The state of a Change Calendar changes. You can add one or both of the following state changes to an event rule:+  OPEN <br />+  CLOSED State changes for calendars shared from other AWS accounts aren't supported. | 

## Event type: Change Manager
<a name="event-type-change-manager"></a>

**Change Manager availability change**  
AWS Systems Manager Change Manager will no longer be open to new customers starting November 7, 2025. If you would like to use Change Manager, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS Systems Manager Change Manager availability change](https://docs.aws.amazon.com/systems-manager/latest/userguide/change-manager-availability-change.html). 



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| Change Request Status Update | The state of a Change Manager change request. You can use the following states in an event rule:+  Approved <br />+  Rejected <br />+  InProgress   | 

## Event type: Configuration Compliance
<a name="event-type-configuration-compliance"></a>



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| Configuration Compliance State Change | The state of a managed node changes, for either association compliance or patch compliance. You can add one or more of the following state changes to an event rule:+  compliant <br />+  non\_compliant  | 

## Event type: Inventory
<a name="event-type-inventory"></a>



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| Inventory Resource State Change | The deletion of custom inventory and a [PutInventory](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_PutInventory.html) call that uses an old schema version. You can add one or more of the following state changes to an event rule:+  Custom inventory type deleted event on a specific node. EventBridge sends one event per node per custom InventoryType. <br />+  Custom inventory type deleted event for all nodes. <br />+  PutInventory call with old schema version event. EventBridge sends this event when the schema version is less than the current schema. This event applies to all inventory types. For more information, see [Using EventBridge to monitor Inventory events](systems-manager-inventory-setting-up-eventbridge.md). | 

## Event type: Maintenance Window
<a name="event-type-maintenance-window"></a>



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| Maintenance Window Status-change Notification | The overall status of one or more maintenance windows changes. You can add one or more of the following state changes to an event rule:+  DISABLED <br />+  ENABLED  | 
| Maintenance Window Target Registration Notification | The status of one or more maintenance window targets changes. You can add one or more of the following state changes to an event rule:+  DEREGISTERED <br />+  REGISTERED <br />+  UPDATED  | 
| Maintenance Window Execution State-change Notification | The overall status of a maintenance window changes while it's running. You can add one or more of the following state changes to an event rule:+  CANCELLED <br />+  CANCELLING <br />+  FAILED <br />+  IN\_PROGRESS <br />+  PENDING <br />+  SKIPPED\_OVERLAPPING <br />+  SUCCESS <br />+  TIMED\_OUT  | 
| Maintenance Window Task Execution State-change Notification | The state of a task in a maintenance window changes while it's running. You can add one or more of the following state changes to an event rule:+  CANCELLED <br />+  CANCELLING <br />+  FAILED <br />+  IN\_PROGRESS <br />+  SUCCESS <br />+  TIMED\_OUT  | 
| Maintenance Window Task Target Invocation State-change Notification | The state of a maintenance window task on a specific target changes.<br />This notification is fully supported only for Run Command tasks. For this type of task, you can add one or more of the following state changes to an event rule:+  CANCELLED <br />+  CANCELLING <br />+  FAILED <br />+  IN\_PROGRESS <br />+  SUCCESS <br />+  TIMED\_OUT <br />For Automation, AWS Lambda, and AWS Step Functions tasks, EventBridge reports only the states `IN_PROGRESS` and `COMPLETE`. `COMPLETE` is reported whether the task is successful or not. | 
| Maintenance Window Task Registration Notification | The state of one or more maintenance window tasks changes. You can add one or more of the following state changes to an event rule:+  DEREGISTERED <br />+  REGISTERED <br />+  UPDATED  | 

## Event type: OpsCenter
<a name="event-type-OpsCenter"></a>



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| OpsItem Create | Occurs when an OpsItem is created. You can add rules for one of the following OpsItem types:+  /aws/issue <br />+  /aws/task <br />+  /aws/insight <br />+  /aws/actionitem  | 
| OpsItem Update | Occurs when an OpsItem is updated. You can add rules for one of the following OpsItem types:+  /aws/issue <br />+  /aws/task <br />+  /aws/insight <br />+  /aws/actionitem  | 

## Event type: Parameter Store
<a name="event-type-parameter-store"></a>



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| Parameter Store Change | The state of a parameter changes. You can add one or more of the following state changes to an event rule:+  Create <br />+  Update <br />+  Delete <br />+  LabelParameterVersion For more information, see [Configuring EventBridge rules for parameters and parameter policies](sysman-paramstore-cwe.md#cwe-parameter-changes). | 
| Parameter Store Policy Action | A condition of an advanced parameter policy change is met. You can add one or more of the following status changes to an event rule:+  Expiration <br />+  ExpirationNotification <br />+  NoChangeNotification For more information, see [Configuring EventBridge rules for parameters and parameter policies](sysman-paramstore-cwe.md#cwe-parameter-changes). | 

## Event type: Run Command
<a name="event-type-run-command"></a>



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| EC2 Command Invocation Status-change Notification | The status of a command sent to an individual managed instance changes. You can add one or more of the following status changes to an event rule:+  Success <br />+  InProgress <br />+  TimedOut <br />+  Canceled <br />+  Failed  | 
| EC2 Command Status-change Notification  | The overall status of a command changes. You can add one or more of the following status changes to an event rule:+  Success <br />+  InProgress <br />+  TimedOut <br />+  Canceled <br />+  Failed  | 

## Event type: State Manager
<a name="event-type-state-manager"></a>



| Event type name | Description of events you can add to a rule | 
| --- | --- | 
| EC2 State Manager Association State Change | The overall state of an Association changes as it's being applied. You can add one or more of the following state changes to an event rule:+  Failed <br />+  Pending <br />+  Success  | 
| EC2 State Manager Instance Association State Change | The state of a single managed instance that is targeted by an Association changes. You can add one or more of the following state changes to an event rule:+  Failed <br />+  Pending <br />+  Success  | 