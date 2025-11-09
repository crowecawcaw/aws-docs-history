# Monitoring Oracle Database@AWS events in Amazon EventBridge

You can monitor Oracle Database@AWS events in EventBridge, which delivers a stream of real-time data from
applications and AWS services. EventBridge routes this data to targets such as AWS Lambda and
Amazon Simple Notification Service.

###### Note

EventBridge was formerly called Amazon CloudWatch Events. For more information, see [EventBridge is the evolution of
Amazon CloudWatch Events](../../../eventbridge/latest/userguide/eb-cwe-now-eb.md "../../../eventbridge/latest/userguide/eb-cwe-now-eb.md") in the _Amazon EventBridge User Guide_.

## Overview of Oracle Database@AWS events

Oracle Database@AWS events are structured messages that indicate changes in resource lifecycles. An
_event bus_ is a router that receives events and delivers them to zero
or more destinations, or _targets_. Oracle Database@AWS events can be generated
from the following sources:

**Events from AWS**

These events are generated from Oracle Database@AWS APIs on the AWS side and are delivered
to the default event bus in your AWS account.

**Events from OCI**

These events are generated directly from OCI, such as events related to Oracle Exadata infrastructure
or VM clusters. When you subscribe to Oracle Database@AWS, an event bus with prefix
`aws.partner/odb/` is created in your AWS account to receive events from
OCI.

## Oracle Database@AWS events from AWS

Oracle Database@AWS events from AWS include lifecycle changes related to the ODB network during
creation and deletion. These events are delivered to the default event bus in your
AWS account. The delivery type is [_best effort_](../../../eventbridge/latest/ref/event-delivery-level.md "../../../eventbridge/latest/ref/event-delivery-level.md").

| ODB network events | Event          | Event ID                                     | Message |
| ------------------ | -------------- | -------------------------------------------- | ------- |
| Creation           | ODB-EVENT-0001 | Successfully created ODB network _odbnet_ID_ |
| Creation failed    | ODB-EVENT-0011 | Failed to create ODB network _odbnet_ID_     |
| Deletion           | ODB-EVENT-0002 | Successfully deleted ODB network _odbnet_ID_ |
| Deletion failed    | ODB-EVENT-0012 | Failed to delete ODB network _odbnet_ID_     |

### Example: ODB network creation event

The following example shows an event for a successful ODB network creation.

```
{
  "version": "0",
  "id": "01234567-EXAMPLE",
  "detail-type": "ODB Network Event",
  "source": "aws.odb",
  "account": "123456789012",
  "time": "2025-06-12T10:23:43Z",
  "region": "us-east-1",
  "resources": [
    "arn:aws:odb:us-east-1:123456789012:odbnetwork/odbnet-1234567890abcdef"
  ],
  "detail": {
    "eventId": "ODB-EVENT-0001",
    "message": "Successfully created ODB network odbnet-1234567890abcdef"
  }
}
```

## Oracle Database@AWS events from OCI

Most events are generated directly from OCI. Oracle Database@AWS creates an event bus with prefix
`aws.partner/odb/` in your AWS account to receive events from OCI. We
recommend that you do not delete this event bus.

OCI provides comprehensive event types, including the following:

- Oracle Exadata infrastructure
- VM cluster events
- CDB events
- PDB events

For more information about the specific event types and details that OCI supports, see
[Oracle Exadata Database Service on Dedicated Infrastructure Events](https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/ecs-events.html "https://docs.oracle.com/en/engineered-systems/exadata-cloud-service/ecscm/ecs-events.html") and [Events for Autonomous Database on Dedicated Exadata Infrastructure](https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/arfad/index.html#articletitle "https://docs.oracle.com/en/cloud/paas/autonomous-database/dedicated/arfad/index.html#articletitle").

## Filtering Oracle Database@AWS events

You can follow EventBridge suggested best practices on event bus setup at [Event buses in
Amazon EventBridge](../../../eventbridge/latest/userguide/eb-event-bus.md "../../../eventbridge/latest/userguide/eb-event-bus.md"). Depending on your use cases, you can set up EventBridge rules to filter events
and targets to receive and use events.

### Filtering ODB network events from AWS

For ODB network events from AWS, you can filter using the following event pattern:

```
{
  "source": ["aws.odb"],
  "detail-type": ["ODB Network Event"]
}
```

You can apply this pattern using the EventBridge `put-rule` API with the default
event bus. For more information, see PutRule in the _Amazon EventBridge API
Reference_.

### Filtering Oracle Database@AWS events from OCI

For Oracle Database@AWS events from OCI, you can set up a rule using a command similar to the
example in PutRule in the _Amazon EventBridge API Reference_.
Note the following guidelines:

- Use a custom event pattern depending on the event types that you want to
  filter.
- Set **EventBusName** to the name of the bus that
  Oracle Database@AWS created.

For more information about how to filter events and set up EventBridge targets across accounts,
see [Sending and receiving events between AWS accounts in Amazon EventBridge](../../../eventbridge/latest/userguide/eb-cross-account.md "../../../eventbridge/latest/userguide/eb-cross-account.md").

## Troubleshooting Oracle Database@AWS events

If you encounter an issue with event delivery or event content, do the following:

- For ODB network events, contact AWS Support.
- For Oracle Database@AWS events other than ODB network events, contact Oracle Cloud Support.

For more information, see [Getting support for Oracle Database@AWS](odb-troubleshooting-overview.md#oracle-database-aws-support "odb-troubleshooting-overview.md#oracle-database-aws-support").
