# AWS Supply Chain events detail reference

All events from AWS services have a common set of fields containing
metadata about the event, such as the AWS service that is the source of
the event, the time the event was generated, the account and region in which the event
took place, and others. For definitions of these general fields, see [Event structure reference](../../../eventbridge/latest/userguide/eb-events-structure.md "../../../eventbridge/latest/userguide/eb-events-structure.md") in the _Amazon EventBridge User
Guide_.

In addition, each event has a `detail` field that contains data specific to
that particular event. The reference below defines the detail fields for the various
AWS Supply Chain events.

When using EventBridge to select and manage AWS Supply Chain events, it's useful to
keep the following in mind:

- The `source` field for all events from AWS Supply Chain is set to
  `aws.supplychain`.
- The `detail-type` field specifies the event type.

For example, `AWS Supply Chain Data Integration Status Change`.

- The `detail` field contains the data that is specific to that
  particular event.
  For information on constructing event patterns that enable rules to match AWS Supply Chain
  events, see [Event patterns](../../../eventbridge/latest/userguide/eb-event-patterns.md "../../../eventbridge/latest/userguide/eb-event-patterns.md") in
  the _Amazon EventBridge User Guide_.

For more information on events and how EventBridge processes them, see [Amazon EventBridge events](../../../eventbridge/latest/userguide/eb-events.md "../../../eventbridge/latest/userguide/eb-events.md") in the _Amazon EventBridge User
Guide_.

## AWS Supply Chain Data Integration Status Change

Below is an example for the `AWS Supply Chain Data Integration Status Change event` event.

```

{
    "version": "0",
    "id": "`instanceID`",
    "detail-type": "AWS Supply Chain Data Integration Status Change",
    "source": "aws.supplychain",
    "account": "`acccountID`",
    "time": "2024-03-30T12:26:13Z",
    "region": "us-east-1",
    "resources": [],
    "detail": {
        "version": "1.0",
        "instanceId": "`instanceID`",
        "flowArn": "arn:aws:scn:`region`:`acccountID`:instance/`instanceID`/data-integration-flows/`flowname`",
        "flowExecutionId": "`flowExecutionId`",
        "status": "IN_PROGRESS",
        "startTime": "2024-03-30T12:26:13Z",
        "endTime": "",
        "message": "",
        "sourceType": "S3",
        "sourceInfo": {
            "s3Source": {
                "bucketName": "aws-supply-chain-data-`instanceID`",
                "key": "`flowname`"
            }
        }
    }
}
```

`endTime` is only available when the _status_ is failure or success.
