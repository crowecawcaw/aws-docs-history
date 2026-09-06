

# AWS Glue events
<a name="events-ref-glue"></a>

AWS Glue sends service events directly to EventBridge, as well as via AWS CloudTrail.

## AWS Glue service events
<a name="events-ref-glue-events"></a>

AWS Glue sends the following events directly to EventBridge: 
+ Glue Job State Change
+ Glue Catalog State Change
+ Glue Crawler State Change
+ Glue Scheduled Crawler Invocation Failure
+ Glue Job Run Status
+ Glue Crawler Table Change
+ Glue Data Catalog Database State Change
+ Glue Data Catalog Table State Change
+ Glue Statistics Task Started
+ Glue Statistics Task Succeeded
+ Glue Statistics Task Failed
+ Glue Auto Statistics Invocation Failure
+ Glue Scheduled Statistics Invocation Failure
+ Data Quality Task State Change
+ Data Quality Evaluation Results Available
+ Entity Metering Event
+ Auto debug metadata key shared from Orca

*Delivery type*: [ Best effort ](event-delivery-level.md) 

To match against all events from this service, create an event pattern that matches against the following event attribute:
+ `source`: aws.glue

```
{
  "source": ["aws.glue"]
}
```

To match against specific events, include a `detail-type` attribute specifying an array of event names to match. For example:

```
{
  "source": ["aws.glue"],
  "detail-type": ["{{Glue Job State Change}}"]
}
```

For more information, see [Creating event patterns](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-patterns.html#eb-create-pattern) in the *Amazon EventBridge User Guide*.

## AWS Glue events delivered via AWS CloudTrail
<a name="event-ref-glue-events-via-CT"></a>

AWS CloudTrail sends events originating from AWS Glue to EventBridge. AWS services deliver events to CloudTrail on a [best effort](event-delivery-level.md) basis. For more information, see [AWS service events delivered via AWS CloudTrail](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-service-event-cloudtrail.html) in the *Amazon EventBridge User Guide*.

To match events from this service delivered by AWS CloudTrail, create an event pattern that matches against the following event attributes:
+ `source`: aws.glue
+ `eventSource`: glue.amazonaws.com

```
{
  "source": ["aws.glue"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["glue.amazonaws.com"]
  }
}
```

To match against a specific API calls from this service, include an `eventName` attribute specifying an array of API calls to match:

```
{
  "source": ["aws.glue"],
  "detail-type": ["AWS API Call via CloudTrail"],
  "detail": {
    "eventSource": ["glue.amazonaws.com"],
    "eventName": ["{{api-action-name}}"]
  }
}
```