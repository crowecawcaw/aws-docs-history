# AWS Glue Data Quality events

AWS Glue Data Quality sends service events directly to EventBridge.

## AWS Glue Data Quality service events

AWS Glue Data Quality sends the following events directly to EventBridge:

- Glue Job State Change
- Glue Catalog State Change
- Glue Crawler State Change
- Glue Scheduled Crawler Invocation Failure
- Glue Job Run Status
- Glue Crawler Table Change
- Glue Data Catalog Database State Change
- Glue Data Catalog Table State Change
- Glue Statistics Task Started
- Glue Statistics Task Succeeded
- Glue Statistics Task Failed
- Glue Auto Statistics Invocation Failure
- Glue Scheduled Statistics Invocation Failure
- Data Quality Task State Change
- Data Quality Evaluation Results Available
- Entity Metering Event
- Auto debug metadata key shared from Orca

_Delivery type_:
[Best effort](event-delivery-level.md "event-delivery-level.md")

To match against all events from this service, create an event pattern that matches
against the following event attribute:

- `source`: aws.glue-dataquality

```
{
  "source": ["aws.glue-dataquality"]
}
```

To match against specific events, include a `detail-type` attribute
specifying an array of event names to match. For example:

```
{
  "source": ["aws.glue-dataquality"],
  "detail-type": ["`Glue Job State Change`"]
}
```

For more information, see
[Creating event patterns](../userguide/eb-event-patterns.md#eb-create-pattern "../userguide/eb-event-patterns.md#eb-create-pattern") in the _Amazon EventBridge User Guide_.
