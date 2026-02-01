• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Monitoring Systems Manager events with

Amazon EventBridge

Amazon EventBridge is a serverless event bus service that allows you to connect your applications
with data from a variety of sources. EventBridge delivers a stream of real-time data from your own
applications, software-as-a-service (SaaS) applications, and AWS services and routes that
data to targets such as AWS Lambda. You can set up routing rules to determine where to send
your data to build application architectures that react in real time to all of your data
sources. EventBridge allows you to build event driven architectures, which are loosely coupled and
distributed.

EventBridge was formerly called Amazon CloudWatch Events. EventBridge includes new features that allow you to receive
events from SaaS partners and your own applications. Existing CloudWatch Events users can access their
existing default bus, rules, and events in the new EventBridge console and in the CloudWatch Events console.
EventBridge uses the same CloudWatch Events API, so all of your existing CloudWatch Events API usage remains the same.

EventBridge can add events from dozens of AWS services to your rules, and targets from over 20
AWS services.

EventBridge provides support for both AWS Systems Manager events and Systems Manager targets.

###### Supported Systems Manager event types

Among the many types of Systems Manager events that EventBridge can detect are:

- A just-in-time node access request status update for manual approvals.
- A failed just-in-time node access request.
- A maintenance window being turned off.
- An Automation workflow completing successfully. Automation is a tool in
  AWS Systems Manager.
- A managed node being out of patch compliance.
- A parameter value being updated.
  EventBridge supports events from the following AWS Systems Manager tools:

- Just-in-time node access (Events are emitted on a best effort basis.)
- Automation (Events are emitted on a best effort basis.)
- Change Calendar (Events are emitted on a best effort basis.)
- Compliance
- Inventory (Events are emitted on a best effort basis.)
- Maintenance Windows (Events are emitted on a best effort basis.)
- Parameter Store (Events are emitted on a best effort basis.)
- Run Command (Events are emitted on a best effort basis.)
- State Manager (Events are emitted on a best effort basis.)
  For complete details about supported Systems Manager event types, see [Reference: Amazon EventBridge event patterns and types
  for Systems Manager](reference-eventbridge-events.md "reference-eventbridge-events.md")
  and [Amazon EventBridge event examples for
  Systems Manager](monitoring-systems-manager-event-examples.md "monitoring-systems-manager-event-examples.md").

###### Supported Systems Manager target types

EventBridge supports the following three Systems Manager tools as targets of an event rule:

- Running an Automation workflow
- Running a Run Command Command document (Events are emitted on a best effort
  basis.)
- Creating an OpsCenter OpsItem
  For suggested ways you might use these targets, see [Sample scenarios: Systems Manager targets in
  Amazon EventBridge rules](monitoring-systems-manager-targets.md "monitoring-systems-manager-targets.md").

For more information about how to get started with EventBridge and set up rules, see [Getting
started with Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User Guide_. For complete
information about working with EventBridge, see the [_Amazon EventBridge User Guide_](../../../eventbridge/latest/userguide.md "../../../eventbridge/latest/userguide.md").

###### Topics

- [Configuring EventBridge for Systems Manager
  events](monitoring-systems-manager-events.md "monitoring-systems-manager-events.md")
- [Amazon EventBridge event examples for
  Systems Manager](monitoring-systems-manager-event-examples.md "monitoring-systems-manager-event-examples.md")
- [Sample scenarios: Systems Manager targets in
  Amazon EventBridge rules](monitoring-systems-manager-targets.md "monitoring-systems-manager-targets.md")
