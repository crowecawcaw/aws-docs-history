# Monitoring Amazon RDS events

An _event_ indicates a change in an environment. This can be an AWS environment, an SaaS partner service or
application, or a custom application or service. For descriptions of the RDS events, see [Amazon RDS event categories and event messages](USER_Events.md "USER_Events.md").

###### Topics

- [Overview of events for Amazon RDS](#rds-cloudwatch-events.sample "#rds-cloudwatch-events.sample")
- [Viewing Amazon RDS events](USER_ListEvents.md "USER_ListEvents.md")
- [Working with Amazon RDS event notification](USER_Events.md "USER_Events.md")
- [Creating a rule that triggers on an Amazon RDS event](rds-cloud-watch-events.md "rds-cloud-watch-events.md")
- [Amazon RDS event categories and event messages](USER_Events.md "USER_Events.md")

## Overview of events for Amazon RDS

An _RDS event_ indicates a change in the Amazon RDS environment. For example, Amazon RDS generates an event when the state of a DB instance changes from pending to
running. Amazon RDS
delivers events to EventBridge in near-real time.

###### Note

Amazon RDS emits events on a best effort basis. We recommend that you avoid writing programs that depend on the order or existence of
notification events, because they might be out of sequence or missing.

Amazon RDS records events that relate to the following resources:

- DB instances

For a list of DB instance events, see [DB instance events](USER_Events.md#USER_Events.Messages.instance "USER_Events.md#USER_Events.Messages.instance").

- DB parameter groups

For a list of DB parameter group events, see [DB parameter group events](USER_Events.md#USER_Events.Messages.parameter-group "USER_Events.md#USER_Events.Messages.parameter-group").

- DB security groups

For a list of DB security group events, see [DB security group events](USER_Events.md#USER_Events.Messages.security-group "USER_Events.md#USER_Events.Messages.security-group").

- DB snapshots

For a list of DB snapshot events, see [DB snapshot events](USER_Events.md#USER_Events.Messages.snapshot "USER_Events.md#USER_Events.Messages.snapshot").

- RDS Proxy events

For a list of RDS Proxy events, see [RDS Proxy events](USER_Events.md#USER_Events.Messages.rds-proxy "USER_Events.md#USER_Events.Messages.rds-proxy").

- Blue/green deployment events

For a list of blue/green deployment events, see [Blue/green deployment events](USER_Events.md#USER_Events.Messages.BlueGreenDeployments "USER_Events.md#USER_Events.Messages.BlueGreenDeployments").

This information includes the following:

- The date and time of the event
- The source name and source type of the event
- A message associated with the event
- Event notifications include tags from when
  the message was sent and may not reflect tags at the time when the event
  occurred
