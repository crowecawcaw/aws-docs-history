# Monitor AWS FIS experiments using Amazon EventBridge

When the state of an experiment changes, AWS FIS emits a notification. These notifications
are made available as events through Amazon EventBridge (formerly called CloudWatch Events). AWS FIS emits these
events on a best effort basis. Events are delivered to EventBridge in near real time.

With EventBridge, you can create rules that trigger programmatic actions in response to an event.
For example, you can configure a rule that invokes an SNS topic to send an email notification
or invokes a Lambda function to take some action.

For more information about EventBridge, see [Getting started with
Amazon EventBridge](../../../eventbridge/latest/userguide/eb-get-started.md "../../../eventbridge/latest/userguide/eb-get-started.md") in the _Amazon EventBridge User Guide_.

The following is the syntax of an experiment state change event:

```
{
    "version": "0",
    "id": "`12345678-1234-1234-1234-123456789012`",
    "detail-type": "FIS Experiment State Change",
    "source": "aws.fis",
    "account": "`123456789012`",
    "time": "`yyyy`-`mm`-`dd`T`hh`:`mm`:`ss`Z",
    "region": "`region`",
    "resources": [
        "arn:aws:fis:`region`:`account_id`:experiment/`experiment-id`"
    ],
    "detail": {
        "experiment-id": "`EXPaBCD1efg2HIJkL3`",
        "experiment-template-id": "`EXTa1b2c3de5f6g7h`",
        "new-state": {
            "status": "`new_value`",
            "reason": "`reason_string`"
        },
        "old-state": {
           "status": "`old_value`",
           "reason": "`reason_string`"
        }
    }
}
```

`experiment-id`

The ID of the experiment whose state changed.

`experiment-template-id`

The ID of the experiment template used by the experiment.

`new_value`

The new state of the experiment. The possible values are:

- `completed`
- `failed`
- `initiating`
- `running`
- `stopped`
- `stopping`

`old_value`

The previous state of the experiment. The possible values are:

- `initiating`
- `pending`
- `running`
- `stopping`
